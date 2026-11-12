"""Build ``uau_api/catalog/endpoints.json`` from ``swagger.json``.

The catalog is a compact, ``$ref``-resolved index of every endpoint. It is
shared by the CLI (and the future MCP server) and has no dependency on the
generated ``uau_api/groups`` classes.

Usage:
    python helpers/build_catalog.py [swagger.json] [output.json]
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

from helpers.generate_api_classes_from_swagger import SwaggerRefResolver

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SWAGGER = ROOT / 'swagger.json'
DEFAULT_OUTPUT = ROOT / 'uau_api' / 'catalog' / 'endpoints.json'

SKIP_PARAMS = {
    'version',
    'api-version',
    'Authorization',
    'X-INTEGRATION-Authorization',
}
VERSION_PREFIX = re.compile(r'^/api/v\{version\}/')
SCALARS = {'string', 'integer', 'number', 'boolean'}


def _short(text: str, limit: int = 300) -> str:
    text = re.sub(r'\s+', ' ', text or '').strip()
    return text if len(text) <= limit else text[: limit - 1] + '…'


def _body_info(
    schema: Dict[str, Any], resolver: SwaggerRefResolver
) -> Dict[str, Any]:
    """Describe the body: its type and top-level properties."""
    definition = schema
    if '$ref' in schema:
        definition = resolver.resolve_ref(schema['$ref']) or {}
    body_type = definition.get('type', 'object')
    required = set(definition.get('required', []))
    props: List[Dict[str, Any]] = []
    for name, prop in definition.get('properties', {}).items():
        resolved = (
            resolver.resolve_ref(prop['$ref']) if '$ref' in prop else prop
        )
        resolved = resolved or {}
        ptype = resolved.get('type', 'object')
        props.append(
            {
                'name': name,
                'type': ptype,
                'format': resolved.get('format'),
                'required': name in required,
                'description': _short(prop.get('description', ''), 120),
            }
        )
    return {'type': body_type, 'properties': props}


def build_catalog(swagger: Dict[str, Any]) -> List[Dict[str, Any]]:
    resolver = SwaggerRefResolver(swagger)
    endpoints: List[Dict[str, Any]] = []
    for path, methods in swagger['paths'].items():
        for method, op in methods.items():
            params, body = [], None
            for p in op.get('parameters', []):
                if p['in'] == 'body':
                    body = _body_info(p.get('schema', {}), resolver)
                elif p['name'] not in SKIP_PARAMS and p['in'] in (
                    'query',
                    'path',
                ):
                    params.append(
                        {
                            'name': p['name'],
                            'in': p['in'],
                            'type': p.get('type', 'string'),
                            'required': p.get('required', False),
                            'description': _short(
                                p.get('description', ''), 120
                            ),
                        }
                    )
            # Unversioned swagger paths (/api/X/Y) live one level above the
            # versioned base URL (.../api/v1/), so they become ../X/Y.
            rel = VERSION_PREFIX.sub('', path)
            if rel == path and path.startswith('/api/'):
                rel = '../' + path[len('/api/') :]
            endpoints.append(
                {
                    'group': (op.get('tags') or ['General'])[0],
                    'name': [
                        s for s in rel.split('/') if not s.startswith('{')
                    ][-1],
                    'method': method.upper(),
                    'path': rel,
                    'summary': _short(op.get('summary', ''), 200),
                    'description': _short(op.get('description', '')),
                    'operation_id': op.get('operationId', ''),
                    'params': params,
                    'body': body,
                }
            )
    endpoints.sort(key=lambda e: (e['group'], e['path'], e['method']))
    return endpoints


def main(argv: List[str]) -> None:
    src = Path(argv[1]) if len(argv) > 1 else DEFAULT_SWAGGER
    out = Path(argv[2]) if len(argv) > 2 else DEFAULT_OUTPUT
    endpoints = build_catalog(json.loads(src.read_text(encoding='utf-8')))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(endpoints, ensure_ascii=False, indent=1), encoding='utf-8'
    )
    print(f'{len(endpoints)} endpoints -> {out}')


if __name__ == '__main__':
    main(sys.argv)
