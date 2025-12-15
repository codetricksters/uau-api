from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class ChavePix:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def by_cpfcnpj(
        self,
        version: str,
        cpf_cnpj: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        1. É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        
        Endpoint: `/api/v{version}/ChavePix/Pessoas/Consultar/{cpfCnpj}`
        HTTP Method: `GET`
        
        Implementation Notes:
        Retorna as chaves pix cadastradas ao CPF/CNPJ informado.
        
        Args:
            cpfCnpj (Dict[str, Any]): The cnpj
            version (Dict[str, Any]): The version
            Authorization (Dict[str, Any]): Token Authentication
            X-INTEGRATION-Authorization (Dict[str, Any]): Token De Integração
        
        Parameter Structure:
        
            {
                "cpfCnpj": {
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
            >>> api = ChavePix()
            >>> response = api.{cpf_cnpj}(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ChavePix/Pessoas/Consultar/{cpfCnpj}"
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

    def deletar(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        1. É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        2. O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        3. A chave pix deve ter no máximo 77 caracteres.
        
        Endpoint: `/api/v{version}/ChavePix/Pessoas/Deletar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Remove uma chave pix de pessoa.
        
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
                            "cpfCnpj",
                            "chavePix",
                            "tipoChavePix"
                        ],
                        "type": "object",
                        "properties": {
                            "cpfCnpj": {
                                "description": "CPF do cliente",
                                "type": "string"
                            },
                            "chavePix": {
                                "description": "Chave Pix",
                                "type": "string"
                            },
                            "tipoChavePix": {
                                "format": "int32",
                                "description": "0 - CPF/CNPJ, 1 - Celular, 2 - E-mail, 3 - Chave aleatória",
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
            >>> api = ChavePix()
            >>> response = api._deletar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ChavePix/Pessoas/Deletar"
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

    def atualizar(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        1. É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        2. O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        3. A chave pix deve ter no máximo 77 caracteres.
        4. A chave padrão deve ser: 0 - NÃO, 1 - SIM.
        5. O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.
        
        Endpoint: `/api/v{version}/ChavePix/Pessoas/Atualizar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Atualiza a chave pix de uma pessoa.
        
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
                            "cpfCnpj",
                            "chavePix",
                            "tipoChavePix",
                            "chavePixPadrao",
                            "ativoInativo"
                        ],
                        "type": "object",
                        "properties": {
                            "cpfCnpj": {
                                "description": "CPF do cliente",
                                "type": "string"
                            },
                            "chavePix": {
                                "description": "Chave Pix",
                                "type": "string"
                            },
                            "tipoChavePix": {
                                "format": "int32",
                                "description": "0 - CPF/CNPJ, 1 - Celular, 2 - E-mail, 3 - Chave aleatória",
                                "type": "integer"
                            },
                            "chavePixPadrao": {
                                "format": "int32",
                                "description": "0 - SIM, 1 - NÃO",
                                "type": "integer"
                            },
                            "ativoInativo": {
                                "format": "int32",
                                "description": "0 - ATIVO, 1 - INATIVO",
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
            >>> api = ChavePix()
            >>> response = api._atualizar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ChavePix/Pessoas/Atualizar"
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

    def cadastrar(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request com os dados do usuário para uso do método.
        
        Regras de Negócio:
        1. É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
        2. O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
        3. A chave pix deve ter no máximo 77 caracteres.
        4. A chave padrão deve ser: 0 - NÃO, 1 - SIM.
        5. O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.
        
        Endpoint: `/api/v{version}/ChavePix/Pessoas/Cadastrar`
        HTTP Method: `POST`
        
        Implementation Notes:
        Cadastra uma nova chave pix para a pessoa.
        
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
                            "cpfCnpj",
                            "chavePix",
                            "tipoChavePix",
                            "chavePixPadrao",
                            "ativoInativo"
                        ],
                        "type": "object",
                        "properties": {
                            "cpfCnpj": {
                                "description": "CPF do cliente",
                                "type": "string"
                            },
                            "chavePix": {
                                "description": "Chave Pix",
                                "type": "string"
                            },
                            "tipoChavePix": {
                                "format": "int32",
                                "description": "0 - CPF/CNPJ, 1 - Celular, 2 - E-mail, 3 - Chave aleatória",
                                "type": "integer"
                            },
                            "chavePixPadrao": {
                                "format": "int32",
                                "description": "0 - SIM, 1 - NÃO",
                                "type": "integer"
                            },
                            "ativoInativo": {
                                "format": "int32",
                                "description": "0 - ATIVO, 1 - INATIVO",
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
            >>> api = ChavePix()
            >>> response = api._cadastrar(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/ChavePix/Pessoas/Cadastrar"
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

