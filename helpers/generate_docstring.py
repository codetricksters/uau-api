"""This module contains functions for generating docstrings for API methods."""

from typing import Dict, Any, List, Optional
from textwrap import indent
import json
import re


def format_type_hint(param_type: Any) -> str:
    """Convert API parameter type to Python type hint string.

    Args:
        param_type: The parameter type from the API spec

    Returns:
        str: The formatted type hint
    """
    if isinstance(param_type, dict):
        return 'Dict[str, Any]'
    elif isinstance(param_type, list):
        return 'List[Dict[str, Any]]'
    elif param_type == 'string':
        return 'str'
    elif isinstance(param_type, (int, float)):
        return 'int'
    elif isinstance(param_type, bool):
        return 'bool'
    elif isinstance(param_type, str) and (
        'T' in param_type or 'Date' in param_type
    ):
        return 'datetime'
    else:
        return 'Any'


def format_param_description(param_name: str, param_type: Any) -> str:
    """Generate parameter description with type information.

    Args:
        param_name: The name of the parameter
        param_type: The parameter type specification

    Returns:
        str: Formatted parameter description
    """
    type_hint = format_type_hint(param_type)
    if isinstance(param_type, dict) and param_type.get('description'):
        return f'{param_name} ({type_hint}): {param_type["description"]}'
    else:
        # Generate a reasonable default description based on the parameter name
        words = re.findall('[A-Z][^A-Z]*', param_name)
        if not words:
            words = [param_name]
        description = ' '.join(words).lower()
        return f'{param_name} ({type_hint}): The {description}'


def generate_docstring(api_metadata: Dict[str, Any]) -> str:
    """Generate a complete docstring for an API method.

    Args:
        api_metadata: Dictionary containing API method metadata including:
            - path: The API endpoint path
            - http_method: The HTTP method (GET, POST, etc)
            - markdown: The method description
            - implementation_notes: Additional implementation details
            - parameters: Dictionary of parameters and their types
            - class_name: The name of the API class

    Returns:
        str: The generated docstring
    """
    path = api_metadata.get('path', '')
    http_method = api_metadata.get('http_method', 'post').upper()
    summary = api_metadata.get('markdown', '')
    implementation_notes = api_metadata.get('implementation_notes', '')
    parameters = api_metadata.get('parameters', {})
    class_name = api_metadata.get('class_name', 'API')

    # Build the docstring sections
    sections = []

    # Main description
    if summary:
        sections.append(summary)

    # Technical details section
    tech_details = []
    tech_details.append(f'Endpoint: `{path}`')
    tech_details.append(f'HTTP Method: `{http_method}`')
    if implementation_notes:
        tech_details.append('\nImplementation Notes:')
        tech_details.append(implementation_notes)
    sections.append('\n'.join(tech_details))

    # Parameters section
    if parameters:
        param_docs = []
        param_docs.append('Args:')
        if isinstance(parameters, dict):
            for param_name, param_type in parameters.items():
                param_docs.append(
                    f'    {format_param_description(param_name, param_type)}'
                )
        elif isinstance(parameters, list):
            param_docs.append(
                '    parameters (List[Dict]): List of parameter dictionaries for the request'
            )
        sections.append('\n'.join(param_docs))

        # Add example parameter structure
        sections.append('Parameter Structure:')
        sections.append(
            indent(
                json.dumps(parameters, indent=4, ensure_ascii=False), '    '
            )
        )

    # Returns section
    returns_section = ['Returns:', '    dict: The API response']
    sections.append('\n'.join(returns_section))

    # Raises section
    raises_section = [
        'Raises:',
        '    requests.HTTPError: If the API request fails',
        '    ValueError: If required parameters are missing or invalid',
    ]
    sections.append('\n'.join(raises_section))

    # Example section
    snake_name = re.sub('([A-Z][a-z]+)', r'_\1', path.split('/')[-1]).lower()
    example_section = [
        'Examples:',
        f'    >>> api = {class_name}()',
        f'    >>> response = api.{snake_name}(',
        "    ...     parameter1='value1',",
        "    ...     parameter2='value2'",
        '    ... )',
    ]
    sections.append('\n'.join(example_section))

    # Combine all sections
    full_docstring = '\n\n'.join(sections)

    # Format for Python
    return f'    """{full_docstring}\n    """'
