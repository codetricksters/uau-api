from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Empresa:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_empresa(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Empresa/ConsultarEmpresa`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar os dados da empresa.
        
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
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
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
            >>> api = Empresa()
            >>> response = api._consultar_empresa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Empresa/ConsultarEmpresa"
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

    def obter_empresas_ativas(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Empresa/ObterEmpresasAtivas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta e retorna uma lista de Empresas cadastradas e ativas na base de dados UAU
        
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
            >>> api = Empresa()
            >>> response = api._obter_empresas_ativas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Empresa/ObterEmpresasAtivas"
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

    def consultar_dados_basicos_empresas_por_filtro(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Empresa/DadosBasicosEmpresa
        3. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Consultar dados de empresas por meio dos seguintes filtros (empresa, cnpj e descricaoEmpresa), os resultados da busca será de acordo com o limite especificado no parâmetro (limitarRetornoEm).
        2. Se apenas informar o código da empresa parâmetro (empresa) o mesmo deve estar completo.
        3. Os parâmetros (DescricaoEmpresa e Cnpj) devem possuir no mínimo 3 caracteres..
        4. Os parâmetros (DescricaoEmpresa e Cnpj) podem conter o sinal de porcentagem (%), caso necessite fazer a consulta a partir de um caractere curinga. Exemplos: %UAU, %UAU%, UAU%.
        5. O campo LimitarRetornoEm é obrigatório.
        6. Caso não informe nenhum dos parâmetros o resultado será os N primeiros registros encontrados, obedecendo o parâmetro LimitarRetornoEm.
        7. O método usa o operador “Or” para montar a consulta de acordo com os parâmetros do request, consultando informações por código ou descrição ou CNPJ da empresa.
        
        
        VirtUau:
        - http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Empresa/Empresa_ConsultarDadosBasicosEmpresasPorFiltro
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777099/
        
        Endpoint: `/api/v{version}/Empresa/ConsultarDadosBasicosEmpresasPorFiltro`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar dados básicos da empresa por filtro, com limite de registros.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "LimitarRetornoEm"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "DescricaoEmpresa": {
                                "description": "Descrição da empresa",
                                "type": "string"
                            },
                            "Cnpj": {
                                "description": "CNPJ da empresa (sem máscara)",
                                "type": "string"
                            },
                            "LimitarRetornoEm": {
                                "format": "int32",
                                "description": "Limite de retorno da consulta",
                                "type": "integer"
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
            >>> api = Empresa()
            >>> response = api._consultar_dados_basicos_empresas_por_filtro(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Empresa/ConsultarDadosBasicosEmpresasPorFiltro"
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

