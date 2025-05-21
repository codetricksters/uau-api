from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
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
        try:
            response = self.api.post(
                path,
                json={
                    "dadoslacamentos_xml": dadoslacamentos_xml,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

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
        try:
            response = self.api.post(
                path,
                json={
                    "dadoslacamentos_xml": dadoslacamentos_xml,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

