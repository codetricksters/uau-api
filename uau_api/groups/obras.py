"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Obras:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def obter_obras_ativas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta obras cadastradas e ativas no UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta obras cadastradas e ativas dentro do UAU.


        """
        path = "Obras/ObterObrasAtivas"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_obra_por_chave(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """Consultar obra por chave

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta dados de uma obra filtrando por chave.
Valida os campos passados como parâmetros.


        """
        path = "Obras/ConsultarObraPorChave"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
            }
        )

    def obter_meses_abertos_por_empresa_obra(
        self,
        empresa_obra: Optional[str] = None
    ) -> dict:
        path = "Obras/ObterMesesAbertosPorEmpresaObra"
        return self.api.post(
            path,
            json={
                "empresaObra": empresa_obra,
            }
        )

