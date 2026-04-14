import requests
from _typeshed import Incomplete
from datetime import datetime as datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class RelatorioIRPF:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def gerar_pdfrel_irpf(self, vendasobras_empresa: list[dict] | None = None, ano_base: int | None = None, naomostradados_venda: bool | None = None) -> requests.Response: ...
    def gerar_pdfrel_irpfv2(self, vendasobras_empresa: list[dict] | None = None, ano_base: int | None = None, naomostradados_venda: bool | None = None) -> requests.Response: ...
