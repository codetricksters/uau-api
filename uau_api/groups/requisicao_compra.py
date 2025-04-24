"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class RequisicaoCompra:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def aprovar_requisicoes_compra(
        self,
        requisicoes: Optional[List[Dict]] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        cod_justificativa: Optional[int] = None,
        obs_justificativa: Optional[str] = None
    ) -> dict:
        """Método com finalidade de aprovar requisições de compra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras básicas:

É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA


        """
        path = "RequisicaoCompra/AprovarRequisicoesCompra"
        return self.api.post(
            path,
            json={
                "Requisicoes": requisicoes,
                "Departamento": departamento,
                "Cargo": cargo,
                "CodJustificativa": cod_justificativa,
                "ObsJustificativa": obs_justificativa,
            }
        )

    def desaprovar_requisicoes_compra(
        self,
        requisicoes: Optional[List[Dict]] = None,
        cod_justificativa_desaprovacao: Optional[int] = None,
        obs_justificativa_desaprovacao: Optional[str] = None
    ) -> dict:
        """Método com finalidade de desaprovar requisições de compra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras básicas:

É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA
Será permitido desaprovar apenas requisições de compra com estágio 0 - Criada


        """
        path = "RequisicaoCompra/DesaprovarRequisicoesCompra"
        return self.api.post(
            path,
            json={
                "Requisicoes": requisicoes,
                "CodJustificativaDesaprovacao": cod_justificativa_desaprovacao,
                "ObsJustificativaDesaprovacao": obs_justificativa_desaprovacao,
            }
        )

