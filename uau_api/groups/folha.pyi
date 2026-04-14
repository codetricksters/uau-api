import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class Folha:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def gravar_alocacao_mao_obra(self, lista_alocacao: list[dict] | None = None) -> requests.Response: ...
    def gravar_movimentacao_mensal_obra(self, lista_movimentacao_obra: list[dict] | None = None) -> requests.Response: ...
