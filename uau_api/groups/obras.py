from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class Obras:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def obter_obras_ativas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Obras/ObterObrasAtivas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta obras cadastradas e ativas dentro do UAU.
        
        
        
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
            >>> api = Obras()
            >>> response = api._obter_obras_ativas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Obras/ObterObrasAtivas"
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
        except requests.exceptions.RequestException:
            return response.text

    def consultar_obra_por_chave(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Obras/ConsultarObraPorChave`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Consulta dados de uma obra filtrando por chave.
        Valida os campos passados como parâmetros.
        
        
        
        Args:
            empresa (int): The empresa
            obra (str): The obra
        
        Parameter Structure:
        
            {
                "empresa": 0,
                "obra": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Obras()
            >>> response = api._consultar_obra_por_chave(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Obras/ConsultarObraPorChave"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def obter_meses_abertos_por_empresa_obra(
        self,
        empresa_obra: Optional[str] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Args:
            empresaObra (str): The obra
        
        Parameter Structure:
        
            {
                "empresaObra": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Obras()
            >>> response = api._obter_meses_abertos_por_empresa_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Obras/ObterMesesAbertosPorEmpresaObra"
        try:
            response = self.api.post(
                path,
                json={
                    "empresaObra": empresa_obra,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

