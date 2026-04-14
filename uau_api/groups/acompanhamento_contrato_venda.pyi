import requests
from _typeshed import Incomplete
from datetime import datetime
from http import HTTPStatus as HTTPStatus
from uau_api.requestsapi import RequestsApi as RequestsApi

class AcompanhamentoContratoVenda:
    api: Incomplete
    def __init__(self, api: RequestsApi) -> None: ...
    def gravar_acompanhamento(self, num_acompanhamento: int | None = None, empresa: int | None = None, obra: str | None = None, num_contrato: str | None = None, periodo_inicio: datetime | None = None, periodo_fim: datetime | None = None, lista_de_produtos: list[dict] | None = None, responsavel: int | None = None, status: int | None = None, observacao_para_entrega: str | None = None, motorista: int | None = None, caminhao_placa: str | None = None, uf_placa: str | None = None) -> requests.Response: ...
