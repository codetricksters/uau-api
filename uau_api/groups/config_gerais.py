from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ConfigGerais:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def retornar_versao_bd(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `ConfigGerais/RetornarVersaoBD`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Retornar a versão do BD.
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ConfigGerais()
            >>> response = api._retornar_versaobd(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ConfigGerais/RetornarVersaoBD"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
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
                        print("retornar_versao_bd::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("retornar_versao_bd::Server returned an error")
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
                print("retornar_versao_bd::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def retornar_versao_ws(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `ConfigGerais/RetornarVersaoWS`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Retornar a versão do WS (Web Service).
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ConfigGerais()
            >>> response = api._retornar_versaows(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ConfigGerais/RetornarVersaoWS"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
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
                        print("retornar_versao_ws::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("retornar_versao_ws::Server returned an error")
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
                print("retornar_versao_ws::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

    def obter_configuracao_de_casas_decimais(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `ConfigGerais/ObterConfiguracaoDeCasasDecimais`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Retorna a configuração de quantidade de casas decimais do sistema.
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ConfigGerais()
            >>> response = api._obter_configuracao_de_casas_decimais(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ConfigGerais/ObterConfiguracaoDeCasasDecimais"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
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
                        print("obter_configuracao_de_casas_decimais::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("obter_configuracao_de_casas_decimais::Server returned an error")
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
                print("obter_configuracao_de_casas_decimais::Success, but response is not a JSON object. {response.text}")
                return None
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

