import requests
from _typeshed import Incomplete
from datetime import datetime
from http import HTTPStatus as HTTPStatus
from typing import Any
from uau_api.requestsapi import RequestsApi as RequestsApi

class NotasFiscais:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def consultar_nfentrada(self, listanf_entrada: list[dict] | None = None, codigo_empresa: int | None = None, codigo_obra: str | None = None, cnpj_fornecedor: str | None = None, codigo_fornecedor: str | None = None, data_inicial: datetime | None = None, data_final: datetime | None = None, tipo_periodo: Any | None = None) -> requests.Response: ...
    def salvar_arquivo_xmlnotafiscal_entrada(self, parameters: list[dict] | None = None) -> requests.Response: ...
