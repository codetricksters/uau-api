"""
Generate Markdown API reference docs from a Swagger 2.0 specification.

Reads swagger.json, groups operations by tag (one Markdown file per tag,
matching the resource grouping already used in uau_api/groups/), and
renders each endpoint with its parameters, request body and response
schemas fully expanded (nested $ref definitions resolved recursively).
"""

from pathlib import Path
import json
import re
import typer
from typing import Any, Dict, List, Optional, Set, Tuple

HTTP_METHOD_ORDER = ['get', 'post', 'put', 'patch', 'delete']


def resolve_ref(swagger_data: Dict[str, Any], ref: str) -> Optional[Dict[str, Any]]:
    """Resolve a local '#/definitions/...' pointer to its definition."""
    if not isinstance(ref, str) or not ref.startswith('#/'):
        return None
    current: Any = swagger_data
    for part in ref[2:].split('/'):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return None
    return current if isinstance(current, dict) else None


def ref_name(ref: str) -> str:
    """Extract the definition name from a '#/definitions/Name' pointer."""
    return ref.rsplit('/', 1)[-1]


def anchor(name: str) -> str:
    """GitHub/mkdocs-style heading anchor for a schema name."""
    slug = re.sub(r'[^a-z0-9_\- ]', '', name.lower())
    return re.sub(r'\s+', '-', slug.strip())


def render_type(
    swagger_data: Dict[str, Any],
    schema: Dict[str, Any],
    collected: Dict[str, Dict[str, Any]],
) -> str:
    """Render a schema's type as Markdown, queuing any $ref for the appendix."""
    if '$ref' in schema:
        name = ref_name(schema['$ref'])
        resolved = resolve_ref(swagger_data, schema['$ref'])
        if resolved is not None and name not in collected:
            collected[name] = resolved
        return f'[`{name}`](#{anchor(name)})'

    schema_type = schema.get('type', 'object')

    if schema_type == 'array':
        items = schema.get('items', {})
        return f'array de {render_type(swagger_data, items, collected)}'

    fmt = schema.get('format')
    label = f'{schema_type} ({fmt})' if fmt else schema_type

    enum = schema.get('enum')
    if enum:
        label += f" — valores possíveis: {', '.join(str(v) for v in enum)}"

    return label


def render_schema_table(
    swagger_data: Dict[str, Any],
    name: str,
    definition: Dict[str, Any],
    collected: Dict[str, Dict[str, Any]],
) -> List[str]:
    """Render one definition as a Markdown heading + properties table."""
    lines = [f'### {name}', '']

    description = definition.get('description')
    if description:
        lines += [description.strip(), '']

    properties = definition.get('properties')
    if not properties:
        # Non-object definition (enum, primitive, etc.)
        lines += [f'Tipo: {render_type(swagger_data, definition, collected)}', '']
        return lines

    required = set(definition.get('required', []))

    lines += ['| Propriedade | Tipo | Obrigatório | Descrição |', '|---|---|---|---|']
    for prop_name, prop_def in properties.items():
        prop_type = render_type(swagger_data, prop_def, collected)
        is_required = '✓' if prop_name in required else ''
        prop_desc = (prop_def.get('description') or '').replace('\n', ' ').replace('\r', '')
        lines.append(f'| `{prop_name}` | {prop_type} | {is_required} | {prop_desc} |')
    lines.append('')

    return lines


