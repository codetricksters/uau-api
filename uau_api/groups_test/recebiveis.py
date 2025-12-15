from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Recebiveis:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_meios_preferenciais_recebimento(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        Permite consultar os meios preferenciais de recebimento que estão ativos.
        
        Endpoint: `/api/v{version}/Recebiveis/ConsultarMeiosPreferenciaisRecebimento`
        HTTP Method: `GET`
        
        Implementation Notes:
        Consulta o meio preferencial de recebimento do cliente.
        
        Args:
            version (Dict[str, Any]): The version
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
            >>> api = Recebiveis()
            >>> response = api._consultar_meios_preferenciais_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Recebiveis/ConsultarMeiosPreferenciaisRecebimento"
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

    def by_numpadraocobranca(
        self,
        version: str,
        id_empresa: str,
        num_padrao_cobranca: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        1. É necessário que exista uma empresa cadastrada.
        2. Numero do padrão de cobrança 0 busca todos os padrões de cobrança.
        
        Endpoint: `/api/v{version}/Recebiveis/PadraoDeCobranca/{IdEmpresa}/{NumPadraoCobranca}`
        HTTP Method: `GET`
        
        Implementation Notes:
        Retorna as chaves pix cadastradas ao CPF/CNPJ informado.
        
        Args:
            IdEmpresa (Dict[str, Any]): The id empresa
            NumPadraoCobranca (Dict[str, Any]): The num padrao cobranca
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "IdEmpresa": {
                    "type": "integer",
                    "in": "path",
                    "required": true,
                    "description": ""
                },
                "NumPadraoCobranca": {
                    "type": "integer",
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
            >>> api = Recebiveis()
            >>> response = api.{_num_padrao_cobranca}(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Recebiveis/PadraoDeCobranca/{IdEmpresa}/{NumPadraoCobranca}"
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

    def parcelas_ecobrancas_do_cliente(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         
         Definição de Negócio:
         1. Busca parcelas e cobranças em aberto do cliente, informando o CPF.
         2. O parametro PesquisaPorNaoTitulares não é obrigatório, se não informado no request ou informado false, buscará somente dos clientes da venda que possuam o tipo 0 - Titular. Caso informado true buscará de todos os clientes da venda independente do tipo.
        
        Endpoint: `/api/v{version}/Recebiveis/ParcelasECobrancasDoCliente`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta as parcelas e cobranças do cliente.
        
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
                            "Cpf",
                            "ValorReajustado"
                        ],
                        "type": "object",
                        "properties": {
                            "Cpf": {
                                "description": "CPF do cliente",
                                "type": "string"
                            },
                            "ValorReajustado": {
                                "description": "False - Não reajustar | True - Reajustar valores",
                                "type": "boolean"
                            },
                            "QtdeParcelas": {
                                "format": "int32",
                                "description": "Quantidade de parcelas a serem retornadas na venda, a contar da mais antiga a receber",
                                "type": "integer"
                            },
                            "DataInicioVencimento": {
                                "format": "date-time",
                                "description": "Periodo inicial de busca dos vencimentos das parcelas",
                                "type": "string"
                            },
                            "DataFimVencimento": {
                                "format": "date-time",
                                "description": "Periodo final de busca dos vencimentos das parcelas",
                                "type": "string"
                            },
                            "PesquisaPorNaoTitulares": {
                                "description": "Informa se a busca deverá ser realizada informando o CPF de qualquer cliente ou apenas de titulares da venda",
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
            >>> api = Recebiveis()
            >>> response = api._parcelase_cobrancas_do_cliente(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Recebiveis/ParcelasECobrancasDoCliente"
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

    def alterar_meio_preferencial_de_recebimento_da_parcela(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        Permite alteração na parcela do meio preferencial de recebimento.
        Permite consultar a alteração realizada na parcela.
        
        Endpoint: `/api/v{version}/Recebiveis/AlterarMeioPreferencialDeRecebimentoDaParcela`
        HTTP Method: `POST`
        
        Implementation Notes:
        Altera o meio preferencial de recebimento do cliente.
        
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
                            "Obra",
                            "Venda",
                            "NumeroParcela",
                            "TipoParcela",
                            "NumeroParcelaGeral",
                            "MeioPreferencialRecebimento"
                        ],
                        "type": "object",
                        "properties": {
                            "Empresa": {
                                "format": "int32",
                                "description": "Empresa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Obra",
                                "type": "string"
                            },
                            "Venda": {
                                "format": "int32",
                                "description": "Número da venda",
                                "type": "integer"
                            },
                            "NumeroParcela": {
                                "format": "int32",
                                "description": "Número da parcela",
                                "type": "integer"
                            },
                            "TipoParcela": {
                                "description": "Tipo de parcela",
                                "type": "string"
                            },
                            "NumeroParcelaGeral": {
                                "format": "int32",
                                "description": "Número geral da parcela",
                                "type": "integer"
                            },
                            "MeioPreferencialRecebimento": {
                                "format": "int32",
                                "description": "Código do novo meio preferencial de recebimento",
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
            >>> api = Recebiveis()
            >>> response = api._alterar_meio_preferencial_de_recebimento_da_parcela(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Recebiveis/AlterarMeioPreferencialDeRecebimentoDaParcela"
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

