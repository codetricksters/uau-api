from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class CobrancaPix:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def pix_por_parcelas(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/PixPorParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        O objetivo desta rota de API é permitir a consulta e retorno das informações dos PIX gerados para uma determinada parcela ou lista de parcelas
        Serão retornados os dados do PIX, caso tenha sido gerado para a(s) parcela(s) requisitada(s)
        Limite máximo de 50 parcelas por requisição
        
        
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "Empresa": 0,
                    "Obra": "string",
                    "NumeroVenda": 0,
                    "NumeroParcela": 0,
                    "TipoParcela": "string",
                    "NumeroParcelaGeral": 0
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._pix_por_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/PixPorParcelas"
        kwargs = parameters if parameters is not None else {}
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
                        print("pix_por_parcelas::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("pix_por_parcelas::Server returned an error")
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

    def reimpressao_pix(
        self,
        tx_id: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/ReimpressaoPix`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        O objetivo desta rota de API é permitir a consulta e retorno das informações do pix de modo que o usuário possa fazer a impressão 
          dos dados de cobrança.
        Será retornado o PDF completo e o QRCode em base64.
        Será retornado o texto do Pix Copia e Cola.
        
        Instituições bancárias suportadas: 
        
        341 = Banco Itaú
        
        756 = Banco Sicoob
        
        237 = Banco Bradesco
        
        246 = Banco Abc
        
        
        
        
        Args:
            TxId (str): The tx id
        
        Parameter Structure:
        
            {
                "TxId": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._reimpressao_pix(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/ReimpressaoPix"
        kwargs = {
            "TxId": tx_id,
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
                        print("reimpressao_pix::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("reimpressao_pix::Server returned an error")
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

    def consultar_pix_status(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/ConsultarPixStatus`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        O objetivo desta rota de API e permitir a consulta do status do PIX 
        
        Instituições bancárias suportadas: 
        
        341 = Banco Itaú
        246 = Banco Abc
        341 = Banco Itaú
        756 = Banco Sicoob
        237 = Banco Bradesco
        
        Pré requisito:
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        URL + /api/v{version}/Pix/GerarCobrancaPIX 
          Anexos:
        
        
        Exemplo Postman: [ALTERAR EXEMPLO]
        
        
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "TxId": "string"
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._consultar_pix_status(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/ConsultarPixStatus"
        kwargs = parameters if parameters is not None else {}
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
                        print("consultar_pix_status::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_pix_status::Server returned an error")
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

    def gerar_cobranca_venda(
        self,
        data_de_calculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        usar_padrao_pix_avulso: Optional[bool] = None,
        agrupar_parcelas: Optional[bool] = None,
        padrao_cobranca: Optional[int] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/GerarCobrancaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        O objetivo desta rota de API é permitir o registro de cobrança por PIX junto à instituição financeira.
        O BASE64 gerado é somente o QR Code do PIX.
        Instituições bancárias suportadas:
        
        341 Banco Itaú
        756 Banco Sicoob
        237 Banco Bradesco
        246 Banco ABC
        
        
        
        Pré Requisitos:
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        URL + /api/v{version}/Venda/GerarCobrancaPIX
        
        
        
        
        Args:
            DataDeCalculo (datetime): The data de calculo
            Antecipar (int): The antecipar
            UsarPadraoPixAvulso (int): The usar padrao pix avulso
            AgruparParcelas (int): The agrupar parcelas
            PadraoCobranca (int): The padrao cobranca
            Parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "DataDeCalculo": "2025-04-23T13:46:12.715Z",
                "Antecipar": true,
                "UsarPadraoPixAvulso": true,
                "AgruparParcelas": true,
                "PadraoCobranca": 0,
                "Parcelas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "NumeroVenda": 0,
                        "NumeroParcela": 0,
                        "TipoParcela": "string",
                        "NumeroParcelaGeral": 0,
                        "ValorDesconto": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._gerar_cobranca_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/GerarCobrancaVenda"
        kwargs = {
            "DataDeCalculo": data_de_calculo,
            "Antecipar": antecipar,
            "UsarPadraoPixAvulso": usar_padrao_pix_avulso,
            "AgruparParcelas": agrupar_parcelas,
            "PadraoCobranca": padrao_cobranca,
            "Parcelas": parcelas,
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
                        print("gerar_cobranca_venda::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("gerar_cobranca_venda::Server returned an error")
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

    def gerar_cobranca_proposta(
        self,
        data_de_calculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        usar_padrao_pix_avulso: Optional[bool] = None,
        agrupar_parcelas: Optional[bool] = None,
        padrao_cobranca: Optional[int] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Pix/GerarCobrancaProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        O objetivo desta rota de API é permitir o registro de cobrança por PIX junto a instituição financeira 
        O BASE64 gerado é somente o QRCODE do PIX
        
        Instituições bancárias suportadas: 
        
        341 = Banco Itaú
        756 = Banco Sicoob
        237 = Banco Bradesco
        246 = Banco Abc
        
        Pré requisito:
        
        Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
        URL + /api/v{version}/Venda/GerarCobrancaPIX
        
        
        
        
        
        Args:
            DataDeCalculo (datetime): The data de calculo
            Antecipar (int): The antecipar
            UsarPadraoPixAvulso (int): The usar padrao pix avulso
            AgruparParcelas (int): The agrupar parcelas
            PadraoCobranca (int): The padrao cobranca
            Parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "DataDeCalculo": "2025-04-23T13:46:12.721Z",
                "Antecipar": true,
                "UsarPadraoPixAvulso": true,
                "AgruparParcelas": true,
                "PadraoCobranca": 0,
                "Parcelas": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "NumeroProposta": 0,
                        "NumeroParcela": 0,
                        "TipoParcela": "string",
                        "NumeroParcelaGeral": 0,
                        "ValorDesconto": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = CobrancaPix()
            >>> response = api._gerar_cobranca_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Pix/GerarCobrancaProposta"
        kwargs = {
            "DataDeCalculo": data_de_calculo,
            "Antecipar": antecipar,
            "UsarPadraoPixAvulso": usar_padrao_pix_avulso,
            "AgruparParcelas": agrupar_parcelas,
            "PadraoCobranca": padrao_cobranca,
            "Parcelas": parcelas,
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
                        print("gerar_cobranca_proposta::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("gerar_cobranca_proposta::Server returned an error")
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

