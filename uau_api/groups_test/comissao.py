from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Comissao:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_vendedores(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario;
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consulta os vendedores da estrutura de comissão;
        2. Caso não seja informado o código da comissão retornará todos os vendedores relacionados à estrutura de comissão;
        3. Caso seja informado um código que não esteja relacionado a estrutura de comissão o sistema retornará "vazio".
        
        Informação:
        1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
        
        Endpoint: `/api/v{version}/Comissao/ConsultarVendedores`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os vendedores da estrutura de comissão.
        
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
                            "codigoModeloComissao": {
                                "format": "int32",
                                "description": "Código do modelo de comissão",
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
            >>> api = Comissao()
            >>> response = api._consultar_vendedores(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Comissao/ConsultarVendedores"
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

    def atualizar_status_comissao(
        self,
        version: str,
        lista_atualizar_status_comissao: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Alterar os status de pagamento das comissões de uma pessoa(beneficiário).
        2. Não é possível cancelar ou reativar status de pagamento da comissão via Endpoint.
        3. Todos os campos são obrigatórios informar.
        4. Os dados informados passam por validações.
        5. Não é permitido marcar como "pago" comissões que geram processos de pagamento
        6. Não é permitido reativar ou cancelar status de pagamento da comissão.
        7. Status disponíveis:
            - 0 - Não liberada
            - 1 - Liberada
            - 2 - Paga
            - 4 - Bloqueada
        
        Endpoint: `/api/v{version}/Comissao/AtualizarStatusComissao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar status de pagamento da comissão.
        
        Args:
            listaAtualizarStatusComissao (Dict[str, Any]): The atualizar status comissao
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "listaAtualizarStatusComissao": {
                    "definition": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/UAUApi.Models.Comissao.AtualizarStatusComissaoRequest"
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
            >>> api = Comissao()
            >>> response = api._atualizar_status_comissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Comissao/AtualizarStatusComissao"
        kwargs = {
            "listaAtualizarStatusComissao": lista_atualizar_status_comissao,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_modelo_comissao(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario;
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consulta o Modelo de Comissão disponível para utilização em uma proposta de venda.
        
        Informação:
        1. A propriedade "Padrão" no retorno indica o modelo de comissão padrão utilizado pelo vendedor, no entanto, ela será retornada como True.
        
        Endpoint: `/api/v{version}/Comissao/ConsultarModeloComissao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os Modelos de Comissão disponíveis
        
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
                            "codigoEmpresa",
                            "codigoObra"
                        ],
                        "type": "object",
                        "properties": {
                            "codigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "codigoObra": {
                                "description": "Código da Obra",
                                "type": "string"
                            },
                            "codigoVendedor": {
                                "format": "int32",
                                "description": "Código do Vendedor",
                                "type": "integer"
                            },
                            "dataVenda": {
                                "description": "Data da Venda",
                                "type": "string"
                            },
                            "qtdeParcelas": {
                                "format": "int32",
                                "description": "Quantidade de Parcelas",
                                "type": "integer"
                            },
                            "listaUnidades": {
                                "description": "Lista de Unidades",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Comissao.ListaUnidades"
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
            >>> api = Comissao()
            >>> response = api._consultar_modelo_comissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Comissao/ConsultarModeloComissao"
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

    def consultar_estrutura_comissao(
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
        1. Consulta a estrutura de comissão do vendedor.
        2. A propriedade SobreRecebimento está descontinuada, mas continuará retornando as informações nela conforme o preenchimento da nova propriedade, chamada RegraLiberacao.
        3. A propriedade codigo da hierarquia se tornou obsoleta, precisamos apenas do número da comissão que é um número único no sistema.
        4. A propriedade numModelo é referente a nova estrutura de modelos de comissão.
        5. Caso seja informado uma pessoa que não participa do modelo de comissão, o sistema não irá montar a estrutura;
        
        Endpoint: `/api/v{version}/Comissao/ConsultarEstruturaComissao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta a estrutura de comissão do vendedor
        
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
                            "empresa",
                            "obra",
                            "codigoVendedor",
                            "numeroComissao",
                            "valorComissao",
                            "produtos"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "codigoVendedor": {
                                "format": "int32",
                                "description": "Código do vendedor",
                                "type": "integer"
                            },
                            "codigoHierarquia": {
                                "format": "int32",
                                "description": "Código da hierarquia de comissão\r\n*Obsoleto* Utilizamos apenas o numero da comissão.",
                                "type": "integer"
                            },
                            "numeroComissao": {
                                "format": "int32",
                                "description": "Código do modelo de comissão.",
                                "type": "integer"
                            },
                            "valorComissao": {
                                "format": "double",
                                "description": "Valor da comissão",
                                "type": "number"
                            },
                            "produtos": {
                                "description": "Lista de produtos - Utilizamos para verificar se há captadores no produto.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Comissao.DadosProdutosComissao"
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
            >>> api = Comissao()
            >>> response = api._consultar_estrutura_comissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Comissao/ConsultarEstruturaComissao"
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

