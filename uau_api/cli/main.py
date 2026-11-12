"""``uau`` command line interface.

Subcommands for every API endpoint are generated lazily from the endpoint
catalog (``uau_api.catalog``): ``uau <group> <endpoint> [--opt ...] [--body ...]``.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import quote

import click
import typer
from rich.console import Console
from rich.table import Table
from typer.core import TyperGroup

from uau_api import catalog
from uau_api.catalog import Endpoint, kebab, normalize
from uau_api.cli.config import (
    CliConfig,
    ConfigError,
    default_config_path,
    load_config,
    mask,
    resolve_credentials,
    save_config,
)

console = Console()
err_console = Console(stderr=True)

_SCALAR_TYPES = {
    'string': click.STRING,
    'integer': click.INT,
    'number': click.FLOAT,
    'boolean': click.BOOL,
}


def _fail(message: str, code: int = 2) -> None:
    err_console.print(f'[red]Erro:[/red] {message}', highlight=False)
    raise typer.Exit(code)


# --------------------------------------------------------------------------
# Dynamic endpoint commands
# --------------------------------------------------------------------------


def _read_body(value: str) -> Any:
    try:
        if value == '-':
            return json.load(sys.stdin)
        if value.startswith('@'):
            return json.loads(Path(value[1:]).read_text(encoding='utf-8'))
        return json.loads(value)
    except (OSError, json.JSONDecodeError) as exc:
        raise click.BadParameter(
            f'JSON inválido em --body: {exc}', param_hint='--body'
        )


def _build_endpoint_command(ep: Endpoint) -> click.Command:
    params: List[click.Parameter] = []
    # dest name -> (kind, original name); kind in {'path', 'query', 'body'}
    targets: Dict[str, tuple] = {}
    seen = {'--body', '--help'}

    def add(
        opt_name: str,
        kind: str,
        orig: str,
        ptype: str,
        required: bool,
        help_: str,
    ):
        flag = f'--{kebab(opt_name)}'
        if flag in seen:
            return
        seen.add(flag)
        dest = f'p{len(targets)}'
        targets[dest] = (kind, orig)
        params.append(
            click.Option(
                [flag, dest],
                type=_SCALAR_TYPES.get(ptype, click.STRING),
                required=required,
                default=None,
                help=help_ or None,
            )
        )

    for p in ep.params:
        add(
            p['name'],
            p['in'],
            p['name'],
            p['type'],
            p['required'] and p['in'] == 'path',
            p['description'],
        )

    body = ep.body
    if body and body['type'] == 'object':
        for prop in body['properties']:
            if prop['type'] in _SCALAR_TYPES:
                add(
                    prop['name'],
                    'body',
                    prop['name'],
                    prop['type'],
                    False,
                    prop['description'],
                )

    if body:
        required = [p['name'] for p in body['properties'] if p['required']]
        hint = (
            f' Campos obrigatórios: {", ".join(required)}.' if required else ''
        )
        params.append(
            click.Option(
                ['--body'],
                default=None,
                help=(
                    'Corpo da requisição: JSON, @arquivo.json ou - (stdin). '
                    f'As opções individuais sobrepõem chaves do corpo.{hint}'
                ),
            )
        )

    @click.pass_context
    def callback(ctx: click.Context, **kwargs: Any) -> None:
        _run_endpoint(ctx, ep, targets, kwargs)

    return click.Command(
        name=kebab(ep.name),
        params=params,
        callback=callback,
        help=ep.summary or ep.description,
        short_help=(ep.summary or '')[:80] or None,
    )


class EndpointGroup(click.Group):
    """One API group (tag); endpoint commands are created on demand."""

    def __init__(self, group: str):
        self.group = group
        n = len(catalog.endpoints_in(group))
        super().__init__(name=kebab(group), help=f'{group} ({n} endpoints)')

    def list_commands(self, ctx: click.Context) -> List[str]:
        return sorted(kebab(e.name) for e in catalog.endpoints_in(self.group))

    def get_command(
        self, ctx: click.Context, cmd_name: str
    ) -> Optional[click.Command]:
        ep = catalog.get(self.group, cmd_name)
        return _build_endpoint_command(ep) if ep else None


class RootGroup(TyperGroup):
    """Fixed commands plus one lazy sub-group per catalog group."""

    def list_commands(self, ctx: click.Context) -> List[str]:
        fixed = super().list_commands(ctx)
        return fixed + [
            kebab(g) for g in catalog.groups() if kebab(g) not in fixed
        ]

    def get_command(
        self, ctx: click.Context, cmd_name: str
    ) -> Optional[click.Command]:
        cmd = super().get_command(ctx, cmd_name)
        if cmd is not None:
            return cmd
        for g in catalog.groups():
            if normalize(g) == normalize(cmd_name):
                return EndpointGroup(g)
        return None


def _run_endpoint(
    ctx: click.Context,
    ep: Endpoint,
    targets: Dict[str, tuple],
    kwargs: Dict[str, Any],
) -> None:
    from uau_api.client import UauAPI  # imported lazily: keeps --help fast

    obj = ctx.find_root().obj or {}
    path_values: Dict[str, Any] = {}
    query: Dict[str, Any] = {}
    overrides: Dict[str, Any] = {}
    for dest, (kind, orig) in targets.items():
        value = kwargs.get(dest)
        if value is None:
            continue
        {'path': path_values, 'query': query, 'body': overrides}[kind][
            orig
        ] = value

    body: Any = None
    if kwargs.get('body') is not None:
        body = _read_body(kwargs['body'])
    if overrides:
        if body is None:
            body = {}
        if not isinstance(body, dict):
            raise click.UsageError(
                '--body deve ser um objeto JSON para combinar com opções individuais.'
            )
        body.update(overrides)
    if body is None and ep.method == 'POST':
        body = {}

    try:
        cfg = load_config(obj.get('config') or default_config_path())
    except ConfigError as exc:
        _fail(str(exc))

    api = UauAPI(cfg.api_url.rstrip('/') + '/', cfg.api_key)
    username, password = resolve_credentials(
        cfg
    )  # password only lives in this local
    try:
        auth = api.authenticate(username, password)
    except Exception as exc:  # network error or non-JSON auth reply
        _fail(f'Falha na autenticação: {exc}', 1)
    finally:
        del password
    if not auth.ok:
        _fail(f'Autenticação recusada (HTTP {auth.status_code}).', 1)

    path = ep.path
    for name in ep.path_params:
        if name not in path_values:
            _fail(f'Parâmetro de rota obrigatório ausente: --{kebab(name)}')
        path = path.replace(
            '{%s}' % name, quote(str(path_values[name]), safe='')
        )

    kwargs_req: Dict[str, Any] = {'params': query} if query else {}
    if body is not None:
        kwargs_req['json'] = body
    try:
        resp = api.request(ep.method, path, **kwargs_req)
    except Exception as exc:
        _fail(f'Falha na requisição: {exc}', 1)

    _print_response(resp, bool(obj.get('raw')))
    if resp.status_code >= 400:
        err_console.print(f'[red]HTTP {resp.status_code}[/red]')
        raise typer.Exit(1)


def _print_response(resp: Any, raw: bool) -> None:
    try:
        data = resp.json()
    except ValueError:
        click.echo(resp.text)
        return
    if raw:
        click.echo(json.dumps(data, ensure_ascii=False))
    else:
        console.print_json(data=data, ensure_ascii=False)


# --------------------------------------------------------------------------
# Fixed commands
# --------------------------------------------------------------------------

app = typer.Typer(
    cls=RootGroup,
    help='CLI do UAU Globaltec. Subcomandos de endpoints: uau <grupo> <endpoint>.',
    no_args_is_help=True,
    add_completion=False,
)
config_app = typer.Typer(
    help='Gerencia o arquivo de configuração.', no_args_is_help=True
)
app.add_typer(config_app, name='config')


@app.callback()
def _root(
    ctx: typer.Context,
    config: Optional[Path] = typer.Option(
        None,
        '--config',
        help='Caminho do arquivo de configuração (padrão: UAU_CONFIG ou ~/.config/uau-api/config.toml).',
    ),
    raw: bool = typer.Option(
        False, '--raw', help='Saída JSON compacta, sem formatação.'
    ),
) -> None:
    ctx.obj = {'config': config, 'raw': raw}


@config_app.command('init')
def config_init(ctx: typer.Context) -> None:
    """Cria o arquivo de configuração (token, URL e, opcionalmente, usuário/senha)."""
    path = (ctx.obj or {}).get('config') or default_config_path()
    if path.exists() and not typer.confirm(
        f'{path} já existe. Sobrescrever?', default=False
    ):
        raise typer.Exit(1)
    api_url = typer.prompt('URL da API (ex.: https://host/uauAPI/api/v1/)')
    api_key = typer.prompt('Token de integração', hide_input=True)
    username = typer.prompt(
        'Usuário (vazio para perguntar a cada chamada)',
        default='',
        show_default=False,
    )
    password = None
    if username and typer.confirm('Salvar a senha no arquivo?', default=False):
        password = typer.prompt(
            'Senha', hide_input=True, confirmation_prompt=True
        )
    save_config(
        path,
        CliConfig(
            api_url=api_url,
            api_key=api_key,
            username=username or None,
            password=password,
        ),
    )
    console.print(f'Configuração salva em {path} (permissão 600).')


@config_app.command('show')
def config_show(ctx: typer.Context) -> None:
    """Mostra a configuração atual, com segredos mascarados."""
    path = (ctx.obj or {}).get('config') or default_config_path()
    try:
        cfg = load_config(path)
    except ConfigError as exc:
        _fail(str(exc))
    console.print(f'arquivo:  {path}', highlight=False)
    console.print(f'api_url:  {cfg.api_url}', highlight=False)
    console.print(f'api_key:  {mask(cfg.api_key)}', highlight=False)
    console.print(
        f'username: {cfg.username or "(perguntar)"}', highlight=False
    )
    console.print(
        f'password: {mask(cfg.password) if cfg.password else "(perguntar)"}',
        highlight=False,
    )


@app.command('search')
def search_cmd(
    text: List[str] = typer.Argument(..., help='Termos de busca.')
) -> None:
    """Busca endpoints no catálogo."""
    results = catalog.search(' '.join(text))
    table = Table('Comando', 'Método', 'Resumo')
    for e in results:
        table.add_row(f'{kebab(e.group)} {kebab(e.name)}', e.method, e.summary)
    console.print(table)
    console.print(f'{len(results)} resultado(s).')


@app.command('describe')
def describe_cmd(group: str, endpoint: str) -> None:
    """Mostra parâmetros e corpo de um endpoint."""
    ep = catalog.get(group, endpoint)
    if ep is None:
        _fail(
            f'Endpoint não encontrado: {group} {endpoint}. Use `uau search`.'
        )
    console.print(f'[bold]{ep.method} {ep.path}[/bold]', highlight=False)
    console.print(ep.summary, highlight=False)
    if ep.description:
        console.print(f'\n{ep.description}', highlight=False)
    if ep.params:
        table = Table(
            'Parâmetro',
            'Em',
            'Tipo',
            'Obrig.',
            'Descrição',
            title='Parâmetros',
        )
        for p in ep.params:
            table.add_row(
                f'--{kebab(p["name"])}',
                p['in'],
                p['type'],
                'sim' if p['required'] else '',
                p['description'],
            )
        console.print(table)
    if ep.body:
        table = Table(
            'Campo',
            'Tipo',
            'Obrig.',
            'Descrição',
            title=f'Corpo ({ep.body["type"]})',
        )
        for p in ep.body['properties']:
            table.add_row(
                p['name'],
                p['type'],
                'sim' if p['required'] else '',
                p['description'],
            )
        console.print(table)


def main() -> None:
    app()


if __name__ == '__main__':
    main()
