"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Funcionario:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_funcionario(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        codigo_pessoa: Optional[int] = None,
        codigo_funcionario: Optional[int] = None,
        matricula: Optional[str] = None,
        situacao: Optional[int] = None
    ) -> dict:
        """Objetivo: Consultar os dados de funcionários do UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os dados dos funcionários URI + api/v{version:apiVersion}/Funcionario/ConsultarFuncionario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Consulta os dados de funcionários do UAU, podendo fazer filtros pela empresa, obra, pessoa, funcionário, matrícula e situação.

Deve informar obrigatoriamente o código da empresa.
Pode informar opcionalmente o código da obra, pessoa, funcionário, matrícula e situação.

VirtUau:

Link para Virtuau relacionado:https://ajuda.globaltec.com.br/virtuau/cadastro-de-funcionarios/


        """
        path = "Funcionario/ConsultarFuncionario"
        return self.api.post(
            path,
            json={
                "CodigoEmpresa": codigo_empresa,
                "CodigoObra": codigo_obra,
                "CodigoPessoa": codigo_pessoa,
                "CodigoFuncionario": codigo_funcionario,
                "Matricula": matricula,
                "Situacao": situacao,
            }
        )

