"""Endpoint catalog built from the swagger spec (``endpoints.json``).

The catalog is independent of the generated ``uau_api.groups`` classes and of
the network; it is shared by the CLI and (later) the MCP server.
"""

import json
import re
from dataclasses import dataclass, field
from functools import lru_cache
from importlib import resources
from typing import Any, Dict, List, Optional, Tuple


@dataclass(frozen=True)
class Endpoint:
    group: str
    name: str
    method: str
    path: str
    summary: str = ''
    description: str = ''
    operation_id: str = ''
    params: Tuple[Dict[str, Any], ...] = field(default_factory=tuple)
    body: Optional[Dict[str, Any]] = None

    @property
    def path_params(self) -> List[str]:
        return re.findall(r'{(\w+)}', self.path)


def normalize(text: str) -> str:
    """Lower-case and drop separators: ``obter-obras_ativas`` -> ``obterobrasativas``."""
    return re.sub(r'[\s_\-]', '', text).lower()


def kebab(text: str) -> str:
    """``ObterObrasAtivas`` -> ``obter-obras-ativas``."""
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', text)
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', text)
    return text.replace('_', '-').lower()


@lru_cache(maxsize=1)
def load_catalog() -> Tuple[Endpoint, ...]:
    raw = (
        resources.files('uau_api.catalog')
        .joinpath('endpoints.json')
        .read_text(encoding='utf-8')
    )
    return tuple(
        Endpoint(**{**e, 'params': tuple(e['params'])})
        for e in json.loads(raw)
    )


def groups() -> List[str]:
    return sorted({e.group for e in load_catalog()})


def endpoints_in(group: str) -> List[Endpoint]:
    key = normalize(group)
    return [e for e in load_catalog() if normalize(e.group) == key]


def get(group: str, name: str) -> Optional[Endpoint]:
    """Case/separator-insensitive lookup (``obter-obras-ativas`` works)."""
    key = normalize(name)
    for e in endpoints_in(group):
        if normalize(e.name) == key:
            return e
    return None


def search(text: str) -> List[Endpoint]:
    """Every term must appear in group, name, summary or path."""
    terms = [normalize(t) for t in text.split() if t.strip()]
    result = []
    for e in load_catalog():
        hay = normalize(f'{e.group} {e.name} {e.summary} {e.path}')
        if all(t in hay for t in terms):
            result.append(e)
    return result
