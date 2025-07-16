from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

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
        kwargs = {
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
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
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
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
            "numeroContrato": numero_contrato,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "nomeFornecedor": nome_fornecedor,
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "ordemDeCompra": ordem_de_compra,
            "tipoResposta": tipo_resposta,
            "observacao": observacao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
            "numeroContrato": numero_contrato,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

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
        kwargs = {
            "dadosPedido": dados_pedido,
            "listaDadosItemPedido": lista_dados_item_pedido,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            
            # Check for specific error codes (HTTPStatus.BAD_REQUEST and HTTPStatus.INTERNAL_SERVER_ERROR) before raising for status
            if response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
                print(f"Server error occurred - Status Code: {response.status_code}")
                # Attempt to parse the error JSON response
                try:
                    error_data = response.json()
                    if isinstance(error_data, (dict, list)):
                        # Extract the specific error fields if they exist
                        error_data = [error_data] if isinstance(error_data, dict) else error_data
                        for idx, error_item in enumerate(error_data, start=1):
                            detalhe = error_item.get("Detalhe", "N/A")
                            mensagem = error_item.get("Mensagem", "N/A")
                            descricao = error_item.get("Descricao", "N/A")
                            
                            print(f"Error Details: [{idx}]")
                            print(f"  Detalhe: {detalhe}")
                            print(f"  Mensagem: {mensagem}")
                            print(f"  Descrição: {descricao}")
                        
                        # Return the error data for caller to handle
                        return error_data
                    else:
                        print("Is not dict or list, but it's not a JSON object.")
                        print(error_data)
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
                    print(error_data)
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print("Server returned an error, but it's not in JSON format.")
                print(http_err)
                return None
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            return None
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An unknown error occurred: {req_err}")
            return None
        
        # On success, attempt to return JSON response
        try:
            json_data = response.json()
            if isinstance(json_data, (list, dict)):
                return json_data
            else:
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

