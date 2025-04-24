"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Comissao:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_vendedores(
        self,
        codigo_modelo_comissao: Optional[int] = None
    ) -> dict:
        """Consulta os vendedores da estrutura de comissão.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario;
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta os vendedores da estrutura de comissão;
Caso não seja informado o código da comissão retornará todos os vendedores relacionados à estrutura de comissão;
Caso seja informado um código que não esteja relacionado a estrutura de comissão o sistema retornará "vazio".

Informação:

Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


        """
        path = "Comissao/ConsultarVendedores"
        return self.api.post(
            path,
            json={
                "codigoModeloComissao": codigo_modelo_comissao,
            }
        )

    def atualizar_status_comissao(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """Atualizar status de pagamento da comissão.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Alterar os status de pagamento das comissões de uma pessoa(beneficiário).
Não é possível cancelar ou reativar status de pagamento da comissão via Endpoint.
Todos os campos são obrigatórios informar.
Os dados informados passam por validações.
Não é permitido marcar como "pago" comissões que geram processos de pagamento
Não é permitido reativar ou cancelar status de pagamento da comissão.
Status disponíveis:
0 - Não liberada
1 - Liberada
2 - Paga
4 - Bloqueada




        """
        path = "Comissao/AtualizarStatusComissao"
        return self.api.post(
            path,
            json=parameters if parameters is not None else {}
        )

    def consultar_modelo_comissao(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        codigo_vendedor: Optional[int] = None,
        data_venda: Optional[str] = None,
        qtde_parcelas: Optional[int] = None,
        lista_unidades: Optional[List[Dict]] = None
    ) -> dict:
        """Consulta os Modelos de Comissão disponíveis

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario;
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta o Modelo de Comissão disponível para utilização em uma proposta de venda.

Informação:

A propriedade "Padrão" no retorno indica o modelo de comissão padrão utilizado pelo vendedor, no entanto, ela será retornada como True.


        """
        path = "Comissao/ConsultarModeloComissao"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "codigoVendedor": codigo_vendedor,
                "dataVenda": data_venda,
                "qtdeParcelas": qtde_parcelas,
                "listaUnidades": lista_unidades,
            }
        )

    def consultar_estrutura_comissao(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        codigo_vendedor: Optional[int] = None,
        codigo_hierarquia: Optional[int] = None,
        numero_comissao: Optional[int] = None,
        valor_comissao: Optional[int] = None,
        produtos: Optional[List[Dict]] = None
    ) -> dict:
        """Consulta a estrutura de comissão do vendedor

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta a estrutura de comissão do vendedor.
A propriedade SobreRecebimento está descontinuada, mas continuará retornando as informações nela conforme o preenchimento da nova propriedade, chamada RegraLiberacao.
A propriedade codigo da hierarquia se tornou obsoleta, precisamos apenas do número da comissão que é um número único no sistema.
A propriedade numModelo é referente a nova estrutura de modelos de comissão.
Caso seja informado uma pessoa que não participa do modelo de comissão, o sistema não irá montar a estrutura;


        """
        path = "Comissao/ConsultarEstruturaComissao"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "codigoVendedor": codigo_vendedor,
                "codigoHierarquia": codigo_hierarquia,
                "numeroComissao": numero_comissao,
                "valorComissao": valor_comissao,
                "produtos": produtos,
            }
        )

