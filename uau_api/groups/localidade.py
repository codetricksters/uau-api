from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class Localidade:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_localidade_por_cep(
        self,
        cep: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Localidade/ConsultarLocalidadePorCEP`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Consultar as informações da localidade informando apenas o CEP.
        
        Valida a presença do CEP;
        Retorna uma ou mais localidades para o CEP informado;
        Retorna somente endereços ativos.
        
        
        
        Args:
            Cep (str): The cep
        
        Parameter Structure:
        
            {
                "Cep": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Localidade()
            >>> response = api._consultar_localidade_porcep(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Localidade/ConsultarLocalidadePorCEP"
        kwargs = {
            "Cep": cep,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

