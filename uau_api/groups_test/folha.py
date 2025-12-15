from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Folha:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gravar_alocacao_mao_obra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método GravarAlocacaoMaoObra.
        
        Definição de Negócio:
        1. Efetua a inclusão ou alteração(caso o registro já exista) na alocação de mão de obra para funcionários do UAU.
        2. Deve informar obrigatoriamente os campos:
          - Código da empresa de lotação do funcionário
          - Matrícula do funcionário
          - Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY
          - Código da empresa que o funcionário será alocado
          - Código da obra que o funcionário será alocado
          - Quantidade de dias que o funcionário está sendo alocado
        
        VirtUau:
        1. Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-a-importacao-de-alocação-de-mão-de-obra
        2. Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/alocacao-de-mao-de-obra-de-funcionarios/
        
        Endpoint: `/api/v{version}/Folha/GravarAlocacaoMaoObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Objetivo: Incluir/Alterar alocação de mão de obra para funcionários do UAU
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "ListaAlocacao"
                        ],
                        "type": "object",
                        "properties": {
                            "ListaAlocacao": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AlocacaoMaoObra.EntidadeAlocacaoMaoObra"
                                }
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Folha/GravarAlocacaoMaoObra"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def gravar_movimentacao_mensal_obra(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método GravarMovimentacaoMensalObra.
        
        Definição de Negócio:
        1. Efetua a inclusão ou alteração(caso o registro já exista) na movimentação mensal por obra dos funcionários do UAU.
        2. Deve informar obrigatoriamente os campos:
          - Código da empresa de lotação do funcionário
          - Matrícula do funcionário
          - Código da rubrica a ser rateada na empresa/obra
          - Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY
          - Código da empresa de rateio dos cálculos do funcionário
          - Código da obra de rateio dos cálculos do funcionário
          - Quantidade ou valor da proporção definida para a empresa/obra de rateio
        
        VirtUau:
        1. Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-a-importacao-de-movimentacao-mensal-e-movimentacao-por-obra/
        2. Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-calculo-da-folha-de-pagamento-com-rateio
        
        Endpoint: `/api/v{version}/Folha/GravarMovimentacaoMensalObra`
        HTTP Method: `POST`
        
        Implementation Notes:
        Objetivo: Incluir/Alterar movimentação mensal por obra dos funcionários do UAU
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "required": [
                            "ListaMovimentacaoObra"
                        ],
                        "type": "object",
                        "properties": {
                            "ListaMovimentacaoObra": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.MovimentacaoObra.EntidadeMovimentacaoObra"
                                }
                            }
                        }
                    },
                    "in": "body",
                    "required": true
                },
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token Authentication"
                },
                "X-INTEGRATION-Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": true,
                    "description": "Token De Integração"
                }
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
        path = f"/api/v{version}/Folha/GravarMovimentacaoMensalObra"
        kwargs = {
            "request": request,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

