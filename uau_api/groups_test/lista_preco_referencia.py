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
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         
        Regras Básicas:
         
         1. O usuário deve possuir permissão de inclusao no programa "ALLISTAPRECOREF"
         2. Para incluir um fornecedor, a lista já deve existir no sistema.
         3. A lista deve estar em aberto, não pode ter nenhuma confirmação de aprovação.
        
        Endpoint: `/api/v{version}/ListaPrecoReferencia/InserirFornecedores`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de inserir fornecedor na Lista de Preço Referência.
        
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
                            "NumeroLista",
                            "CodigoFornecedor"
                        ],
                        "type": "object",
                        "properties": {
                            "NumeroLista": {
                                "format": "int32",
                                "description": "Identificador único da lista de preço referência",
                                "type": "integer"
                            },
                            "CodigoFornecedor": {
                                "format": "int32",
                                "description": "Código do fornecedor",
                                "type": "integer"
                            },
                            "CPFCNPJ": {
                                "description": "CPF/CNPJ do fornecedor",
                                "type": "string"
                            },
                            "ValorMinimoPedFOB": {
                                "format": "double",
                                "description": "Valor mínimo de pedido para o tipo FOB",
                                "type": "number"
                            },
                            "ValorMinimoPedCIF": {
                                "format": "double",
                                "description": "Valor mínimo de pedido para o tipo CIF",
                                "type": "number"
                            },
                            "DataInicio": {
                                "format": "date-time",
                                "description": "Data início",
                                "type": "string"
                            },
                            "DataTermino": {
                                "format": "date-time",
                                "description": "Data terminio",
                                "type": "string"
                            },
                            "Contato": {
                                "description": "Contato",
                                "type": "string"
                            },
                            "ItensPorFornecedor": {
                                "description": "Itens por fornecedor",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ListaPrecoReferencia.ItemPorFornecedorRequest"
                                }
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
            >>> api = ListaPrecoReferencia()
            >>> response = api._inserir_fornecedores(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ListaPrecoReferencia/InserirFornecedores"
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

    def atualizar_item_fornecedor(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         
        Regras Básicas:
         
         1. O usuário deve possuir permissão de alteração no programa "ALLISTAPRECOREF"
         2. Para atualizar um fornecedor, a lista já deve existir no sistema e o fornecedor já deve estar cadastro.
         3. A lista deve estar em aberto, não pode ter nenhuma confirmação de aprovação.
        
        Endpoint: `/api/v{version}/ListaPrecoReferencia/AtualizarItemFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de atualizar um fornecedor na Lista de Preço Referência.
        
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
                            "NumeroLista",
                            "CodigoFornecedor"
                        ],
                        "type": "object",
                        "properties": {
                            "NumeroLista": {
                                "format": "int32",
                                "description": "Identificador único da lista de preço referência",
                                "type": "integer"
                            },
                            "CodigoFornecedor": {
                                "format": "int32",
                                "description": "Código do fornecedor",
                                "type": "integer"
                            },
                            "CPFCNPJ": {
                                "description": "CPF/CNPJ do fornecedor",
                                "type": "string"
                            },
                            "ValorMinimoPedFOB": {
                                "format": "double",
                                "description": "Valor mínimo de pedido para o tipo FOB",
                                "type": "number"
                            },
                            "ValorMinimoPedCIF": {
                                "format": "double",
                                "description": "Valor mínimo de pedido para o tipo CIF",
                                "type": "number"
                            },
                            "DataInicio": {
                                "format": "date-time",
                                "description": "Data início",
                                "type": "string"
                            },
                            "DataTermino": {
                                "format": "date-time",
                                "description": "Data terminio",
                                "type": "string"
                            },
                            "Contato": {
                                "description": "Contato",
                                "type": "string"
                            },
                            "ItensPorFornecedor": {
                                "description": "Itens por fornecedor",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.ListaPrecoReferencia.ItemPorFornecedorRequest"
                                }
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
            >>> api = ListaPrecoReferencia()
            >>> response = api._atualizar_item_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ListaPrecoReferencia/AtualizarItemFornecedor"
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

    def consultar_lista_preco_referencia(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         
        Regras Básicas:
         1. Pelo menos um parâmetro deve ser preenchido para consulta.
         2. Parâmetros:
        -  CodigoLista: Parâmetro principal, caso seja informado irá sobrepor todos os outros.
        -  FornecedorCodigo: Fará a pesquisa pelo código do fornecedor, caso não possua o CNPJ.
        -  FornecedorCNPJ: Fará a pesquisa pelo CNPJ do fornecedor, caso não possua o código do fornecedor.
        -  DataValidade: Data de validade da lista de preço.
        -  Status:   
             - 0 - Em aberto
             - 1 - Em Análise
             - 2 - Aprovada
             - 3 - Migrada
        
        Endpoint: `/api/v{version}/ListaPrecoReferencia/ConsultarListaPrecoReferencia`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de consultar a Lista de Preco Referência, com itens da lista de preço e itens de fornecedores preenchidos ou não.
        
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
                            "NumeroLista": {
                                "format": "int32",
                                "description": "Identificador único da lista de preço referência",
                                "type": "integer"
                            },
                            "DataValidade": {
                                "format": "date-time",
                                "description": "Data de vencimento da lista.",
                                "type": "string"
                            },
                            "Status": {
                                "format": "int32",
                                "description": "Status da lista: 0 - Em aberto; 1 - Em Análise; 2 - Aprovada;  3 - Migrada.",
                                "type": "integer"
                            },
                            "FornecedorCNPJ": {
                                "description": "Número de CNPJ do fornecedor",
                                "type": "string"
                            },
                            "FornecedorCodigo": {
                                "format": "int32",
                                "description": "Número do código do fornecedor",
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
            >>> api = ListaPrecoReferencia()
            >>> response = api._consultar_lista_preco_referencia(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ListaPrecoReferencia/ConsultarListaPrecoReferencia"
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

