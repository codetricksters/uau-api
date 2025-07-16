from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ChavePix:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def by_cpfcnpj(
        self,
        cpf_cnpj: str,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `ChavePix/Pessoas/Consultar/{cpfCnpj}`
        HTTP Method: `GET`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        
        
        
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
            >>> api = ChavePix()
            >>> response = api.{cpf_cnpj}(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"ChavePix/Pessoas/Consultar/{cpfCnpj}"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.get(
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

    def deletar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ChavePix/Pessoas/Deletar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        A chave pix deve ter no máximo 77 caracteres.
        
        
        
        Args:
            cpfCnpj (str): The cnpj
            chavePix (str): The pix
            tipoChavePix (int): The chave pix
        
        Parameter Structure:
        
            {
                "cpfCnpj": "string",
                "chavePix": "string",
                "tipoChavePix": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ChavePix()
            >>> response = api._deletar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ChavePix/Pessoas/Deletar"
        kwargs = {
            "cpfCnpj": cpf_cnpj,
            "chavePix": chave_pix,
            "tipoChavePix": tipo_chave_pix,
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

    def atualizar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None,
        chave_pix_padrao: Optional[int] = None,
        ativo_inativo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ChavePix/Pessoas/Atualizar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        A chave pix deve ter no máximo 77 caracteres.
        A chave padrão deve ser: 0 - NÃO, 1 - SIM.
        O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.
        
        
        
        Args:
            cpfCnpj (str): The cnpj
            chavePix (str): The pix
            tipoChavePix (int): The chave pix
            chavePixPadrao (int): The pix padrao
            ativoInativo (int): The inativo
        
        Parameter Structure:
        
            {
                "cpfCnpj": "string",
                "chavePix": "string",
                "tipoChavePix": 0,
                "chavePixPadrao": 0,
                "ativoInativo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ChavePix()
            >>> response = api._atualizar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ChavePix/Pessoas/Atualizar"
        kwargs = {
            "cpfCnpj": cpf_cnpj,
            "chavePix": chave_pix,
            "tipoChavePix": tipo_chave_pix,
            "chavePixPadrao": chave_pix_padrao,
            "ativoInativo": ativo_inativo,
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

    def cadastrar(
        self,
        cpf_cnpj: Optional[str] = None,
        chave_pix: Optional[str] = None,
        tipo_chave_pix: Optional[int] = None,
        chave_pix_padrao: Optional[int] = None,
        ativo_inativo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ChavePix/Pessoas/Cadastrar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        
        É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        A chave pix deve ter no máximo 77 caracteres.
        A chave padrão deve ser: 0 - NÃO, 1 - SIM.
        O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.
        
        
        
        Args:
            cpfCnpj (str): The cnpj
            chavePix (str): The pix
            tipoChavePix (int): The chave pix
            chavePixPadrao (int): The pix padrao
            ativoInativo (int): The inativo
        
        Parameter Structure:
        
            {
                "cpfCnpj": "string",
                "chavePix": "string",
                "tipoChavePix": 0,
                "chavePixPadrao": 0,
                "ativoInativo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ChavePix()
            >>> response = api._cadastrar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ChavePix/Pessoas/Cadastrar"
        kwargs = {
            "cpfCnpj": cpf_cnpj,
            "chavePix": chave_pix,
            "tipoChavePix": tipo_chave_pix,
            "chavePixPadrao": chave_pix_padrao,
            "ativoInativo": ativo_inativo,
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

