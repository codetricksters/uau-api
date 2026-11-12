"""CLI configuration file handling.

The integration token (``api_key``) must live in the config file. Username and
password are optional there; when absent they are requested interactively, the
password through a hidden prompt (never as a command-line argument).
"""

import getpass
import os
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Tuple

import typer

CONFIG_ENV = 'UAU_CONFIG'


class ConfigError(Exception):
    """Raised when the configuration is missing or invalid."""


def default_config_path() -> Path:
    env = os.environ.get(CONFIG_ENV)
    if env:
        return Path(env).expanduser()
    if sys.platform == 'win32':
        base = Path(
            os.environ.get('APPDATA', Path.home() / 'AppData' / 'Roaming')
        )
    else:
        base = Path(os.environ.get('XDG_CONFIG_HOME', Path.home() / '.config'))
    return base / 'uau-api' / 'config.toml'


@dataclass
class CliConfig:
    api_url: str
    api_key: str = field(repr=False)
    username: Optional[str] = None
    password: Optional[str] = field(default=None, repr=False)


def _escape(value: str) -> str:
    return value.replace('\\', '\\\\').replace('"', '\\"')


def save_config(path: Path, cfg: CliConfig) -> None:
    lines = [
        f'api_url = "{_escape(cfg.api_url)}"',
        f'api_key = "{_escape(cfg.api_key)}"',
    ]
    if cfg.username:
        lines.append(f'username = "{_escape(cfg.username)}"')
    if cfg.password:
        lines.append(f'password = "{_escape(cfg.password)}"')
    path.parent.mkdir(parents=True, exist_ok=True)
    # Create with 0600 from the start so secrets are never world-readable.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines) + '\n')
    if os.name == 'posix':
        os.chmod(path, 0o600)


def load_config(path: Path) -> CliConfig:
    if not path.exists():
        raise ConfigError(
            f'Configuração não encontrada em {path}. Rode `uau config init`.'
        )
    try:
        data = tomllib.loads(path.read_text(encoding='utf-8'))
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(
            f'Arquivo de configuração inválido ({path}): {exc}'
        ) from None
    for key in ('api_url', 'api_key'):
        if not data.get(key):
            hint = (
                ' O token deve ficar no arquivo.' if key == 'api_key' else ''
            )
            raise ConfigError(
                f'Campo obrigatório "{key}" ausente em {path}.{hint} Rode `uau config init`.'
            )
    return CliConfig(
        api_url=data['api_url'],
        api_key=data['api_key'],
        username=data.get('username') or None,
        password=data.get('password') or None,
    )


def resolve_credentials(cfg: CliConfig) -> Tuple[str, str]:
    """Username/password from the file, otherwise prompt (password hidden)."""
    username = cfg.username or typer.prompt('Usuário')
    password = cfg.password or getpass.getpass('Senha: ')
    return username, password


def mask(value: Optional[str]) -> str:
    return '(não definido)' if not value else '********'
