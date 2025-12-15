from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Reserva:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gravar_reserva(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        
        1. Preencher os parâmetros de request para uso do método.
         - As contrabarras são impotantes para não encerrar a string antes do fim.
         - As datas devem estar no formato: AAAA-MM-DD.
         - SE O VALOR A SER PASSADO É NULL OU VAZIO, NÃO O INFORME NO JSON.
         - Troque apenas os ❌ pelos valores desejados.
         - o JSON deve ser uma string no seguinte formato:
                 {
                   "dados_reserva_json": 
                   "[
                     {
                       \"reserva\": [
                         {
                           \"Empresa_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"NumProd_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"NumPer_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Num_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"CodDvg_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Vendedor_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Login_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Data_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Periodo_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Cliente_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Fone_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"TempoIndet_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Status_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"NumProposta_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"DataConfir_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"UsrConfir_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"UsrCancel_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"DataCancel_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"NumConf_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"CodPesConfir_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"GeraTaxaReserva_rsv\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"ValReserva_rsv\": \"System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"ReservaPaga_rsv\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Banco_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Conta_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"NumEs_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"EntSai_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"DataCad_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"
                         },
                         {
                           \"Empresa_rsv\": \"❌\",
                           \"NumProd_rsv\": \"❌\",
                           \"NumPer_rsv\": \"❌\",
                           \"Num_rsv\": \"❌\",
                           \"CodDvg_rsv\": \"❌\",
                           \"Vendedor_rsv\": \"❌\",
                           \"Login_rsv\": \"❌\",
                           \"Data_rsv\": \"❌\",
                           \"Periodo_rsv\": \"❌\",
                           \"Cliente_rsv\": \"❌\",
                           \"Fone_rsv\": \"❌\",
                           \"TempoIndet_rsv\": \"❌\",
                           \"Status_rsv\": \"❌\",
                           \"NumProposta_rsv\": \"❌\",
                           \"DataConfir_rsv\": \"❌\",
                           \"UsrConfir_rsv\": \"❌\",
                           \"UsrCancel_rsv\": \"❌\",
                           \"DataCancel_rsv\": \"❌\",
                           \"NumConf_rsv\": \"❌\",
                           \"CodPesConfir_rsv\": \"❌\",
                           \"GeraTaxaReserva_rsv\": \"❌\",
                           \"ValReserva_rsv\": \"❌\",
                           \"ReservaPaga_rsv\": \"❌\",
                           \"Banco_rsv\": \"❌\",
                           \"Conta_rsv\": \"❌\",
                           \"NumEs_rsv\": \"❌\",
                           \"EntSai_rsv\": \"❌\",
                           \"DataCad_rsv\": \"❌\"
                         }
                       ]
                     },
                     {
                       \"Taxa\": [
                         {
                           \"Empresa_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Banco_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Conta_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Num_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"EntSai_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Obra_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Data_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Usuario_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Valor_es\": \"System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Natureza_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Cap_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"MesPL_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"NumDoc_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"Emissao_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"HistLanc_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"CategMovFin_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"NumAplic_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"StatusAplic_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"NumSeq_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                           \"DataCad_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"
                         },
                         {
                           \"Empresa_es\": \"❌\",
                           \"Banco_es\": \"❌\",
                           \"Conta_es\": \"❌\",
                           \"Num_es\": \"❌\",
                           \"EntSai_es\": \"❌\",
                           \"Obra_es\": \"❌\",
                           \"Data_es\": \"❌\",
                           \"Usuario_es\": \"❌\",
                           \"Valor_es\": \"❌\",
                           \"Natureza_es\": \"❌\",
                           \"Cap_es\": \"❌\",
                           \"MesPL_es\": \"❌\",
                           \"NumDoc_es\": \"❌\",
                           \"Emissao_es\": \"❌\",
                           \"HistLanc_es\": \"❌\",
                           \"CategMovFin_es\": \"❌\",
                           \"NumAplic_es\": \"❌\",
                           \"StatusAplic_es\": \"❌\",
                           \"NumSeq_es\": \"❌\",
                           \"DataCad_es\": \"❌\"
                         }
                       ]
                     }
                   ]"
                 }
        
        Endpoint: `/api/v{version}/Reserva/GravarReserva`
        HTTP Method: `POST`
        
        Implementation Notes:
        Grava ou altera uma reserva
        
        Rotina de persistência responsável por gerenciar gravação/alteração de uma reserva
        
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
                            "dados_reserva_json": {
                                "description": "Objeto que contém as tabelas 'reserva' e 'taxa'.",
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
            >>> api = Reserva()
            >>> response = api._gravar_reserva(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Reserva/GravarReserva"
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

    def excluir_reserva(
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
        1. Valida usuário e permissões
        
        Endpoint: `/api/v{version}/Reserva/ExcluirReserva`
        HTTP Method: `POST`
        
        Implementation Notes:
        Excluir uma reserva
        
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
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Código da obra",
                                "type": "string"
                            },
                            "num_proposta": {
                                "format": "int32",
                                "description": "Número da proposta",
                                "type": "integer"
                            },
                            "cod_produto": {
                                "format": "int32",
                                "description": "Código do produto",
                                "type": "integer"
                            },
                            "cod_person": {
                                "format": "int32",
                                "description": "Código da personalização",
                                "type": "integer"
                            },
                            "cod_reserva": {
                                "format": "int32",
                                "description": "Codígo da reserva",
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
            >>> api = Reserva()
            >>> response = api._excluir_reserva(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Reserva/ExcluirReserva"
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

    def consultar_reservas(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consulta reservas da personalização que possuem o status informado na request.
        
        Endpoint: `/api/v{version}/Reserva/ConsultarReservas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta as reservas da personalização filtrando por status
        
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
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "cod_produto": {
                                "format": "int32",
                                "description": "Código do produto",
                                "type": "integer"
                            },
                            "cod_person": {
                                "format": "int32",
                                "description": "Código da personalização",
                                "type": "integer"
                            },
                            "status": {
                                "description": "Status da unidade",
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
            >>> api = Reserva()
            >>> response = api._consultar_reservas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Reserva/ConsultarReservas"
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

    def consultar_reserva_vendedor(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint
        
        Definição de Negócio:
        1. Valida usuário e permissões
        
        Endpoint: `/api/v{version}/Reserva/ConsultarReservaVendedor`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta a reserva da personalização filtrando pelo vendedor
        
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
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "num_prod": {
                                "format": "int32",
                                "description": "Código do produto",
                                "type": "integer"
                            },
                            "num_per": {
                                "format": "int32",
                                "description": "Código da personalização",
                                "type": "integer"
                            },
                            "vendedor": {
                                "format": "int32",
                                "description": "Código do vendedor",
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
            >>> api = Reserva()
            >>> response = api._consultar_reserva_vendedor(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Reserva/ConsultarReservaVendedor"
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

    def consultar_reserva_por_codigo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Consulta todas as reservas da personalização que tem o código informado.
        2. Valida usuário e suas permissões.
        
        Endpoint: `/api/v{version}/Reserva/ConsultarReservaPorCodigo`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta as reservas da personalização filtrando pelo código
        
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
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "cod_produto": {
                                "format": "int32",
                                "description": "Código do produto",
                                "type": "integer"
                            },
                            "cod_person": {
                                "format": "int32",
                                "description": "Código da personalização",
                                "type": "integer"
                            },
                            "cod_reserva": {
                                "format": "int32",
                                "description": "Código da reserva",
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
            >>> api = Reserva()
            >>> response = api._consultar_reserva_por_codigo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Reserva/ConsultarReservaPorCodigo"
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

    def consulta_reserva_por_proposta(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Valida usuário e permissões
        
        Endpoint: `/api/v{version}/Reserva/ConsultaReservaPorProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Consulta as reservas da personalização filtrando po código
        
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
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "obra": {
                                "description": "Obra",
                                "type": "string"
                            },
                            "num_proposta": {
                                "format": "int32",
                                "description": "Código da proposta",
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
            >>> api = Reserva()
            >>> response = api._consulta_reserva_por_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Reserva/ConsultaReservaPorProposta"
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

    def consultar_dados_controle_reserva(
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
        1. Valida usuário e permissões.
        
        Endpoint: `/api/v{version}/Reserva/ConsultarDadosControleReserva`
        HTTP Method: `POST`
        
        Implementation Notes:
        Cosulta dados da reserva
        
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
                                "description": "Código da empresa",
                                "type": "integer"
                            },
                            "cod_produto": {
                                "format": "int32",
                                "description": "Código do produto",
                                "type": "integer"
                            },
                            "cod_person": {
                                "format": "int32",
                                "description": "Código da personalização",
                                "type": "integer"
                            },
                            "status": {
                                "description": "Status da unidade",
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
            >>> api = Reserva()
            >>> response = api._consultar_dados_controle_reserva(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Reserva/ConsultarDadosControleReserva"
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

