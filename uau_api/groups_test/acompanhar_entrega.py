from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class AcompanharEntrega:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_processos(
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
         
         1. Retorna os processos e itens que estão com o acompanhamento de entrega pendente para uma dada empresa e obra informada.
        
        Endpoint: `/api/v{version}/AcompanharEntrega/ConsultarProcessos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de consultar processos do acompanhamento de entrega.
        
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
                            "obra"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "obra": {
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
            >>> api = AcompanharEntrega()
            >>> response = api._consultar_processos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanharEntrega/ConsultarProcessos"
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

    def acompanhar_pre_entrega(
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
         
         1. O usuário deve possuir acesso na empresa e obra informada.
         2. O usuário deve possuir permissão de alteração no programa FIANALISE.
         3. O número do processo deve ser um processo existente.
         4. A NF e NF de frete devem ser númericos e válidos.
         5. O código de barras deve ser númerico e possuir no mínimo 36 caracteres.
        
        Endpoint: `/api/v{version}/AcompanharEntrega/AcompanharPreEntrega`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de acompanhar pre entrega
        
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
                            "Processo",
                            "Itens"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa no UAU",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da obra no UAU",
                                "type": "string"
                            },
                            "Processo": {
                                "format": "int32",
                                "description": "Número do processo de pagamento no UAU",
                                "type": "integer"
                            },
                            "ChaveNotaFiscal": {
                                "description": "Chave da nota fiscal para inclusão no UAU",
                                "type": "string"
                            },
                            "ChaveNotaFiscalFrete": {
                                "description": "Chave da nota fiscal do frete para inclusão no UAU",
                                "type": "string"
                            },
                            "CodigoDoBoleto": {
                                "description": "Linha digitável do boleto",
                                "type": "string"
                            },
                            "CodigoDoBoletoFrete": {
                                "description": "Linha digitável do boleto do frete",
                                "type": "string"
                            },
                            "Itens": {
                                "description": "Itens a serem acompanhados",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanharEntrega.ItemPreEntregaRequest"
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
            >>> api = AcompanharEntrega()
            >>> response = api._acompanhar_pre_entrega(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanharEntrega/AcompanharPreEntrega"
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

