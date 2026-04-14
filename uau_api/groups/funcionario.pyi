import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class Funcionario:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def consultar_funcionario(self, codigo_empresa: int | None = None, codigo_obra: str | None = None, codigo_pessoa: int | None = None, codigo_funcionario: int | None = None, matricula: str | None = None, situacao: int | None = None) -> requests.Response: ...
