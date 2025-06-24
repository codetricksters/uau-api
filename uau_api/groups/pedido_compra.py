from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class PedidoCompra:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

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
        """
        
        Endpoint: `PedidoCompra/AprovarPedidoCompraServicoApp`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Aprovar um item do pedido do tipo serviço.
        Valida as entradas dos pedidos de compras.
        
        
        
        Args:
            codigo_empresa (int): The codigo_empresa
            codigo_obra (str): The codigo_obra
            servico (str): The servico
            num_pedido (int): The num_pedido
            mensagem_retorno (str): The mensagem_retorno
            departamento (str): The departamento
            cargo (str): The cargo
            cod_justificativa (int): The cod_justificativa
            obs_justificativa (str): The obs_justificativa
        
        Parameter Structure:
        
            {
                "codigo_empresa": 0,
                "codigo_obra": "string",
                "servico": "string",
                "num_pedido": 0,
                "mensagem_retorno": "string",
                "departamento": "string",
                "cargo": "string",
                "cod_justificativa": 0,
                "obs_justificativa": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._aprovar_pedido_compra_servico_app(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/AprovarPedidoCompraServicoApp"
        try:
            response = self.api.post(
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
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

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
        """
        
        Endpoint: `PedidoCompra/AprovarPedidoCompraMaterialApp`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Aprovar um item do pedido de material realizado.
        Valida as entradas dos pedidos de compras.
        
        
        
        Args:
            codigo_empresa (int): The codigo_empresa
            codigo_obra (str): The codigo_obra
            insumo (str): The insumo
            item_ped (int): The item_ped
            num_pedido (int): The num_pedido
            mensagem_retorno (str): The mensagem_retorno
            departamento (str): The departamento
            cargo (str): The cargo
            cod_justificativa (int): The cod_justificativa
            obs_justificativa (str): The obs_justificativa
        
        Parameter Structure:
        
            {
                "codigo_empresa": 0,
                "codigo_obra": "string",
                "insumo": "string",
                "item_ped": 0,
                "num_pedido": 0,
                "mensagem_retorno": "string",
                "departamento": "string",
                "cargo": "string",
                "cod_justificativa": 0,
                "obs_justificativa": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._aprovar_pedido_compra_material_app(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/AprovarPedidoCompraMaterialApp"
        try:
            response = self.api.post(
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
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_servico(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoServico`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoServico": "string",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "unidade": "string",
                        "origemServico": 0,
                        "numOrcamento": 0,
                        "itemOrcamento": "string",
                        "mesPl": "string",
                        "itemPl": "string",
                        "produtoPl": 0,
                        "contratoPl": 0,
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "dataInicio": "2025-04-23T13:46:13.620Z",
                        "especificacao": "string",
                        "observacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "categoria": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServico"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_material(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoMaterial`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoInsumo": "string",
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "unidade": "string",
                        "controleEstoque": 0,
                        "dataEntrega": "2025-04-23T13:46:13.627Z",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "observacao": "string",
                        "especificacao": "string",
                        "codDepreciacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "codJustificativa": 0,
                        "justificativa": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_material(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoMaterial"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_patrimonio(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoPatrimonio`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoInsumo": "string",
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "unidade": "string",
                        "controleEstoque": 0,
                        "dataEntrega": "2025-04-23T13:46:13.633Z",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "observacao": "string",
                        "especificacao": "string",
                        "codDepreciacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "codJustificativa": 0,
                        "justificativa": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_patrimonio(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoPatrimonio"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_complemento(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoComplemento`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoInsumo": "string",
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "unidade": "string",
                        "controleEstoque": 0,
                        "dataEntrega": "2025-04-23T13:46:13.640Z",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "observacao": "string",
                        "especificacao": "string",
                        "codDepreciacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "codJustificativa": 0,
                        "justificativa": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_complemento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoComplemento"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_emergencial(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoEmergencial`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoInsumo": "string",
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "unidade": "string",
                        "controleEstoque": 0,
                        "dataEntrega": "2025-04-23T13:46:13.645Z",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "observacao": "string",
                        "especificacao": "string",
                        "codDepreciacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "codJustificativa": 0,
                        "justificativa": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_emergencial(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoEmergencial"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_adiantamento(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None,
        numero_contrato: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoAdiantamento`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
            numeroContrato (int): The contrato
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoInsumo": "string",
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "unidade": "string",
                        "controleEstoque": 0,
                        "dataEntrega": "2025-04-23T13:46:13.652Z",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "observacao": "string",
                        "especificacao": "string",
                        "codDepreciacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "codJustificativa": 0,
                        "justificativa": "string"
                    }
                ],
                "numeroContrato": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_adiantamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoAdiantamento"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                    "numeroContrato": numero_contrato,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_regularizacao(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoRegularizacao`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoInsumo": "string",
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "unidade": "string",
                        "controleEstoque": 0,
                        "dataEntrega": "2025-04-23T13:46:13.658Z",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "observacao": "string",
                        "especificacao": "string",
                        "codDepreciacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "codJustificativa": 0,
                        "justificativa": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_regularizacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoRegularizacao"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def confirmar_recebimento_ordem_compra_fornecedor(
        self,
        nome_fornecedor: Optional[str] = None,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        ordem_de_compra: Optional[int] = None,
        tipo_resposta: Optional[int] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/ConfirmarRecebimentoOrdemCompraFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras Básicas:
        
        
        Args:
            nomeFornecedor (str): The fornecedor
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            ordemDeCompra (int): The de compra
            tipoResposta (int): The resposta
            observacao (str): The observacao
        
        Parameter Structure:
        
            {
                "nomeFornecedor": "string",
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "ordemDeCompra": 0,
                "tipoResposta": 0,
                "observacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._confirmar_recebimento_ordem_compra_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/ConfirmarRecebimentoOrdemCompraFornecedor"
        try:
            response = self.api.post(
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
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_servico_contrato(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoServicoContrato`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoServico": "string",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "unidade": "string",
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "dataInicio": "2025-04-23T13:46:13.669Z",
                        "especificacao": "string",
                        "observacao": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoContrato"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_contrato_material(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoContratoMaterial`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoInsumo": "string",
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "unidade": "string",
                        "controleEstoque": 0,
                        "dataEntrega": "2025-04-23T13:46:13.675Z",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "observacao": "string",
                        "especificacao": "string",
                        "categoria": "string",
                        "codJustificativa": 0,
                        "justificativa": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_contrato_material(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoContratoMaterial"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_servico_complemento(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoServicoComplemento`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoServico": "string",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "unidade": "string",
                        "origemServico": 0,
                        "numOrcamento": 0,
                        "itemOrcamento": "string",
                        "mesPl": "string",
                        "itemPl": "string",
                        "produtoPl": 0,
                        "contratoPl": 0,
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "dataInicio": "2025-04-23T13:46:13.680Z",
                        "especificacao": "string",
                        "observacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "categoria": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_complemento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoComplemento"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_servico_emergencial(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoServicoEmergencial`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoServico": "string",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "unidade": "string",
                        "origemServico": 0,
                        "numOrcamento": 0,
                        "itemOrcamento": "string",
                        "mesPl": "string",
                        "itemPl": "string",
                        "produtoPl": 0,
                        "contratoPl": 0,
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "dataInicio": "2025-04-23T13:46:13.687Z",
                        "especificacao": "string",
                        "observacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "categoria": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_emergencial(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoEmergencial"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_servico_adiantamento(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None,
        numero_contrato: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoServicoAdiantamento`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
            numeroContrato (int): The contrato
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoServico": "string",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "unidade": "string",
                        "origemServico": 0,
                        "numOrcamento": 0,
                        "itemOrcamento": "string",
                        "mesPl": "string",
                        "itemPl": "string",
                        "produtoPl": 0,
                        "contratoPl": 0,
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "dataInicio": "2025-04-23T13:46:13.693Z",
                        "especificacao": "string",
                        "observacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "categoria": "string"
                    }
                ],
                "numeroContrato": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_adiantamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoAdiantamento"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                    "numeroContrato": numero_contrato,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def gravar_pedido_de_compra_do_tipo_servico_regularizacao(
        self,
        dados_pedido: Optional[Dict] = None,
        lista_dados_item_pedido: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `PedidoCompra/GravarPedidoDeCompraDoTipoServicoRegularizacao`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            dadosPedido (Dict[str, Any]): The pedido
            listaDadosItemPedido (List[Dict[str, Any]]): The dados item pedido
        
        Parameter Structure:
        
            {
                "dadosPedido": {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "considerarVinculoSemSaldoMes": true,
                    "codigoObraFiscal": "string",
                    "usuario": "string",
                    "observacao": "string"
                },
                "listaDadosItemPedido": [
                    {
                        "codigoServico": "string",
                        "quantidade": 0,
                        "precoOrcado": 0,
                        "unidade": "string",
                        "origemServico": 0,
                        "numOrcamento": 0,
                        "itemOrcamento": "string",
                        "mesPl": "string",
                        "itemPl": "string",
                        "produtoPl": 0,
                        "contratoPl": 0,
                        "CAP": "string",
                        "CategoriaMovimentacaoFinanceira": "string",
                        "dataInicio": "2025-04-23T13:46:13.700Z",
                        "especificacao": "string",
                        "observacao": "string",
                        "listaVinculo": [
                            {
                                "produtoPl": 0,
                                "contratoPl": 0,
                                "itemPl": "string",
                                "servicoPl": "string",
                                "mesPl": "string",
                                "codigoInsumoPl": "string",
                                "quantidadeVinculo": 0,
                                "numeroItemContrato": 0
                            }
                        ],
                        "categoria": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_regularizacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "PedidoCompra/GravarPedidoDeCompraDoTipoServicoRegularizacao"
        try:
            response = self.api.post(
                path,
                json={
                    "dadosPedido": dados_pedido,
                    "listaDadosItemPedido": lista_dados_item_pedido,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

