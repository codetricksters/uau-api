# Swagger API Class Generator

## Overview

The `generate_api_classes_from_swagger.py` module automatically generates Python API client classes from Swagger 2.0 / OpenAPI 3.0 specifications. It replaces and enhances the original `generate_api_classes.py` by reading directly from the `swagger.json` specification file instead of requiring a separate JSONL format.

## Key Features

- **Automatic $ref Resolution**: Resolves all JSON Pointer references (`$ref`) to their actual definitions in the spec
- **Parameter Extraction**: Automatically extracts and handles all parameter types (path, query, header, body)
- **Tag-based Organization**: Groups endpoints by their tags to create organized, logical class groupings
- **Full Documentation**: Generates comprehensive docstrings from API descriptions
- **Type Hints**: Includes Python type hints for better IDE support and type checking

## Architecture

### SwaggerRefResolver Class

Handles the resolution of JSON Pointer references as specified in the OpenAPI 3.0 standard.

#### Syntax Supported

According to [RFC 3986](https://tools.ietf.org/html/rfc3986), `$ref` strings use JSON Pointer notation:

- **Local references**: `#/definitions/MyType` 
  - Points to `swagger_data['definitions']['MyType']`
- **Nested references**: `#/definitions/UAUApi.Models.Some.Type`
  - Traverses the object hierarchy: `swagger_data['definitions']['UAUApi.Models.Some.Type']`

#### Key Methods

- `resolve_ref(ref: str) -> Optional[Dict]`: Resolves a $ref string to its definition
- `get_definition_type(definition: Dict) -> str`: Extracts type from a definition
- `get_properties(definition: Dict) -> Dict`: Gets properties with nested $refs resolved

### Main Generation Function

`generate_api_classes_from_swagger()` orchestrates the full generation process:

1. **Load Specification**: Reads swagger.json and initializes the resolver
2. **Parse Endpoints**: Iterates through all paths and operations
3. **Extract Metadata**: Extracts class names, method names, parameters, documentation
4. **Group by Class**: Groups endpoints by their tag into logical classes
5. **Generate Files**: Creates Python class files organized by resource

## Usage

### Basic Command

```bash
python -m helpers.generate_api_classes_from_swagger \
  --input swagger.json \
  --output uau_api/groups
```

### Options

- `--input` / `-i`: Path to the Swagger/OpenAPI JSON file (required)
- `--output` / `-o`: Output directory for generated Python files (required)
- `--replace` / `--no-replace`: Whether to replace existing files (default: True)

### Example Output

For a path like `/api/v{version}/AcompanhamentoContratoVenda/GravarAcompanhamento` with tag `AcompanhamentoContratoVenda`:

**Generated File**: `acompanhamento_contrato_venda.py`

**Class**: `AcompanhamentoContratoVenda`

**Method**: `gravar_acompanhamento()`

## Generated Code Structure

Each generated class file includes:

### Imports
```python
from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi
import requests
from http import HTTPStatus
```

### Class Template
```python
class ResourceName:
    def __init__(self, api: RequestsApi):
        """Initialize with API client"""
        self.api = api
    
    def method_name(self, **parameters) -> dict:
        """Full docstring from API spec"""
        # Auto-generated implementation
        path = "..."
        response = self.api.post(path, json=params)
        return response
```

## Parameter Handling

The generator handles different parameter types:

### Path Parameters
```python
def method_name(self, version: str, work_id: str) -> dict:
    path = f"/api/v{version}/Works/{work_id}"
```

### Query/Header Parameters
```python
def method_name(self, authorization: Optional[str] = None) -> dict:
    kwargs = {"Authorization": authorization}
    params = {k: v for k, v in kwargs.items() if v is not None}
```

### Body Parameters (with $ref)
```python
def method_name(self, request: Optional[Dict] = None) -> dict:
    kwargs = {"request": request}
    params = {k: v for k, v in kwargs.items() if v is not None}
    response = self.api.post(path, json=params)
```

## $ref Resolution Details

When the generator encounters a `$ref`:

1. **Extract Reference Path**: Removes the `#/` prefix
2. **Split Path**: Splits by `/` to get hierarchy parts
3. **Traverse Object**: Walks through the swagger_data dictionary
4. **Return Definition**: Returns the resolved object or None if not found

### Example Resolution

```
$ref: "#/definitions/UAUApi.Models.AcompanhamentoContratoVenda.AcompanhamentoContratoVendaRequest"
↓
swagger_data
  ↓ definitions
    ↓ UAUApi.Models.AcompanhamentoContratoVenda.AcompanhamentoContratoVendaRequest
      → Returns the actual definition object
```

## Relationship to Original Generator

The new generator **does not modify** the original `generate_api_classes.py`:

- **Original** (`generate_api_classes.py`): Reads JSONL format files
- **New** (`generate_api_classes_from_swagger.py`): Reads Swagger/OpenAPI JSON directly
- Both can coexist and serve different input formats
- The new one is the recommended approach for Swagger-based projects

## Benefits Over Original

1. **Single Source of Truth**: Uses swagger.json directly instead of separate JSONL
2. **Full $ref Support**: Properly resolves all JSON Pointer references
3. **Better Documentation**: Extracts complete descriptions and summaries
4. **Standardized Format**: Uses OpenAPI/Swagger standard format
5. **Maintained Classes**: Easier to regenerate when API spec changes

## Error Handling

The generator handles edge cases gracefully:

- **Missing $ref targets**: Returns None and continues
- **Non-dict operations**: Skips vendor extensions (x-* fields)
- **Malformed paths**: Continues with next endpoint
- **File conflicts**: Skips existing files when `--no-replace` is used

## Integration with Existing Code

The generated classes integrate seamlessly with the existing codebase:

```python
from uau_api.requestsapi import RequestsApi
from uau_api.groups.acompanhamento_contrato_venda import AcompanhamentoContratoVenda

api = RequestsApi(...)
service = AcompanhamentoContratoVenda(api)
response = service.gravar_acompanhamento(
    version="1",
    request={...},
    authorization="token"
)
```

## Testing

The generator was tested by:

1. Parsing the full swagger.json with 92,067 lines
2. Generating all 50+ API class files
3. Validating parameter extraction and method generation
4. Confirming $ref resolution for nested definitions

## Contributing

When updating this generator:

1. Maintain backward compatibility with generated code
2. Test with real swagger.json files
3. Update documentation for new features
4. Keep the original generator unchanged
5. Add comprehensive docstrings
