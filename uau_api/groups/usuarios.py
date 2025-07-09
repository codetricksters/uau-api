from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Usuarios:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_usuarios_ativos(
        self,
        login_usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Usuarios/ConsultarUsuariosAtivos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Se não informar o parâmetro “login_usuario”, vai está retornando todos os usuários ativos disponíveis.
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.       
        
        Parâmetros da request
        
        login_usuario: Nome do login usuario.
        
        
        
        Args:
            login_usuario (str): The login_usuario
        
        Parameter Structure:
        
            {
                "login_usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Usuarios()
            >>> response = api._consultar_usuarios_ativos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Usuarios/ConsultarUsuariosAtivos"
        kwargs = {
            "login_usuario": login_usuario,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

    def consultar_grupos_de_usuario(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Usuarios/ConsultarGruposDeUsuario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Usuarios()
            >>> response = api._consultar_grupos_de_usuario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Usuarios/ConsultarGruposDeUsuario"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            if response.status_code == HTTPStatus.BAD_REQUEST:
                return response.json()
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e.response.text

