from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class Folha:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gravar_alocacao_mao_obra(
        self,
        lista_alocacao: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Folha/GravarAlocacaoMaoObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método GravarAlocacaoMaoObra.
        
        Definição de Negócio:
        
        Efetua a inclusão ou alteração(caso o registro já exista) na alocação de mão de obra para funcionários do UAU.
        Deve informar obrigatoriamente os campos:
        Código da empresa de lotação do funcionário
        Matrícula do funcionário
        Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY
        Código da empresa que o funcionário será alocado
        Código da obra que o funcionário será alocado
        Quantidade de dias que o funcionário está sendo alocado
        
        
        
        VirtUau:
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-a-importacao-de-alocação-de-mão-de-obra
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/alocacao-de-mao-de-obra-de-funcionarios/
        
        
        
        Args:
            ListaAlocacao (List[Dict[str, Any]]): The lista alocacao
        
        Parameter Structure:
        
            {
                "ListaAlocacao": [
                    {
                        "CodEmpresaLotacao": 0,
                        "Matricula": "string",
                        "MesFolha": "2025-04-23T13:46:13.222Z",
                        "CodEmpresaAlocacao": 0,
                        "CodObraAlocacao": "string",
                        "QtdeAlocada": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Folha()
            >>> response = api._gravar_alocacao_mao_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Folha/GravarAlocacaoMaoObra"
        try:
            response = self.api.post(
                path,
                json={
                    "ListaAlocacao": lista_alocacao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def gravar_movimentacao_mensal_obra(
        self,
        lista_movimentacao_obra: Optional[List[Dict]] = None
    ) -> dict:
        """
        
        Endpoint: `Folha/GravarMovimentacaoMensalObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método GravarMovimentacaoMensalObra.
        
        Definição de Negócio:
        
        Efetua a inclusão ou alteração(caso o registro já exista) na movimentação mensal por obra dos funcionários do UAU.
        Deve informar obrigatoriamente os campos:
        Código da empresa de lotação do funcionário
        Matrícula do funcionário
        Código da rubrica a ser rateada na empresa/obra
        Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY
        Código da empresa de rateio dos cálculos do funcionário
        Código da obra de rateio dos cálculos do funcionário
        Quantidade ou valor da proporção definida para a empresa/obra de rateio
        
        
        
        VirtUau:
        
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-a-importacao-de-movimentacao-mensal-e-movimentacao-por-obra/
        Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-calculo-da-folha-de-pagamento-com-rateio
        
        
        
        Args:
            ListaMovimentacaoObra (List[Dict[str, Any]]): The lista movimentacao obra
        
        Parameter Structure:
        
            {
                "ListaMovimentacaoObra": [
                    {
                        "CodEmpresaLotacao": 0,
                        "Matricula": "string",
                        "CodigoRubrica": 0,
                        "MesFolha": "2025-04-23T13:46:13.229Z",
                        "CodEmpresaRateio": 0,
                        "CodObraRateio": "string",
                        "Proporcao": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Folha()
            >>> response = api._gravar_movimentacao_mensal_obra(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Folha/GravarMovimentacaoMensalObra"
        try:
            response = self.api.post(
                path,
                json={
                    "ListaMovimentacaoObra": lista_movimentacao_obra,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

