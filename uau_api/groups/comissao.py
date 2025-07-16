from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Comissao:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_vendedores(
        self,
        codigo_modelo_comissao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Comissao/ConsultarVendedores`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            codigoModeloComissao (int): The modelo comissao
        
        Parameter Structure:
        
            {
                "codigoModeloComissao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Comissao()
            >>> response = api._consultar_vendedores(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Comissao/ConsultarVendedores"
        kwargs = {
            "codigoModeloComissao": codigo_modelo_comissao,
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

    def atualizar_status_comissao(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Comissao/AtualizarStatusComissao`
        HTTP Method: `POST`
        
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
        
        
        
        
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "numeroVenda": 0,
                    "codigoPessoa": 0,
                    "numeroComissao": 0,
                    "statusControleComissao": 0,
                    "loginUsuario": "string"
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Comissao()
            >>> response = api._atualizar_status_comissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Comissao/AtualizarStatusComissao"
        kwargs = parameters if parameters is not None else {}
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

    def consultar_modelo_comissao(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        codigo_vendedor: Optional[int] = None,
        data_venda: Optional[str] = None,
        qtde_parcelas: Optional[int] = None,
        lista_unidades: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Comissao/ConsultarModeloComissao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario;
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consulta o Modelo de Comissão disponível para utilização em uma proposta de venda.
        
        Informação:
        
        A propriedade "Padrão" no retorno indica o modelo de comissão padrão utilizado pelo vendedor, no entanto, ela será retornada como True.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            codigoVendedor (int): The vendedor
            dataVenda (str): The venda
            qtdeParcelas (int): The parcelas
            listaUnidades (List[Dict[str, Any]]): The unidades
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "codigoVendedor": 0,
                "dataVenda": "string",
                "qtdeParcelas": 0,
                "listaUnidades": [
                    {
                        "codigoProduto": 0,
                        "codigoPersonalizacao": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Comissao()
            >>> response = api._consultar_modelo_comissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Comissao/ConsultarModeloComissao"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "codigoVendedor": codigo_vendedor,
            "dataVenda": data_venda,
            "qtdeParcelas": qtde_parcelas,
            "listaUnidades": lista_unidades,
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
        """
        
        Endpoint: `Comissao/ConsultarEstruturaComissao`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            codigoVendedor (int): The vendedor
            codigoHierarquia (int): The hierarquia
            numeroComissao (int): The comissao
            valorComissao (int): The comissao
            produtos (List[Dict[str, Any]]): The produtos
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "codigoVendedor": 0,
                "codigoHierarquia": 0,
                "numeroComissao": 0,
                "valorComissao": 0,
                "produtos": [
                    {
                        "codigoProduto": 0,
                        "codigoPersonalizacao": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Comissao()
            >>> response = api._consultar_estrutura_comissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Comissao/ConsultarEstruturaComissao"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "codigoVendedor": codigo_vendedor,
            "codigoHierarquia": codigo_hierarquia,
            "numeroComissao": numero_comissao,
            "valorComissao": valor_comissao,
            "produtos": produtos,
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

