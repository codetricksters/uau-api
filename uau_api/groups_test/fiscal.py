from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Fiscal:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def buscar_caps(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Formato dos dados retornados:
         - Codigo (String): Código do CAP
         - Descricao (String): Descrição do CAP
         - Tipo (Integer): Tipo do CAP
                - 0: Geral
                - 1: Acresc/Desc
        
        Endpoint: `/api/v{version}/Fiscal/BuscarCAPs`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retornar a lista de CAPs ativos
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Fiscal()
            >>> response = api._buscarca_ps(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Fiscal/BuscarCAPs"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def buscar_codigo_servico_fiscal(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consulta os códigos de serviços fiscais ativos.
        
        Endpoint: `/api/v{version}/Fiscal/BuscarCodigoServicoFiscal`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta a lista de cógidos de serviços fiscais
        
        Args:
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Fiscal()
            >>> response = api._buscar_codigo_servico_fiscal(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Fiscal/BuscarCodigoServicoFiscal"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def importar_lancamentos_fiscais(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Recebe string no formato XML com os dados do lançamento para importação.
        4. Utiliza o formato antigo do XML na string passada como parâmetro.
        
        Definição de Negócio:
        1. Importa lançamentos fiscais e/ou societários.
        2. Valida o XML passado no request.
        3. Valida o usuário e suas permissões.
        
        Endpoint: `/api/v{version}/Fiscal/ImportarLancamentosFiscais`
        HTTP Method: `POST`
        
        Implementation Notes:
        Importa lançamentos fiscais e/ou societários - Formato antigo
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "dadoslacamentos_xml": {
                                "description": "Contem uma string com os dados do lançamento em formato de documento xml",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Fiscal()
            >>> response = api._importar_lancamentos_fiscais(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Fiscal/ImportarLancamentosFiscais"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def importar_lancamentos_contabeis(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Utiliza o novo formato do XML na string passada como parâmetro.
        
        Definição de Negócio:
        1. Importa lançamentos fiscais e/ou societários.
        2. Valida o XML passado no request.
        3. Valida usuário e suas permissões.
        
        Endpoint: `/api/v{version}/Fiscal/ImportarLancamentosContabeis`
        HTTP Method: `POST`
        
        Implementation Notes:
        Importa lançamentos fiscais e/ou societários - Formato novo
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "dadoslacamentos_xml": {
                                "description": "Contem uma string com os dados do lancamento em formato de documento xml",
                                "type": "string"
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Fiscal()
            >>> response = api._importar_lancamentos_contabeis(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Fiscal/ImportarLancamentosContabeis"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

