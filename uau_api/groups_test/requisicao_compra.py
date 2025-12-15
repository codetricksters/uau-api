from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class RequisicaoCompra:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def aprovar_requisicoes_compra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        1. É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA
        
        Endpoint: `/api/v{version}/RequisicaoCompra/AprovarRequisicoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de aprovar requisições de compra
        
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
                            "Requisicoes"
                        ],
                        "type": "object",
                        "properties": {
                            "Requisicoes": {
                                "description": "Requisições de compra a serem aprovadas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.RequisicaoDeCompra.AprovarRequisicaoCompraRequest"
                                }
                            },
                            "Departamento": {
                                "description": "Código do departamento do usuário para aprovação",
                                "type": "string"
                            },
                            "Cargo": {
                                "description": "Código do cargo do usuário para aprovação",
                                "type": "string"
                            },
                            "CodJustificativa": {
                                "format": "int32",
                                "description": "Código da justificativa para aprovação fora da sequência do usuário",
                                "type": "integer"
                            },
                            "ObsJustificativa": {
                                "description": "Observação da justificativa para aprovação fora da sequência do usuário",
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
            >>> api = RequisicaoCompra()
            >>> response = api._aprovar_requisicoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/RequisicaoCompra/AprovarRequisicoesCompra"
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

    def desaprovar_requisicoes_compra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        1. É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA
        2. Será permitido desaprovar apenas requisições de compra com estágio 0 - Criada
        
        Endpoint: `/api/v{version}/RequisicaoCompra/DesaprovarRequisicoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método com finalidade de desaprovar requisições de compra
        
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
                            "Requisicoes"
                        ],
                        "type": "object",
                        "properties": {
                            "Requisicoes": {
                                "description": "Requisições de compra a serem aprovadas",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.RequisicaoDeCompra.DesaprovarRequisicaoCompraRequest"
                                }
                            },
                            "CodJustificativaDesaprovacao": {
                                "format": "int32",
                                "description": "Código da justificativa para desaprovação da requisição de compra. \r\nÉ necessário quando o sistema está configurado para obrigar informar o motivo da desaprovação.",
                                "type": "integer"
                            },
                            "ObsJustificativaDesaprovacao": {
                                "description": "Observação da justificativa para desaprovação da requisição de compra",
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
            >>> api = RequisicaoCompra()
            >>> response = api._desaprovar_requisicoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/RequisicaoCompra/DesaprovarRequisicoesCompra"
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

