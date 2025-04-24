"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Localidade:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_localidade_por_cep(
        self,
        cep: Optional[str] = None
    ) -> dict:
        """Consulta Localidades por CEP.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Consultar as informações da localidade informando apenas o CEP.

Valida a presença do CEP;
Retorna uma ou mais localidades para o CEP informado;
Retorna somente endereços ativos.


        """
        path = "Localidade/ConsultarLocalidadePorCEP"
        return self.api.post(
            path,
            json={
                "Cep": cep,
            }
        )

