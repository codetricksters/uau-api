import requests
from _typeshed import Incomplete
from datetime import datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class Eventos:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def consultar_log_eventos(self, chave: str | None = None, data_inicial: datetime | None = None, data_final: datetime | None = None) -> requests.Response: ...
    def consultar_chaves_log_de_eventos(self, detalhe: str | None = None, mensagem: str | None = None, descricao: str | None = None) -> requests.Response: ...
