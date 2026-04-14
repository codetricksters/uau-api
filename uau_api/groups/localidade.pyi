import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class Localidade:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def consultar_localidade_por_cep(self, cep: str | None = None) -> requests.Response: ...
