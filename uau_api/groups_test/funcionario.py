from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class Funcionario:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def consultar_funcionario(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Consultar os dados dos funcionários URI + api/v{version:apiVersion}/Funcionario/ConsultarFuncionario
        3. Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        Consulta os dados de funcionários do UAU, podendo fazer filtros pela empresa, obra, pessoa, funcionário, matrícula e situação.
        1. Deve informar obrigatoriamente o código da empresa.
        2. Pode informar opcionalmente o código da obra, pessoa, funcionário, matrícula e situação.
        
        VirtUau:
        -  Link para Virtuau relacionado:https://ajuda.globaltec.com.br/virtuau/cadastro-de-funcionarios/
        
        Endpoint: `/api/v{version}/Funcionario/ConsultarFuncionario`
        HTTP Method: `POST`
        
        Implementation Notes:
        Objetivo: Consultar os dados de funcionários do UAU
        
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
                            "CodigoEmpresa"
                        ],
                        "type": "object",
                        "properties": {
                            "CodigoEmpresa": {
                                "format": "int32",
                                "description": "Código da empresa de lotação do funcionário.",
                                "type": "integer"
                            },
                            "CodigoObra": {
                                "description": "Código da obra de lotação do funcionário.",
                                "type": "string"
                            },
                            "CodigoPessoa": {
                                "format": "int32",
                                "description": "Código do cadastro de pessoas.",
                                "type": "integer"
                            },
                            "CodigoFuncionario": {
                                "format": "int32",
                                "description": "Controle interno (NumCap).",
                                "type": "integer"
                            },
                            "Matricula": {
                                "description": "Matrícula do funcionário.",
                                "type": "string"
                            },
                            "Situacao": {
                                "format": "int32",
                                "description": "Código da situação do funcionário.\r\n  [0 - Ativo, 1 - Demitido, 2 - Doente, 3 - Licenciado, 4 - Outros, 5 - Em demissão, 6 - Em férias, 7 - Resc.Complementar, 8 - Término de Vínculo]",
                                "enum": [
                                    0,
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6,
                                    7,
                                    8
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
            >>> api = Funcionario()
            >>> response = api._consultar_funcionario(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/Funcionario/ConsultarFuncionario"
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

