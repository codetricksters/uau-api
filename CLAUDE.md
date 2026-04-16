# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python client library for the **UAU Globaltec** ERP API. It provides auto-generated wrapper classes for 50+ API resource groups, built from Swagger/OpenAPI specs.

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `master` | All source code (`codetricksters/uau-api`). Receives every change. |
| `minified` | Distribution branch on `hy-brazil-energia/uau-api`. Contains Cython-generated `.c` files (no `.py` source, no `.so`). At install time the user's `gcc` compiles `.c` → `.so` for their Python version. Never edited directly; always rebuilt from `master`. |

---

## Commands (master branch)

This project uses `taskipy` as a task runner and `uv` as the package manager.

```bash
# Install dependencies
uv sync

# Run tests (includes lint + coverage)
task test

# Run a single test file
pytest tests/test_login.py

# Run a single test by name
pytest tests/test_login.py::TestLogin::test_settings_loaded_from_env

# Lint only (blue + isort check)
task lint

# Serve docs locally
task docs
```

**Note:** Tests require a `.env` file with real credentials. Copy `.env.example` and fill in `API_URL`, `API_KEY`, `USERNAME`, and `PASSWORD`. Integration tests are skipped by default (`@pytest.mark.skip`).

---

## Updating the minified branch from master

Run this procedure whenever `master` has changes that should be published.

The `minified` branch distributes **Cython-generated `.c` files** instead of Python source. At install time (`uv add git+...` or `pip install git+...`) the user's local `gcc` compiles those `.c` files into native extensions (`.so`/`.pyd`) for their Python version — no Cython needed on their machine.

### Prerequisites (one-time)

```bash
sudo apt-get install -y gcc python3-dev   # Debian / Ubuntu / WSL
uv sync --group dev                        # instala Cython, mypy, setuptools
```

### Step-by-step

```bash
# 1. Garantir que master está limpo e atualizado
git checkout master
git pull origin master

# 2. Ir para minified e trazer os arquivos-fonte do master
git checkout minified
git checkout master -- uau_api/

# 3. Verificar e corrigir bugs de f-string (o Cython rejeita variáveis
#    camelCase não declaradas como parâmetros)
python3 -c "
import ast, glob
for path in sorted(glob.glob('uau_api/**/*.py', recursive=True)):
    if path.endswith('__init__.py'): continue
    tree = ast.parse(open(path).read())
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)): continue
        params = {a.arg for a in node.args.args} | {'self','type','str','int','bool','e','version'}
        for child in ast.walk(node):
            if not isinstance(child, ast.JoinedStr): continue
            for part in ast.walk(child):
                if isinstance(part, ast.Name) and part.id not in params:
                    print(f'{path}:{child.lineno}: {part.id}')
"

# 4. Transpilação Python → C  (requer Cython; NÃO compila para .so)
PATH="/usr/bin:$PATH" .venv/bin/python compile.py build_ext --inplace

# 5. Remover .py (exceto __init__.py) e artefatos de build
find uau_api -name "*.py" ! -name "__init__.py" -delete
rm -rf build/

# 6. Regenerar stubs de tipo (.pyi)
uv run stubgen -p uau_api -o .

# 7. Atualizar uau_api/client.pyi manualmente:
#    stubgen não captura atributos definidos em _init_api_groups().
#    Adicione qualquer novo grupo seguindo o padrão existente.

# 8. Commit e push para hy-brazil/minified
git add -A
git commit -m "minified: rebuild from master — <descrição breve>"
git push hy-brazil minified
```

### O que o stubgen não captura automaticamente
Atributos de instância de `UauAPI` (`uau.Obras`, `uau.Venda`, …) são definidos dinamicamente em `_init_api_groups()`. Após rodar o stubgen, abra [uau_api/client.pyi](uau_api/client.pyi) e adicione novos grupos seguindo o padrão existente.

---

## Architecture

### Core Client

- [uau_api/client.py](uau_api/client.py) — `UauAPI`: the main entry point. Extends `RequestsApi` and instantiates all 50+ API group classes as attributes in `_init_api_groups()`.
- [uau_api/requestsapi.py](uau_api/requestsapi.py) — `RequestsApi`: thin HTTP wrapper around `requests.Session` with automatic retry logic (retries on 408, 429, 500–504).
- [uau_api/settings.py](uau_api/settings.py) — Pydantic `BaseSettings` that loads `API_URL`, `API_KEY`, `USERNAME`, `PASSWORD` from `.env`.

### Generated API Groups

All files in [uau_api/groups/](uau_api/groups/) are auto-generated. Each file defines one class (e.g., `Obras`, `Venda`) that takes a `RequestsApi` instance and exposes endpoint methods returning `requests.Response`. Do not hand-edit these files; regenerate them instead.

[uau_api/groups_test/](uau_api/groups_test/) contains equivalent classes for a test/sandbox environment.

### Code Generators

Both generators live in [helpers/](helpers/):

- `generate_api_classes_from_swagger.py` — **preferred**: reads a `swagger.json` directly, resolves `$ref` pointers via `SwaggerRefResolver`, and outputs group classes.
- `generate_api_classes.py` — original generator using JSONL format files (kept for backward compatibility).

### Operations / Legacy

[uau_api/operations.py](uau_api/operations.py) contains a legacy `Uau` base class with logging and Pydantic models. New code should use `UauAPI` from `client.py` instead.

## Key Conventions

- **Retry logic** is defined in `RequestsApi.__init__` — modify there to change retry behavior globally.
- **Authentication** is set as the `X-INTEGRATION-Authorization` header on the session after calling `UauAPI.authenticate(username, password)`.
- **pytest** is configured with `pythonpath=.` and `--doctest-modules` (doctests run as part of the test suite).
- **Formatting**: `blue` (Black-compatible) + `isort` with the `black` profile. Run `task lint` before committing.
