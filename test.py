from pathlib import Path
from requests.compat import urljoin, urlencode
from rich.progress import track
from typing import List, Dict
from uau_api import UauAPI
from uau_api.settings import Settings
from uau_api.utils import save_base64_to_file, write_jsonl
import aiofiles
import aiohttp
import asyncio
import dateutil
import json
import pandas as pd
import random
import re
import requests
# Initialize the client
uau = UauAPI(Settings().API_URL, Settings().API_KEY)
wd  = Path(Settings().WORKDIR)
uau.authenticate('leonardo', 'hybr01')
url = urljoin(Settings().API_URL, 'Obras/ObterObrasAtivas')
async def fetch_content():
    async with aiohttp.ClientSession() as session:
        async with session.request(method='POST', url=url, headers=uau.session.headers) as response:
            if response.status == 200:
                return await response.read()
            else:
                return f"Error: {response.status}"
def main():
    content = asyncio.run(fetch_content())
    try:
        out = json.loads(content)
        print(out[0])
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()