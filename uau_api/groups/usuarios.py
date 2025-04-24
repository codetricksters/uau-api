from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
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
        try:
            response = self.api.post(
                path,
                json={
                    "login_usuario": login_usuario,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

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
        try:
            response = self.api.post(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

