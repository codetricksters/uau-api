from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class CorreioEletronico:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def enviar_mail_interno_uau(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint
        
        Definição de Negócio:
        1. Possibilita envio de email interno para o usuário root.
        2. Valida as informaçõe passadas no request.
        
        Endpoint: `/api/v{version}/CorreioEletronico/EnviarMailInternoUau`
        HTTP Method: `POST`
        
        Implementation Notes:
        Enviar email interno para o usuário root
        
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
                            "mensagem_envio": {
                                "description": "Mensagem que será enviada",
                                "type": "string"
                            },
                            "usuariosuau_destino": {
                                "description": "Usuário do uau que receberá a mensagem",
                                "type": "string"
                            },
                            "usuariouau_envio": {
                                "description": "Usuário que está enviando o e-mail",
                                "type": "string"
                            },
                            "assunto": {
                                "description": "Assunto do mail",
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
            >>> api = CorreioEletronico()
            >>> response = api._enviar_mail_interno_uau(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/CorreioEletronico/EnviarMailInternoUau"
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

