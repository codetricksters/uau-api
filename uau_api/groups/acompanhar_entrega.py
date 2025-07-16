from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class AcompanharEntrega:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_processos(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanharEntrega/ConsultarProcessos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras Básicas:
        
        Retorna os processos e itens que estão com o acompanhamento de entrega pendente para uma dada empresa e obra informada.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanharEntrega()
            >>> response = api._consultar_processos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanharEntrega/ConsultarProcessos"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
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

    def acompanhar_pre_entrega(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        chave_nota_fiscal: Optional[str] = None,
        chave_nota_fiscal_frete: Optional[str] = None,
        codigo_do_boleto: Optional[str] = None,
        codigo_do_boleto_frete: Optional[str] = None,
        itens: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanharEntrega/AcompanharPreEntrega`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras Básicas:
        
        O usuário deve possuir acesso na empresa e obra informada.
        O usuário deve possuir permissão de alteração no programa FIANALISE.
        O número do processo deve ser um processo existente.
        A NF e NF de frete devem ser númericos e válidos.
        O código de barras deve ser númerico e possuir no mínimo 36 caracteres.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Processo (int): The processo
            ChaveNotaFiscal (str): The chave nota fiscal
            ChaveNotaFiscalFrete (str): The chave nota fiscal frete
            CodigoDoBoleto (str): The codigo do boleto
            CodigoDoBoletoFrete (str): The codigo do boleto frete
            Itens (List[Dict[str, Any]]): The itens
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Processo": 0,
                "ChaveNotaFiscal": "string",
                "ChaveNotaFiscalFrete": "string",
                "CodigoDoBoleto": "string",
                "CodigoDoBoletoFrete": "string",
                "Itens": [
                    {
                        "CodigoItem": "string",
                        "Quantidade": 0,
                        "Preco": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanharEntrega()
            >>> response = api._acompanhar_pre_entrega(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanharEntrega/AcompanharPreEntrega"
        kwargs = {
            "Empresa": empresa,
            "Obra": obra,
            "Processo": processo,
            "ChaveNotaFiscal": chave_nota_fiscal,
            "ChaveNotaFiscalFrete": chave_nota_fiscal_frete,
            "CodigoDoBoleto": codigo_do_boleto,
            "CodigoDoBoletoFrete": codigo_do_boleto_frete,
            "Itens": itens,
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

