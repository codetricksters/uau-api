from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Espelho:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def alterar_status_unidade(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None,
        novo_status_unidade: Optional[int] = None,
        motivo_alteracao: Optional[str] = None,
        categoria_status_personalizacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/AlterarStatusUnidade`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoProduto (int): The produto
            numeroPersonalizacao (int): The personalizacao
            novoStatusUnidade (int): The status unidade
            motivoAlteracao (str): The alteracao
            categoriaStatusPersonalizacao (int): The status personalizacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoProduto": 0,
                "numeroPersonalizacao": 0,
                "novoStatusUnidade": 0,
                "motivoAlteracao": "string",
                "categoriaStatusPersonalizacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._alterar_status_unidade(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/AlterarStatusUnidade"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoProduto": codigo_produto,
            "numeroPersonalizacao": numero_personalizacao,
            "novoStatusUnidade": novo_status_unidade,
            "motivoAlteracao": motivo_alteracao,
            "categoriaStatusPersonalizacao": categoria_status_personalizacao,
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
                        print("alterar_status_unidade::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("alterar_status_unidade::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("alterar_status_unidade::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_espelhos_venda(
        self,
        usuario_logado: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/ConsultarEspelhosVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario_logado (str): The usuario_logado
        
        Parameter Structure:
        
            {
                "usuario_logado": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._consultar_espelhos_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/ConsultarEspelhosVenda"
        kwargs = {
            "usuario_logado": usuario_logado,
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
                        print("consultar_espelhos_venda::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_espelhos_venda::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("consultar_espelhos_venda::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def retornar_menor_preco_person(
        self,
        tipo_contrato: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_categ_preco: Optional[str] = None,
        numero_person: Optional[int] = None,
        empresa: Optional[int] = None,
        data_categ_preco_produto: Optional[datetime] = None,
        porc_preco_minimo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/RetornarMenorPrecoPerson`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            tipoContrato (int): The contrato
            codProduto (int): The produto
            codCategPreco (str): The categ preco
            numeroPerson (int): The person
            empresa (int): The empresa
            dataCategPrecoProduto (datetime): The categ preco produto
            porcPrecoMinimo (int): The preco minimo
        
        Parameter Structure:
        
            {
                "tipoContrato": 0,
                "codProduto": 0,
                "codCategPreco": "string",
                "numeroPerson": 0,
                "empresa": 0,
                "dataCategPrecoProduto": "2025-04-23T13:46:13.128Z",
                "porcPrecoMinimo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._retornar_menor_preco_person(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/RetornarMenorPrecoPerson"
        kwargs = {
            "tipoContrato": tipo_contrato,
            "codProduto": cod_produto,
            "codCategPreco": cod_categ_preco,
            "numeroPerson": numero_person,
            "empresa": empresa,
            "dataCategPrecoProduto": data_categ_preco_produto,
            "porcPrecoMinimo": porc_preco_minimo,
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
                        print("retornar_menor_preco_person::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("retornar_menor_preco_person::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("retornar_menor_preco_person::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def atualizar_campos_customizados(
        self,
        campos_custom: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/AtualizarCamposCustomizados`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            campos_custom (Dict[str, Any]): The campos_custom
        
        Parameter Structure:
        
            {
                "campos_custom": {
                    "ListChavesUnid": [
                        {
                            "Empresa": 0,
                            "Obra": "string",
                            "Produto": 0,
                            "CodPerson": 0
                        }
                    ],
                    "ListValoresUnid": [
                        {
                            "CampoCustom": "string",
                            "CampoCustomValor": "string"
                        }
                    ]
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._atualizar_campos_customizados(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/AtualizarCamposCustomizados"
        kwargs = {
            "campos_custom": campos_custom,
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
                        print("atualizar_campos_customizados::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("atualizar_campos_customizados::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("atualizar_campos_customizados::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_unidade_per_por_chave(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/ConsultarUnidadePerPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoProduto (int): The produto
            numeroPersonalizacao (int): The personalizacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoProduto": 0,
                "numeroPersonalizacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._consultar_unidade_per_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/ConsultarUnidadePerPorChave"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoProduto": codigo_produto,
            "numeroPersonalizacao": numero_personalizacao,
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
                        print("consultar_unidade_per_por_chave::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_unidade_per_por_chave::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("consultar_unidade_per_por_chave::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def busca_unidades_de_acordo_com_where(
        self,
        where: Optional[str] = None,
        retorna_venda: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/BuscaUnidadesDeAcordoComWhere`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            where (str): The where
            retorna_venda (int): The retorna_venda
        
        Parameter Structure:
        
            {
                "where": "string",
                "retorna_venda": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._busca_unidades_de_acordo_com_where(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/BuscaUnidadesDeAcordoComWhere"
        kwargs = {
            "where": where,
            "retorna_venda": retorna_venda,
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
                        print("busca_unidades_de_acordo_com_where::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("busca_unidades_de_acordo_com_where::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("busca_unidades_de_acordo_com_where::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def alterar_data_entrega_chaves_unidade(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None,
        data_entrega_chaves: Optional[datetime] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/AlterarDataEntregaChavesUnidade`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoProduto (int): The produto
            numeroPersonalizacao (int): The personalizacao
            dataEntregaChaves (datetime): The entrega chaves
            observacao (str): The observacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoProduto": 0,
                "numeroPersonalizacao": 0,
                "dataEntregaChaves": "2025-04-23T13:46:13.149Z",
                "observacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._alterar_data_entrega_chaves_unidade(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/AlterarDataEntregaChavesUnidade"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoProduto": codigo_produto,
            "numeroPersonalizacao": numero_personalizacao,
            "dataEntregaChaves": data_entrega_chaves,
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
                        print("alterar_data_entrega_chaves_unidade::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("alterar_data_entrega_chaves_unidade::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("alterar_data_entrega_chaves_unidade::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def consultar_personalizacoes_com_precos(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        num_produto: Optional[int] = None,
        cod_obra: Optional[str] = None,
        num_personalizacao: Optional[int] = None,
        consultarapenasnao_vendidos: Optional[bool] = None,
        tipo_contrato: Optional[int] = None,
        datatabela_preco: Optional[datetime] = None,
        campos_person: Optional[str] = None,
        status_person: Optional[str] = None,
        num_espelho: Optional[int] = None,
        tipocontrato_grafico: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/ConsultarPersonalizacoesComPrecos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            usuario (str): The usuario
            empresa (int): The empresa
            num_produto (int): The num_produto
            cod_obra (str): The cod_obra
            num_personalizacao (int): The num_personalizacao
            consultarapenasnao_vendidos (int): The consultarapenasnao_vendidos
            tipo_contrato (int): The tipo_contrato
            datatabela_preco (datetime): The datatabela_preco
            campos_person (str): The campos_person
            status_person (str): The status_person
            num_espelho (int): The num_espelho
            tipocontrato_grafico (int): The tipocontrato_grafico
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "empresa": 0,
                "num_produto": 0,
                "cod_obra": "string",
                "num_personalizacao": 0,
                "consultarapenasnao_vendidos": true,
                "tipo_contrato": 0,
                "datatabela_preco": "2025-04-23T13:46:13.153Z",
                "campos_person": "string",
                "status_person": "string",
                "num_espelho": 0,
                "tipocontrato_grafico": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._consultar_personalizacoes_com_precos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/ConsultarPersonalizacoesComPrecos"
        kwargs = {
            "usuario": usuario,
            "empresa": empresa,
            "num_produto": num_produto,
            "cod_obra": cod_obra,
            "num_personalizacao": num_personalizacao,
            "consultarapenasnao_vendidos": consultarapenasnao_vendidos,
            "tipo_contrato": tipo_contrato,
            "datatabela_preco": datatabela_preco,
            "campos_person": campos_person,
            "status_person": status_person,
            "num_espelho": num_espelho,
            "tipocontrato_grafico": tipocontrato_grafico,
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
                        print("consultar_personalizacoes_com_precos::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_personalizacoes_com_precos::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("consultar_personalizacoes_com_precos::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def busca_unidades_de_acordo_com_where_detalhado(
        self,
        where: Optional[str] = None,
        retorna_venda: Optional[bool] = None,
        data_tabela_preco: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Espelho/BuscaUnidadesDeAcordoComWhereDetalhado`
        HTTP Method: `POST`
        
        Implementation Notes:
        
        parâmetros de request da classe BuscaUnidadesDeAcordoComWhereDetalhadoRequest
        
        
        
        Args:
            where (str): The where
            retorna_venda (int): The retorna_venda
            data_tabela_preco (datetime): The data_tabela_preco
        
        Parameter Structure:
        
            {
                "where": "string",
                "retorna_venda": true,
                "data_tabela_preco": "2025-04-23T13:46:13.157Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Espelho()
            >>> response = api._busca_unidades_de_acordo_com_where_detalhado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Espelho/BuscaUnidadesDeAcordoComWhereDetalhado"
        kwargs = {
            "where": where,
            "retorna_venda": retorna_venda,
            "data_tabela_preco": data_tabela_preco,
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
                        print("busca_unidades_de_acordo_com_where_detalhado::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("busca_unidades_de_acordo_com_where_detalhado::Server returned an error")
                    return None
            
            # Raise an error for other HTTP error statuses
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
            # Attempt to return server's JSON error details for other HTTP errors
            try:
                return response.json()
            except ValueError:
                print(f"Server returned {http_err}")
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
                print("busca_unidades_de_acordo_com_where_detalhado::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

