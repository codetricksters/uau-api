"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class ListaPrecoReferencia:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def inserir_fornecedores(
        self,
        numero_lista: Optional[int] = None,
        codigo_fornecedor: Optional[int] = None,
        cpfcnpj: Optional[str] = None,
        valor_minimo_pedfob: Optional[int] = None,
        valor_minimo_pedcif: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_termino: Optional[datetime] = None,
        contato: Optional[str] = None,
        itens_por_fornecedor: Optional[List[Dict]] = None
    ) -> dict:
        """Método com finalidade de inserir fornecedor na Lista de Preço Referência.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras Básicas:

O usuário deve possuir permissão de inclusao no programa "ALLISTAPRECOREF"
Para incluir um fornecedor, a lista já deve existir no sistema.
A lista deve estar em aberto, não pode ter nenhuma confirmação de aprovação.


        """
        path = "ListaPrecoReferencia/InserirFornecedores"
        return self.api.post(
            path,
            json={
                "NumeroLista": numero_lista,
                "CodigoFornecedor": codigo_fornecedor,
                "CPFCNPJ": cpfcnpj,
                "ValorMinimoPedFOB": valor_minimo_pedfob,
                "ValorMinimoPedCIF": valor_minimo_pedcif,
                "DataInicio": data_inicio,
                "DataTermino": data_termino,
                "Contato": contato,
                "ItensPorFornecedor": itens_por_fornecedor,
            }
        )

    def atualizar_item_fornecedor(
        self,
        numero_lista: Optional[int] = None,
        codigo_fornecedor: Optional[int] = None,
        cpfcnpj: Optional[str] = None,
        valor_minimo_pedfob: Optional[int] = None,
        valor_minimo_pedcif: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_termino: Optional[datetime] = None,
        contato: Optional[str] = None,
        itens_por_fornecedor: Optional[List[Dict]] = None
    ) -> dict:
        """Método com finalidade de atualizar um fornecedor na Lista de Preço Referência.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras Básicas:

O usuário deve possuir permissão de alteração no programa "ALLISTAPRECOREF"
Para atualizar um fornecedor, a lista já deve existir no sistema e o fornecedor já deve estar cadastro.
A lista deve estar em aberto, não pode ter nenhuma confirmação de aprovação.


        """
        path = "ListaPrecoReferencia/AtualizarItemFornecedor"
        return self.api.post(
            path,
            json={
                "NumeroLista": numero_lista,
                "CodigoFornecedor": codigo_fornecedor,
                "CPFCNPJ": cpfcnpj,
                "ValorMinimoPedFOB": valor_minimo_pedfob,
                "ValorMinimoPedCIF": valor_minimo_pedcif,
                "DataInicio": data_inicio,
                "DataTermino": data_termino,
                "Contato": contato,
                "ItensPorFornecedor": itens_por_fornecedor,
            }
        )

    def consultar_lista_preco_referencia(
        self,
        numero_lista: Optional[int] = None,
        data_validade: Optional[datetime] = None,
        status: Optional[int] = None,
        fornecedorcnpj: Optional[str] = None,
        fornecedor_codigo: Optional[int] = None
    ) -> dict:
        """Método com finalidade de consultar a Lista de Preco Referência, com itens da lista de preço e itens de fornecedores preenchidos ou não.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras Básicas:

Pelo menos um parâmetro deve ser preenchido para consulta.
Parâmetros:
CodigoLista: Parâmetro principal, caso seja informado irá sobrepor todos os outros.
FornecedorCodigo: Fará a pesquisa pelo código do fornecedor, caso não possua o CNPJ.
FornecedorCNPJ: Fará a pesquisa pelo CNPJ do fornecedor, caso não possua o código do fornecedor.
DataValidade: Data de validade da lista de preço.
Status:   
0 - Em aberto
1 - Em Análise
2 - Aprovada
3 - Migrada






        """
        path = "ListaPrecoReferencia/ConsultarListaPrecoReferencia"
        return self.api.post(
            path,
            json={
                "NumeroLista": numero_lista,
                "DataValidade": data_validade,
                "Status": status,
                "FornecedorCNPJ": fornecedorcnpj,
                "FornecedorCodigo": fornecedor_codigo,
            }
        )

