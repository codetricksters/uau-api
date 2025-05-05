from functools import wraps
from pathlib import Path
from typing import Union, List, Dict
import aiofiles
import aiohttp
import asyncio
import base64
import json
import logging
import random

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)


def write_jsonl(data: Union[Dict, List[Dict]], filepath: str, mode: str = "w"):
    """
    Writes data to a .jsonl file. Supports write ('w') and append ('a') modes.

    Parameters:
        data (dict or list of dict): Data to write.
        filepath (str): Path to the .jsonl file.
        mode (str): Write mode - 'w' for write (overwrite), 'a' for append.
    """
    if mode not in ("w", "a"):
        raise ValueError("Mode must be 'w' for write or 'a' for append.")

    if isinstance(data, dict):
        data = [data]  # Convert single dict to list

    with open(filepath, mode, encoding="utf-8") as f:
        for item in data:
            json_line = json.dumps(item)
            f.write(json_line + "\n")


def save_base64_to_file(base64_string, output_filename):
    try:
        file_bytes = base64.b64decode(base64_string)
        with open(output_filename, "wb") as file:
            file.write(file_bytes)
        print(f"File saved successfully as: {output_filename}")
    except Exception as e:
        print(f"Error saving file: {str(e)}")


def exception_handler(func):
    @wraps(func)
    def inner_function(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # Extract function arguments, excluding `self` or `cls`
            filtered_args = [arg for arg in args if not hasattr(arg, "__dict__")]
            response = (
                getattr(e.response, "json", lambda: None)()
                if hasattr(e, "response")
                else None
            )
            error = json.dumps(
                {
                    "error": str(e),
                    "function": func.__name__,
                    "args": filtered_args,  # Exclude `self`
                    "kwargs": kwargs,
                    "response": response,
                }
            )
            logging.error(error)

    return inner_function


async def async_download_file(session: aiohttp.ClientSession, url: str) -> bytes:
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.read()
            return None
    except Exception:
        return None


async def async_save_file(content: bytes, destination: Path) -> None:
    if content is None:
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists():
        async with aiofiles.open(destination, mode="wb") as f:
            await f.write(content)


async def process_url(
    session: aiohttp.ClientSession, url: str, destination: Path | str
) -> None:
    """ """
    destination = Path(destination)

    if destination.exists():
        return

    content = await async_download_file(session, url)
    await async_save_file(content, destination)
    await asyncio.sleep(random.uniform(0.1, 0.3))
