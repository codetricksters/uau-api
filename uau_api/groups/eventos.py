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
        chave: Optional[str] = None,
        data_inicial: Optional[datetime] = None,
        data_final: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Eventos/ConsultarLogEventos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Os campos do tipo data devem obedecer o formato especificado pelo JSON.
        yyyy-MM-dd HH:mm:ss > 2019-01-22 00:00:00
        yyyy-MM-dd > 2018-12-25
        
        
        
        Definição de Negócio:
          Permite consultar logs de eventos.
        
        Verifique as chaves de consultas disponíveis no endpoint:
        URI + /api/v{version}/Eventos/ConsultarChavesLogDeEventos
        
        
        Deve informar uma data inicial e outra final.
        
        Anexos:
        
        Postman: https://ajuda.globaltec.com.br/download/777172/
        Retorno: https://ajuda.globaltec.com.br/download/777175/
        
        
        
        Args:
            Chave (str): The chave
            DataInicial (datetime): The data inicial
            DataFinal (datetime): The data final
        
        Parameter Structure:
        
            {
                "Chave": "string",
                "DataInicial": "2025-04-23T13:46:13.183Z",
                "DataFinal": "2025-04-23T13:46:13.183Z"
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
        path = "Eventos/ConsultarLogEventos"
        kwargs = {
            "Chave": chave,
            "DataInicial": data_inicial,
            "DataFinal": data_final,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_chaves_log_de_eventos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Eventos/ConsultarChavesLogDeEventos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Regras de Negócio:
        
        A chave de acesso consultada informa quais chaves poderão ser utilizadas no seguinte endpoint:
        URI + /api/v{version}/Eventos/ConsultarLogEventos
        
        
        
        Anexos:
        
        Postman: https://ajuda.globaltec.com.br/download/777172/
        
        
        
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
            >>> api = Eventos()
            >>> response = api._consultar_chaves_log_de_eventos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Eventos/ConsultarChavesLogDeEventos"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

