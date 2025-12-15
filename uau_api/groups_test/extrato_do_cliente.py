from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ExtratoDoCliente:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gerar_pdfextrato_cliente(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Preencher as opções de visualização do extrato nos módulos Vendas/Shopping, menu Utilitários, submenu Configurações extrato da venda (Visão Cliente)
        
        Obs.: Parâmetros para impressão deste extrato são configurados na tela descrita neste virtuau: https://ajuda.globaltec.com.br/virtuau/configuracao-extrato-de-vendas-visao-cliente
        
        Endpoint: `/api/v{version}/ExtratoDoCliente/GerarPDFExtratoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método utilizado gerar os extratos em arquivos PDF e converte-los para string base64.
        
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
                            "empresa",
                            "obra",
                            "numVenda",
                            "dataCalculo"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Número da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "numVenda": {
                                "format": "int32",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "tipoOrdenacao": {
                                "format": "int32",
                                "description": "Verifica se irá ordernar por data de vencimento. 0 - Ordenação padrão, 1 - Ordenação por data de vencimento",
                                "type": "integer"
                            },
                            "valorAntecipado": {
                                "description": "Verifica se irá mostrar o extrato antecipado. TRUE - Irá mostrar. FALSE - Não irá mostrar",
                                "type": "boolean"
                            },
                            "dataProrrogacao": {
                                "description": "Verifica se irá mostrar a data de prorrogação. TRUE - Irá mostrar. FALSE - Não irá mostrar",
                                "type": "boolean"
                            },
                            "ocultarPersonalizacao": {
                                "description": "Verifica se irá as personalizações. TRUE - Irá ocultar. FALSE - Não irá ocultar",
                                "type": "boolean"
                            },
                            "ocultarUsuario": {
                                "description": "Verifica se irá ocultar o usuário. TRUE - Irá ocultar. FALSE - Não irá ocultar",
                                "type": "boolean"
                            },
                            "dataCalculo": {
                                "format": "date-time",
                                "description": "Data de cálculo a ser utilizada para calcular as parcelas do relatório.",
                                "type": "string"
                            },
                            "residuoIraComporValorTotal": {
                                "description": "Indica se o valor do resíduo será somado ao valor total. TRUE - Irá somar; FALSE - Não irá somar",
                                "type": "boolean"
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
            >>> api = ExtratoDoCliente()
            >>> response = api._gerarpdf_extrato_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ExtratoDoCliente/GerarPDFExtratoCliente"
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

    def gerar_pdfextrato_cliente_v2(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Preencher as opções de visualização do extrato nos módulos Vendas/Shopping, menu Utilitários, submenu Configurações extrato da venda (Visão Cliente)
        
        Obs.: Parâmetros para impressão deste extrato são configurados na tela descrita neste virtuau: https://ajuda.globaltec.com.br/virtuau/configuracao-extrato-de-vendas-visao-cliente
        
        Endpoint: `/api/v{version}/ExtratoDoCliente/GerarPDFExtratoClienteV2`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método utilizado gerar os extratos em arquivos PDF e converte-los para string base64.
        
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
                            "empresa",
                            "obra",
                            "numVenda",
                            "dataCalculo"
                        ],
                        "type": "object",
                        "properties": {
                            "empresa": {
                                "format": "int32",
                                "description": "Número da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "numVenda": {
                                "format": "int32",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "tipoOrdenacao": {
                                "format": "int32",
                                "description": "Verifica se irá ordernar por data de vencimento. 0 - Ordenação padrão, 1 - Ordenação por data de vencimento",
                                "type": "integer"
                            },
                            "valorAntecipado": {
                                "description": "Verifica se irá mostrar o extrato antecipado. TRUE - Irá mostrar. FALSE - Não irá mostrar",
                                "type": "boolean"
                            },
                            "dataProrrogacao": {
                                "description": "Verifica se irá mostrar a data de prorrogação. TRUE - Irá mostrar. FALSE - Não irá mostrar",
                                "type": "boolean"
                            },
                            "ocultarPersonalizacao": {
                                "description": "Verifica se irá as personalizações. TRUE - Irá ocultar. FALSE - Não irá ocultar",
                                "type": "boolean"
                            },
                            "ocultarUsuario": {
                                "description": "Verifica se irá ocultar o usuário. TRUE - Irá ocultar. FALSE - Não irá ocultar",
                                "type": "boolean"
                            },
                            "dataCalculo": {
                                "format": "date-time",
                                "description": "Data de cálculo a ser utilizada para calcular as parcelas do relatório.",
                                "type": "string"
                            },
                            "residuoIraComporValorTotal": {
                                "description": "Indica se o valor do resíduo será somado ao valor total. TRUE - Irá somar; FALSE - Não irá somar",
                                "type": "boolean"
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
            >>> api = ExtratoDoCliente()
            >>> response = api._gerarpdf_extrato_clientev2(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ExtratoDoCliente/GerarPDFExtratoClienteV2"
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

    def consultar_saldo_cessoes_direito_anteriores(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/ExtratoDoCliente/ConsultarSaldoCessoesDireitoAnteriores`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta as vendas anteriores a essa, gerada por cessão de direito, retornando o saldo já pago nas vendas anteriores
        
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
                            "empresa": {
                                "format": "int32",
                                "description": "Código da Empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da Obra",
                                "type": "string"
                            },
                            "num_venda": {
                                "format": "int32",
                                "description": "Número da venda",
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
            >>> api = ExtratoDoCliente()
            >>> response = api._consultar_saldo_cessoes_direito_anteriores(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ExtratoDoCliente/ConsultarSaldoCessoesDireitoAnteriores"
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

    def consultar_dados_demonstrativo_pagto_cliente(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        Endpoint: `/api/v{version}/ExtratoDoCliente/ConsultarDadosDemonstrativoPagtoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta os dados das parcelas pagas, informações do cliente e as unidades/produtos de uma determinada venda.
        Contém as chamadas dos métodos ConsultarItensRecebidas e ConsultarParcelasRecebidasCliente retornando um dataset e suas tabelas.
        OBS.: A instruçãoa [tipos_parc] se refere à parcelas que não devem ser mostradas no extrato do cliente, se enviar vazio, vai mostrar todas.
        
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
                            "empresa": {
                                "format": "int32",
                                "description": "Número da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "num_venda": {
                                "format": "int32",
                                "description": "Número do contrato de venda",
                                "type": "integer"
                            },
                            "tipos_parc": {
                                "description": "Tipos de parcelas a NÃO serem exibidos no relatório",
                                "type": "string"
                            },
                            "tipo_ordenacao": {
                                "format": "int32",
                                "description": "Tipo ordenação",
                                "type": "integer"
                            },
                            "mostrara_pagas": {
                                "description": "Identifica se deve mostrar dados a pagar",
                                "type": "boolean"
                            },
                            "princ_juros": {
                                "description": "Identifica se deve mostrar principal com juros",
                                "type": "boolean"
                            },
                            "descontopor_adiantamento": {
                                "description": "Identifica se deve aplicar desconto por adiantamento",
                                "type": "boolean"
                            },
                            "valor_antecipado": {
                                "description": "Identifica se os valores devem vir com antecipação ou não",
                                "type": "boolean"
                            },
                            "nome_fantasia": {
                                "description": "Nome Fantasia",
                                "type": "boolean"
                            },
                            "ocultapref_custas": {
                                "description": "Identifica se deve ocultar o prefixo \"Custa-\"  das descrições de custas",
                                "type": "boolean"
                            },
                            "dataCalculo": {
                                "format": "date-time",
                                "description": "Data de cálculo a ser calculado as parcelas",
                                "type": "string"
                            },
                            "exibirDataDeposito": {
                                "description": "Exibe data de depósito",
                                "type": "boolean"
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
            >>> api = ExtratoDoCliente()
            >>> response = api._consultar_dados_demonstrativo_pagto_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ExtratoDoCliente/ConsultarDadosDemonstrativoPagtoCliente"
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

