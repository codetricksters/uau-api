from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class PedidoCompra:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def grava_pedido_de_compra(
        self,
        dados: Optional[Dict] = None,
        tipo: Optional[int] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
        Args:
            dados (Dict[str, Any]): The dados
            tipo (Dict[str, Any]): The tipo
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "dados": {
                    "definition": {
                        "type": "object"
                    },
                    "in": "body",
                    "required": true
                },
                "tipo": {
                    "type": "integer",
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
            >>> api = PedidoCompra()
            >>> response = api._grava_pedido_de_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/PedidoCompra/GravaPedidoDeCompra"
        kwargs = {
            "dados": dados,
            "tipo": tipo,
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

    def aprovar_pedido_compra_servico_app(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Aprovar um item do pedido do tipo serviço.
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/AprovarPedidoCompraServicoApp`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar o item do pedido serviço
        
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
                            "codigo_empresa",
                            "codigo_obra",
                            "servico",
                            "num_pedido"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo_empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "codigo_obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "servico": {
                                "description": "Código do servico",
                                "type": "string"
                            },
                            "num_pedido": {
                                "format": "int32",
                                "description": "Númedo do pedido",
                                "type": "integer"
                            },
                            "mensagem_retorno": {
                                "description": "Mensagem retornada do método de aprovação",
                                "type": "string"
                            },
                            "departamento": {
                                "description": "Departamento da aprovação",
                                "type": "string"
                            },
                            "cargo": {
                                "description": "Cargo da aprovação",
                                "type": "string"
                            },
                            "cod_justificativa": {
                                "format": "int32",
                                "description": "Código da justificativa de aprovação",
                                "type": "integer"
                            },
                            "obs_justificativa": {
                                "description": "Observação da justificativa de aprovação",
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
            >>> api = PedidoCompra()
            >>> response = api._aprovar_pedido_compra_servico_app(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/AprovarPedidoCompraServicoApp"
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

    def aprovar_pedido_compra_material_app(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Aprovar um item do pedido de material realizado.
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/AprovarPedidoCompraMaterialApp`
        HTTP Method: `POST`
        
        Implementation Notes:
        Aprovar o item do pedido de material
        
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
                            "codigo_empresa",
                            "codigo_obra",
                            "insumo",
                            "item_ped",
                            "num_pedido"
                        ],
                        "type": "object",
                        "properties": {
                            "codigo_empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "codigo_obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "insumo": {
                                "description": "Código do insumo do pedido",
                                "type": "string"
                            },
                            "item_ped": {
                                "format": "int32",
                                "description": "Código do item do pedido",
                                "type": "integer"
                            },
                            "num_pedido": {
                                "format": "int32",
                                "description": "Númedo do pedido",
                                "type": "integer"
                            },
                            "mensagem_retorno": {
                                "description": "Mensagem retornada do método de aprovação",
                                "type": "string"
                            },
                            "departamento": {
                                "description": "Departamento da aprovação",
                                "type": "string"
                            },
                            "cargo": {
                                "description": "Cargo da aprovação",
                                "type": "string"
                            },
                            "cod_justificativa": {
                                "format": "int32",
                                "description": "Código da justificativa de aprovação",
                                "type": "integer"
                            },
                            "obs_justificativa": {
                                "description": "Observação da justificativa de aprovação",
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
            >>> api = PedidoCompra()
            >>> response = api._aprovar_pedido_compra_material_app(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/AprovarPedidoCompraMaterialApp"
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

    def gravar_pedido_de_compra_do_tipo_servico(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo Serviço (2).
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServico`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "2 - Serviço".
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido de serviço."
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os serviços que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServico"
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

    def gravar_pedido_de_compra_do_tipo_material(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo material (0).
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoMaterial`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gravar novo pedido de compra do tipo "0 - Material"
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Informações do pedido de material"
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os itens de material que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompra"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_material(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoMaterial"
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

    def gravar_pedido_de_compra_do_tipo_patrimonio(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo Patrimônio (3).
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoPatrimonio`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "3 - Patrimônio"
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido de patrimônio"
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os itens de patriônio que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompra"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_patrimonio(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoPatrimonio"
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

    def gravar_pedido_de_compra_do_tipo_complemento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo complemento (10).
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoComplemento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gravar novo pedido de compra do tipo "10 - Complemento"
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Informações do pedido de complemento"
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os itens de complemento que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompra"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_complemento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoComplemento"
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

    def gravar_pedido_de_compra_do_tipo_emergencial(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo emergêncial (6).
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoEmergencial`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "6 - Emergêncial"
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido emergencial"
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os itens emergenciais que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompra"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_emergencial(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoEmergencial"
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

    def gravar_pedido_de_compra_do_tipo_adiantamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo adiantamento (1).
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoAdiantamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "1 -Adiantamento de Contrato"
        
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
                            "dadosPedido",
                            "listaDadosItemPedido",
                            "numeroContrato"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Informações do pedido de adiantamento de contrato"
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os itens de adiantamento de compra que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompra"
                                }
                            },
                            "numeroContrato": {
                                "format": "int32",
                                "description": "Numero do contrato de material que terá o pedido vinculado.",
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_adiantamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoAdiantamento"
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

    def gravar_pedido_de_compra_do_tipo_regularizacao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo regularização (9).
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoRegularizacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gravar novo pedido de compra do tipo "9 - Regularização"
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Informações do pedido de regularizacao"
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os itens de regularizacao que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompra"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_regularizacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoRegularizacao"
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

    def confirmar_recebimento_ordem_compra_fornecedor(
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
        
        Endpoint: `/api/v{version}/PedidoCompra/ConfirmarRecebimentoOrdemCompraFornecedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de confirmar a cotação.
        
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
                            "nomeFornecedor": {
                                "description": "Nome do fornecedor do pedido",
                                "type": "string"
                            },
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Empresa do pedido",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Obra do pedido",
                                "type": "string"
                            },
                            "ordemDeCompra": {
                                "format": "int32",
                                "description": "Número da ordem de compra do pedido",
                                "type": "integer"
                            },
                            "tipoResposta": {
                                "format": "int32",
                                "description": "Tipo da resposta do fornecedor ao email do followUp. 1 = Aceito 3 = Recusado",
                                "type": "integer"
                            },
                            "observacao": {
                                "description": "Observação do fornecedor",
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
            >>> api = PedidoCompra()
            >>> response = api._confirmar_recebimento_ordem_compra_fornecedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/ConfirmarRecebimentoOrdemCompraFornecedor"
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

    def gravar_pedido_de_compra_do_tipo_servico_contrato(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo 16 - Serviço contrato.
        2. Valida as entradas dos pedidos.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoContrato`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "16 - Serviço contrato".
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido de serviço."
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os serviços que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServicoContrato"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_contrato(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoContrato"
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

    def gravar_pedido_de_compra_do_tipo_contrato_material(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo Contrato de material (4).
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoContratoMaterial`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "4 - Contrato de Material"
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido de contrato de material"
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os itens de contrato de material que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompraContratoMaterial"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_contrato_material(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoContratoMaterial"
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

    def gravar_pedido_de_compra_do_tipo_servico_complemento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo 13 - Serviço complemento.
        2. Valida as entradas dos pedidos.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoComplemento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "13 - Pedido serviço complemento".
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido de serviço complemento."
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os serviços que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_complemento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoComplemento"
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

    def gravar_pedido_de_compra_do_tipo_servico_emergencial(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo 11 - Serviço emergencial.
        2. Valida as entradas dos pedidos.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoEmergencial`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "11 - Pedido serviço emergencial".
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido de serviço emergencial."
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os serviços que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_emergencial(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoEmergencial"
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

    def gravar_pedido_de_compra_do_tipo_servico_adiantamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo 15 - Serviço adiantamento de contrato.
        2. Valida as entradas dos pedidos de compras.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoAdiantamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "15 - Serviço adiantamento de contrato".
        
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
                            "dadosPedido",
                            "listaDadosItemPedido",
                            "numeroContrato"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido de serviço."
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os serviços que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServicoAdiantamento"
                                }
                            },
                            "numeroContrato": {
                                "format": "int32",
                                "description": "Numero do contrato de serviço que terá o pedido vinculado.",
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_adiantamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoAdiantamento"
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

    def gravar_pedido_de_compra_do_tipo_servico_regularizacao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
            - Posição 0 = Numero do pedido;
            - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);
        
        Definição de Negócio:
        1. Gerar um novo pedido de compra do tipo 12 - Serviço regularização.
        2. Valida as entradas dos pedidos.
        
        Endpoint: `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoRegularizacao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Gera um novo pedido de compra do tipo "12 - Pedido serviço regularização".
        
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
                            "dadosPedido",
                            "listaDadosItemPedido"
                        ],
                        "type": "object",
                        "properties": {
                            "dadosPedido": {
                                "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosPedidoCompra",
                                "description": "Dados do pedido de serviço regularização."
                            },
                            "listaDadosItemPedido": {
                                "description": "Lista com todos os serviços que serão inseridos no pedido",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico"
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
            >>> api = PedidoCompra()
            >>> response = api._gravar_pedido_de_compra_do_tipo_servico_regularizacao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoRegularizacao"
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

    def validar_permissao_assistente_pedido_servico(
        self,
        request: Optional[Dict] = None,
        tipo_pedido: Optional[int] = None,
        api_version: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        HTTP Method: `POST`
        
        Args:
            request (Dict[str, Any]): The request
            tipoPedido (Dict[str, Any]): The pedido
            api-version (Dict[str, Any]): The api-version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object"
                    },
                    "in": "body",
                    "required": true
                },
                "tipoPedido": {
                    "type": "integer",
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
            >>> api = PedidoCompra()
            >>> response = api._validar_permissao_assistente_pedido_servico(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/PedidoCompra/ValidarPermissaoAssistentePedidoServico"
        kwargs = {
            "request": request,
            "tipoPedido": tipo_pedido,
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

