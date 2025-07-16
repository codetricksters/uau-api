from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class RelatorioIRPF:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_pdfrel_irpf(
        self,
        vendasobras_empresa: Optional[List[Dict]] = None,
        ano_base: Optional[int] = None,
        naomostradados_venda: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `RelatorioIRPF/GerarPDFRelIRPF`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.
        
        A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
        Substituir cada parâmetro pelo valor correspondente:
        
        "Venda" - Número da Venda.
        "Obra" - Código da Obra.
        "Empresa" - Número da Empresa.
        "ano_base" - ano base para geração do IRPF.
        "naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).
          {
                "vendasobras_empresa" [
                    [
                    "Venda", 
                    "Obra", 
                    "Empresa"
                    ]
                ],
                    "ano_base": 2018,
                    "naomostradados_venda": true
            }
          
        
        
        Segue exemplo  após substituição dos parâmetros:
              {
                     "vendasobras_empresa" [
                       [
                       "838",
                       "424V",
                       "308"
                       ]
                   ],
                     "ano_base": 2021,
                     "naomostradados_venda": false
                }
          
        
        
        
        
        
        Args:
            vendasobras_empresa (List[Dict[str, Any]]): The vendasobras_empresa
            ano_base (int): The ano_base
            naomostradados_venda (int): The naomostradados_venda
        
        Parameter Structure:
        
            {
                "vendasobras_empresa": [
                    {}
                ],
                "ano_base": 0,
                "naomostradados_venda": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RelatorioIRPF()
            >>> response = api._gerarpdf_relirpf(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RelatorioIRPF/GerarPDFRelIRPF"
        kwargs = {
            "vendasobras_empresa": vendasobras_empresa,
            "ano_base": ano_base,
            "naomostradados_venda": naomostradados_venda,
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
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
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

    def gerar_pdfrel_irpfv2(
        self,
        vendasobras_empresa: Optional[List[Dict]] = None,
        ano_base: Optional[int] = None,
        naomostradados_venda: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `RelatorioIRPF/GerarPDFRelIRPFV2`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.
        
        A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
        Substituir cada parâmetro pelo valor correspondente:
        
        "Venda" - Número da Venda.
        "Obra" - Código da Obra.
        "Empresa" - Número da Empresa.
        "ano_base" - ano base para geração do IRPF.
        "naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).
          {
                "vendasobras_empresa" [
                    [
                    "Venda", 
                    "Obra", 
                    "Empresa"
                    ]
                ],
                    "ano_base": 2018,
                    "naomostradados_venda": true
            }
          
        
        
        Segue exemplo  após substituição dos parâmetros:
              {
                     "vendasobras_empresa" [
                       [
                       "838",
                       "424V",
                       "308"
                       ]
                   ],
                     "ano_base": 2021,
                     "naomostradados_venda": false
                }
          
        
        
        
        
        
        Args:
            vendasobras_empresa (List[Dict[str, Any]]): The vendasobras_empresa
            ano_base (int): The ano_base
            naomostradados_venda (int): The naomostradados_venda
        
        Parameter Structure:
        
            {
                "vendasobras_empresa": [
                    {}
                ],
                "ano_base": 0,
                "naomostradados_venda": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RelatorioIRPF()
            >>> response = api._gerarpdf_relirpfv2(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RelatorioIRPF/GerarPDFRelIRPFV2"
        kwargs = {
            "vendasobras_empresa": vendasobras_empresa,
            "ano_base": ano_base,
            "naomostradados_venda": naomostradados_venda,
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
                        print("Server returned an error, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("Server returned an error, but it's not in JSON format.")
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

