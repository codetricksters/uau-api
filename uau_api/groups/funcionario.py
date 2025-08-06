from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Funcionario:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_funcionario(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        codigo_pessoa: Optional[int] = None,
        codigo_funcionario: Optional[int] = None,
        matricula: Optional[str] = None,
        situacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Funcionario/ConsultarFuncionario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar os dados dos funcionários URI + api/v{version:apiVersion}/Funcionario/ConsultarFuncionario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Consulta os dados de funcionários do UAU, podendo fazer filtros pela empresa, obra, pessoa, funcionário, matrícula e situação.
        
        Deve informar obrigatoriamente o código da empresa.
        Pode informar opcionalmente o código da obra, pessoa, funcionário, matrícula e situação.
        
        VirtUau:
        
        Link para Virtuau relacionado:https://ajuda.globaltec.com.br/virtuau/cadastro-de-funcionarios/
        
        
        
        Args:
            CodigoEmpresa (int): The codigo empresa
            CodigoObra (str): The codigo obra
            CodigoPessoa (int): The codigo pessoa
            CodigoFuncionario (int): The codigo funcionario
            Matricula (str): The matricula
            Situacao (int): The situacao
        
        Parameter Structure:
        
            {
                "CodigoEmpresa": 0,
                "CodigoObra": "string",
                "CodigoPessoa": 0,
                "CodigoFuncionario": 0,
                "Matricula": "string",
                "Situacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Funcionario()
            >>> response = api._consultar_funcionario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Funcionario/ConsultarFuncionario"
        kwargs = {
            "CodigoEmpresa": codigo_empresa,
            "CodigoObra": codigo_obra,
            "CodigoPessoa": codigo_pessoa,
            "CodigoFuncionario": codigo_funcionario,
            "Matricula": matricula,
            "Situacao": situacao,
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
                        print("consultar_funcionario::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_funcionario::Server returned an error")
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
            return response.text
        except ValueError as json_err:
            print(f"Failed to parse JSON: {json_err}")
            return None