def render_operation(
    swagger_data: Dict[str, Any],
    path: str,
    http_method: str,
    operation: Dict[str, Any],
    collected: Dict[str, Dict[str, Any]],
) -> List[str]:
    """Render one endpoint (method + path) as Markdown."""
    lines = [f'## {http_method.upper()} `{path}`', '']

    summary = operation.get('summary')
    if summary:
        lines += [f'**{summary.strip()}**', '']

    description = operation.get('description')
    if description:
        lines += [description.strip(), '']

    parameters = operation.get('parameters', [])
    non_body_params = [p for p in parameters if p.get('in') != 'body']
    body_params = [p for p in parameters if p.get('in') == 'body']

    if non_body_params:
        lines += ['### Parâmetros', '', '| Nome | Em | Tipo | Obrigatório | Descrição |', '|---|---|---|---|---|']
        for param in non_body_params:
            schema = param if 'type' in param else param.get('schema', {})
            param_type = render_type(swagger_data, schema, collected)
            required = '✓' if param.get('required') else ''
            desc = (param.get('description') or '').replace('\n', ' ').replace('\r', '')
            lines.append(f"| `{param.get('name')}` | {param.get('in')} | {param_type} | {required} | {desc} |")
        lines.append('')

    for param in body_params:
        schema = param.get('schema', {})
        required = '✓' if param.get('required') else ''
        lines += [
            '### Corpo da requisição',
            '',
            f'Obrigatório: {required or "não"}  ',
            f'Esquema: {render_type(swagger_data, schema, collected)}',
            '',
        ]

    responses = operation.get('responses', {})
    if responses:
        lines += ['### Respostas', '', '| Status | Descrição | Esquema |', '|---|---|---|']
        for status, resp in sorted(responses.items()):
            desc = (resp.get('description') or '').replace('\n', ' ').replace('\r', '')
            schema = resp.get('schema')
            schema_label = render_type(swagger_data, schema, collected) if schema else ''
            lines.append(f'| {status} | {desc} | {schema_label} |')
        lines.append('')

    lines.append('---')
    lines.append('')
    return lines


def generate_markdown_from_swagger(
    input_file: Path = typer.Option(
        ..., '--input', '-i', help='Path to the Swagger 2.0 JSON file'
    ),
    output_dir: Path = typer.Option(
        ..., '--output', '-o', help='Directory where one .md file per tag is written'
    ),
):
    """Generate one Markdown reference file per tag from a Swagger 2.0 spec."""
    with open(input_file, 'r', encoding='utf-8') as f:
        swagger_data = json.load(f)

    paths = swagger_data.get('paths', {})

    operations_by_tag: Dict[str, List[Tuple[str, str, Dict[str, Any]]]] = {}
    for path, path_item in paths.items():
        for http_method, operation in path_item.items():
            if http_method.startswith('x-') or not isinstance(operation, dict):
                continue
            tags = operation.get('tags') or ['Geral']
            operations_by_tag.setdefault(tags[0], []).append((path, http_method, operation))

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    info = swagger_data.get('info', {})

    for tag, operations in sorted(operations_by_tag.items()):
        collected: Dict[str, Dict[str, Any]] = {}
        body: List[str] = [f'# {tag}', '']

        operations.sort(key=lambda op: (op[0], HTTP_METHOD_ORDER.index(op[1]) if op[1] in HTTP_METHOD_ORDER else 99))
        for path, http_method, operation in operations:
            body += render_operation(swagger_data, path, http_method, operation, collected)

        # Expand schemas referenced by this tag's endpoints, including nested refs.
        rendered_schemas: Set[str] = set()
        pending = dict(collected)
        schema_lines: List[str] = []
        while pending:
            name, definition = pending.popitem()
            if name in rendered_schemas:
                continue
            rendered_schemas.add(name)
            schema_lines += render_schema_table(swagger_data, name, definition, pending)

        if schema_lines:
            body += ['## Esquemas', ''] + schema_lines

        file_name = re.sub(r'[^A-Za-z0-9_-]', '_', tag)
        file_path = output_dir / f'{file_name}.md'
        file_path.write_text('\n'.join(body), encoding='utf-8')
        typer.echo(f'Generated {file_path} ({len(operations)} endpoints, {len(rendered_schemas)} schemas)')

    index_lines = [f"# {info.get('title', 'API')}", '', info.get('description', '').strip(), '', '## Recursos', '']
    for tag in sorted(operations_by_tag):
        file_name = re.sub(r'[^A-Za-z0-9_-]', '_', tag)
        index_lines.append(f'- [{tag}]({file_name}.md) — {len(operations_by_tag[tag])} endpoint(s)')
    (output_dir / 'index.md').write_text('\n'.join(index_lines) + '\n', encoding='utf-8')
    typer.echo(f'Generated {output_dir / "index.md"}')


if __name__ == '__main__':
    typer.run(generate_markdown_from_swagger)
