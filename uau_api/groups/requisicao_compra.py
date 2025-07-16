from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class RequisicaoCompra:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def aprovar_requisicoes_compra(
        self,
        requisicoes: Optional[List[Dict]] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        cod_justificativa: Optional[int] = None,
        obs_justificativa: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RequisicaoCompra/AprovarRequisicoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        
        É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA
        
        
        
        Args:
            Requisicoes (List[Dict[str, Any]]): The requisicoes
            Departamento (str): The departamento
            Cargo (str): The cargo
            CodJustificativa (int): The cod justificativa
            ObsJustificativa (str): The obs justificativa
        
        Parameter Structure:
        
            {
                "Requisicoes": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "NumRequisicao": 0
                    }
                ],
                "Departamento": "string",
                "Cargo": "string",
                "CodJustificativa": 0,
                "ObsJustificativa": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RequisicaoCompra()
            >>> response = api._aprovar_requisicoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RequisicaoCompra/AprovarRequisicoesCompra"
        kwargs = {
            "Requisicoes": requisicoes,
            "Departamento": departamento,
            "Cargo": cargo,
            "CodJustificativa": cod_justificativa,
            "ObsJustificativa": obs_justificativa,
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

    def desaprovar_requisicoes_compra(
        self,
        requisicoes: Optional[List[Dict]] = None,
        cod_justificativa_desaprovacao: Optional[int] = None,
        obs_justificativa_desaprovacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RequisicaoCompra/DesaprovarRequisicoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        
        É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA
        Será permitido desaprovar apenas requisições de compra com estágio 0 - Criada
        
        
        
        Args:
            Requisicoes (List[Dict[str, Any]]): The requisicoes
            CodJustificativaDesaprovacao (int): The cod justificativa desaprovacao
            ObsJustificativaDesaprovacao (str): The obs justificativa desaprovacao
        
        Parameter Structure:
        
            {
                "Requisicoes": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "NumRequisicao": 0
                    }
                ],
                "CodJustificativaDesaprovacao": 0,
                "ObsJustificativaDesaprovacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RequisicaoCompra()
            >>> response = api._desaprovar_requisicoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RequisicaoCompra/DesaprovarRequisicoesCompra"
        kwargs = {
            "Requisicoes": requisicoes,
            "CodJustificativaDesaprovacao": cod_justificativa_desaprovacao,
            "ObsJustificativaDesaprovacao": obs_justificativa_desaprovacao,
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

