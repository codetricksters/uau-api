from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class CobrancaPix:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def pix_por_parcelas(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - O objetivo desta rota de API é permitir a consulta e retorno das informações dos PIX gerados para uma determinada parcela ou lista de parcelas
        - Serão retornados os dados do PIX, caso tenha sido gerado para a(s) parcela(s) requisitada(s)
        - Limite máximo de 50 parcelas por requisição
        
        Endpoint: `/api/v{version}/Pix/PixPorParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna as informações do PIX com base na chave de uma ou mais parcelas
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/UAUApi.Models.Venda.PixParcelaVendaRequest"
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
            >>> api = CobrancaPix()
            >>> response = api._pix_por_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Pix/PixPorParcelas"
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

    def reimpressao_pix(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - O objetivo desta rota de API é permitir a consulta e retorno das informações do pix de modo que o usuário possa fazer a impressão 
          dos dados de cobrança.
        - Será retornado o PDF completo e o QRCode em base64.
        - Será retornado o texto do Pix Copia e Cola.
        
        Instituições bancárias suportadas: 
         - 341 = Banco Itaú
         
         - 756 = Banco Sicoob
         
         - 237 = Banco Bradesco
        
         - 246 = Banco Abc
        
        Endpoint: `/api/v{version}/Pix/ReimpressaoPix`
        HTTP Method: `POST`
        
        Implementation Notes:
        Retorna as informações de impreesão do PIX com o PDF, QRCode e Pix Copia e Cola
        
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
                            "TxId"
                        ],
                        "type": "object",
                        "properties": {
                            "TxId": {
                                "description": "Identificador da transação PIX",
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
            >>> api = CobrancaPix()
            >>> response = api._reimpressao_pix(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Pix/ReimpressaoPix"
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

    def consultar_pix_status(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - O objetivo desta rota de API e permitir a consulta do status do PIX 
        
        Instituições bancárias suportadas: 
         - 341 = Banco Itaú
         - 246 = Banco Abc
         - 341 = Banco Itaú
         - 756 = Banco Sicoob
         - 237 = Banco Bradesco
        
        Pré requisito:
        - Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
            - URL + /api/v{version}/Pix/GerarCobrancaPIX 
        Anexos:
        - Exemplo Postman: [ALTERAR EXEMPLO]
        
        Endpoint: `/api/v{version}/Pix/ConsultarPixStatus`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta o status do registro PIX junto a instituição bancária
        
        Args:
            request (Dict[str, Any]): The request
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "request": {
                    "definition": {
                        "type": "array",
                        "items": {
                            "$ref": "#/definitions/UAUApi.Models.Venda.ConsultaPixRequest"
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
            >>> api = CobrancaPix()
            >>> response = api._consultar_pix_status(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Pix/ConsultarPixStatus"
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

    def gerar_cobranca_venda(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        <list type="bullet">
          <item>1. O objetivo desta rota de API é permitir o registro de cobrança por PIX junto à instituição financeira.</item>
          <item>2. O BASE64 gerado é somente o QR Code do PIX.</item>
          <item>3. Instituições bancárias suportadas:</item>
          <list type="bullet">
            <item> - 341 Banco Itaú</item>
            <item> - 756 Banco Sicoob</item>
            <item> - 237 Banco Bradesco</item>
            <item> - 246 Banco ABC</item>
          </list>
        </list>
        <b>Pré Requisitos:</b>
        <list type="bullet">
          <item>1. Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:</item>
          <list type="bullet">
            <item>URL + /api/v{version}/Venda/GerarCobrancaPIX</item>
          </list>
        </list>
        
        Endpoint: `/api/v{version}/Pix/GerarCobrancaVenda`
        HTTP Method: `POST`
        
        Implementation Notes:
        Solicita o registro de cobrança por PIX de uma ou mais parcelas da venda junto a instituição bancária.
        
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
                            "DataDeCalculo",
                            "Antecipar",
                            "UsarPadraoPixAvulso",
                            "AgruparParcelas",
                            "Parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "DataDeCalculo": {
                                "format": "date-time",
                                "description": "Data de cálculo",
                                "type": "string"
                            },
                            "Antecipar": {
                                "description": "Se irá antecipar ou não as parcelas",
                                "type": "boolean"
                            },
                            "UsarPadraoPixAvulso": {
                                "description": "Se irá usar o padrão de pix avulso cadastrado na obra\r\n<list type=\"bullet\"><item>1. Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão de PIX informado, \r\nesse padrão irá sobrepor o padrão da obra, mantendo da configuração de grupo de cobrança.</item></list>",
                                "type": "boolean"
                            },
                            "AgruparParcelas": {
                                "description": "Se irá agrupar ou não as parcelas",
                                "type": "boolean"
                            },
                            "PadraoCobranca": {
                                "format": "int32",
                                "description": "Número do padrão de cobrança que deve ser utilizado. Se informado, irá desconsiderar o da obra e o da parcela\r\n<list type=\"bullet\"><item>1. Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão de PIX informado, \r\nesse padrão irá sobrepor o padrão informado no JSON, o da obra e o da parcela, mantendo da configuração de grupo de cobrança.</item></list>",
                                "type": "integer"
                            },
                            "Parcelas": {
                                "description": "Lista com as parcelas para gerar a cobrança",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ParcelaPixVendaRequest"
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
            >>> api = CobrancaPix()
            >>> response = api._gerar_cobranca_venda(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Pix/GerarCobrancaVenda"
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

    def gerar_cobranca_proposta(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        - O objetivo desta rota de API é permitir o registro de cobrança por PIX junto a instituição financeira 
        - O BASE64 gerado é somente o QRCODE do PIX
        
        Instituições bancárias suportadas: 
         - 341 = Banco Itaú
         - 756 = Banco Sicoob
         - 237 = Banco Bradesco
         - 246 = Banco Abc
        
        Pré requisito:
        - Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
            - URL + /api/v{version}/Venda/GerarCobrancaPIX
        
        Endpoint: `/api/v{version}/Pix/GerarCobrancaProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Solicita o registro de cobrança por PIX de uma ou mais parcelas da venda junto a instituição bancária
        
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
                            "DataDeCalculo",
                            "Antecipar",
                            "UsarPadraoPixAvulso",
                            "AgruparParcelas",
                            "Parcelas"
                        ],
                        "type": "object",
                        "properties": {
                            "DataDeCalculo": {
                                "format": "date-time",
                                "description": "Data de cálculo das parcelas",
                                "type": "string"
                            },
                            "Antecipar": {
                                "description": "Se irá antecipar ou não as parcelas",
                                "type": "boolean"
                            },
                            "UsarPadraoPixAvulso": {
                                "description": "Se irá usar o padrão de pix avulso cadastrado na obra",
                                "type": "boolean"
                            },
                            "AgruparParcelas": {
                                "description": "Se irá agrupar ou não as parcelas",
                                "type": "boolean"
                            },
                            "PadraoCobranca": {
                                "format": "int32",
                                "description": "Número do padrão de cobrança que deve ser utilizado. Se informado, irá desconsiderar o da obra e o da parcela",
                                "type": "integer"
                            },
                            "Parcelas": {
                                "description": "Lista com as parcelas para gerar a cobrança",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.Venda.ParcelaPixPropostaRequest"
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
            >>> api = CobrancaPix()
            >>> response = api._gerar_cobranca_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Pix/GerarCobrancaProposta"
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

