from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class AcompanharEntrega:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_processos(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanharEntrega/ConsultarProcessos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras Básicas:
        
        Retorna os processos e itens que estão com o acompanhamento de entrega pendente para uma dada empresa e obra informada.
        
        
        
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
            >>> api = AcompanharEntrega()
            >>> response = api._consultar_processos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanharEntrega/ConsultarProcessos"
        try:
            response = self.api.post(
                path,
                json={
                    "empresa": empresa,
                    "obra": obra,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def acompanhar_pre_entrega(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        chave_nota_fiscal: Optional[str] = None,
        chave_nota_fiscal_frete: Optional[str] = None,
        codigo_do_boleto: Optional[str] = None,
        codigo_do_boleto_frete: Optional[str] = None,
        itens: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `AcompanharEntrega/AcompanharPreEntrega`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Regras Básicas:
        
        O usuário deve possuir acesso na empresa e obra informada.
        O usuário deve possuir permissão de alteração no programa FIANALISE.
        O número do processo deve ser um processo existente.
        A NF e NF de frete devem ser númericos e válidos.
        O código de barras deve ser númerico e possuir no mínimo 36 caracteres.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Processo (int): The processo
            ChaveNotaFiscal (str): The chave nota fiscal
            ChaveNotaFiscalFrete (str): The chave nota fiscal frete
            CodigoDoBoleto (str): The codigo do boleto
            CodigoDoBoletoFrete (str): The codigo do boleto frete
            Itens (List[Dict[str, Any]]): The itens
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Processo": 0,
                "ChaveNotaFiscal": "string",
                "ChaveNotaFiscalFrete": "string",
                "CodigoDoBoleto": "string",
                "CodigoDoBoletoFrete": "string",
                "Itens": [
                    {
                        "CodigoItem": "string",
                        "Quantidade": 0,
                        "Preco": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = AcompanharEntrega()
            >>> response = api._acompanhar_pre_entrega(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "AcompanharEntrega/AcompanharPreEntrega"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Obra": obra,
                    "Processo": processo,
                    "ChaveNotaFiscal": chave_nota_fiscal,
                    "ChaveNotaFiscalFrete": chave_nota_fiscal_frete,
                    "CodigoDoBoleto": codigo_do_boleto,
                    "CodigoDoBoletoFrete": codigo_do_boleto_frete,
                    "Itens": itens,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

