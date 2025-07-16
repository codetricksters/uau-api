from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Estrutura:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def excluir_estrutura(
        self,
        codigo_estrutura: Optional[int] = None,
        sequencia: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/ExcluirEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite excluir uma estrutura completa caso o valor do parâmetro sequência seja (0 - raiz) ou apenas um item da estrutura(Caso o tipo do item seja "0 - Nível", também serão excluídos os itens filhos).
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            codigoEstrutura (int): The estrutura
            sequencia (str): The sequencia
        
        Parameter Structure:
        
            {
                "codigoEstrutura": 0,
                "sequencia": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._excluir_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/ExcluirEstrutura"
        kwargs = {
            "codigoEstrutura": codigo_estrutura,
            "sequencia": sequencia,
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
                print("Success, but response is not a JSON object.")
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def inserir_estrutura(
        self,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/InserirEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite inserir uma estrutura. Após inserir, poderá vincular os itens da estrutura.
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._inserir_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/InserirEstrutura"
        kwargs = {
            "descricao": descricao,
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
                print("Success, but response is not a JSON object.")
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def excluir_item_de_estrutura(
        self,
        codigo_item: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/ExcluirItemDeEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite excluir um item de estrutura que não está sendo utilizado no cadastro de estrutura, orçamento, contrato ou serviços do planejamento .
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            codigoItem (str): The item
        
        Parameter Structure:
        
            {
                "codigoItem": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._excluir_item_de_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/ExcluirItemDeEstrutura"
        kwargs = {
            "codigoItem": codigo_item,
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
                print("Success, but response is not a JSON object.")
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def inserir_item_de_estrutura(
        self,
        codigo_item: Optional[str] = None,
        descricao_item: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/InserirItemDeEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite inserir um item de estrutura. Após inserir, poderá se utilizado no cadastro de estrutura e ser vinculado em orçamento, contrato e serviços do planejamento.
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            codigoItem (str): The item
            descricaoItem (str): The item
        
        Parameter Structure:
        
            {
                "codigoItem": "string",
                "descricaoItem": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._inserir_item_de_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/InserirItemDeEstrutura"
        kwargs = {
            "codigoItem": codigo_item,
            "descricaoItem": descricao_item,
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
                print("Success, but response is not a JSON object.")
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def inserir_item_na_estrutura(
        self,
        codigo_estrutura: Optional[int] = None,
        tipo_estrutura: Optional[int] = None,
        sequencia: Optional[str] = None,
        codigo_item: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/InserirItemNaEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite inserir item em uma estrutura. Após concluir o cadastro da estrutura, poderá ser vinculada em orçamento, contrato e serviços do planejamento. 
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            codigoEstrutura (int): The estrutura
            tipoEstrutura (int): The estrutura
            sequencia (str): The sequencia
            codigoItem (str): The item
        
        Parameter Structure:
        
            {
                "codigoEstrutura": 0,
                "tipoEstrutura": 0,
                "sequencia": "string",
                "codigoItem": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._inserir_item_na_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/InserirItemNaEstrutura"
        kwargs = {
            "codigoEstrutura": codigo_estrutura,
            "tipoEstrutura": tipo_estrutura,
            "sequencia": sequencia,
            "codigoItem": codigo_item,
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
                print("Success, but response is not a JSON object.")
                print("Success, but response is not a JSON object.")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

