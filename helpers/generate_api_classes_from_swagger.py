"""
Generate Python API classes from Swagger 2.0 / OpenAPI 3.0 specification.

This module reads a Swagger/OpenAPI JSON specification file, resolves all
$ref references to their definitions, and generates Python API client classes
organized by resource/tag.

The $ref resolution follows JSON Pointer notation:
- Local references: "#/definitions/MyType" points to definitions.MyType
- All references are resolved by traversing the JSON structure
"""

from pathlib import Path
import json
import re
import typer
from typing import Any, Dict, Optional, List
from helpers.generate_docstring import generate_docstring


class SwaggerRefResolver:
    """Resolves $ref references in Swagger/OpenAPI specifications."""

    def __init__(self, swagger_data: Dict[str, Any]):
        """Initialize resolver with swagger specification data.

        Args:
            swagger_data: The loaded swagger.json as a dictionary
        """
        self.swagger_data = swagger_data

    def resolve_ref(self, ref: str) -> Optional[Dict[str, Any]]:
        """Resolve a $ref string to its actual definition.

        Handles JSON Pointer notation like "#/definitions/MyType"

        Args:
            ref: The reference string (e.g., "#/definitions/SomePath.SomeClass")

        Returns:
            The resolved definition object or None if not found
        """
        if not isinstance(ref, str) or not ref.startswith('#/'):
            return None

        # Remove the leading '#/'
        path = ref[2:]
        # Split by '/' to traverse the object hierarchy
        parts = path.split('/')

        current = self.swagger_data
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None

        return current if isinstance(current, dict) else None

    def get_definition_type(self, definition: Dict[str, Any]) -> str:
        """Extract the type from a definition.

        Args:
            definition: The definition object

        Returns:
            The type string (object, string, integer, array, etc.)
        """
        return definition.get('type', 'object')

    def get_properties(
        self, definition: Dict[str, Any]
    ) -> Dict[str, Dict[str, Any]]:
        """Get properties from a definition, resolving nested $refs.

        Args:
            definition: The definition object

        Returns:
            Dictionary of properties with resolved $refs
        """
        properties = definition.get('properties', {})
        resolved_properties = {}

        for prop_name, prop_def in properties.items():
            if '$ref' in prop_def:
                # Resolve the reference
                resolved = self.resolve_ref(prop_def['$ref'])
                if resolved:
                    resolved_properties[prop_name] = resolved
                else:
                    resolved_properties[prop_name] = prop_def
            else:
                resolved_properties[prop_name] = prop_def

        return resolved_properties


def clean_method_name(path: str) -> str:
    """Extract method name from path and clean it.

    Converts paths like "/api/v{version}/Class/MethodName" to "method_name"

    Args:
        path: The API path

    Returns:
        Clean snake_case method name
    """
    # Extract the last part of the path
    method = path.split('/')[-1]

    # Replace variable parts in curly braces with 'by' + variable name
    method = re.sub(r'{(\w+)}', lambda m: 'by_' + m.group(1).lower(), method)

    # Convert to snake_case
    method = re.sub('([A-Z]+)', r'_\1', method).lower()
    method = re.sub('-', '_', method)

    # Make it a valid Python identifier and remove duplicate underscores
    method = re.sub(r'[^a-zA-Z0-9_]', '_', method)
    method = re.sub(r'_+', '_', method)
    method = method.strip('_')

    return method


def get_type_hint(param_type: Any) -> str:
    """Determine the Python type hint for a parameter.

    Args:
        param_type: The parameter type value

    Returns:
        Python type hint string
    """
    if isinstance(param_type, dict):
        return 'Dict'
    elif isinstance(param_type, list):
        return 'List[Dict]'
    elif param_type == 'string':
        return 'str'
    elif param_type == 0 or param_type == 'integer':
        return 'int'
    elif isinstance(param_type, bool):
        return 'bool'
    elif isinstance(param_type, str) and 'T' in param_type:  # ISO date format
        return 'datetime'
    else:
        return 'Any'


