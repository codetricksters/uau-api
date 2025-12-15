from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Shopping:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def grava_rendimentos(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        
        Endpoint: `/api/v{version}/Shopping/GravaRendimentos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta a situação das vendas dos lojistas
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "dia": {
                                "format": "date-time",
                                "type": "string"
                            },
                            "lojista": {
                                "type": "boolean"
                            },
                            "empresa": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "obra": {
                                "type": "string"
                            },
                            "venda": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "valor_lancamento": {
                                "format": "double",
                                "type": "number"
                            },
                            "usuario": {
                                "type": "string"
                            },
                            "tipo_usuario": {
                                "format": "int32",
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
            >>> api = Shopping()
            >>> response = api._grava_rendimentos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Shopping/GravaRendimentos"
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

    def importacao_de_parcelas(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Importação de parcelas a receber/recebida para vendas do tipo Aluguel Shopping:
         - URI + /api/v{version}/Shopping/ImportacaoDeParcelas
         
        Definição de Negócio:
        1. Permite importar parcelas a receber/recebida para vendas do tipo Aluguel Shopping com as seguintes regras:
         - Para importação de parcelas A RECEBER, os seguintes campos devem ser desconsiderados ou não preenchidos:
        ValorJurosContrato,ValorCorrecao,ValorMulta,ValorCorrecaoAtraso,ValorJurosAtraso,ValorDesconto,ValorAcrescimo,DataRecebimento,
        DataCalculoReajuste,ValorRecebimento,BancoDeposito,ContaDeposito,Depositado,DataDeposito,Conciliado,DataConciliacao,ValorDescontoCondicional
         - O campo ParcelaRecebida deve estar com o valor '0', indicando que a parcela não foi recebida.
        
        1. Para importação de parcelas RECEBIDAS, a maioria dos campos devem estar preenchidos, exceto nos casos de Parcela tipo Custa, Parcela Depositada ou Conciliada.
         - O campo ParcelaRecebida deve estar com o valor '1', indicando que a parcela foi recebida.
          - Caso a parcela seja do tipo Custa, os campos TipoDaCusta, ObservacaoCusta, OrigemCusta devem estar preenchidos.
          - Caso o campo Depositado seja '1', os campos ValorRecebimento,BancoDeposito,ContaDeposito e DataDeposito devem estar preenchidos.
          - Caso o campo Conciliado seja '1', os campos ValorRecebimento,BancoDeposito,ContaDeposito,DataDeposito e DataConciliacao devem estar preenchidos.
        
        Anexos:
        1. Link para download de exemplos para Postman:
        - Exemplo de parcela a receber: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcela-a-Receber.postman_collection.zip
        - Exemplo de parcela recebida: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcela-Recebida.postman_collection.zip
        
        Endpoint: `/api/v{version}/Shopping/ImportacaoDeParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Importar parcelas de venda tipo Aluguel Shopping.
        
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
                            "Parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "Parcelas": {
                                "description": "Lista de Parcelas a receber/recebidas.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Shopping.Parcelas.ParcelaShoppingRequest"
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
            >>> api = Shopping()
            >>> response = api._importacao_de_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Shopping/ImportacaoDeParcelas"
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

    def consultar_rendimento_lojista(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Shopping/ConsultarRendimentoLojista`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método que consulta para lançamentos de rendimento de lojista e auditor.
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "object",
                        "properties": {
                            "cod_empresa": {
                                "format": "int32",
                                "description": "Código da empresa que possui a obra com controle de rendimento de lojista e auditor",
                                "type": "integer"
                            },
                            "cod_obra": {
                                "type": "string"
                            },
                            "num_venda": {
                                "format": "int32",
                                "type": "integer"
                            },
                            "ini_lancamento": {
                                "format": "date-time",
                                "description": "Data inicial de lançamento da venda registrada com rendimento de lojista e auditor",
                                "type": "string"
                            },
                            "fim_lancamento": {
                                "format": "date-time",
                                "description": "Data final de lançamento da venda registrada com rendimento de lojista e auditor",
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
            >>> api = Shopping()
            >>> response = api._consultar_rendimento_lojista(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Shopping/ConsultarRendimentoLojista"
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

