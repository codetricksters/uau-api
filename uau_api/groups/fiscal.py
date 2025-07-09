from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Fiscal:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def buscar_caps(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Fiscal/BuscarCAPs`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        Formato dos dados retornados:
        Codigo (String): Código do CAP
        Descricao (String): Descrição do CAP
        Tipo (Integer): Tipo do CAP
        0: Geral
        1: Acresc/Desc
        
        
        
        
        
        
        
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
            >>> api = Fiscal()
            >>> response = api._buscarca_ps(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Fiscal/BuscarCAPs"
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

    def buscar_codigo_servico_fiscal(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Fiscal/BuscarCodigoServicoFiscal`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        
        Consulta os códigos de serviços fiscais ativos.
        
        
        
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
            >>> api = Fiscal()
            >>> response = api._buscar_codigo_servico_fiscal(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Fiscal/BuscarCodigoServicoFiscal"
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

    def importar_lancamentos_fiscais(
        self,
        dadoslacamentos_xml: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Fiscal/ImportarLancamentosFiscais`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        Recebe string no formato XML com os dados do lançamento para importação.
        Utiliza o formato antigo do XML na string passada como parâmetro.
        
        Definição de Negócio:
        
        Importa lançamentos fiscais e/ou societários.
        Valida o XML passado no request.
        Valida o usuário e suas permissões.
        
        
        
        Args:
            dadoslacamentos_xml (str): The dadoslacamentos_xml
        
        Parameter Structure:
        
            {
                "dadoslacamentos_xml": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Fiscal()
            >>> response = api._importar_lancamentos_fiscais(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Fiscal/ImportarLancamentosFiscais"
        kwargs = {
            "dadoslacamentos_xml": dadoslacamentos_xml,
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

    def importar_lancamentos_contabeis(
        self,
        dadoslacamentos_xml: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Fiscal/ImportarLancamentosContabeis`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do endpoint.
        Utiliza o novo formato do XML na string passada como parâmetro.
        
        Definição de Negócio:
        
        Importa lançamentos fiscais e/ou societários.
        Valida o XML passado no request.
        Valida usuário e suas permissões.
        
        
        
        Args:
            dadoslacamentos_xml (str): The dadoslacamentos_xml
        
        Parameter Structure:
        
            {
                "dadoslacamentos_xml": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Fiscal()
            >>> response = api._importar_lancamentos_contabeis(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Fiscal/ImportarLancamentosContabeis"
        kwargs = {
            "dadoslacamentos_xml": dadoslacamentos_xml,
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

