from pathlib import Path
import json
import re
import typer
from generate_docstring import generate_docstring

def clean_method_name(path):
    """Extract method name from path and clean it"""
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

def get_type_hint(param_type):
    """Determine the Python type hint for a parameter"""
    if isinstance(param_type, dict):
        return 'Dict'
    elif isinstance(param_type, list):
        return 'List[Dict]'
    elif param_type == "string":
        return 'str'
    elif param_type == 0:
        return 'int'
    elif isinstance(param_type, bool):
        return 'bool'
    elif isinstance(param_type, str) and 'T' in param_type:  # ISO date format
        return 'datetime'
    else:
        return 'Any'

def generate_api_classes(
    input_file: Path = typer.Option(..., "--input", "-i", help="Path to the input JSONL file"),
    output_dir: Path = typer.Option(..., "--output", "-o", help="Path to output directory"),
    replace: bool = typer.Option(True, "--replace/--no-replace", help="Replace existing files")
):
    """Generate Python API classes from JSONL specification file"""
    # Read the API functions from the JSONL file
    api_classes = {}
    
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() and not line.startswith('//'):
                data = json.loads(line)
                class_name = data['class_name']
                if class_name not in api_classes:
                    api_classes[class_name] = []
                api_classes[class_name].append(data)

    # Create the output directory if it doesn't exist
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for class_name, methods in api_classes.items():
        # Convert CamelCase to snake_case for filename
        file_name = re.sub('(?!^)([A-Z]+)', r'_\1', class_name).lower()
        file_path = output_dir / f'{file_name}.py'
        if file_path.exists() and not replace:
            continue

        with open(file_path, 'w', encoding='utf-8') as f:
            # Write file header and imports
            f.write('from typing import Dict, Any, List, Optional\n')
            f.write('from datetime import datetime\n')
            f.write('from ..requestsapi import RequestsApi\n\n')
            f.write('import requests\n')

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
            for method in methods:
                method_name = clean_method_name(method['path'])
                params = method.get('parameters', {})
                param_list = []
                
                # Extract path parameters
                path_params = re.findall(r'{(\w+)}', method['path'])
                for param in path_params:
                    snake_param = re.sub('([A-Z][a-z]+)', r'_\1', param).lower().strip('_')
                    param_list.append(f'{snake_param}: str')
                
                # Handle regular parameters
                if isinstance(params, dict):
                    for param_name, param_type in params.items():
                        if param_name.lower() in [p.lower() for p in path_params]:
                            continue
                        # Convert camelCase or PascalCase to snake_case
                        snake_name = re.sub('([A-Z][a-z]+)', r'_\1', param_name).lower().strip('_')
                        snake_name = re.sub(r'[^a-zA-Z0-9_]', '_', snake_name)
                        snake_name = re.sub(r'_+', '_', snake_name)
                        type_hint = get_type_hint(param_type)
                        param_list.append(f'{snake_name}: Optional[{type_hint}] = None')
                elif isinstance(params, list):
                    param_list.append('parameters: Optional[List[Dict]] = None')
                
                params_str = ',\n        '.join(param_list)
                
                # Write method signature
                f.write(f'    def {method_name}(\n')
                f.write('        self,\n')
                if params_str:
                    f.write(f'        {params_str}\n')
                f.write('    ) -> dict:\n')

                # Generate and write docstring
                docstring = generate_docstring({
                    "path": method['path'],
                    "http_method": method.get('http_method', 'post'),
                    "markdown": method.get('markdown', ''),
                    "implementation_notes": method.get('implementation_notes', ''),
                    "parameters": params,
                    "class_name": class_name
                })
                lines = docstring.split('\n')
                # Ensure proper indentation for docstring
                f.write('        """\n')
                for line in lines[1:-1]:  # Skip first/last lines that have the triple quotes
                    f.write(f'        {line}\n')
                f.write('        """\n')

                # Write method implementation
                path = method['path']
                f.write('        path = ' + (f'f"{path}"\n' if path_params else f'"{path}"\n'))
                f.write('        try:\n')
                f.write('            response = self.api.' + (method.get('http_method', 'post')).lower() + '(\n')
                f.write('                path,\n')
                
                if isinstance(params, dict):
                    f.write('                json={\n')
                    for param_name in params:
                        if param_name not in path_params:
                            snake_name = re.sub('([A-Z][a-z]+)', r'_\1', param_name).lower().strip('_')
                            snake_name = re.sub(r'[^a-zA-Z0-9_]', '_', snake_name)
                            snake_name = re.sub(r'_+', '_', snake_name)
                            f.write(f'                    "{param_name}": {snake_name},\n')
                    f.write('                }\n')
                elif isinstance(params, list):
                    f.write('                json=parameters if parameters is not None else {}\n')
                else:
                    f.write('                json={}\n')
                f.write('            )\n')
                f.write('            response.raise_for_status()\n')
                f.write('            return response.json()\n')
                f.write('        except requests.exceptions.RequestException as e:\n')
                f.write('            print(f"An error occurred: {e}")\n')
                f.write('            return None\n\n')

if __name__ == '__main__':
    typer.run(generate_api_classes)