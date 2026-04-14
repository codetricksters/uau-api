import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class RequisicaoCompra:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def aprovar_requisicoes_compra(self, requisicoes: list[dict] | None = None, departamento: str | None = None, cargo: str | None = None, cod_justificativa: int | None = None, obs_justificativa: str | None = None) -> requests.Response: ...
    def desaprovar_requisicoes_compra(self, requisicoes: list[dict] | None = None, cod_justificativa_desaprovacao: int | None = None, obs_justificativa_desaprovacao: str | None = None) -> requests.Response: ...
