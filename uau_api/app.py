from rich.console import Console
from rich.table import Table
from typer import Argument, run
from uau_api.settings import Settings
from uau_api import UauAPI
import functools


uau = UauAPI(Settings().API_URL, Settings().API_KEY)
uau.authenticate(Settings().USERNAME, Settings().PASSWORD)


def consulta_api(class_name: str, function_name: str):
    result = functools.reduce(getattr, [class_name, function_name], uau)()

    print(result.json())


run(consulta_api)