def extract_class_name_from_tag(tag: str) -> str:
    """Extract clean class name from tag.

    Tags are like "AcompanhamentoContratoVenda"

    Args:
        tag: The tag string

    Returns:
        Clean class name
    """
    # Tags are already in PascalCase, just return as-is
    return tag if tag else 'General'


def extract_parameters_from_operation(
    operation: Dict[str, Any], resolver: SwaggerRefResolver
) -> Dict[str, Dict[str, Any]]:
    """Extract and resolve parameters from an operation.

    Handles both direct parameters and body parameters with $ref.

    Args:
        operation: The operation object from the swagger spec
        resolver: The reference resolver

    Returns:
        Dictionary mapping parameter names to their definitions
    """
    parameters = {}
    swagger_params = operation.get('parameters', [])

    for param in swagger_params:
        param_name = param.get('name', '')
        param_in = param.get('in', '')

        if param_name:
            if param_in == 'body':
                # Body parameters use $ref
                schema = param.get('schema', {})
                if '$ref' in schema:
                    resolved = resolver.resolve_ref(schema['$ref'])
                    if resolved:
                        parameters[param_name] = {
                            'definition': resolved,
                            'in': 'body',
                            'required': param.get('required', False),
                        }
                else:
                    parameters[param_name] = {
                        'definition': schema,
                        'in': 'body',
                        'required': param.get('required', False),
                    }
            else:
                # Path, query, header parameters
                param_type = param.get('type', 'string')
                parameters[param_name] = {
                    'type': param_type,
                    'in': param_in,
                    'required': param.get('required', False),
                    'description': param.get('description', ''),
                }

    return parameters


