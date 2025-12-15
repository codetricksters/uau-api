from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Orcamento:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def alterar_insumo_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/AlterarInsumoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar insumo no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Paulo Roberto de Almeida Júnior Data: 20/11/2018",
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Numero do orçamento.",
                                "type": "integer"
                            },
                            "composicao": {
                                "description": "Código da composição",
                                "type": "string"
                            },
                            "insumo": {
                                "description": "Código do insumo",
                                "type": "string"
                            },
                            "usuario": {
                                "description": "Usuário logado",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do insumo do serviço, poderá ser 0 ou maior que zero.",
                                "type": "number"
                            },
                            "preco": {
                                "format": "double",
                                "description": "preco do insumo do serviço, poderá ser 0 ou maior que zero.",
                                "type": "number"
                            },
                            "tipoInsumo": {
                                "format": "int32",
                                "description": "Tipo do insumo em CInsOrca",
                                "type": "integer"
                            },
                            "encargo": {
                                "format": "int32",
                                "description": "Insumos de mão de obra podem ser de encargo",
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
            >>> api = Orcamento()
            >>> response = api._alterar_insumo_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/AlterarInsumoOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def excluir_insumo_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ExcluirInsumoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir insumo no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Paulo Roberto de Almeida Júnior Data: 20/11/2018",
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Numero do orçamento.",
                                "type": "integer"
                            },
                            "composicao": {
                                "description": "Código da composição",
                                "type": "string"
                            },
                            "insumo": {
                                "description": "Código do insumo",
                                "type": "string"
                            },
                            "usuario": {
                                "description": "Usuário logado",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do insumo do serviço, poderá ser 0 ou maior que zero.",
                                "type": "number"
                            },
                            "preco": {
                                "format": "double",
                                "description": "preco do insumo do serviço, poderá ser 0 ou maior que zero.",
                                "type": "number"
                            },
                            "tipoInsumo": {
                                "format": "int32",
                                "description": "Tipo do insumo em CInsOrca",
                                "type": "integer"
                            },
                            "encargo": {
                                "format": "int32",
                                "description": "Insumos de mão de obra podem ser de encargo",
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
            >>> api = Orcamento()
            >>> response = api._excluir_insumo_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ExcluirInsumoOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def inserir_insumo_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/InserirInsumoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir insumos no orçamento. Podem ser informados diversos insumos para que sejam inseridos em lote.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Leonrique Oliveira \r\nProjeto: 367085 - Sprint 77",
                        "type": "object",
                        "properties": {
                            "InsumosOrcamento": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Orcamento.ManterInsumoOrcamentoRequest"
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
            >>> api = Orcamento()
            >>> response = api._inserir_insumo_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/InserirInsumoOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def alterar_servico_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/AlterarServicoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar serviço no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Ulisses Cardoso de Souza Data: 21/06/2018",
                        "required": [
                            "empresa",
                            "obra",
                            "numOrcamento",
                            "item",
                            "servico"
                        ],
                        "type": "object",
                        "properties": {
                            "usuario": {
                                "description": "Usuário logado",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do item/serviço",
                                "type": "number"
                            },
                            "dataInicio": {
                                "format": "date-time",
                                "description": "Data de início do serviço",
                                "type": "string"
                            },
                            "dataFim": {
                                "format": "date-time",
                                "description": "Data final do serviço",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração vinculado ao serviço",
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
            >>> api = Orcamento()
            >>> response = api._alterar_servico_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/AlterarServicoOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def excluir_servico_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ExcluirServicoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Exclui serviço ou item do orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Ulisses Cardoso de Souza Data: 21/06/2018",
                        "required": [
                            "empresa",
                            "obra",
                            "numOrcamento",
                            "item",
                            "servico"
                        ],
                        "type": "object",
                        "properties": {
                            "usuario": {
                                "description": "Usuário logado",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração vinculado ao serviço",
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
            >>> api = Orcamento()
            >>> response = api._excluir_servico_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ExcluirServicoOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def inserir_servico_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/InserirServicoOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir serviços no orçamento. Podem ser informados diversos serviços para que sejam inseridos em lote.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Leonrique Oliveira \r\nProjeto: 367085 - Sprint 77",
                        "type": "object",
                        "properties": {
                            "ServicosOrcamento": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Orcamento.InserirServicoOrcamentoRequest"
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
            >>> api = Orcamento()
            >>> response = api._inserir_servico_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/InserirServicoOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_insumos_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ConsultarInsumosPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar a tabela PlanilhaCronograma pela sua chave
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Paulo Roberto de Almeida Júnior Data: 20/11/2018",
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Numero do orçamento.",
                                "type": "integer"
                            },
                            "composicao": {
                                "description": "Código da composição",
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
            >>> api = Orcamento()
            >>> response = api._consultar_insumos_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ConsultarInsumosPorChave"
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

    def alterar_planilha_cronograma(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/AlterarPlanilhaCronograma`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar cronograma no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Paulo Roberto de Almeida Júnior Data: 16/11/2018",
                        "type": "object",
                        "properties": {
                            "usuario": {
                                "description": "Usuário logado no sistema",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "periodo": {
                                "description": "Código externo de integração vinculado ao serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serviço no cronograma do orçamento, poderá ser 0 ou maior que zero.",
                                "type": "number"
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
            >>> api = Orcamento()
            >>> response = api._alterar_planilha_cronograma(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/AlterarPlanilhaCronograma"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def excluir_planilha_cronograma(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ExcluirPlanilhaCronograma`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir cronograma no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Paulo Roberto de Almeida Júnior Data: 16/11/2018",
                        "type": "object",
                        "properties": {
                            "usuario": {
                                "description": "Usuário logado no sistema",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "periodo": {
                                "description": "Código externo de integração vinculado ao serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serviço no cronograma do orçamento, poderá ser 0 ou maior que zero.",
                                "type": "number"
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
            >>> api = Orcamento()
            >>> response = api._excluir_planilha_cronograma(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ExcluirPlanilhaCronograma"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def inserir_planilha_cronograma(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/InserirPlanilhaCronograma`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir cronograma no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Paulo Roberto de Almeida Júnior Data: 16/11/2018",
                        "type": "object",
                        "properties": {
                            "usuario": {
                                "description": "Usuário logado no sistema",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "periodo": {
                                "description": "Código externo de integração vinculado ao serviço",
                                "type": "string"
                            },
                            "quantidade": {
                                "format": "double",
                                "description": "Quantidade do serviço no cronograma do orçamento, poderá ser 0 ou maior que zero.",
                                "type": "number"
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
            >>> api = Orcamento()
            >>> response = api._inserir_planilha_cronograma(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/InserirPlanilhaCronograma"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def exportar_orcamento_estrutura(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ExportarOrcamentoEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Exportar orçamento com suas estruturas
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "required": [
                            "empresa",
                            "obra",
                            "orcamento"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Numero do orçamento.",
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
            >>> api = Orcamento()
            >>> response = api._exportar_orcamento_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ExportarOrcamentoEstrutura"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_estrutura_orca_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ConsultarEstruturaOrcaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar estrutura de serviço do orçamento de acordo com a chave do orçamento.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Ulisses Cardoso de Souza Data: 21/06/2018",
                        "required": [
                            "sequencia",
                            "empresa",
                            "obra",
                            "numOrcamento",
                            "item",
                            "servico"
                        ],
                        "type": "object",
                        "properties": {
                            "sequencia": {
                                "description": "Código da sequência da estrutura do serviço",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração vinculado ao serviço",
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
            >>> api = Orcamento()
            >>> response = api._consultar_estrutura_orca_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ConsultarEstruturaOrcaPorChave"
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

    def consultar_estrutura_orca_por_servico(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ConsultarEstruturaOrcaPorServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar as estruturas do orçamento para um determinado serviço.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Ulisses Cardoso de Souza Data: 21/06/2018",
                        "required": [
                            "empresa",
                            "obra",
                            "numOrcamento",
                            "item",
                            "servico"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração vinculado ao serviço",
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
            >>> api = Orcamento()
            >>> response = api._consultar_estrutura_orca_por_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ConsultarEstruturaOrcaPorServico"
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

    def consultar_servico_orcamento_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ConsultarServicoOrcamentoPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Buscar os serviços do orçamento de acordo com a chave do orçamento.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Ulisses Cardoso de Souza Data: 21/06/2018",
                        "required": [
                            "empresa",
                            "obra",
                            "numOrcamento",
                            "item",
                            "servico"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "codExternoIntegracao": {
                                "description": "Código externo de integração vinculado ao serviço",
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
            >>> api = Orcamento()
            >>> response = api._consultar_servico_orcamento_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ConsultarServicoOrcamentoPorChave"
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

    def consultar_servico_orcado_desintegrado(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ConsultarServicoOrcadoDesintegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar serviço orçado desintegrado.
        
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
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Numero do orçamento.",
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
            >>> api = Orcamento()
            >>> response = api._consultar_servico_orcado_desintegrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ConsultarServicoOrcadoDesintegrado"
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

    def excluir_estrutura_servico_de_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite excluir níveis ou itens de estruturas do serviço do orçamento.
        1. Deve preencher os parâmetros de acordo com a estrutura que deseja excluir.
           1.1 Informar se é nível ou item que esta excluindo, a sequencia e os dados do orçamento e serviço.
        2. Valida se a estrutura poderá ser excluída.
        3. Valida campos obrigatórios.
        4. Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem excluídas.
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/776140/
        
        Endpoint: `/api/v{version}/Orcamento/ExcluirEstruturaServicoDeOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir uma determinada estrutura de serviço no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "- Lista de estruturas de serviço de orçamento, para permitir a exclusão em massa.",
                        "type": "object",
                        "properties": {
                            "EstruturasDeServicoDeOrcamento": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Orcamento.ExcluirEstruturaServicoDeOrcamentoRequest"
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
            >>> api = Orcamento()
            >>> response = api._excluir_estrutura_servico_de_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ExcluirEstruturaServicoDeOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def exportar_orcamento_estrutura_paginada(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ExportarOrcamentoEstruturaPaginada`
        HTTP Method: `POST`
        
        Implementation Notes:
        Exporta os itens de um orçamento com suporte à paginação.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "Classe de requisição para exportação paginada dos itens de estrutura de um orçamento.",
                        "required": [
                            "empresa",
                            "obra",
                            "orcamento",
                            "Page",
                            "PageSize"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa responsável pelo orçamento.",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Identificador da obra vinculada ao orçamento.",
                                "type": "string"
                            },
                            "orcamento": {
                                "format": "int32",
                                "description": "Número do orçamento a ser exportado.",
                                "type": "integer"
                            },
                            "Page": {
                                "format": "int32",
                                "description": "Número da página a ser consultada (inicia em 1).",
                                "type": "integer"
                            },
                            "PageSize": {
                                "format": "int32",
                                "description": "Quantidade de registros por página.",
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
            >>> api = Orcamento()
            >>> response = api._exportar_orcamento_estrutura_paginada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ExportarOrcamentoEstruturaPaginada"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def inserir_estrutura_servico_de_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite inserir níveis ou itens de estruturas no serviço existente no orçamento.
        1. Deve preencher os parâmetros de acordo com a estrutura que deseja inserir.
           1.1 Informar se é nível ou item que esta inserindo, a sequencia e os dados do orçamento e serviço.
        2. Valida se a estrutura poderá ser inserida.
        3. Valida campos obrigatórios.
        4. Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem inseridas.
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/776144/
        
        Endpoint: `/api/v{version}/Orcamento/InserirEstruturaServicoDeOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir estrutura para um determinado serviço no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "- Lista de estruturas de serviço de orçamento, para permitir a inserção em massa.",
                        "type": "object",
                        "properties": {
                            "EstruturasDeServicoDeOrcamento": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Orcamento.InserirEstruturaServicoDeOrcamentoRequest"
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
            >>> api = Orcamento()
            >>> response = api._inserir_estrutura_servico_de_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/InserirEstruturaServicoDeOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_planilha_cronograma_por_chave(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ConsultarPlanilhaCronogramaPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar a tabela PlanilhaCronograma pela sua chave
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Paulo Roberto de Almeida Júnior Data: 16/11/2018",
                        "type": "object",
                        "properties": {
                            "usuario": {
                                "description": "Usuário logado no sistema",
                                "type": "string"
                            },
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "item": {
                                "description": "Código do item do orçamento",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do serviço do orçamento",
                                "type": "string"
                            },
                            "periodo": {
                                "description": "Código externo de integração vinculado ao serviço",
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
            >>> api = Orcamento()
            >>> response = api._consultar_planilha_cronograma_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ConsultarPlanilhaCronogramaPorChave"
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

    def atualizar_estrutura_servico_de_orcamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Permite alterar níveis ou itens de uma estrutura do serviço existente no orçamento
        1. Deve preencher os parâmetros de acordo com a estrutura que deseja alterar .
           1.1 Informar se é nível ou item que esta inserindo, a sequencia e os dados do orçamento e serviço.
        2. Valida se a estrutura poderá ser alterada.
        3. Valida campos obrigatórios.
        4. Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem inseridas.
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/776147/
        
        Endpoint: `/api/v{version}/Orcamento/AtualizarEstruturaServicoDeOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar a quantidade e/ou preço de uma lista de estruturas de serviço no orçamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "description": "- Lista de estruturas de serviço de orçamento, para permitir a inserção em massa.",
                        "type": "object",
                        "properties": {
                            "EstruturasDeServicoDeOrcamento": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Orcamento.InserirEstruturaServicoDeOrcamentoRequest"
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
            >>> api = Orcamento()
            >>> response = api._atualizar_estrutura_servico_de_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/AtualizarEstruturaServicoDeOrcamento"
        kwargs = {
            "req": req,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_servico_orcamento_por_orcamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Orcamento/ConsultarServicoOrcamentoPorOrcamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Buscar os serviços do orçamento de acordo com o código do orçamento.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Ulisses Cardoso de Souza Data: 21/06/2018",
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Codigo da empresa do orçamento",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Codigo da obra do orçamento",
                                "type": "string"
                            },
                            "numOrcamento": {
                                "format": "int32",
                                "description": "Número do orçamento",
                                "type": "integer"
                            },
                            "tipoItem": {
                                "format": "int32",
                                "description": "Tipo do item\r\n0 - Atividade (Item)\r\n1 - Servico \r\n2 - Ambos",
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
            >>> api = Orcamento()
            >>> response = api._consultar_servico_orcamento_por_orcamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Orcamento/ConsultarServicoOrcamentoPorOrcamento"
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

