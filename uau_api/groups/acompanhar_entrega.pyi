import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class AcompanharEntrega:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def consultar_processos(self, empresa: int | None = None, obra: str | None = None) -> requests.Response: ...
    def acompanhar_pre_entrega(self, empresa: int | None = None, obra: str | None = None, processo: int | None = None, chave_nota_fiscal: str | None = None, chave_nota_fiscal_frete: str | None = None, codigo_do_boleto: str | None = None, codigo_do_boleto_frete: str | None = None, itens: list[dict] | None = None) -> requests.Response: ...
