from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Estrutura:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def excluir_estrutura(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        Permite excluir uma estrutura completa caso o valor do parâmetro sequência seja (0 - raiz) ou apenas um item da estrutura(Caso o tipo do item seja "0 - Nível", também serão excluídos os itens filhos).
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        Endpoint: `/api/v{version}/Estrutura/ExcluirEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir estrutura.
        
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
                            "codigoEstrutura",
                            "sequencia"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoEstrutura": {
                                "format": "int32",
                                "description": "Código da estrutura",
                                "type": "integer"
                            },
                            "sequencia": {
                                "description": "Sequência da estrutura\r\n Obs: Quando a sequência for (0 - Raiz) será excluído a estrutura pai e os filhos.",
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
            >>> api = Estrutura()
            >>> response = api._excluir_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Estrutura/ExcluirEstrutura"
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

    def inserir_estrutura(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        Permite inserir uma estrutura. Após inserir, poderá vincular os itens da estrutura.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        Endpoint: `/api/v{version}/Estrutura/InserirEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir uma estrutura.
        
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
                            "descricao"
                        ],
                        "type": "object",
                        "properties": {
                            "descricao": {
                                "description": "Descrição da estrutura",
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
            >>> api = Estrutura()
            >>> response = api._inserir_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Estrutura/InserirEstrutura"
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

    def excluir_item_de_estrutura(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        Permite excluir um item de estrutura que não está sendo utilizado no cadastro de estrutura, orçamento, contrato ou serviços do planejamento .
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        Endpoint: `/api/v{version}/Estrutura/ExcluirItemDeEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir item de estrutura.
        
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
                            "codigoItem"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoItem": {
                                "description": "Código do item de estrutura",
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
            >>> api = Estrutura()
            >>> response = api._excluir_item_de_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Estrutura/ExcluirItemDeEstrutura"
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

    def inserir_item_de_estrutura(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        Permite inserir um item de estrutura. Após inserir, poderá se utilizado no cadastro de estrutura e ser vinculado em orçamento, contrato e serviços do planejamento.
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        Endpoint: `/api/v{version}/Estrutura/InserirItemDeEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir um item de estrutura.
        
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
                            "codigoItem",
                            "descricaoItem"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoItem": {
                                "description": "Código do item de estrutura",
                                "type": "string"
                            },
                            "descricaoItem": {
                                "description": "Descrição do item de estrutura",
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
            >>> api = Estrutura()
            >>> response = api._inserir_item_de_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Estrutura/InserirItemDeEstrutura"
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

    def inserir_item_na_estrutura(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
        Permite inserir item em uma estrutura. Após concluir o cadastro da estrutura, poderá ser vinculada em orçamento, contrato e serviços do planejamento. 
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        Endpoint: `/api/v{version}/Estrutura/InserirItemNaEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir item em uma estrutura.
        
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
                            "codigoEstrutura",
                            "tipoEstrutura",
                            "sequencia",
                            "codigoItem"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoEstrutura": {
                                "format": "int32",
                                "description": "Código da estrutura",
                                "type": "integer"
                            },
                            "tipoEstrutura": {
                                "format": "int32",
                                "description": "Tipo da estrutura\r\n 0 - Nível\r\n 1 - Item",
                                "type": "integer"
                            },
                            "sequencia": {
                                "description": "Sequência da estrutura",
                                "type": "string"
                            },
                            "codigoItem": {
                                "description": "Código do item de estrutura a ser vinculado. \r\nDeve existir no cadastrado de itens de estrutura.",
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
            >>> api = Estrutura()
            >>> response = api._inserir_item_na_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Estrutura/InserirItemNaEstrutura"
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

