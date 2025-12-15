from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Eventos:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_log_eventos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        3. Preencher os parâmetros de request para uso do método.
        4. Os campos do tipo data devem obedecer o formato especificado pelo JSON.
            1. yyyy-MM-dd HH:mm:ss &gt; 2019-01-22 00:00:00
            2. yyyy-MM-dd &gt; 2018-12-25
        
        Definição de Negócio:
        Permite consultar logs de eventos.
        1. Verifique as chaves de consultas disponíveis no endpoint:
            - URI + /api/v{version}/Eventos/ConsultarChavesLogDeEventos
        2. Deve informar uma data inicial e outra final.
        
        Anexos:
        1. Postman: https://ajuda.globaltec.com.br/download/777172/
        2. Retorno: https://ajuda.globaltec.com.br/download/777175/
        
        Endpoint: `/api/v{version}/Eventos/ConsultarLogEventos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consultar os logs de eventos do sistema
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "description": "Classe para mapeamento do request. Endpoint: /api/v{version}/Eventos/ConsultarChavesLogDeEventos",
                        "required": [
                            "Chave",
                            "DataInicial",
                            "DataFinal"
                        ],
                        "type": "object",
                        "properties": {
                            "Chave": {
                                "description": "Chave para consulta",
                                "type": "string"
                            },
                            "DataInicial": {
                                "format": "date-time",
                                "description": "Data inicial",
                                "type": "string"
                            },
                            "DataFinal": {
                                "format": "date-time",
                                "description": "Data final",
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
            >>> api = Eventos()
            >>> response = api._consultar_log_eventos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Eventos/ConsultarLogEventos"
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

    def consultar_chaves_log_de_eventos(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Regras de Negócio:
        1. A chave de acesso consultada informa quais chaves poderão ser utilizadas no seguinte endpoint:
            1. URI + /api/v{version}/Eventos/ConsultarLogEventos
            
        Anexos:
        1. Postman: https://ajuda.globaltec.com.br/download/777172/
        
        Endpoint: `/api/v{version}/Eventos/ConsultarChavesLogDeEventos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta a lista com as chaves dos eventos que podem ser consultados
        
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
            >>> api = Eventos()
            >>> response = api._consultar_chaves_log_de_eventos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Eventos/ConsultarChavesLogDeEventos"
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

