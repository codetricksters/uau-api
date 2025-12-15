from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class NotasFiscais:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_nfentrada(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Ao menos uma chave de pesquisa deve ser preenchida sendo elas ([CodigoEmpresa],
        [CnpjFornecedor], [CodigoFornecedor], [DataInicial], [ListaNFEntrada]).
        2. Caso tenha informado a propriedade da Obra, a Empresa torna-se obrigatória.
        3. Preenchimento da [DataInicial] torna [DataFinal] obrigatória.
        4. Preenchimento da [DataFinal] torna [DataInicial] obrigatória.
        5. Obra só vai achar informação se a nota estiver vinculada a um processo.
        6. [ListaNFEntrada] Cada objeto deve ter obrigatoriamente o [CodigoEmpresa] e o [NumeroNotaFiscal ou NumeroNotaFiscalEletronica]
        6.1 NumeroNotaFiscal = Número de controle da nota fiscal (Obs: no retorno dos dados esse valor fica no campo Numero)
        6.2 NumeroNotaFiscalEletronica = Número da nota fiscal eletrônica, informado na DANFE ou NFS-e (Obs: no retorno dos dados esse valor fica no campo NumeroNotaFiscal)
        
        Endpoint: `/api/v{version}/NotasFiscais/ConsultarNFEntrada`
        HTTP Method: `POST`
        
        Implementation Notes:
        Listagem de nota fiscal
        
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
                            "ListaNFEntrada": {
                                "description": "Lista com notas fiscais especificas para busca.",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.UAUApi.Models.NFEntrada"
                                }
                            },
                            "CodigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa onde foi lançada a nota.",
                                "type": "integer"
                            },
                            "CodigoObra": {
                                "description": "Código da obra *Obra do processo vinculado a nota.",
                                "type": "string"
                            },
                            "CnpjFornecedor": {
                                "description": "CNPJ/CPF do fornecedor, somente números.",
                                "type": "string"
                            },
                            "CodigoFornecedor": {
                                "description": "Código da pessoa (fornecedor) no UAU.",
                                "type": "string"
                            },
                            "DataInicial": {
                                "format": "date-time",
                                "description": "Data inicial para busca de notas em um período.",
                                "type": "string"
                            },
                            "DataFinal": {
                                "format": "date-time",
                                "description": "Data final para busca de notas em um período.",
                                "type": "string"
                            },
                            "TipoPeriodo": {
                                "format": "int32",
                                "description": "Indica por qual tipo de data irá ser feito o filtro 1 - Entrada ou 2 - Emissão",
                                "enum": [
                                    1,
                                    2
                                ],
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
            >>> api = NotasFiscais()
            >>> response = api._consultarnf_entrada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/NotasFiscais/ConsultarNFEntrada"
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

    def salvar_arquivo_xmlnotafiscal_entrada(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
        2. Preencher os parâmetros de request para uso do endpoint.
        
        Definição de Negócio:
        1. Poderá ser enviado uma lista de arquivos XML.
        2. Será permitido no máximo uma lista com 20 arquivos.
        3. Tipo do arquivo XML [TipoXML]
            0 para NF-e
            1 para CT-e
            2 para NFS-e,
        4. Arquivo XML da nota fiscal (Texto do arquivo) [ArquivoXML].
        
        Endpoint: `/api/v{version}/NotasFiscais/SalvarArquivoXMLnotafiscalEntrada`
        HTTP Method: `POST`
        
        Implementation Notes:
        Salvar o arquivo XML das notas fiscais para importação no sistema.
        
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
                            "$ref": "#/definitions/UAUApi.Models.NotasFiscais.SalvarArquivoXMLnotafiscalEntradaRequest"
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
            >>> api = NotasFiscais()
            >>> response = api._salvar_arquivoxm_lnotafiscal_entrada(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/NotasFiscais/SalvarArquivoXMLnotafiscalEntrada"
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

