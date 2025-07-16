from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ListaPrecoReferencia:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def inserir_fornecedores(
        self,
        numero_lista: Optional[int] = None,
        codigo_fornecedor: Optional[int] = None,
        cpfcnpj: Optional[str] = None,
        valor_minimo_pedfob: Optional[int] = None,
        valor_minimo_pedcif: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_termino: Optional[datetime] = None,
        contato: Optional[str] = None,
        itens_por_fornecedor: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `ListaPrecoReferencia/InserirFornecedores`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras Básicas:
        
        O usuário deve possuir permissão de inclusao no programa "ALLISTAPRECOREF"
        Para incluir um fornecedor, a lista já deve existir no sistema.
        A lista deve estar em aberto, não pode ter nenhuma confirmação de aprovação.
        
        
        
        Args:
            NumeroLista (int): The numero lista
            CodigoFornecedor (int): The codigo fornecedor
            CPFCNPJ (str): The c p f c n p j
            ValorMinimoPedFOB (int): The valor minimo ped f o b
            ValorMinimoPedCIF (int): The valor minimo ped c i f
            DataInicio (datetime): The data inicio
            DataTermino (datetime): The data termino
            Contato (str): The contato
            ItensPorFornecedor (List[Dict[str, Any]]): The itens por fornecedor
        
        Parameter Structure:
        
            {
                "NumeroLista": 0,
                "CodigoFornecedor": 0,
                "CPFCNPJ": "string",
                "ValorMinimoPedFOB": 0,
                "ValorMinimoPedCIF": 0,
                "DataInicio": "2025-04-23T13:46:13.278Z",
                "DataTermino": "2025-04-23T13:46:13.278Z",
                "Contato": "string",
                "ItensPorFornecedor": [
                    {
                        "CodigoItem": "string",
                        "PrecoItem": 0,
                        "QtdeMinima": 0,
                        "Multiplo": 0,
                        "DiasEntrega": 0,
                        "TipoFrete": 0,
                        "Observacao": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ListaPrecoReferencia()
            >>> response = api._inserir_fornecedores(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ListaPrecoReferencia/InserirFornecedores"
        kwargs = {
            "NumeroLista": numero_lista,
            "CodigoFornecedor": codigo_fornecedor,
            "CPFCNPJ": cpfcnpj,
            "ValorMinimoPedFOB": valor_minimo_pedfob,
            "ValorMinimoPedCIF": valor_minimo_pedcif,
            "DataInicio": data_inicio,
            "DataTermino": data_termino,
            "Contato": contato,
            "ItensPorFornecedor": itens_por_fornecedor,
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

    def atualizar_item_fornecedor(
        self,
        numero_lista: Optional[int] = None,
        codigo_fornecedor: Optional[int] = None,
        cpfcnpj: Optional[str] = None,
        valor_minimo_pedfob: Optional[int] = None,
        valor_minimo_pedcif: Optional[int] = None,
        data_inicio: Optional[datetime] = None,
        data_termino: Optional[datetime] = None,
        contato: Optional[str] = None,
        itens_por_fornecedor: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `ListaPrecoReferencia/AtualizarItemFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras Básicas:
        
        O usuário deve possuir permissão de alteração no programa "ALLISTAPRECOREF"
        Para atualizar um fornecedor, a lista já deve existir no sistema e o fornecedor já deve estar cadastro.
        A lista deve estar em aberto, não pode ter nenhuma confirmação de aprovação.
        
        
        
        Args:
            NumeroLista (int): The numero lista
            CodigoFornecedor (int): The codigo fornecedor
            CPFCNPJ (str): The c p f c n p j
            ValorMinimoPedFOB (int): The valor minimo ped f o b
            ValorMinimoPedCIF (int): The valor minimo ped c i f
            DataInicio (datetime): The data inicio
            DataTermino (datetime): The data termino
            Contato (str): The contato
            ItensPorFornecedor (List[Dict[str, Any]]): The itens por fornecedor
        
        Parameter Structure:
        
            {
                "NumeroLista": 0,
                "CodigoFornecedor": 0,
                "CPFCNPJ": "string",
                "ValorMinimoPedFOB": 0,
                "ValorMinimoPedCIF": 0,
                "DataInicio": "2025-04-23T13:46:13.284Z",
                "DataTermino": "2025-04-23T13:46:13.284Z",
                "Contato": "string",
                "ItensPorFornecedor": [
                    {
                        "CodigoItem": "string",
                        "PrecoItem": 0,
                        "QtdeMinima": 0,
                        "Multiplo": 0,
                        "DiasEntrega": 0,
                        "TipoFrete": 0,
                        "Observacao": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ListaPrecoReferencia()
            >>> response = api._atualizar_item_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ListaPrecoReferencia/AtualizarItemFornecedor"
        kwargs = {
            "NumeroLista": numero_lista,
            "CodigoFornecedor": codigo_fornecedor,
            "CPFCNPJ": cpfcnpj,
            "ValorMinimoPedFOB": valor_minimo_pedfob,
            "ValorMinimoPedCIF": valor_minimo_pedcif,
            "DataInicio": data_inicio,
            "DataTermino": data_termino,
            "Contato": contato,
            "ItensPorFornecedor": itens_por_fornecedor,
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

    def consultar_lista_preco_referencia(
        self,
        numero_lista: Optional[int] = None,
        data_validade: Optional[datetime] = None,
        status: Optional[int] = None,
        fornecedorcnpj: Optional[str] = None,
        fornecedor_codigo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ListaPrecoReferencia/ConsultarListaPrecoReferencia`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras Básicas:
        
        Pelo menos um parâmetro deve ser preenchido para consulta.
        Parâmetros:
        CodigoLista: Parâmetro principal, caso seja informado irá sobrepor todos os outros.
        FornecedorCodigo: Fará a pesquisa pelo código do fornecedor, caso não possua o CNPJ.
        FornecedorCNPJ: Fará a pesquisa pelo CNPJ do fornecedor, caso não possua o código do fornecedor.
        DataValidade: Data de validade da lista de preço.
        Status:   
        0 - Em aberto
        1 - Em Análise
        2 - Aprovada
        3 - Migrada
        
        
        
        
        
        
        
        Args:
            NumeroLista (int): The numero lista
            DataValidade (datetime): The data validade
            Status (int): The status
            FornecedorCNPJ (str): The fornecedor c n p j
            FornecedorCodigo (int): The fornecedor codigo
        
        Parameter Structure:
        
            {
                "NumeroLista": 0,
                "DataValidade": "2025-04-23T13:46:13.293Z",
                "Status": 0,
                "FornecedorCNPJ": "string",
                "FornecedorCodigo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ListaPrecoReferencia()
            >>> response = api._consultar_lista_preco_referencia(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ListaPrecoReferencia/ConsultarListaPrecoReferencia"
        kwargs = {
            "NumeroLista": numero_lista,
            "DataValidade": data_validade,
            "Status": status,
            "FornecedorCNPJ": fornecedorcnpj,
            "FornecedorCodigo": fornecedor_codigo,
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

