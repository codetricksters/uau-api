from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Contabil:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_saldo_de_contas(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar os saldo das contas conbaeis com a URI + /api/v{version}/Contabil/SaldoDeContas
        3. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Pode-se consultar o saldo das contas contábeis do UAU, podendo fazer filtros pela empresa, 
        tipo, ano e mês, com isso é possível fazer a integração da parte de saldos contábeis com o UAU
        1. Deve informar obrigatoriamente todos os parâmetros da request.
        
        VirtUau:
        - http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Contabil/Contabil_ConsultarSaldoDeContas
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777058/
        
        Endpoint: `/api/v{version}/Contabil/ConsultarSaldoDeContas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta o saldo de contas contábeis do UAU
        
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
                            "Empresa",
                            "MesAno",
                            "Tipo"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "MesAno": {
                                "format": "date-time",
                                "description": "Ano do Lançamento Societário e mês do Lançamento Fiscal\r\nO Mês do lançamento fiscal irá retornar somente lançamentos com mês igual ou inferior ao passado.",
                                "type": "string"
                            },
                            "Tipo": {
                                "description": "Tipo do Lançamento Fiscal e Societário, os valores passados serão desconsiderados na requisição. \r\nSe For passado mais de um valor os mesmos devem ser separados por virgula.\r\n0 - Manual\r\n1 - Automático\r\n2 - Inicialização de Saldo\r\n3 - Apuração Trimestral\r\n4 - Equivalência Patrimonial\r\n5 - Apuração Contábil\r\n6 - Apuração Anual",
                                "type": "string"
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
            >>> api = Contabil()
            >>> response = api._consultar_saldo_de_contas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Contabil/ConsultarSaldoDeContas"
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

    def consultar_contas_contabeis(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar os dados das contas contábeis com a URI + /api/v{version}/Contabil/ConsultarContasContabeis
        3. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Consulta os dados de contas contábeis do UAU, podendo fazer filtros pela empresa,
        ano, conta ou descrição da conta, com o intuito de buscar informações de uma conta contábil.
        1. Deve informar obrigatoriamente o código da empresa, ano da máscara de plano de contas e o a propriedade limitarRetornoEm.
        2. Pode informar opcionalmente o código da conta ou a descrição da conta.
        3. Os parâmetros (DescricaoConta, Conta) podem conter o sinal de porcentagem (%), 
        caso necessite fazer a consulta a partir de um caractere curinga. Exemplos: %UAU, %UAU%, UAU%.
        
        VirtUau:
        - http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Contabil/Contabil_ConsultarContasContabeis
        
        Anexos:
        - Exemplo Postman: https://ajuda.globaltec.com.br/download/777058/
        
        Endpoint: `/api/v{version}/Contabil/ConsultarContasContabeis`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os dados de contas contábeis do UAU
        
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
                            "Empresa",
                            "Ano",
                            "LimitarRetornoEm"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "Ano": {
                                "format": "int32",
                                "description": "Ano da máscara de plano de contas",
                                "type": "integer"
                            },
                            "Conta": {
                                "description": "Código da Conta",
                                "type": "string"
                            },
                            "DescricaoConta": {
                                "description": "Descrição da conta",
                                "type": "string"
                            },
                            "LimitarRetornoEm": {
                                "format": "int32",
                                "description": "Limite resultados a serem retornados",
                                "type": "integer"
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
            >>> api = Contabil()
            >>> response = api._consultar_contas_contabeis(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Contabil/ConsultarContasContabeis"
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

