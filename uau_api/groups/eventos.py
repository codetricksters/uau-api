"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Eventos:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_log_eventos(
        self,
        chave: Optional[str] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None
    ) -> dict:
        """Consultar os logs de eventos do sistema

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Os campos do tipo data devem obedecer o formato especificado pelo JSON.
yyyy-MM-dd HH:mm:ss > 2019-01-22 00:00:00
yyyy-MM-dd > 2018-12-25



Definição de Negócio:
  Permite consultar logs de eventos.

Verifique as chaves de consultas disponíveis no endpoint:
URI + /api/v{version}/Eventos/ConsultarChavesLogDeEventos


Deve informar uma data inicial e outra final.

Anexos:

Postman: https://ajuda.globaltec.com.br/download/777172/
Retorno: https://ajuda.globaltec.com.br/download/777175/


        """
        path = "Eventos/ConsultarLogEventos"
        return self.api.post(
            path,
            json={
                "Chave": chave,
                "DataInicial": data_inicial,
                "DataFinal": data_final,
            }
        )

    def consultar_chaves_log_de_eventos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta a lista com as chaves dos eventos que podem ser consultados

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Regras de Negócio:

A chave de acesso consultada informa quais chaves poderão ser utilizadas no seguinte endpoint:
URI + /api/v{version}/Eventos/ConsultarLogEventos



Anexos:

Postman: https://ajuda.globaltec.com.br/download/777172/


        """
        path = "Eventos/ConsultarChavesLogDeEventos"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

