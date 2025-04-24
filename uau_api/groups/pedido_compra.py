"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class PedidoCompra:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def aprovar_pedido_compra_servico_app(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        servico: Optional[str] = None,
        num_pedido: Optional[int] = None,
        mensagem_retorno: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        cod_justificativa: Optional[int] = None,
        obs_justificativa: Optional[str] = None
    ) -> dict:
        """Aprovar o item do pedido serviço

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Aprovar um item do pedido do tipo serviço.
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/AprovarPedidoCompraServicoApp"
        return self.api.post(
            path,
            json={
                "codigo_empresa": codigo_empresa,
                "codigo_obra": codigo_obra,
                "servico": servico,
                "num_pedido": num_pedido,
                "mensagem_retorno": mensagem_retorno,
                "departamento": departamento,
                "cargo": cargo,
                "cod_justificativa": cod_justificativa,
                "obs_justificativa": obs_justificativa,
            }
        )

    def aprovar_pedido_compra_material_app(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        insumo: Optional[str] = None,
        item_ped: Optional[int] = None,
        num_pedido: Optional[int] = None,
        mensagem_retorno: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        cod_justificativa: Optional[int] = None,
        obs_justificativa: Optional[str] = None
    ) -> dict:
        """Aprovar o item do pedido de material

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Aprovar um item do pedido de material realizado.
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/AprovarPedidoCompraMaterialApp"
        return self.api.post(
            path,
            json={
                "codigo_empresa": codigo_empresa,
                "codigo_obra": codigo_obra,
                "insumo": insumo,
                "item_ped": item_ped,
                "num_pedido": num_pedido,
                "mensagem_retorno": mensagem_retorno,
                "departamento": departamento,
                "cargo": cargo,
                "cod_justificativa": cod_justificativa,
                "obs_justificativa": obs_justificativa,
            }
        )

    def gravar_pedido_de_compra_do_tipo_servico(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "2 - Serviço".

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo Serviço (2).
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServico"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_material(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gravar novo pedido de compra do tipo "0 - Material"

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo material (0).
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoMaterial"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_patrimonio(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "3 - Patrimônio"

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo Patrimônio (3).
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoPatrimonio"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_complemento(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gravar novo pedido de compra do tipo "10 - Complemento"

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo complemento (10).
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoComplemento"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_emergencial(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "6 - Emergêncial"

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo emergêncial (6).
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoEmergencial"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_adiantamento(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None,
        numero_contrato: Optional[int] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "1 -Adiantamento de Contrato"

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo adiantamento (1).
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoAdiantamento"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
                "numeroContrato": numero_contrato,
            }
        )

    def gravar_pedido_de_compra_do_tipo_regularizacao(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gravar novo pedido de compra do tipo "9 - Regularização"

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo regularização (9).
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoRegularizacao"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def confirmar_recebimento_ordem_compra_fornecedor(
        self,
        nome_fornecedor: Optional[str] = None,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        ordem_de_compra: Optional[int] = None,
        tipo_resposta: Optional[int] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """Método com finalidade de confirmar a cotação.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras Básicas:

        """
        path = "PedidoCompra/ConfirmarRecebimentoOrdemCompraFornecedor"
        return self.api.post(
            path,
            json={
                "nomeFornecedor": nome_fornecedor,
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "ordemDeCompra": ordem_de_compra,
                "tipoResposta": tipo_resposta,
                "observacao": observacao,
            }
        )

    def gravar_pedido_de_compra_do_tipo_servico_contrato(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "16 - Serviço contrato".

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo 16 - Serviço contrato.
Valida as entradas dos pedidos.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoContrato"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_contrato_material(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "4 - Contrato de Material"

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo Contrato de material (4).
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoContratoMaterial"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_servico_complemento(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "13 - Pedido serviço complemento".

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo 13 - Serviço complemento.
Valida as entradas dos pedidos.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoComplemento"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_servico_emergencial(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "11 - Pedido serviço emergencial".

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo 11 - Serviço emergencial.
Valida as entradas dos pedidos.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoEmergencial"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

    def gravar_pedido_de_compra_do_tipo_servico_adiantamento(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None,
        numero_contrato: Optional[int] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "15 - Serviço adiantamento de contrato".

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo 15 - Serviço adiantamento de contrato.
Valida as entradas dos pedidos de compras.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoAdiantamento"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
                "numeroContrato": numero_contrato,
            }
        )

    def gravar_pedido_de_compra_do_tipo_servico_regularizacao(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """Gera um novo pedido de compra do tipo "12 - Pedido serviço regularização".

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
Posição 0 = Numero do pedido;
Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);



Definição de Negócio:

Gerar um novo pedido de compra do tipo 12 - Serviço regularização.
Valida as entradas dos pedidos.


        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoRegularizacao"
        return self.api.post(
            path,
            json={
                "dadosPedido": dados_pedido,
                "listaDadosItemPedido": lista_dados_item_pedido,
            }
        )

