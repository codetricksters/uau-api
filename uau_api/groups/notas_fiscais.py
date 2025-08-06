from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class NotasFiscais:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_nfentrada(
        self,
        listanf_entrada: Optional[List[Dict]] = None,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        cnpj_fornecedor: Optional[str] = None,
        codigo_fornecedor: Optional[str] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None,
        tipo_periodo: Optional[Any] = None
    ) -> dict:
        """
        
        Endpoint: `NotasFiscais/ConsultarNFEntrada`
        HTTP Method: `POST`
        
        Implementation Notes:
         Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Ao menos uma chave de pesquisa deve ser preenchida sendo elas ([CodigoEmpresa],
          [CnpjFornecedor], [CodigoFornecedor], [DataInicial], [ListaNFEntrada]).
        Caso tenha informado a propriedade da Obra, a Empresa torna-se obrigatória.
        Preenchimento da [DataInicial] torna [DataFinal] obrigatória.
        Preenchimento da [DataFinal] torna [DataInicial] obrigatória.
        Obra só vai achar informação se a nota estiver vinculada a um processo.
        [ListaNFEntrada] Cada objeto deve ter obrigatoriamente o [CodigoEmpresa] e o [NumeroNotaFiscal ou NumeroNotaFiscalEletronica]
          6.1 NumeroNotaFiscal = Número de controle da nota fiscal (Obs: no retorno dos dados esse valor fica no campo Numero)
          6.2 NumeroNotaFiscalEletronica = Número da nota fiscal eletrônica, informado na DANFE ou NFS-e (Obs: no retorno dos dados esse valor fica no campo NumeroNotaFiscal)
        
        
        
        Args:
            ListaNFEntrada (List[Dict[str, Any]]): The lista n f entrada
            CodigoEmpresa (int): The codigo empresa
            CodigoObra (str): The codigo obra
            CnpjFornecedor (str): The cnpj fornecedor
            CodigoFornecedor (str): The codigo fornecedor
            DataInicial (datetime): The data inicial
            DataFinal (datetime): The data final
            TipoPeriodo (int): The tipo periodo
        
        Parameter Structure:
        
            {
                "ListaNFEntrada": [
                    {
                        "CodigoEmpresa": 0,
                        "NumeroNotaFiscal": 0,
                        "NumeroNotaFiscalEletronica": "string"
                    }
                ],
                "CodigoEmpresa": 0,
                "CodigoObra": "string",
                "CnpjFornecedor": "string",
                "CodigoFornecedor": "string",
                "DataInicial": "2025-04-23T13:46:13.469Z",
                "DataFinal": "2025-04-23T13:46:13.469Z",
                "TipoPeriodo": 1
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = NotasFiscais()
            >>> response = api._consultarnf_entrada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "NotasFiscais/ConsultarNFEntrada"
        kwargs = {
            "ListaNFEntrada": listanf_entrada,
            "CodigoEmpresa": codigo_empresa,
            "CodigoObra": codigo_obra,
            "CnpjFornecedor": cnpj_fornecedor,
            "CodigoFornecedor": codigo_fornecedor,
            "DataInicial": data_inicial,
            "DataFinal": data_final,
            "TipoPeriodo": tipo_periodo,
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
                        print("consultar_nfentrada::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("consultar_nfentrada::Server returned an error")
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

    def salvar_arquivo_xmlnotafiscal_entrada(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `NotasFiscais/SalvarArquivoXMLnotafiscalEntrada`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Poderá ser enviado uma lista de arquivos XML.
        Será permitido no máximo uma lista com 20 arquivos.
        Tipo do arquivo XML [TipoXML]
           0 para NF-e
           1 para CT-e
           2 para NFS-e,
        Arquivo XML da nota fiscal (Texto do arquivo) [ArquivoXML].
        
        
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "TipoXML": 0,
                    "ArquivoXML": "string"
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = NotasFiscais()
            >>> response = api._salvar_arquivoxm_lnotafiscal_entrada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "NotasFiscais/SalvarArquivoXMLnotafiscalEntrada"
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
                        print("salvar_arquivo_xmlnotafiscal_entrada::Is not dict or list, but it's not a JSON object.")
                        return None
                except ValueError:
                    print("salvar_arquivo_xmlnotafiscal_entrada::Server returned an error")
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

