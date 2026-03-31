# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python client library for the **UAU Globaltec** ERP API. It provides auto-generated wrapper classes for 50+ API resource groups, built from Swagger/OpenAPI specs.

## Commands

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
