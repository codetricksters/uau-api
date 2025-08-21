from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class BancoHoras:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def lancar_banco_horas_funcionario(
        self,
        lista_banco_horas: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `BancoHoras/LancarBancoHorasFuncionario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Gravar lançamento de horas no banco de horas para o funcionário.
        
        
        
        Args:
            ListaBancoHoras (List[Dict[str, Any]]): The lista banco horas
        
        Parameter Structure:
        
            {
                "ListaBancoHoras": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "MesFolha": "string",
                        "Tipo": 0,
                        "HorasMinutosLanc": "string",
                        "DataLancamento": "2025-04-23T13:46:12.647Z",
                        "Matricula": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = BancoHoras()
            >>> response = api._lancar_banco_horas_funcionario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "BancoHoras/LancarBancoHorasFuncionario"
        kwargs = {
            "ListaBancoHoras": lista_banco_horas,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