def generate_api_classes_from_swagger(
    input_file: Path = typer.Option(
        ..., '--input', '-i', help='Path to the Swagger/OpenAPI JSON file'
    ),
    output_dir: Path = typer.Option(
        ..., '--output', '-o', help='Path to output directory'
    ),
    replace: bool = typer.Option(
        True, '--replace/--no-replace', help='Replace existing files'
    ),
):
    """Generate Python API classes from Swagger/OpenAPI specification.

    Parses the swagger.json file, resolves all $ref references, extracts
    endpoint information, and generates organized Python API client classes
    grouped by resource tag.

    Args:
        input_file: Path to swagger.json file
        output_dir: Output directory for generated Python files
        replace: Whether to replace existing files
    """
    # Load swagger specification
    with open(input_file, 'r', encoding='utf-8') as f:
        swagger_data = json.load(f)

    # Initialize resolver
    resolver = SwaggerRefResolver(swagger_data)

    # Extract API information
    paths = swagger_data.get('paths', {})
    base_path = swagger_data.get('basePath', '')

    # Group operations by tag/class
    api_classes: Dict[str, List[Dict[str, Any]]] = {}

    for path, path_item in paths.items():
        # Each path can have multiple operations (get, post, put, delete, etc.)
        for http_method, operation in path_item.items():
            if http_method.startswith('x-'):
                # Skip vendor extensions
                continue

            if not isinstance(operation, dict):
                continue

            # Get tags (used to group into classes)
            tags = operation.get('tags', ['General'])
            tag = tags[0] if tags else 'General'
            class_name = extract_class_name_from_tag(tag)

            # Initialize class list if needed
            if class_name not in api_classes:
                api_classes[class_name] = []

            # Extract operation details
            operation_id = operation.get('operationId', '')
            summary = operation.get('summary', '')
            description = operation.get('description', '')
            parameters = extract_parameters_from_operation(
                operation, resolver
            )

            api_classes[class_name].append(
                {
                    'path': path,
                    'http_method': http_method.lower(),
                    'operation_id': operation_id,
                    'summary': summary,
                    'description': description,
                    'parameters': parameters,
                    'markdown': description or summary,
                }
            )

    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate class files
    for class_name, methods in api_classes.items():
        # Convert CamelCase to snake_case for filename
        file_name = re.sub('(?!^)([A-Z]+)', r'_\1', class_name).lower()
        file_path = output_dir / f'{file_name}.py'

        if file_path.exists() and not replace:
            typer.echo(f'Skipping {file_path} (already exists)')
            continue

        with open(file_path, 'w', encoding='utf-8') as f:
            # Write file header and imports
            f.write('from typing import Dict, Any, List, Optional\n')
            f.write('from datetime import datetime\n')
            f.write('from uau_api.requestsapi import RequestsApi\n\n')
            f.write('import requests\n')
            f.write('from http import HTTPStatus\n\n')

            # Write class definition
            f.write(f'class {class_name}:\n')

            # Write constructor
            f.write('    def __init__(self, api: RequestsApi):\n')
            f.write('        """Initialize with API client\n\n')
            f.write('        Args:\n')
            f.write('            api: The API client instance\n')
            f.write('        """\n')
            f.write('        self.api = api\n\n')

            # Generate methods
            for method_info in methods:
                method_name = clean_method_name(method_info['path'])
                parameters = method_info.get('parameters', {})
                param_list = []

                # Extract path parameters
                path_params = re.findall(r'{(\w+)}', method_info['path'])
                for param in path_params:
                    snake_param = (
                        re.sub('([A-Z][a-z]+)', r'_\1', param)
                        .lower()
                        .strip('_')
                    )
                    param_list.append(f'{snake_param}: str')

                # Handle regular parameters
                for param_name, param_def in parameters.items():
                    if param_name.lower() in [
                        p.lower() for p in path_params
                    ]:
                        continue

                    # Convert camelCase or PascalCase to snake_case
                    snake_name = (
                        re.sub('([A-Z][a-z]+)', r'_\1', param_name)
                        .lower()
                        .strip('_')
                    )
                    snake_name = re.sub(r'[^a-zA-Z0-9_]', '_', snake_name)
                    snake_name = re.sub(r'_+', '_', snake_name)

                    # Determine type hint
                    if param_def.get('in') == 'body':
                        type_hint = 'Dict'
                    else:
                        param_type = param_def.get('type', 'string')
                        type_hint = get_type_hint(param_type)

                    param_list.append(
                        f'{snake_name}: Optional[{type_hint}] = None'
                    )

                params_str = ',\n        '.join(param_list)

                # Write method signature
                f.write(f'    def {method_name}(\n')
                f.write('        self,\n')
                if params_str:
                    f.write(f'        {params_str}\n')
                f.write('    ) -> requests.Response:\n')

                # Generate and write docstring
                docstring = generate_docstring(
                    {
                        'path': method_info['path'],
                        'http_method': method_info.get('http_method', 'post'),
                        'markdown': method_info.get('markdown', ''),
                        'implementation_notes': method_info.get('summary', ''),
                        'parameters': parameters,
                        'class_name': class_name,
                    }
                )
                lines = docstring.split('\n')
                f.write('        """\n')
                for line in lines[1:-1]:
                    f.write(f'        {line}\n')
                f.write('        """\n')

                # Write method implementation
                path = method_info['path']
                f.write(
                    '        path = '
                    + (f'f"{path}"\n' if path_params else f'"{path}"\n')
                )
                f.write('        kwargs = {\n')
                for param_name in parameters:
                    if param_name not in path_params:
                        snake_name = (
                            re.sub('([A-Z][a-z]+)', r'_\1', param_name)
                            .lower()
                            .strip('_')
                        )
                        snake_name = re.sub(r'[^a-zA-Z0-9_]', '_', snake_name)
                        snake_name = re.sub(r'_+', '_', snake_name)
                        f.write(f'            "{param_name}": {snake_name},\n')
                f.write('        }\n')
                f.write(
                    '        params = {k: v for k, v in kwargs.items() if v is not None}\n'
                )
                f.write(
                    '        response = self.api.'
                    + method_info.get('http_method', 'post').lower()
                    + '(\n'
                )
                f.write('            path,\n')
                f.write('            json=params\n')
                f.write('        )\n')
                f.write('        return response\n\n')

        typer.echo(f'Generated {file_path}')


if __name__ == '__main__':
    typer.run(generate_api_classes_from_swagger)
