from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ExtratoDoCliente:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_pdfextrato_cliente(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        tipo_ordenacao: Optional[int] = None,
        valor_antecipado: Optional[bool] = None,
        data_prorrogacao: Optional[bool] = None,
        ocultar_personalizacao: Optional[bool] = None,
        ocultar_usuario: Optional[bool] = None,
        data_calculo: Optional[datetime] = None,
        residuo_ira_compor_valor_total: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ExtratoDoCliente/GerarPDFExtratoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Preencher as opções de visualização do extrato nos módulos Vendas/Shopping, menu Utilitários, submenu Configurações extrato da venda (Visão Cliente)
        
        Obs.: Parâmetros para impressão deste extrato são configurados na tela descrita neste virtuau: https://ajuda.globaltec.com.br/virtuau/configuracao-extrato-de-vendas-visao-cliente
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            numVenda (int): The venda
            tipoOrdenacao (int): The ordenacao
            valorAntecipado (int): The antecipado
            dataProrrogacao (int): The prorrogacao
            ocultarPersonalizacao (int): The personalizacao
            ocultarUsuario (int): The usuario
            dataCalculo (datetime): The calculo
            residuoIraComporValorTotal (int): The ira compor valor total
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "numVenda": 0,
                "tipoOrdenacao": 0,
                "valorAntecipado": true,
                "dataProrrogacao": true,
                "ocultarPersonalizacao": true,
                "ocultarUsuario": true,
                "dataCalculo": "2025-04-23T13:46:13.189Z",
                "residuoIraComporValorTotal": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ExtratoDoCliente()
            >>> response = api._gerarpdf_extrato_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ExtratoDoCliente/GerarPDFExtratoCliente"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "numVenda": num_venda,
            "tipoOrdenacao": tipo_ordenacao,
            "valorAntecipado": valor_antecipado,
            "dataProrrogacao": data_prorrogacao,
            "ocultarPersonalizacao": ocultar_personalizacao,
            "ocultarUsuario": ocultar_usuario,
            "dataCalculo": data_calculo,
            "residuoIraComporValorTotal": residuo_ira_compor_valor_total,
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

    def gerar_pdfextrato_cliente_v2(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        tipo_ordenacao: Optional[int] = None,
        valor_antecipado: Optional[bool] = None,
        data_prorrogacao: Optional[bool] = None,
        ocultar_personalizacao: Optional[bool] = None,
        ocultar_usuario: Optional[bool] = None,
        data_calculo: Optional[datetime] = None,
        residuo_ira_compor_valor_total: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `ExtratoDoCliente/GerarPDFExtratoClienteV2`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Preencher as opções de visualização do extrato nos módulos Vendas/Shopping, menu Utilitários, submenu Configurações extrato da venda (Visão Cliente)
        
        Obs.: Parâmetros para impressão deste extrato são configurados na tela descrita neste virtuau: https://ajuda.globaltec.com.br/virtuau/configuracao-extrato-de-vendas-visao-cliente
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            numVenda (int): The venda
            tipoOrdenacao (int): The ordenacao
            valorAntecipado (int): The antecipado
            dataProrrogacao (int): The prorrogacao
            ocultarPersonalizacao (int): The personalizacao
            ocultarUsuario (int): The usuario
            dataCalculo (datetime): The calculo
            residuoIraComporValorTotal (int): The ira compor valor total
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "numVenda": 0,
                "tipoOrdenacao": 0,
                "valorAntecipado": true,
                "dataProrrogacao": true,
                "ocultarPersonalizacao": true,
                "ocultarUsuario": true,
                "dataCalculo": "2025-04-23T13:46:13.194Z",
                "residuoIraComporValorTotal": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ExtratoDoCliente()
            >>> response = api._gerarpdf_extrato_clientev2(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ExtratoDoCliente/GerarPDFExtratoClienteV2"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "numVenda": num_venda,
            "tipoOrdenacao": tipo_ordenacao,
            "valorAntecipado": valor_antecipado,
            "dataProrrogacao": data_prorrogacao,
            "ocultarPersonalizacao": ocultar_personalizacao,
            "ocultarUsuario": ocultar_usuario,
            "dataCalculo": data_calculo,
            "residuoIraComporValorTotal": residuo_ira_compor_valor_total,
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

    def consultar_saldo_cessoes_direito_anteriores(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `ExtratoDoCliente/ConsultarSaldoCessoesDireitoAnteriores`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna o somatório do saldo já pago das vendas anteriores de cessão de direito
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_venda (int): The num_venda
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_venda": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ExtratoDoCliente()
            >>> response = api._consultar_saldo_cessoes_direito_anteriores(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ExtratoDoCliente/ConsultarSaldoCessoesDireitoAnteriores"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_venda": num_venda,
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

    def consultar_dados_demonstrativo_pagto_cliente(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        tipos_parc: Optional[str] = None,
        tipo_ordenacao: Optional[int] = None,
        mostrara_pagas: Optional[bool] = None,
        princ_juros: Optional[bool] = None,
        descontopor_adiantamento: Optional[bool] = None,
        valor_antecipado: Optional[bool] = None,
        nome_fantasia: Optional[bool] = None,
        ocultapref_custas: Optional[bool] = None,
        data_calculo: Optional[datetime] = None,
        exibir_data_deposito: Optional[bool] = None
    ) -> dict:
        """
          Contém as chamadas dos métodos ConsultarItensRecebidas e ConsultarParcelasRecebidasCliente retornando um dataset e suas tabelas.
          OBS.: A instruçãoa [tipos_parc] se refere à parcelas que não devem ser mostradas no extrato do cliente, se enviar vazio, vai mostrar todas.
        
        Endpoint: `ExtratoDoCliente/ConsultarDadosDemonstrativoPagtoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna informações das parcelas pagas, informações do cliente e unidades/produtos de uma determinada venda.
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            num_venda (int): The num_venda
            tipos_parc (str): The tipos_parc
            tipo_ordenacao (int): The tipo_ordenacao
            mostrara_pagas (int): The mostrara_pagas
            princ_juros (int): The princ_juros
            descontopor_adiantamento (int): The descontopor_adiantamento
            valor_antecipado (int): The valor_antecipado
            nome_fantasia (int): The nome_fantasia
            ocultapref_custas (int): The ocultapref_custas
            dataCalculo (datetime): The calculo
            exibirDataDeposito (int): The data deposito
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "num_venda": 0,
                "tipos_parc": "string",
                "tipo_ordenacao": 0,
                "mostrara_pagas": true,
                "princ_juros": true,
                "descontopor_adiantamento": true,
                "valor_antecipado": true,
                "nome_fantasia": true,
                "ocultapref_custas": true,
                "dataCalculo": "2025-04-23T13:46:13.203Z",
                "exibirDataDeposito": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = ExtratoDoCliente()
            >>> response = api._consultar_dados_demonstrativo_pagto_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "ExtratoDoCliente/ConsultarDadosDemonstrativoPagtoCliente"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "num_venda": num_venda,
            "tipos_parc": tipos_parc,
            "tipo_ordenacao": tipo_ordenacao,
            "mostrara_pagas": mostrara_pagas,
            "princ_juros": princ_juros,
            "descontopor_adiantamento": descontopor_adiantamento,
            "valor_antecipado": valor_antecipado,
            "nome_fantasia": nome_fantasia,
            "ocultapref_custas": ocultapref_custas,
            "dataCalculo": data_calculo,
            "exibirDataDeposito": exibir_data_deposito,
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

