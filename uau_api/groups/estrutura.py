"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Estrutura:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def excluir_estrutura(
        self,
        codigo_estrutura: Optional[int] = None,
        sequencia: Optional[str] = None
    ) -> dict:
        """Excluir estrutura.

        Implementation Notes:
        Definição técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Permite excluir uma estrutura completa caso o valor do parâmetro sequência seja (0 - raiz) ou apenas um item da estrutura(Caso o tipo do item seja "0 - Nível", também serão excluídos os itens filhos).
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

        """
        path = "Estrutura/ExcluirEstrutura"
        return self.api.post(
            path,
            json={
                "codigoEstrutura": codigo_estrutura,
                "sequencia": sequencia,
            }
        )

    def inserir_estrutura(
        self,
        descricao: Optional[str] = None
    ) -> dict:
        """Inserir uma estrutura.

        Implementation Notes:
        Definição técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Permite inserir uma estrutura. Após inserir, poderá vincular os itens da estrutura.
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

        """
        path = "Estrutura/InserirEstrutura"
        return self.api.post(
            path,
            json={
                "descricao": descricao,
            }
        )

    def excluir_item_de_estrutura(
        self,
        codigo_item: Optional[str] = None
    ) -> dict:
        """Excluir item de estrutura.

        Implementation Notes:
        Definição técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Permite excluir um item de estrutura que não está sendo utilizado no cadastro de estrutura, orçamento, contrato ou serviços do planejamento .
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

        """
        path = "Estrutura/ExcluirItemDeEstrutura"
        return self.api.post(
            path,
            json={
                "codigoItem": codigo_item,
            }
        )

    def inserir_item_de_estrutura(
        self,
        codigo_item: Optional[str] = None,
        descricao_item: Optional[str] = None
    ) -> dict:
        """Inserir um item de estrutura.

        Implementation Notes:
        Definição técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Permite inserir um item de estrutura. Após inserir, poderá se utilizado no cadastro de estrutura e ser vinculado em orçamento, contrato e serviços do planejamento.
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

        """
        path = "Estrutura/InserirItemDeEstrutura"
        return self.api.post(
            path,
            json={
                "codigoItem": codigo_item,
                "descricaoItem": descricao_item,
            }
        )

    def inserir_item_na_estrutura(
        self,
        codigo_estrutura: Optional[int] = None,
        tipo_estrutura: Optional[int] = None,
        sequencia: Optional[str] = None,
        codigo_item: Optional[str] = None
    ) -> dict:
        """Inserir item em uma estrutura.

        Implementation Notes:
        Definição técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Permite inserir item em uma estrutura. Após concluir o cadastro da estrutura, poderá ser vinculada em orçamento, contrato e serviços do planejamento. 
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

        """
        path = "Estrutura/InserirItemNaEstrutura"
        return self.api.post(
            path,
            json={
                "codigoEstrutura": codigo_estrutura,
                "tipoEstrutura": tipo_estrutura,
                "sequencia": sequencia,
                "codigoItem": codigo_item,
            }
        )

