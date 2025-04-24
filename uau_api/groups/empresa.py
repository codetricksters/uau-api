from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class Empresa:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_empresa(
        self,
        codigo_empresa: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Empresa/ConsultarEmpresa`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
        Args:
            codigoEmpresa (int): The empresa
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Empresa()
            >>> response = api._consultar_empresa(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Empresa/ConsultarEmpresa"
        try:
            response = self.api.post(
                path,
                json={
                    "codigoEmpresa": codigo_empresa,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def obter_empresas_ativas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Empresa/ObterEmpresasAtivas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        
        
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
            >>> api = Empresa()
            >>> response = api._obter_empresas_ativas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Empresa/ObterEmpresasAtivas"
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
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def consultar_dados_basicos_empresas_por_filtro(
        self,
        empresa: Optional[int] = None,
        descricao_empresa: Optional[str] = None,
        cnpj: Optional[str] = None,
        limitar_retorno_em: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Empresa/ConsultarDadosBasicosEmpresasPorFiltro`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Empresa/DadosBasicosEmpresa
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Consultar dados de empresas por meio dos seguintes filtros (empresa, cnpj e descricaoEmpresa), os resultados da busca será de acordo com o limite especificado no parâmetro (limitarRetornoEm).
        
        Se apenas informar o código da empresa parâmetro (empresa) o mesmo deve estar completo.
        Os parâmetros (DescricaoEmpresa e Cnpj) devem possuir no mínimo 3 caracteres..
        Os parâmetros (DescricaoEmpresa e Cnpj) podem conter o sinal de porcentagem (%), caso necessite fazer a consulta a partir de um caractere curinga. Exemplos: %UAU, %UAU%, UAU%.
        O campo LimitarRetornoEm é obrigatório.
        Caso não informe nenhum dos parâmetros o resultado será os N primeiros registros encontrados, obedecendo o parâmetro LimitarRetornoEm.
        O método usa o operador “Or” para montar a consulta de acordo com os parâmetros do request, consultando informações por código ou descrição ou CNPJ da empresa.
        
        VirtUau:
        
        http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Empresa/Empresa_ConsultarDadosBasicosEmpresasPorFiltro
        
        Anexos:
        
        Exemplo Postman: https://ajuda.globaltec.com.br/download/777099/
        
        
        
        Args:
            Empresa (int): The empresa
            DescricaoEmpresa (str): The descricao empresa
            Cnpj (str): The cnpj
            LimitarRetornoEm (int): The limitar retorno em
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "DescricaoEmpresa": "string",
                "Cnpj": "string",
                "LimitarRetornoEm": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Empresa()
            >>> response = api._consultar_dados_basicos_empresas_por_filtro(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Empresa/ConsultarDadosBasicosEmpresasPorFiltro"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "DescricaoEmpresa": descricao_empresa,
                    "Cnpj": cnpj,
                    "LimitarRetornoEm": limitar_retorno_em,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

