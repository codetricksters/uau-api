from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class RequisicaoCompra:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def aprovar_requisicoes_compra(
        self,
        requisicoes: Optional[List[Dict]] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        cod_justificativa: Optional[int] = None,
        obs_justificativa: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RequisicaoCompra/AprovarRequisicoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        
        É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA
        
        
        
        Args:
            Requisicoes (List[Dict[str, Any]]): The requisicoes
            Departamento (str): The departamento
            Cargo (str): The cargo
            CodJustificativa (int): The cod justificativa
            ObsJustificativa (str): The obs justificativa
        
        Parameter Structure:
        
            {
                "Requisicoes": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "NumRequisicao": 0
                    }
                ],
                "Departamento": "string",
                "Cargo": "string",
                "CodJustificativa": 0,
                "ObsJustificativa": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RequisicaoCompra()
            >>> response = api._aprovar_requisicoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RequisicaoCompra/AprovarRequisicoesCompra"
        kwargs = {
            "Requisicoes": requisicoes,
            "Departamento": departamento,
            "Cargo": cargo,
            "CodJustificativa": cod_justificativa,
            "ObsJustificativa": obs_justificativa,
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

    def desaprovar_requisicoes_compra(
        self,
        requisicoes: Optional[List[Dict]] = None,
        cod_justificativa_desaprovacao: Optional[int] = None,
        obs_justificativa_desaprovacao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `RequisicaoCompra/DesaprovarRequisicoesCompra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras básicas:
        
        É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA
        Será permitido desaprovar apenas requisições de compra com estágio 0 - Criada
        
        
        
        Args:
            Requisicoes (List[Dict[str, Any]]): The requisicoes
            CodJustificativaDesaprovacao (int): The cod justificativa desaprovacao
            ObsJustificativaDesaprovacao (str): The obs justificativa desaprovacao
        
        Parameter Structure:
        
            {
                "Requisicoes": [
                    {
                        "Empresa": 0,
                        "Obra": "string",
                        "NumRequisicao": 0
                    }
                ],
                "CodJustificativaDesaprovacao": 0,
                "ObsJustificativaDesaprovacao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = RequisicaoCompra()
            >>> response = api._desaprovar_requisicoes_compra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "RequisicaoCompra/DesaprovarRequisicoesCompra"
        kwargs = {
            "Requisicoes": requisicoes,
            "CodJustificativaDesaprovacao": cod_justificativa_desaprovacao,
            "ObsJustificativaDesaprovacao": obs_justificativa_desaprovacao,
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

