from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Cotacao:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def atualizar_item_cotacao(
        self,
        lista_itens_cotacao: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/AtualizarItemCotacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AtualizarItemCotacao
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Permite atualizar os dados dos itens de cotação, seja ela de material ou de serviço.
        Para cotações específicas que forem pertencentes à cotação geral, serão alteradas somente a quantidade e a marca (no caso de cotação de material). 
          Os demais valores só serão alterados se a cotação geral for informada na requisição.
        Para cotações que forem pertencentes à cotação geral, durante a execução se não existir insumo para um dos itens da cotação informada a execução irá finalizar, efetivando somente a atualização dos itens de cotação anteriores.
        Informações de IPI, ICMS e Marca só estão relacionadas às cotações de material, portanto podem ser omitidas na requisição.
        
        
        
        Args:
            listaItensCotacao (List[Dict[str, Any]]): The itens cotacao
        
        Parameter Structure:
        
            {
                "listaItensCotacao": [
                    {
                        "empresa": 0,
                        "cotacao": 0,
                        "origem": 0,
                        "fornecedor": 0,
                        "insumo": "string",
                        "quantidade": 0,
                        "preco": 0,
                        "porcentagemIPI": 0,
                        "valorIPI": 0,
                        "marca": "string",
                        "porcentagemICMS": 0,
                        "valorICMS": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._atualizar_item_cotacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/AtualizarItemCotacao"
        kwargs = {
            "listaItensCotacao": lista_itens_cotacao,
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

    def conta_cotacoes_aprov_mob(
        self,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/ContaCotacoesAprovMob`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/ContaCotacoesMob
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consultar a quantidade de cotações de material e serviço que possuem simulações que o usuário pode aprovar.
        
        
        
        Args:
            usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._conta_cotacoes_aprov_mob(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/ContaCotacoesAprovMob"
        kwargs = {
            "usuario": usuario,
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

    def aprovar_simulacoes_compra(
        self,
        simulacoes: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/AprovarSimulacoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        É necessário permissão de aprovação para o programa ALSIMULCOT
        
        
        
        Args:
            Simulacoes (List[Dict[str, Any]]): The simulacoes
        
        Parameter Structure:
        
            {
                "Simulacoes": [
                    {
                        "codigoEmpresa": 0,
                        "numeroSimulacao": 0,
                        "numeroCotacao": 0,
                        "tipoAprovacaoCotacaoServico": 0,
                        "Codigojustificativa": 0,
                        "Observacaojustificativa": "string",
                        "departamento": "string",
                        "cargo": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._aprovar_simulacoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/AprovarSimulacoesCompra"
        kwargs = {
            "Simulacoes": simulacoes,
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

    def adicionar_fornecedor_cotacao(
        self,
        cod_fornecedor: Optional[int] = None,
        cnpj_fornecedor: Optional[str] = None,
        numero_cotacao: Optional[int] = None,
        numero_cotacao_geral: Optional[int] = None,
        empresa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/AdicionarFornecedorCotacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AdicionarFornecedorCotacao
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Permite vincular um fornecedor a uma cotação em aberto de material ou serviço.
        Para identificação do fornecedor, são aceitos o código ou CPF/CNPJ deste no sistema.
        Para vínculo do fornecedor a uma cotação específica, o código dessa cotação, empresa e, o CPF/CNPJ ou código do fornecedor devem ser informados.
        Para vínculo do fornecedor a uma cotação geral, somente o código da cotação geral e, o CPF/CNPJ ou código do fornecedor devem ser informados.
        
        
        
        Args:
            codFornecedor (int): The fornecedor
            CNPJFornecedor (str): The c n p j fornecedor
            numeroCotacao (int): The cotacao
            numeroCotacaoGeral (int): The cotacao geral
            empresa (int): The empresa
        
        Parameter Structure:
        
            {
                "codFornecedor": 0,
                "CNPJFornecedor": "string",
                "numeroCotacao": 0,
                "numeroCotacaoGeral": 0,
                "empresa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._adicionar_fornecedor_cotacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/AdicionarFornecedorCotacao"
        kwargs = {
            "codFornecedor": cod_fornecedor,
            "CNPJFornecedor": cnpj_fornecedor,
            "numeroCotacao": numero_cotacao,
            "numeroCotacaoGeral": numero_cotacao_geral,
            "empresa": empresa,
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

    def buscar_itens_cotacao_fornecedor(
        self,
        empresa: Optional[int] = None,
        cotacao: Optional[int] = None,
        fornecedor: Optional[int] = None,
        origem: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/BuscarItensCotacaoFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Cotacao/BuscarItensCotacaoFornecedor
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Permite consultar os dados de itens de cotação de material ou serviço por código do fornecedor.
        Somente cotações com status "0 - Criada" são retornadas.
        
        
        
        Args:
            empresa (int): The empresa
            cotacao (int): The cotacao
            fornecedor (int): The fornecedor
            origem (int): The origem
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "cotacao": 0,
                "fornecedor": 0,
                "origem": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._buscar_itens_cotacao_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/BuscarItensCotacaoFornecedor"
        kwargs = {
            "empresa": empresa,
            "cotacao": cotacao,
            "fornecedor": fornecedor,
            "origem": origem,
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

    def consultar_itens_cotacao_por_obra(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        cotacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/ConsultarItensCotacaoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Permite consultar itens da cotação de material ou serviço que esteja aguardando confirmação por obra, filtrando por empresa, obra e número da cotação.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
            cotacao (int): The cotacao
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string",
                "cotacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._consultar_itens_cotacao_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/ConsultarItensCotacaoPorObra"
        kwargs = {
            "empresa": empresa,
            "obra": obra,
            "cotacao": cotacao,
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

    def buscar_cotacao_aberta_fornecedor(
        self,
        cnpj: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/BuscarCotacaoAbertaFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio: 
        
        Permite consultar os dados de cotações de material ou serviço que estão disponíveis para o fornecedor. Os tipos de cotações retornadas são:
        0 - Cot. material regular
        1 - Cot. material adiant. contrato
        2 - Cot. serviço regular
        3 - Cot. patrimônio
        4 - Cot. material contrato
        5 - Cot. material emergencial
        6 - Cot. manutenção de patrimônio
        7 - Cot. material regularização
        8 - Cot. material complemento
        9 - Cot. serviço emergencial
        10 - Cot. serviço regularização
        11 - Cot. serviço complemento
        12 - Cot. serviço adiant. contrato
        13 - Cot. serviço contrato
        
        
        É obrigatório informar o CNPJ do fornecedor para realizar a consulta.
        
        
        
        Args:
            cnpj (str): The cnpj
        
        Parameter Structure:
        
            {
                "cnpj": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._buscar_cotacao_aberta_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/BuscarCotacaoAbertaFornecedor"
        kwargs = {
            "cnpj": cnpj,
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

    def aprovar_confirmacao_cotacao_por_obra(
        self,
        lista_confirmar_aprovacao_cotacao: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/AprovarConfirmacaoCotacaoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Possibilita aprovar a confirmação da cotação de material ou serviço por obra.
        
        
        
        Args:
            listaConfirmarAprovacaoCotacao (List[Dict[str, Any]]): The confirmar aprovacao cotacao
        
        Parameter Structure:
        
            {
                "listaConfirmarAprovacaoCotacao": [
                    {
                        "empresa": 0,
                        "obra": "string",
                        "NumCotacao": 0,
                        "numSimulacao": 0,
                        "tipoCotacao": 0,
                        "totalCotacao": 0,
                        "departamentoUsr": "string",
                        "cargoUsr": "string",
                        "usuario": "string",
                        "codJustificativa": 0,
                        "obsJustificativa": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._aprovar_confirmacao_cotacao_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/AprovarConfirmacaoCotacaoPorObra"
        kwargs = {
            "listaConfirmarAprovacaoCotacao": lista_confirmar_aprovacao_cotacao,
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

    def remover_aprovacao_simulacoes_compra(
        self,
        simulacoes: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/RemoverAprovacaoSimulacoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        É necessário permissão de exclusão para o programa ALCONFCOT caso a cotação esteja no fechamento de compra
          e permissão exclusão para o programa ALANALISE caso a cotação esteja na confirmação de cotação por obra.
        
        
        
        Args:
            Simulacoes (List[Dict[str, Any]]): The simulacoes
        
        Parameter Structure:
        
            {
                "Simulacoes": [
                    {
                        "codigoEmpresa": 0,
                        "numeroSimulacao": 0,
                        "numeroCotacao": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._remover_aprovacao_simulacoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/RemoverAprovacaoSimulacoesCompra"
        kwargs = {
            "Simulacoes": simulacoes,
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

    def atualizar_condicao_pagamento_entrega(
        self,
        empresa: Optional[int] = None,
        cotacao: Optional[int] = None,
        numero_cotacao_geral: Optional[int] = None,
        fornecedor: Optional[int] = None,
        dias_entrega: Optional[int] = None,
        quantidade_entrega: Optional[int] = None,
        intervalo_entrega: Optional[int] = None,
        dias_pagamento: Optional[int] = None,
        quantidade_parcela: Optional[int] = None,
        intervalo_parcela: Optional[int] = None,
        tipo_frete: Optional[int] = None,
        tipo_pagamento: Optional[int] = None,
        condicao_pagamento: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/AtualizarCondicaoPagamentoEntrega`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AtualizarCondicaoPagamentoEntrega
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Permite atualizar os dados de condição de entrega da cotação, bem como dias para entrega, quantidade de parcela, intervalo das parcelas, entre outros.
        A condição de pagamento utilizada será sempre SOBRE A ENTREGA.
        Para atualizar as condições de pagamento de uma cotação específica, o código dessa cotação e empresa devem ser informados.
        Para atualizar as condições de pagamento de uma cotação geral, somente o código da cotação geral deve ser informado.
        
        
        
        Args:
            empresa (int): The empresa
            cotacao (int): The cotacao
            numeroCotacaoGeral (int): The cotacao geral
            fornecedor (int): The fornecedor
            diasEntrega (int): The entrega
            quantidadeEntrega (int): The entrega
            intervaloEntrega (int): The entrega
            diasPagamento (int): The pagamento
            quantidadeParcela (int): The parcela
            intervaloParcela (int): The parcela
            tipoFrete (int): The frete
            tipoPagamento (int): The pagamento
            CondicaoPagamento (str): The condicao pagamento
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "cotacao": 0,
                "numeroCotacaoGeral": 0,
                "fornecedor": 0,
                "diasEntrega": 0,
                "quantidadeEntrega": 0,
                "intervaloEntrega": 0,
                "diasPagamento": 0,
                "quantidadeParcela": 0,
                "intervaloParcela": 0,
                "tipoFrete": 0,
                "tipoPagamento": 0,
                "CondicaoPagamento": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._atualizar_condicao_pagamento_entrega(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/AtualizarCondicaoPagamentoEntrega"
        kwargs = {
            "empresa": empresa,
            "cotacao": cotacao,
            "numeroCotacaoGeral": numero_cotacao_geral,
            "fornecedor": fornecedor,
            "diasEntrega": dias_entrega,
            "quantidadeEntrega": quantidade_entrega,
            "intervaloEntrega": intervalo_entrega,
            "diasPagamento": dias_pagamento,
            "quantidadeParcela": quantidade_parcela,
            "intervaloParcela": intervalo_parcela,
            "tipoFrete": tipo_frete,
            "tipoPagamento": tipo_pagamento,
            "CondicaoPagamento": condicao_pagamento,
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

    def consultar_aprovacao_da_cotacao_por_obra(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_simulacao: Optional[int] = None,
        numero_cotacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/ConsultarAprovacaoDaCotacaoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        São consultadas as aprovações já realizadas para uma determinada cotação de material ou serviço.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            numeroSimulacao (int): The simulacao
            numeroCotacao (int): The cotacao
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "numeroSimulacao": 0,
                "numeroCotacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._consultar_aprovacao_da_cotacao_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/ConsultarAprovacaoDaCotacaoPorObra"
        kwargs = {
            "codigoEmpresa": codigo_empresa,
            "codigoObra": codigo_obra,
            "numeroSimulacao": numero_simulacao,
            "numeroCotacao": numero_cotacao,
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

    def reprovar_confirmacoes_cotacao_por_obra(
        self,
        confirmacoes_cotacao: Optional[List[Dict]] = None,
        justificativa_reprovacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/ReprovarConfirmacoesCotacaoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        É necessário permissão de exclusão para o programa ALCONFCOT caso a cotação esteja no fechamento de compra
          e permissão exclusão para o programa ALANALISE caso a cotação esteja na confirmação de cotação por obra.
        
        
        
        Args:
            ConfirmacoesCotacao (List[Dict[str, Any]]): The confirmacoes cotacao
            justificativaReprovacao (str): The reprovacao
        
        Parameter Structure:
        
            {
                "ConfirmacoesCotacao": [
                    {
                        "codigoEmpresa": 0,
                        "numeroSimulacao": 0,
                        "numeroCotacao": 0
                    }
                ],
                "justificativaReprovacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._reprovar_confirmacoes_cotacao_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/ReprovarConfirmacoesCotacaoPorObra"
        kwargs = {
            "ConfirmacoesCotacao": confirmacoes_cotacao,
            "justificativaReprovacao": justificativa_reprovacao,
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

    def consultar_cotacoes_confirmacao_pendente(
        self,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        lista_emp_obras: Optional[List[Dict]] = None,
        cotacao: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/ConsultarCotacoesConfirmacaoPendente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consulta cotações de material e serviço que estão com as confirmações pendentes.
        
        
        
        Args:
            usuario (str): The usuario
            departamento (str): The departamento
            cargo (str): The cargo
            listaEmpObras (List[Dict[str, Any]]): The emp obras
            cotacao (int): The cotacao
        
        Parameter Structure:
        
            {
                "usuario": "string",
                "departamento": "string",
                "cargo": "string",
                "listaEmpObras": [
                    {
                        "empresa": 0,
                        "obra": "string"
                    }
                ],
                "cotacao": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._consultar_cotacoes_confirmacao_pendente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/ConsultarCotacoesConfirmacaoPendente"
        kwargs = {
            "usuario": usuario,
            "departamento": departamento,
            "cargo": cargo,
            "listaEmpObras": lista_emp_obras,
            "cotacao": cotacao,
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

    def consultar_quantidade_cotacao_pendente_por_obra(
        self,
        login_usuario: Optional[str] = None,
        codigo_departamento: Optional[str] = None,
        codigo_cargo: Optional[str] = None,
        lista_emp_obras: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/ConsultarQuantidadeCotacaoPendentePorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Verifica a quantidade de cotações de material e serviço com pendência na aprovação filtrando por obra.
        
        
        
        Args:
            loginUsuario (str): The usuario
            codigoDepartamento (str): The departamento
            codigoCargo (str): The cargo
            listaEmpObras (List[Dict[str, Any]]): The emp obras
        
        Parameter Structure:
        
            {
                "loginUsuario": "string",
                "codigoDepartamento": "string",
                "codigoCargo": "string",
                "listaEmpObras": [
                    {
                        "empresa": 0,
                        "obra": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._consultar_quantidade_cotacao_pendente_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/ConsultarQuantidadeCotacaoPendentePorObra"
        kwargs = {
            "loginUsuario": login_usuario,
            "codigoDepartamento": codigo_departamento,
            "codigoCargo": codigo_cargo,
            "listaEmpObras": lista_emp_obras,
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

    def consultar_quantidade_cotacao_pendente_por_obra_mob(
        self,
        login_usuario: Optional[str] = None,
        codigo_departamento: Optional[str] = None,
        codigo_cargo: Optional[str] = None,
        lista_emp_obras: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/ConsultarQuantidadeCotacaoPendentePorObraMob`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consultar a quantidade de cotações de material e serviço com pendência na aprovação filtrando por obra.
        
        
        
        Args:
            loginUsuario (str): The usuario
            codigoDepartamento (str): The departamento
            codigoCargo (str): The cargo
            listaEmpObras (List[Dict[str, Any]]): The emp obras
        
        Parameter Structure:
        
            {
                "loginUsuario": "string",
                "codigoDepartamento": "string",
                "codigoCargo": "string",
                "listaEmpObras": [
                    {
                        "empresa": 0,
                        "obra": "string"
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._consultar_quantidade_cotacao_pendente_por_obra_mob(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/ConsultarQuantidadeCotacaoPendentePorObraMob"
        kwargs = {
            "loginUsuario": login_usuario,
            "codigoDepartamento": codigo_departamento,
            "codigoCargo": codigo_cargo,
            "listaEmpObras": lista_emp_obras,
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

    def consultar_justificativas_aprovacao_fora_sequencia(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/ConsultarJustificativasAprovacaoForaSequencia`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consultar as justificativas que podem ser utilizadas em aprovações de confirmação de cotação de material ou serviço que esteja fora da sequência do usuário (Controle de aprovações).
        
        
        
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
            >>> api = Cotacao()
            >>> response = api._consultar_justificativas_aprovacao_fora_sequencia(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/ConsultarJustificativasAprovacaoForaSequencia"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
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

    def inserir_altera_coment_forn_frete(
        self,
        empresa: Optional[int] = None,
        codigo_fornecedor: Optional[int] = None,
        cotacao: Optional[int] = None,
        cond_pagto: Optional[int] = None,
        tipo_coment: Optional[int] = None,
        efet_pgto_parc: Optional[int] = None,
        dtvenc_ini: Optional[str] = None,
        qtde_parc: Optional[int] = None,
        intev_parc: Optional[int] = None,
        obs_pgto: Optional[str] = None,
        obs_entrega: Optional[str] = None,
        tipo_pgto: Optional[int] = None,
        tem_frete: Optional[int] = None,
        diaini_venc: Optional[int] = None,
        freteqtde_ent: Optional[int] = None,
        interv_ent: Optional[int] = None,
        dias_entrega: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Cotacao/InserirAlteraComentFornFrete`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/InserirAlteraComentFornFrete
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Inserir um comentário ou atualizar um já existente.
        
        
        
        Args:
            empresa (int): The empresa
            codigo_fornecedor (int): The codigo_fornecedor
            cotacao (int): The cotacao
            cond_pagto (int): The cond_pagto
            tipo_coment (int): The tipo_coment
            efet_pgto_parc (int): The efet_pgto_parc
            dtvenc_ini (str): The dtvenc_ini
            qtde_parc (int): The qtde_parc
            intev_parc (int): The intev_parc
            obs_pgto (str): The obs_pgto
            obs_entrega (str): The obs_entrega
            tipo_pgto (int): The tipo_pgto
            tem_frete (int): The tem_frete
            diaini_venc (int): The diaini_venc
            freteqtde_ent (int): The freteqtde_ent
            interv_ent (int): The interv_ent
            diasEntrega (int): The entrega
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "codigo_fornecedor": 0,
                "cotacao": 0,
                "cond_pagto": 0,
                "tipo_coment": 0,
                "efet_pgto_parc": 0,
                "dtvenc_ini": "string",
                "qtde_parc": 0,
                "intev_parc": 0,
                "obs_pgto": "string",
                "obs_entrega": "string",
                "tipo_pgto": 0,
                "tem_frete": 0,
                "diaini_venc": 0,
                "freteqtde_ent": 0,
                "interv_ent": 0,
                "diasEntrega": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Cotacao()
            >>> response = api._inserir_altera_coment_forn_frete(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Cotacao/InserirAlteraComentFornFrete"
        kwargs = {
            "empresa": empresa,
            "codigo_fornecedor": codigo_fornecedor,
            "cotacao": cotacao,
            "cond_pagto": cond_pagto,
            "tipo_coment": tipo_coment,
            "efet_pgto_parc": efet_pgto_parc,
            "dtvenc_ini": dtvenc_ini,
            "qtde_parc": qtde_parc,
            "intev_parc": intev_parc,
            "obs_pgto": obs_pgto,
            "obs_entrega": obs_entrega,
            "tipo_pgto": tipo_pgto,
            "tem_frete": tem_frete,
            "diaini_venc": diaini_venc,
            "freteqtde_ent": freteqtde_ent,
            "interv_ent": interv_ent,
            "diasEntrega": dias_entrega,
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

