# %%
from pathlib import Path
from requests.compat import urljoin, urlencode
from rich.progress import track
from typing import List, Dict
from uau_api import UauAPI
from uau_api.settings import Settings
import aiofiles
import aiohttp
import asyncio
import base64
import dateutil
import json
import random
import pandas as pd

# Initialize the client
uau = UauAPI(Settings().API_URL, Settings().API_KEY)
wd = Path(Settings().WORKDIR)
uau.authenticate("leonardo", "hybr01")
destination = wd / "NotasUAU"
url = urljoin(Settings().API_URL, "Pessoas/ConsultarPessoasPorCPFCNPJ")
with open(destination / "downloaded.jsonl") as fc:
    data = [json.loads(line) for line in fc.readlines()]

df = pd.json_normalize(data)
to_process = df["CNPJCPFFornecedor"].unique()


async def async_download(
    session: aiohttp.ClientSession, method: str, url: str, *args, **kwargs
) -> bytes:
    try:
        async with session.request(method=method, url=url, *args, **kwargs) as response:
            if response.status == 200:
                return await response.text()
            return None
    except Exception:
        return None


async def async_save_to_file(
    file_content: bytes | str, destination: Path | str, mode: str
) -> None:
    if mode not in ("a", "w", "wb"):
        return

    if isinstance(destination, str):
        destination = Path(destination)

    if file_content is None:
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        async with aiofiles.open(destination, mode=mode) as file:
            await file.write(file_content)
    except Exception as e:
        print(e)


async def process(
    session: aiohttp.ClientSession, url: str, destination: Path | str, **kwargs
) -> None:
    """ """
    if isinstance(destination, str):
        destination = Path(destination)
    content = await async_download(session=session, method='POST', url=url, **kwargs)
    await async_save_to_file(file_content=content, destination=destination, mode='a')
    await asyncio.sleep(random.uniform(0.1, 0.3))


async def main(data: List[str], url: str, destination: str | Path, **kwargs) -> None:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for row in data:
            task = asyncio.create_task(process(session, url, destination, json={ "cpf_cnpj": row,"status": 2,}, **kwargs))
            tasks.append(task)
            # Process in chunks to avoid overwhelming the server
            if len(tasks) >= 10:
                await asyncio.gather(*tasks)
                tasks = []

        if tasks:
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(
        main(data=to_process, url=url, destination=destination / "pessoas.jsonl", headers=uau.session.headers)
    )
