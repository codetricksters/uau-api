from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Planejamento:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def atualizar_item_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/AtualizarItemPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar item do planejamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Produto": {
                                "type": "string"
                            },
                            "Contrato": {
                                "type": "string"
                            },
                            "Item": {
                                "type": "string"
                            },
                            "DescricaoItem": {
                                "type": "string"
                            },
                            "Usuario": {
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
            >>> api = Planejamento()
            >>> response = api._atualizar_item_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AtualizarItemPlanejamento"
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

    def consultar_item_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarItemPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar item do planejamento de acordo com a chave do planejamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa do planejamento",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra do planejamento",
                                "type": "string"
                            },
                            "Produto": {
                                "description": "Código do produto vinculado ao planejamento",
                                "type": "string"
                            },
                            "Contrato": {
                                "description": "Código do contrato vinculado ao planejamento",
                                "type": "string"
                            },
                            "Item": {
                                "description": "Código do item do planejamento (considerar o código referente ao ITEM e não o código do SERVIÇO)",
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
            >>> api = Planejamento()
            >>> response = api._consultar_item_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarItemPlanejamento"
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

    def consultar_saldo_siplanejada(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Necessário permissão de consulta no programa OBPLNOBR
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarSaldoSIPlanejada`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza consulta de valores aprovados e saldos das SIs do planejamento.
        
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
                            "Empresa",
                            "Obra",
                            "Produto",
                            "Contrato"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa do planejamento",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra do planejamento",
                                "type": "string"
                            },
                            "Produto": {
                                "format": "int32",
                                "description": "Código do produto do planejamento",
                                "type": "integer"
                            },
                            "Contrato": {
                                "format": "int32",
                                "description": "Código do contrato do planejamento",
                                "type": "integer"
                            },
                            "Item": {
                                "description": "Código do item do planejamento",
                                "type": "string"
                            },
                            "Servico": {
                                "description": "Código do serviço do planejamento",
                                "type": "string"
                            },
                            "MesPl": {
                                "description": "Mês do planejamento",
                                "type": "string"
                            },
                            "Insumo": {
                                "description": "Insumo do planejamento",
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
            >>> api = Planejamento()
            >>> response = api._consultar_saldosi_planejada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarSaldoSIPlanejada"
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

    def inserir_servico_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/InserirServicoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir serviços no planejamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Produto": {
                                "type": "string"
                            },
                            "Contrato": {
                                "type": "string"
                            },
                            "Item": {
                                "type": "string"
                            },
                            "Servico": {
                                "type": "string"
                            },
                            "TipoDeCusto": {
                                "type": "string"
                            },
                            "Usuario": {
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
            >>> api = Planejamento()
            >>> response = api._inserir_servico_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/InserirServicoPlanejamento"
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

    def exportar_planejamento_produto(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ExportarPlanejamentoProduto`
        HTTP Method: `POST`
        
        Implementation Notes:
        Exportar planejamento de um produto
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "Contrato": {
                                "format": "int32",
                                "description": "Código do contrato.",
                                "type": "integer"
                            },
                            "Produto": {
                                "format": "int32",
                                "description": "Código do produto",
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
            >>> api = Planejamento()
            >>> response = api._exportar_planejamento_produto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ExportarPlanejamentoProduto"
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

    def atualizar_insumos_planejamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Necessário permissão de alteração no programa OBPLNOBR
        
        Endpoint: `/api/v{version}/Planejamento/AtualizarInsumosPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Alterar valores
        
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
                            "Insumos"
                        ],
                        "type": "object",
                        "properties": {
                            "Insumos": {
                                "description": "Insumos para alteração de custo de planejamento",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Planejamento.InsumoAlterarPlanejamento"
                                }
                            },
                            "justificativaAprovacaoPl": {
                                "description": "Justificativa de solicitação de aprovação de planejamento",
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
            >>> api = Planejamento()
            >>> response = api._atualizar_insumos_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AtualizarInsumosPlanejamento"
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

    def atualizar_servico_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/AtualizarServicoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar serviço do planejamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Produto": {
                                "type": "string"
                            },
                            "Contrato": {
                                "type": "string"
                            },
                            "Item": {
                                "type": "string"
                            },
                            "Servico": {
                                "type": "string"
                            },
                            "Qtde": {
                                "format": "double",
                                "type": "number"
                            },
                            "DataInicio": {
                                "type": "string"
                            },
                            "DataTermino": {
                                "type": "string"
                            },
                            "Usuario": {
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
            >>> api = Planejamento()
            >>> response = api._atualizar_servico_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AtualizarServicoPlanejamento"
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

    def consultar_servico_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarServicoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar serviços do planejamento de acordo com a chave do planejamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa do planejamento",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra do planejamento",
                                "type": "string"
                            },
                            "Produto": {
                                "description": "Código do produto vinculado ao planejamento",
                                "type": "string"
                            },
                            "Contrato": {
                                "description": "Código do contrato vinculado ao planejamento",
                                "type": "string"
                            },
                            "Item": {
                                "description": "Código do item do planejamento (considerar o código referente ao ITEM e não o código do SERVIÇO)",
                                "type": "string"
                            },
                            "Servico": {
                                "description": "Código do serviço do planejamento (considerar o código referente ao SERVIÇO e não o código do ITEM)",
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
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarServicoPlanejamento"
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

    def consultar_solicitacao_insumo_pl(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarSolicitacaoInsumoPL`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar as solicitações de alteração de insumos do planejamento.
        
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
                            "numSolicitacao": {
                                "format": "int32",
                                "description": "Código da solicitação de planejamento.",
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
            >>> api = Planejamento()
            >>> response = api._consultar_solicitacao_insumopl(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarSolicitacaoInsumoPL"
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

    def inserir_estrutura_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/InserirEstruturaPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir estrutura no planejamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Produto": {
                                "type": "string"
                            },
                            "Contrato": {
                                "type": "string"
                            },
                            "Item": {
                                "type": "string"
                            },
                            "Servico": {
                                "type": "string"
                            },
                            "Sequencia": {
                                "type": "string"
                            },
                            "CodigoItem": {
                                "type": "string"
                            },
                            "Tipo": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Qtde": {
                                "format": "double",
                                "type": "number"
                            },
                            "Usuario": {
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
            >>> api = Planejamento()
            >>> response = api._inserir_estrutura_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/InserirEstruturaPlanejamento"
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

    def consultar_solicitacao_servico_pl(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarSolicitacaoServicoPL`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar as solicitações de alteração de serviço do planejamento.
        
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
                            "numSolicitacao": {
                                "format": "int32",
                                "description": "Código da solicitação de planejamento.",
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
            >>> api = Planejamento()
            >>> response = api._consultar_solicitacao_servicopl(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarSolicitacaoServicoPL"
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

    def inserir_servico_planejamento_mes(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/InserirServicoPlanejamentoMes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir serviço do planejamento de acordo com o mês.
        
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
                            "Empresa",
                            "Obra",
                            "Produto",
                            "Contrato",
                            "Item",
                            "Servico",
                            "Mes",
                            "Qtde",
                            "Usuario"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa do planejamento",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra do planejamento",
                                "type": "string"
                            },
                            "Produto": {
                                "description": "Código do produto vinculado ao planejamento",
                                "type": "string"
                            },
                            "Contrato": {
                                "description": "Código do contrato vinculado ao planejamento",
                                "type": "string"
                            },
                            "Item": {
                                "description": "Código do item do planejamento (considerar o código referente ao ITEM e não o código do SERVIÇO)",
                                "type": "string"
                            },
                            "Servico": {
                                "description": "Código do serviço do planejamento (considerar o código referente ao SERVIÇO e não o código do ITEM)",
                                "type": "string"
                            },
                            "Mes": {
                                "description": "Mês do planejamento",
                                "type": "string"
                            },
                            "Qtde": {
                                "format": "double",
                                "description": "Quantidade do serviço do planejamento.",
                                "type": "number"
                            },
                            "Usuario": {
                                "description": "Login usuário.",
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
            >>> api = Planejamento()
            >>> response = api._inserir_servico_planejamento_mes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/InserirServicoPlanejamentoMes"
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

    def aprovar_solicitacao_planejamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Exemplo do json de request:
        
            {
                "NumSolicitacao" 622,
                "Usuario": "root",
                "Departamento": "FIN",
                "Cargo": "10"
            }
        
        Endpoint: `/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar a solicitação de aprovação de planejamento.
        
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
                            "NumSolicitacao": {
                                "format": "int32",
                                "description": "Código da solicitação de planejamento.",
                                "type": "integer"
                            },
                            "Usuario": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "Departamento": {
                                "description": "Código do departamento do usuário",
                                "type": "string"
                            },
                            "Cargo": {
                                "description": "Código do cargo do usuário",
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
            >>> api = Planejamento()
            >>> response = api._aprovar_solicitacao_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamento"
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

    def atualizar_estrutura_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/AtualizarEstruturaPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar estrutura no planejamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Produto": {
                                "type": "string"
                            },
                            "Contrato": {
                                "type": "string"
                            },
                            "Item": {
                                "type": "string"
                            },
                            "Servico": {
                                "type": "string"
                            },
                            "Sequencia": {
                                "type": "string"
                            },
                            "Qtde": {
                                "format": "double",
                                "type": "number"
                            },
                            "Usuario": {
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
            >>> api = Planejamento()
            >>> response = api._atualizar_estrutura_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AtualizarEstruturaPlanejamento"
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

    def consultar_estrutura_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarEstruturaPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar estrutura do planejamento.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Produto": {
                                "type": "string"
                            },
                            "Contrato": {
                                "type": "string"
                            },
                            "Item": {
                                "type": "string"
                            },
                            "Servico": {
                                "type": "string"
                            },
                            "Sequencia": {
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
            >>> api = Planejamento()
            >>> response = api._consultar_estrutura_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarEstruturaPlanejamento"
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

    def atualizar_servico_planejamento_mes(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/AtualizarServicoPlanejamentoMes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar serviço do planejamento de acordo com o mês.
        
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
                            "Empresa",
                            "Obra",
                            "Produto",
                            "Contrato",
                            "Item",
                            "Servico",
                            "Mes",
                            "Qtde",
                            "Usuario"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa do planejamento",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra do planejamento",
                                "type": "string"
                            },
                            "Produto": {
                                "description": "Código do produto vinculado ao planejamento",
                                "type": "string"
                            },
                            "Contrato": {
                                "description": "Código do contrato vinculado ao planejamento",
                                "type": "string"
                            },
                            "Item": {
                                "description": "Código do item do planejamento (considerar o código referente ao ITEM e não o código do SERVIÇO)",
                                "type": "string"
                            },
                            "Servico": {
                                "description": "Código do serviço do planejamento (considerar o código referente ao SERVIÇO e não o código do ITEM)",
                                "type": "string"
                            },
                            "Mes": {
                                "description": "Mês do planejamento",
                                "type": "string"
                            },
                            "Qtde": {
                                "format": "double",
                                "description": "Quantidade do serviço do planejamento.",
                                "type": "number"
                            },
                            "Usuario": {
                                "description": "Login usuário.",
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
            >>> api = Planejamento()
            >>> response = api._atualizar_servico_planejamento_mes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AtualizarServicoPlanejamentoMes"
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

    def consultar_desembolso_planejamento(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. O mês inicial e final deverão ser informados no formato MM/YYYY. Exemplo: 01/2019, 12/2019.
        
        Definição de Negócio:
        Status:
        1. Projetado: Considera a data de pagamento (DtaRef) para realizar o cálculo dos valores.
        2. A pagar: Considera a data de prorrogação da parcela (DtaRef) para realizar o cálculo dos valores.
        3. Pago: Considera a data de pagamento da parcela (DtaRef) para realizar o cálculo dos valores.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarDesembolsoPlanejamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar desembolso (Projetado, A pagar e Pago) por obra e período.
        
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
                            "Empresa",
                            "Obra",
                            "MesInicial",
                            "MesFinal"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra.",
                                "type": "string"
                            },
                            "MesInicial": {
                                "description": "Mês PL inicial.",
                                "type": "string"
                            },
                            "MesFinal": {
                                "description": "Mês PL final.",
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
            >>> api = Planejamento()
            >>> response = api._consultar_desembolso_planejamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarDesembolsoPlanejamento"
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

    def consultar_servico_planejamento_mes(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarServicoPlanejamentoMes`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar serviço do planejamento de acordo com o mês.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Produto": {
                                "type": "string"
                            },
                            "Contrato": {
                                "type": "string"
                            },
                            "Item": {
                                "type": "string"
                            },
                            "Servico": {
                                "type": "string"
                            },
                            "Mes": {
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
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejamento_mes(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarServicoPlanejamentoMes"
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

    def consultar_servico_planejamento_por_obra(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarServicoPlanejamentoPorObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar serviço do planejamento por obra.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra.",
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
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejamento_por_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarServicoPlanejamentoPorObra"
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

    def inserir_servico_planejamento_integrado(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/InserirServicoPlanejamentoIntegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Inserir serviços no planejamento integrado.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "Obra": {
                                "type": "string"
                            },
                            "Produto": {
                                "type": "string"
                            },
                            "Contrato": {
                                "type": "string"
                            },
                            "Item": {
                                "type": "string"
                            },
                            "Servico": {
                                "type": "string"
                            },
                            "TipoDeCusto": {
                                "type": "string"
                            },
                            "CodigoExterno": {
                                "type": "string"
                            },
                            "Usuario": {
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
            >>> api = Planejamento()
            >>> response = api._inserir_servico_planejamento_integrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/InserirServicoPlanejamentoIntegrado"
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

    def recusar_solicitacao_planejamento_geral(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/RecusarSolicitacaoPlanejamentoGeral`
        HTTP Method: `POST`
        
        Implementation Notes:
        Recusar a solicitação de planejamento, como também os itens da solicitação.
        
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
                            "NumSolicitacao": {
                                "format": "int32",
                                "description": "Código da solicitação de planejamento.",
                                "type": "integer"
                            },
                            "NumSolicitacoes": {
                                "description": "Número de solicitação de planejamento.",
                                "type": "array",
                                "items": {
                                    "format": "int32",
                                    "type": "integer"
                                }
                            },
                            "IdsItensSolicitacao": {
                                "description": "Armazena os ID's dos itens de solicitação de aprovação de planejamento.",
                                "type": "array",
                                "items": {
                                    "format": "int32",
                                    "type": "integer"
                                }
                            },
                            "Usuario": {
                                "description": "Código do usuário",
                                "type": "string"
                            },
                            "Departamento": {
                                "description": "- Departamento do usuário, informado para a aprovação.",
                                "type": "string"
                            },
                            "Cargo": {
                                "description": "- Cargo do usuário, informado para a aprovação.",
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
            >>> api = Planejamento()
            >>> response = api._recusar_solicitacao_planejamento_geral(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/RecusarSolicitacaoPlanejamentoGeral"
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

    def aprovar_solicitacao_planejamento_em_lote(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         3. Exemplo do json de request:
         
             {
                 "NumSolicitacoes" [
                     625, 626
                 ],
                 "Usuario": "root",
                 "Departamento": "FIN",
                 "Cargo": "10"
        }
        
        Endpoint: `/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar várias solicitações de aprovação de planejamento em uma única requisição.
        
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
                            "NumSolicitacoes": {
                                "description": "Número das solicitação de planejamento que deseja aprovar. No formato \"NumSolicitacoes\": [0001, 0002, 0003]",
                                "type": "array",
                                "items": {
                                    "format": "int32",
                                    "type": "integer"
                                }
                            },
                            "Usuario": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "Departamento": {
                                "description": "Código do departamento do usuário",
                                "type": "string"
                            },
                            "Cargo": {
                                "description": "Código do cargo do usuário",
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
            >>> api = Planejamento()
            >>> response = api._aprovar_solicitacao_planejamento_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoEmLote"
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

    def atualizar_servico_planejamento_integrado(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/AtualizarServicoPlanejamentoIntegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar serviço do planejamento integrado.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "CodigoExterno": {
                                "type": "string"
                            },
                            "Qtde": {
                                "format": "double",
                                "type": "number"
                            },
                            "DataInicio": {
                                "type": "string"
                            },
                            "DataTermino": {
                                "type": "string"
                            },
                            "Usuario": {
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
            >>> api = Planejamento()
            >>> response = api._atualizar_servico_planejamento_integrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AtualizarServicoPlanejamentoIntegrado"
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

    def consultar_servico_planejado_desintegrado(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarServicoPlanejadoDesintegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar serviço planejado desintegrado.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa.",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra.",
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
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejado_desintegrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarServicoPlanejadoDesintegrado"
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

    def consultar_servico_planejamento_integrado(
        self,
        version: str,
        req: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarServicoPlanejamentoIntegrado`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar serviço do planejamento integrado.
        
        Args:
            req (Dict[str, Any]): The req
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "req": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "CodigoExterno": {
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
            >>> api = Planejamento()
            >>> response = api._consultar_servico_planejamento_integrado(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarServicoPlanejamentoIntegrado"
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

    def consultar_aprovacao_pl_pendente_por_usuario(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarAprovacaoPlPendentePorUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza consulta das aprovações pendentes para o usuário.
        
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
                            "usuario": {
                                "description": "Código do usuário.",
                                "type": "string"
                            },
                            "departamento": {
                                "description": "Departamento do usuário.",
                                "type": "string"
                            },
                            "cargo": {
                                "description": "Cargo do usuário.",
                                "type": "string"
                            },
                            "empresasObras": {
                                "description": "Lista de empresas e obras",
                                "type": "string"
                            },
                            "tipoConsultaAprovacao": {
                                "description": "Tipo da consulta da aprovacao",
                                "type": "string"
                            },
                            "numero_dias": {
                                "format": "int32",
                                "description": "Numero de dias",
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
            >>> api = Planejamento()
            >>> response = api._consultar_aprovacao_pl_pendente_por_usuario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarAprovacaoPlPendentePorUsuario"
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

    def recusar_solicitacao_planejamento_geral_em_lote(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/RecusarSolicitacaoPlanejamentoGeralEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Recusar a solicitação de planejamento em lote, como também os itens da solicitação.
        
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
                            "NumSolicitacao": {
                                "format": "int32",
                                "description": "Código da solicitação de planejamento.",
                                "type": "integer"
                            },
                            "NumSolicitacoes": {
                                "description": "Número de solicitação de planejamento.",
                                "type": "array",
                                "items": {
                                    "format": "int32",
                                    "type": "integer"
                                }
                            },
                            "IdsItensSolicitacao": {
                                "description": "Armazena os ID's dos itens de solicitação de aprovação de planejamento.",
                                "type": "array",
                                "items": {
                                    "format": "int32",
                                    "type": "integer"
                                }
                            },
                            "Usuario": {
                                "description": "Código do usuário",
                                "type": "string"
                            },
                            "Departamento": {
                                "description": "- Departamento do usuário, informado para a aprovação.",
                                "type": "string"
                            },
                            "Cargo": {
                                "description": "- Cargo do usuário, informado para a aprovação.",
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
            >>> api = Planejamento()
            >>> response = api._recusar_solicitacao_planejamento_geral_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/RecusarSolicitacaoPlanejamentoGeralEmLote"
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

    def aprovar_solicitacao_planejamento_insumos_em_lote(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Exemplo do json de request:
        
           {
                "IdsItensSolicitacao" [
                    1615, 1616, 1617            
                ],
                "Usuario": "root",
                "Departamento": "FIN",
                "Cargo": "10"
           }
        
        Endpoint: `/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoInsumosEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar a solicitação de aprovação de planejamento de insumos em lotes de solicitações. Passando como parâmetro o número dos itens das solicitações.
        
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
                            "IdsItensSolicitacao": {
                                "description": "Número dos ITENS de solicitação de planejamento que deseja aprovar. No formato \"IdsItensSolicitacao\": [0001, 0002, 0003]. Não confunda com o Número da solicitação.",
                                "type": "array",
                                "items": {
                                    "format": "int32",
                                    "type": "integer"
                                }
                            },
                            "Usuario": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "Departamento": {
                                "description": "Código do departamento do usuário",
                                "type": "string"
                            },
                            "Cargo": {
                                "description": "Código do cargo do usuário",
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
            >>> api = Planejamento()
            >>> response = api._aprovar_solicitacao_planejamento_insumos_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoInsumosEmLote"
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

    def aprovar_solicitacao_planejamento_servicos_em_lote(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         3. Exemplo do json de request:
         
            {
                "NumSolicitacao": 630,
                "ChavesServico": [
                    {
        	            "empresa": 1,
        	            "obra": "00000",
        	            "produto": 7,
        	            "contrato": 1,
        	            "item": "01.01.01.02",
        	            "servico": "020201P",
        	            "data": "01/09/2005"
                    },
                    {
        	            "empresa": 1,
        	            "obra": "00000",
        	            "produto": 7,
        	            "contrato": 1,
        	            "item": "01.01.01.03",
        	            "servico": "030109P",
        	            "data": "01/09/2005"
                    }
                ],
                "Usuario": "root",
                "Departamento": "FIN",
                "Cargo": "10"
            }
        
        Endpoint: `/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoServicosEmLote`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar a solicitação de aprovação de planejamento de serviços em lotes de solicitações.
        
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
                            "NumSolicitacao": {
                                "format": "int32",
                                "description": "Código da solicitação de aprovação de planejamento.",
                                "type": "integer"
                            },
                            "ChavesServico": {
                                "description": "Armazena uma cadeia de chaves de serviço PL. (Sequência: Empresa, Obra, Produto, Contrato, Item, Servico, Mes do planejamento (MesPL) no formato (dd/mm/yyyy))",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Planejamento.ChaveServicoPlRequest"
                                }
                            },
                            "Usuario": {
                                "description": "Login do usuário logado",
                                "type": "string"
                            },
                            "Departamento": {
                                "description": "Código do departamento que o usuário está alocado",
                                "type": "string"
                            },
                            "Cargo": {
                                "description": "Código do cargo que o usuário está alocado",
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
            >>> api = Planejamento()
            >>> response = api._aprovar_solicitacao_planejamento_servicos_em_lote(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoServicosEmLote"
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

    def consultar_quantidade_aprovacao_pl_pendente_por_usuario(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Planejamento/ConsultarQuantidadeAprovacaoPlPendentePorUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Realiza a busca da quantidade de solicitação pendente para o usuário.
        
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
                            "usuario": {
                                "description": "Código do usuário.",
                                "type": "string"
                            },
                            "departamento": {
                                "description": "Departamento do usuário.",
                                "type": "string"
                            },
                            "cargo": {
                                "description": "Cargo do usuário.",
                                "type": "string"
                            },
                            "empresasObras": {
                                "description": "Lista de empresas e obras",
                                "type": "string"
                            },
                            "tipoConsultaAprovacao": {
                                "description": "Tipo da consulta da aprovacao",
                                "type": "string"
                            },
                            "numero_dias": {
                                "format": "int32",
                                "description": "Numero de dias",
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
            >>> api = Planejamento()
            >>> response = api._consultar_quantidade_aprovacao_pl_pendente_por_usuario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Planejamento/ConsultarQuantidadeAprovacaoPlPendentePorUsuario"
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

    def obter_acesso_usuario_na_obra(
        self,
        login: Optional[str] = None,
        empresa: Optional[str] = None,
        obra: Optional[str] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
        Args:
            login (Dict[str, Any]): The login
            empresa (Dict[str, Any]): The empresa
            obra (Dict[str, Any]): The obra
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "login": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "empresa": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "obra": {
                    "type": "string",
                    "in": "query",
                    "required": true,
                    "description": ""
                },
                "api-version": {
                    "type": "string",
                    "in": "query",
                    "required": false,
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
            >>> api = Planejamento()
            >>> response = api._obter_acesso_usuario_na_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Planejamento/ObterAcessoUsuarioNaObra"
        kwargs = {
            "login": login,
            "empresa": empresa,
            "obra": obra,
            "api-version": api_version,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

