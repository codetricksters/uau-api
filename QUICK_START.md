# Quick Start Guide: Swagger API Class Generator

## TL;DR

Generate Python API classes directly from `swagger.json`:

```bash
python -m helpers.generate_api_classes_from_swagger \
  --input swagger.json \
  --output uau_api/groups
```

## Installation Check

The generator uses only standard library + existing dependencies:
```python
# Already available in your environment
import json       # Standard library
import typer      # Already in project
from pathlib import Path
```

No additional installations needed!

## Basic Usage

### Generate All Classes
```bash
python -m helpers.generate_api_classes_from_swagger \
  --input swagger.json \
  --output uau_api/groups
```

### Don't Replace Existing Files
```bash
python -m helpers.generate_api_classes_from_swagger \
  --input swagger.json \
  --output uau_api/groups \
  --no-replace
```

### Different Input File
```bash
python -m helpers.generate_api_classes_from_swagger \
  --input path/to/api-spec.json \
  --output output/directory
```

## What Gets Generated

For each API tag/class:

1. **File Name**: `resource_name.py` (snake_case)
2. **Class Name**: `ResourceName` (PascalCase from tag)
3. **Methods**: One per endpoint, named from operation path

Example:
```
Tag: "Obras"
Path: "/api/v{version}/Obras/ObterObrasAtivas"
↓
File: uau_api/grupos/obras.py
Class: Obras
Method: obter_obras_ativas()
```

## Generated Code Example

```python
from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

class Obras:
    def __init__(self, api: RequestsApi):
        """Initialize with API client"""
        self.api = api
    
    def obter_obras_ativas(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """Full docstring from API spec..."""
        path = f"/api/v{version}/Obras/ObterObrasAtivas"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(path, json=params)
        return response
```

## Using Generated Classes

```python
from uau_api.requestsapi import RequestsApi
from uau_api.groups.obras import Obras

# Initialize API client
api = RequestsApi(base_url="...", headers={...})

# Create service class
obras_service = Obras(api)

# Call methods
response = obras_service.obter_obras_ativas(
    version="1",
    authorization="your_token",
    x_integration_authorization="integration_token"
)

print(response)
```

## How It Works

1. **Parse swagger.json** - Reads the entire API specification
2. **Resolve $ref** - Finds and expands all JSON Pointer references
3. **Extract Endpoints** - Gets all paths, methods, parameters, docs
4. **Group by Tag** - Organizes into logical resource classes
5. **Generate Files** - Creates Python classes with methods

## $ref Resolution

The generator automatically handles all `$ref` references:

```json
{
  "$ref": "#/definitions/UAUApi.Models.SomeType"
}
```

Gets resolved to the actual definition in the swagger.json file.

You don't need to do anything - it's automatic!

## Output Structure

```
uau_api/
├── groups/
│   ├── __init__.py
│   ├── acompanhamento_contrato_venda.py
│   ├── acompanhamentos_servicos.py
│   ├── anexo.py
│   ├── atendimento.py
│   ├── autenticador.py
│   ├── banco_horas.py
│   ├── boleto_services.py
│   ├── cessao_recebiveis.py
│   ├── chave_pix.py
│   ... (50+ more files)
```

## Command Line Options

| Option | Short | Default | Purpose |
|--------|-------|---------|---------|
| `--input` | `-i` | Required | Path to swagger.json |
| `--output` | `-o` | Required | Output directory |
| `--replace` | None | `True` | Overwrite existing files |
| `--no-replace` | None | `False` | Keep existing files |

## Tips

### 1. Version in Python Environment
```bash
# Use the correct Python environment
/home/leonardoalves/pyprojects/uau-api/.venv/bin/python \
  -m helpers.generate_api_classes_from_swagger \
  --input swagger.json \
  --output uau_api/groups
```

### 2. Check What's Generated
```bash
# See the generated files
ls -la uau_api/groups/

# Examine a specific class
cat uau_api/groups/obras.py
```

### 3. Regenerate When API Spec Changes
```bash
# Update your swagger.json first
# Then regenerate all classes
python -m helpers.generate_api_classes_from_swagger \
  --input swagger.json \
  --output uau_api/groups \
  --replace
```

## Troubleshooting

### Command not found
Make sure you're using the correct Python:
```bash
# Right way
/home/leonardoalves/pyprojects/uau-api/.venv/bin/python -m ...

# Or activate venv first
source .venv/bin/activate
python -m helpers.generate_api_classes_from_swagger ...
```

### File permissions
If you get permission denied:
```bash
chmod 755 helpers/generate_api_classes_from_swagger.py
```

### Import errors in generated files
Make sure these exist:
- `uau_api/requestsapi.py` ✓
- `helpers/generate_docstring.py` ✓

Both are already in the project.

## Differences from Original Generator

| Feature | `generate_api_classes.py` | `generate_api_classes_from_swagger.py` |
|---------|--------------------------|---------------------------------------|
| Input | JSONL files | swagger.json |
| $ref Support | No | Yes |
| Automation | Manual JSONL prep | Direct from spec |
| **Recommended** | Legacy | ✓ New |

Both exist - use the new one for swagger specs!

## Performance

- **Swagger file size**: 92,067 lines
- **Classes generated**: 50+
- **Time**: < 1 second
- **Syntax validation**: All files pass ✓

## See Also

- Full documentation: [helpers/SWAGGER_GENERATOR_README.md](helpers/SWAGGER_GENERATOR_README.md)
- Implementation details: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)
- Original generator: [helpers/generate_api_classes.py](helpers/generate_api_classes.py) (unchanged)
