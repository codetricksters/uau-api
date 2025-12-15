from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Webhook:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def by_token(
        self,
        version: str,
        token: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Projeto   : 427564 - Sprint 5 - Engenhanria
        Manutenção: Alterado para extrair do token o tipo de resposta, sendo 1 = Aceito ou 3 = Recusado.
        
        Endpoint: `/api/v{version}/Webhook/ConfirmarRecebimentoOrdemCompra/{token}`
        HTTP Method: `GET`
        
        Implementation Notes:
        Recebe um token da ordem de compra e o decodifica para atualizar o status da ordem de compra automaticamente.
        
        Args:
            token (Dict[str, Any]): The token
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "token": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
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
                    "required": false,
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
            >>> api = Webhook()
            >>> response = api.{token}(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Webhook/ConfirmarRecebimentoOrdemCompra/{token}"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.get(
            path,
            json=params
        )
        return response

    def atualizar_recebimento_pix(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Definição de Negócio:
        
        Endpoint: `/api/v{version}/Webhook/AtualizarRecebimentoPix`
        HTTP Method: `POST`
        
        Implementation Notes:
        Webhook Banco ITAU, para baixa de cobrança PIX
        
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
                            "endToEndId",
                            "txid",
                            "valor",
                            "horario"
                        ],
                        "type": "object",
                        "properties": {
                            "endToEndId": {
                                "type": "string"
                            },
                            "txid": {
                                "type": "string"
                            },
                            "valor": {
                                "type": "string"
                            },
                            "horario": {
                                "format": "date-time",
                                "type": "string"
                            },
                            "infoPagador": {
                                "type": "string"
                            },
                            "devolucoes": {
                                "$ref": "#/definitions/Globaltec.UAU.Cobranca.Services.Interfaces.Itau.PixNotificacaoDevolucaoItau"
                            },
                            "pagador": {
                                "$ref": "#/definitions/Globaltec.UAU.Cobranca.Services.Interfaces.Itau.IPixNotificacaoPagadorItau"
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
                    "required": false,
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
            >>> api = Webhook()
            >>> response = api._atualizar_recebimento_pix(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Webhook/AtualizarRecebimentoPix"
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

    def atualizar_pedido_rec(
        self,
        version: str,
        request_cpf_cnpj: Optional[str] = None,
        request_intencao_venda_id: Optional[str] = None,
        request_intencao_venda_referencia: Optional[str] = None,
        request_pedido_id: Optional[int] = None,
        request_pedido_referencia: Optional[str] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/Webhook/AtualizarPedidoRec`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualizar o pedido de recebimento no UAU de acordo com o retorno da venda ou proposta de venda(recebimento) pela maquininha de cartão
        
        Args:
            version (Dict[str, Any]): The version
            request.cpfCnpj (Dict[str, Any]): CPF/CNPJ
            request.intencaoVendaId (Dict[str, Any]): ID da intenção de venda
            request.intencaoVendaReferencia (Dict[str, Any]): Referência da intenção de venda
            request.pedidoId (Dict[str, Any]): ID do pedido
            request.pedidoReferencia (Dict[str, Any]): Referência do pedido
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "version": {
                    "type": "string",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "request.cpfCnpj": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": "CPF/CNPJ"
                },
                "request.intencaoVendaId": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": "ID da intenção de venda"
                },
                "request.intencaoVendaReferencia": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": "Referência da intenção de venda"
                },
                "request.pedidoId": {
                    "type": "integer",
                    "in": "query",
                    "required": false,
                    "description": "ID do pedido"
                },
                "request.pedidoReferencia": {
                    "type": "string",
                    "in": "query",
                    "required": false,
                    "description": "Referência do pedido"
                },
                "Authorization": {
                    "type": "string",
                    "in": "header",
                    "required": false,
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
            >>> api = Webhook()
            >>> response = api._atualizar_pedido_rec(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Webhook/AtualizarPedidoRec"
        kwargs = {
            "request.cpfCnpj": request_cpf_cnpj,
            "request.intencaoVendaId": request_intencao_venda_id,
            "request.intencaoVendaReferencia": request_intencao_venda_referencia,
            "request.pedidoId": request_pedido_id,
            "request.pedidoReferencia": request_pedido_referencia,
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

