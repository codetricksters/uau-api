"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Fiscal:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def buscar_caps(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar a lista de CAPs ativos

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Formato dos dados retornados:
Codigo (String): Código do CAP
Descricao (String): Descrição do CAP
Tipo (Integer): Tipo do CAP
0: Geral
1: Acresc/Desc






        """
        path = "Fiscal/BuscarCAPs"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def buscar_codigo_servico_fiscal(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta a lista de cógidos de serviços fiscais

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta os códigos de serviços fiscais ativos.


        """
        path = "Fiscal/BuscarCodigoServicoFiscal"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def importar_lancamentos_fiscais(
        self,
        dadoslacamentos_xml: Optional[str] = None
    ) -> dict:
        """Importa lançamentos fiscais e/ou societários - Formato antigo

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Recebe string no formato XML com os dados do lançamento para importação.
Utiliza o formato antigo do XML na string passada como parâmetro.

Definição de Negócio:

Importa lançamentos fiscais e/ou societários.
Valida o XML passado no request.
Valida o usuário e suas permissões.


        """
        path = "Fiscal/ImportarLancamentosFiscais"
        return self.api.post(
            path,
            json={
                "dadoslacamentos_xml": dadoslacamentos_xml,
            }
        )

    def importar_lancamentos_contabeis(
        self,
        dadoslacamentos_xml: Optional[str] = None
    ) -> dict:
        """Importa lançamentos fiscais e/ou societários - Formato novo

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Utiliza o novo formato do XML na string passada como parâmetro.

Definição de Negócio:

Importa lançamentos fiscais e/ou societários.
Valida o XML passado no request.
Valida usuário e suas permissões.


        """
        path = "Fiscal/ImportarLancamentosContabeis"
        return self.api.post(
            path,
            json={
                "dadoslacamentos_xml": dadoslacamentos_xml,
            }
        )

