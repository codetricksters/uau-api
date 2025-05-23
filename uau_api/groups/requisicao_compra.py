from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
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
        try:
            response = self.api.post(
                path,
                json={
                    "Requisicoes": requisicoes,
                    "Departamento": departamento,
                    "Cargo": cargo,
                    "CodJustificativa": cod_justificativa,
                    "ObsJustificativa": obs_justificativa,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

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
        try:
            response = self.api.post(
                path,
                json={
                    "Requisicoes": requisicoes,
                    "CodJustificativaDesaprovacao": cod_justificativa_desaprovacao,
                    "ObsJustificativaDesaprovacao": obs_justificativa_desaprovacao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

