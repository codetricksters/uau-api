import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class CorreioEletronico:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def enviar_mail_interno_uau(self, mensagem_envio: str | None = None, usuariosuau_destino: str | None = None, usuariouau_envio: str | None = None, assunto: str | None = None) -> requests.Response: ...
