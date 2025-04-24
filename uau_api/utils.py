import json
from typing import Union, List, Dict

def write_jsonl(data: Union[Dict, List[Dict]], filepath: str, mode: str = 'w'):
    """
    Writes data to a .jsonl file. Supports write ('w') and append ('a') modes.

    Parameters:
        data (dict or list of dict): Data to write.
        filepath (str): Path to the .jsonl file.
        mode (str): Write mode - 'w' for write (overwrite), 'a' for append.
    """
    if mode not in ('w', 'a'):
        raise ValueError("Mode must be 'w' for write or 'a' for append.")

    if isinstance(data, dict):
        data = [data]  # Convert single dict to list

    with open(filepath, mode, encoding='utf-8') as f:
        for item in data:
            json_line = json.dumps(item)
            f.write(json_line + '\n')