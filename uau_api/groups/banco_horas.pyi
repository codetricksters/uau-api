import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class BancoHoras:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def lancar_banco_horas_funcionario(self, lista_banco_horas: list[dict] | None = None) -> requests.Response: ...
