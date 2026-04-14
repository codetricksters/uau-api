import requests
from _typeshed import Incomplete
from datetime import datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class Contabil:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def consultar_saldo_de_contas(self, empresa: int | None = None, mes_ano: datetime | None = None, tipo: str | None = None) -> requests.Response: ...
    def consultar_contas_contabeis(self, empresa: int | None = None, ano: int | None = None, conta: str | None = None, descricao_conta: str | None = None, limitar_retorno_em: int | None = None) -> requests.Response: ...
