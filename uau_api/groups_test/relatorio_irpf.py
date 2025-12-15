from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class RelatorioIRPF:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_pdfrel_irpf(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.
            - A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
            - Substituir cada parâmetro pelo valor correspondente:
                - "Venda" - Número da Venda.
                - "Obra" - Código da Obra.
                - "Empresa" - Número da Empresa.
                - "ano_base" - ano base para geração do IRPF.
                - "naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).
        
                        {
                            "vendasobras_empresa" [
                                [
                                "Venda", 
                                "Obra", 
                                "Empresa"
                                ]
                            ],
                                "ano_base": 2018,
                                "naomostradados_venda": true
                        }
            - Segue exemplo  após substituição dos parâmetros:
            
                        {
                             "vendasobras_empresa" [
                               [
                               "838",
                               "424V",
                               "308"
                               ]
                           ],
                             "ano_base": 2021,
                             "naomostradados_venda": false
                        }
        
        Endpoint: `/api/v{version}/RelatorioIRPF/GerarPDFRelIRPF`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método responsável por gerar o PDF do IRPF
        
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
                            "vendasobras_empresa": {
                                "description": "Lista de Empresa, Obra e Venda",
                                "type": "array",
                                "items": {
                                    "type": "object"
                                }
                            },
                            "ano_base": {
                                "format": "int32",
                                "description": "Ano base",
                                "type": "integer"
                            },
                            "naomostradados_venda": {
                                "description": "Se irá mostrar ou não os dados consolidados da venda",
                                "type": "boolean"
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
            >>> api = RelatorioIRPF()
            >>> response = api._gerarpdf_relirpf(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/RelatorioIRPF/GerarPDFRelIRPF"
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

    def gerar_pdfrel_irpfv2(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.
            - A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
            - Substituir cada parâmetro pelo valor correspondente:
                - "Venda" - Número da Venda.
                - "Obra" - Código da Obra.
                - "Empresa" - Número da Empresa.
                - "ano_base" - ano base para geração do IRPF.
                - "naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).
        
                        {
                            "vendasobras_empresa" [
                                [
                                "Venda", 
                                "Obra", 
                                "Empresa"
                                ]
                            ],
                                "ano_base": 2018,
                                "naomostradados_venda": true
                        }
            - Segue exemplo  após substituição dos parâmetros:
            
                        {
                             "vendasobras_empresa" [
                               [
                               "838",
                               "424V",
                               "308"
                               ]
                           ],
                             "ano_base": 2021,
                             "naomostradados_venda": false
                        }
        
        Endpoint: `/api/v{version}/RelatorioIRPF/GerarPDFRelIRPFV2`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método responsável por gerar o PDF do IRPF
        
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
                            "vendasobras_empresa": {
                                "description": "Lista de Empresa, Obra e Venda",
                                "type": "array",
                                "items": {
                                    "type": "object"
                                }
                            },
                            "ano_base": {
                                "format": "int32",
                                "description": "Ano base",
                                "type": "integer"
                            },
                            "naomostradados_venda": {
                                "description": "Se irá mostrar ou não os dados consolidados da venda",
                                "type": "boolean"
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
            >>> api = RelatorioIRPF()
            >>> response = api._gerarpdf_relirpfv2(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/RelatorioIRPF/GerarPDFRelIRPFV2"
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

