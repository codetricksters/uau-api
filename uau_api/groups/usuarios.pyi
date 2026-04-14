import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class Usuarios:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def consultar_usuarios_ativos(self, login_usuario: str | None = None) -> requests.Response: ...
    def consultar_grupos_de_usuario(self, detalhe: str | None = None, mensagem: str | None = None, descricao: str | None = None) -> requests.Response: ...
