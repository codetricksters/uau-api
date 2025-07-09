from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Webhook:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def by_token(
        self,
        token: str,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Webhook/ConfirmarRecebimentoOrdemCompra/{token}`
        HTTP Method: `GET`
        
        Implementation Notes:
        Alteração : Alexandre Mendes         Data: 19/09/2022
          Projeto   : 427564 - Sprint 5 - Engenhanria
          Manutenção: Alterado para extrair do token o tipo de resposta, sendo 1 = Aceito ou 3 = Recusado.
        
        
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
            >>> api = Webhook()
            >>> response = api.{token}(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"Webhook/ConfirmarRecebimentoOrdemCompra/{token}"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.get(
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

    def atualizar_recebimento_pix(
        self,
        end_to_end_id: Optional[str] = None,
        txid: Optional[str] = None,
        valor: Optional[str] = None,
        horario: Optional[datetime] = None,
        info_pagador: Optional[str] = None,
        devolucoes: Optional[Dict] = None,
        pagador: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Webhook/AtualizarRecebimentoPix`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
          Definição de Negócio:
        
        
        Args:
            endToEndId (str): The to end id
            txid (str): The txid
            valor (str): The valor
            horario (datetime): The horario
            infoPagador (str): The pagador
            devolucoes (Dict[str, Any]): The devolucoes
            pagador (Dict[str, Any]): The pagador
        
        Parameter Structure:
        
            {
                "endToEndId": "string",
                "txid": "string",
                "valor": "string",
                "horario": "2025-04-23T13:46:14.982Z",
                "infoPagador": "string",
                "devolucoes": {
                    "id": "string",
                    "rtrId": "string",
                    "valor": "string",
                    "horario": {
                        "solicitacao": "2025-04-23T13:46:14.982Z"
                    },
                    "status": "string"
                },
                "pagador": {
                    "cpf": "string",
                    "cnpj": "string",
                    "nome": "string"
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Webhook()
            >>> response = api._atualizar_recebimento_pix(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Webhook/AtualizarRecebimentoPix"
        kwargs = {
            "endToEndId": end_to_end_id,
            "txid": txid,
            "valor": valor,
            "horario": horario,
            "infoPagador": info_pagador,
            "devolucoes": devolucoes,
            "pagador": pagador,
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

    def atualizar_pedido_rec(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Webhook/AtualizarPedidoRec`
        HTTP Method: `POST`
        
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
            >>> api = Webhook()
            >>> response = api._atualizar_pedido_rec(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Webhook/AtualizarPedidoRec"
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

