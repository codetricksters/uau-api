from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class AcompanhamentoContratoVenda:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def gravar_acompanhamento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        3. Retorna json com as informações de empresa, obra, número do contrato e número do acompanhamento.
        
        Definição de Negócio:
        1. Permite inserir ou alterar um acompanhamento de contrato de venda. 
        2. O usuário autenticado deve ter permissão de inclusão ou alteração em OBACOMPVENDA, a depender do objetivo (inserir ou editar acompanhamento).
        3. O sistema identifica que é uma edição no acompanhamento quando a propriedade [NumAcompanhamento] está preenchida. Em caso de não informação deste campo, será gravado um novo acompanhamento.
        4. O usuário autenticado deve ter permissão de inclusão em OBMEDICAOVENDA.
        5. Em caso de manutenção de um acompanhamento, as informações serão sobrescritas e as quantidades "Qtde medida" e "Qtde falta medir" calculadas a partir da propriedade [QtdeAMedir] informada.
        
        Endpoint: `/api/v{version}/AcompanhamentoContratoVenda/GravarAcompanhamento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Método responsável por gravar o acompanhamento de contrato de vendas
        
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
                            "NumContrato",
                            "PeriodoInicio",
                            "ListaDeProdutos",
                            "Status"
                        ],
                        "type": "object",
                        "properties": {
                            "NumAcompanhamento": {
                                "format": "int32",
                                "description": "Número do acompanhamento para o caso de manutenção. Para criação de um novo acompanhamento, este campo não deve ser informado.",
                                "type": "integer"
                            },
                            "Empresa": {
                                "format": "int32",
                                "description": "Código da Empresa",
                                "type": "integer"
                            },
                            "Obra": {
                                "description": "Código da Obra",
                                "type": "string"
                            },
                            "NumContrato": {
                                "description": "Número do contrato",
                                "type": "string"
                            },
                            "PeriodoInicio": {
                                "format": "date-time",
                                "description": "Período de acompanhamento - Início",
                                "type": "string"
                            },
                            "PeriodoFim": {
                                "format": "date-time",
                                "description": "Período de acompanhamento - Fim",
                                "type": "string"
                            },
                            "ListaDeProdutos": {
                                "description": "Produtos que serão inseridos/alterados no acompanhamento",
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.AcompanhamentoContratoVenda.ProdutoAcompanhamentoRequest"
                                }
                            },
                            "Responsavel": {
                                "format": "int32",
                                "description": "Código do responsável pelo acompanhamento",
                                "type": "integer"
                            },
                            "Status": {
                                "format": "int32",
                                "description": "Status (0 - Não aprovado | 1 - Aprovado)",
                                "type": "integer"
                            },
                            "ObservacaoParaEntrega": {
                                "description": "Observação para entrega",
                                "type": "string"
                            },
                            "Motorista": {
                                "format": "int32",
                                "description": "Código do motorista",
                                "type": "integer"
                            },
                            "CaminhaoPlaca": {
                                "description": "Placa do caminhão",
                                "type": "string"
                            },
                            "UFPlaca": {
                                "description": "Estado da placa do caminhão",
                                "type": "string"
                            },
                            "LocalPrestacaoServico": {
                                "format": "int32",
                                "description": "Local da prestação de serviço - município",
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
            >>> api = AcompanhamentoContratoVenda()
            >>> response = api._gravar_acompanhamento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/AcompanhamentoContratoVenda/GravarAcompanhamento"
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

