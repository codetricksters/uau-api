from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class Estrutura:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def excluir_estrutura(
        self,
        codigo_estrutura: Optional[int] = None,
        sequencia: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/ExcluirEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite excluir uma estrutura completa caso o valor do parâmetro sequência seja (0 - raiz) ou apenas um item da estrutura(Caso o tipo do item seja "0 - Nível", também serão excluídos os itens filhos).
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            codigoEstrutura (int): The estrutura
            sequencia (str): The sequencia
        
        Parameter Structure:
        
            {
                "codigoEstrutura": 0,
                "sequencia": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._excluir_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/ExcluirEstrutura"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoEstrutura": codigo_estrutura,
                    "sequencia": sequencia,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def inserir_estrutura(
        self,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/InserirEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite inserir uma estrutura. Após inserir, poderá vincular os itens da estrutura.
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._inserir_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/InserirEstrutura"
        try:
            response = self.api.post(
                path,
                json={
                    "descricao": descricao,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def excluir_item_de_estrutura(
        self,
        codigo_item: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/ExcluirItemDeEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite excluir um item de estrutura que não está sendo utilizado no cadastro de estrutura, orçamento, contrato ou serviços do planejamento .
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            codigoItem (str): The item
        
        Parameter Structure:
        
            {
                "codigoItem": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._excluir_item_de_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/ExcluirItemDeEstrutura"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoItem": codigo_item,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def inserir_item_de_estrutura(
        self,
        codigo_item: Optional[str] = None,
        descricao_item: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/InserirItemDeEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite inserir um item de estrutura. Após inserir, poderá se utilizado no cadastro de estrutura e ser vinculado em orçamento, contrato e serviços do planejamento.
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            codigoItem (str): The item
            descricaoItem (str): The item
        
        Parameter Structure:
        
            {
                "codigoItem": "string",
                "descricaoItem": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._inserir_item_de_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/InserirItemDeEstrutura"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoItem": codigo_item,
                    "descricaoItem": descricao_item,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

    def inserir_item_na_estrutura(
        self,
        codigo_estrutura: Optional[int] = None,
        tipo_estrutura: Optional[int] = None,
        sequencia: Optional[str] = None,
        codigo_item: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Estrutura/InserirItemNaEstrutura`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de negócio:
          Permite inserir item em uma estrutura. Após concluir o cadastro da estrutura, poderá ser vinculada em orçamento, contrato e serviços do planejamento. 
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas
        
        
        Args:
            codigoEstrutura (int): The estrutura
            tipoEstrutura (int): The estrutura
            sequencia (str): The sequencia
            codigoItem (str): The item
        
        Parameter Structure:
        
            {
                "codigoEstrutura": 0,
                "tipoEstrutura": 0,
                "sequencia": "string",
                "codigoItem": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Estrutura()
            >>> response = api._inserir_item_na_estrutura(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Estrutura/InserirItemNaEstrutura"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoEstrutura": codigo_estrutura,
                    "tipoEstrutura": tipo_estrutura,
                    "sequencia": sequencia,
                    "codigoItem": codigo_item,
                }
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return response.text

