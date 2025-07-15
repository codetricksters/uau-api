from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Contabil:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_saldo_de_contas(
        self,
        empresa: Optional[int] = None,
        mes_ano: Optional[datetime] = None,
        tipo: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Contabil/ConsultarSaldoDeContas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar os saldo das contas conbaeis com a URI + /api/v{version}/Contabil/SaldoDeContas
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Pode-se consultar o saldo das contas contábeis do UAU, podendo fazer filtros pela empresa, 
          tipo, ano e mês, com isso é possível fazer a integração da parte de saldos contábeis com o UAU
        
        Deve informar obrigatoriamente todos os parâmetros da request.
        
        VirtUau:
        
        http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Contabil/Contabil_ConsultarSaldoDeContas
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777058/
        
        
        
        Args:
            Empresa (int): The empresa
            MesAno (datetime): The mes ano
            Tipo (str): The tipo
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "MesAno": "2025-04-23T13:46:12.820Z",
                "Tipo": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Contabil()
            >>> response = api._consultar_saldo_de_contas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Contabil/ConsultarSaldoDeContas"
        kwargs = {
            "Empresa": empresa,
            "MesAno": mes_ano,
            "Tipo": tipo,
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
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
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

    def consultar_contas_contabeis(
        self,
        empresa: Optional[int] = None,
        ano: Optional[int] = None,
        conta: Optional[str] = None,
        descricao_conta: Optional[str] = None,
        limitar_retorno_em: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Contabil/ConsultarContasContabeis`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar os dados das contas contábeis com a URI + /api/v{version}/Contabil/ConsultarContasContabeis
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Consulta os dados de contas contábeis do UAU, podendo fazer filtros pela empresa,
          ano, conta ou descrição da conta, com o intuito de buscar informações de uma conta contábil.
        
        Deve informar obrigatoriamente o código da empresa, ano da máscara de plano de contas e o a propriedade limitarRetornoEm.
        Pode informar opcionalmente o código da conta ou a descrição da conta.
        Os parâmetros (DescricaoConta, Conta) podem conter o sinal de porcentagem (%), 
          caso necessite fazer a consulta a partir de um caractere curinga. Exemplos: %UAU, %UAU%, UAU%.
        
        VirtUau:
        
        http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Contabil/Contabil_ConsultarContasContabeis
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777058/
        
        
        
        Args:
            Empresa (int): The empresa
            Ano (int): The ano
            Conta (str): The conta
            DescricaoConta (str): The descricao conta
            LimitarRetornoEm (int): The limitar retorno em
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Ano": 0,
                "Conta": "string",
                "DescricaoConta": "string",
                "LimitarRetornoEm": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Contabil()
            >>> response = api._consultar_contas_contabeis(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Contabil/ConsultarContasContabeis"
        kwargs = {
            "Empresa": empresa,
            "Ano": ano,
            "Conta": conta,
            "DescricaoConta": descricao_conta,
            "LimitarRetornoEm": limitar_retorno_em,
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
                    if isinstance(error_data, dict):
                        # Extract the specific error fields if they exist
                        detalhe = error_data.get("Detalhe", "N/A")
                        mensagem = error_data.get("Mensagem", "N/A")
                        descricao = error_data.get("Descricao", "N/A")
                        
                        print("Error Details:")
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

