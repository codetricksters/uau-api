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
        mensagem_envio: Optional[str] = None,
        usuariosuau_destino: Optional[str] = None,
        usuariouau_envio: Optional[str] = None,
        assunto: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `CorreioEletronico/EnviarMailInternoUau`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint
        
        Definição de Negócio:
        
        Possibilita envio de email interno para o usuário root.
        Valida as informaçõe passadas no request.
        
        
        
        Args:
            mensagem_envio (str): The mensagem_envio
            usuariosuau_destino (str): The usuariosuau_destino
            usuariouau_envio (str): The usuariouau_envio
            assunto (str): The assunto
        
        Parameter Structure:
        
            {
                "mensagem_envio": "string",
                "usuariosuau_destino": "string",
                "usuariouau_envio": "string",
                "assunto": "string"
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
        path = "CorreioEletronico/EnviarMailInternoUau"
        kwargs = {
            "mensagem_envio": mensagem_envio,
            "usuariosuau_destino": usuariosuau_destino,
            "usuariouau_envio": usuariouau_envio,
            "assunto": assunto,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

