from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
from http import HTTPStatus

class DocumentosDigitaisIntegracao:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def enviar_envelope_de_documento(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
         Rota de envio de documentos digitais para assinatura atraves dos sistemas configurados. <br />
         Sendo possivel utilizar Docusign ou Clicksign <br />
         Passos: 
         1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
         2. Preencher os parâmetros de request para uso do método.
         Parametros:
         1. ListaDePessoas
        -  Nome_enva =&gt;  Nome da pessoa
        -  Ordem_enva =&gt; Ordem de assinatura (Apenas para Docusign)
        -  Email_enva =&gt; Email da pessoa 
         2. ListaDeDocumentos
        -  DocumentoBase64_envd =&gt; Documento em base64
        -  Nome_envd =&gt; nome do documento 
        -  Ordem_envd =&gt; ordem de envio do documento (Apenas para Docusign)
        -  Extensao_envd =&gt; Extensão do arquivo em formato: \*.extensao exemplo: *.pdf
         3. Mensagem (Apenas para ClickSign)
         4. CodigoDoSistema =&gt; Codigo do Sistema Utilizado <br />
         Obs. Consulta utilizando a rota de ConsultaDocumentosDigitaisAtivos
        
        Endpoint: `/api/v{version}/DocumentosDigitais/EnviarEnvelopeDeDocumento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Esta rota faz o envio de documentos digitais para assinatira digital
        
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
                            "ListaDePessoas",
                            "ListaDeDocumentos",
                            "CodigoDoSistema"
                        ],
                        "type": "object",
                        "properties": {
                            "ListaDePessoas": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.DocumentosDigitais.PessoasEvelopeRequest"
                                }
                            },
                            "ListaDeDocumentos": {
                                "type": "array",
                                "items": {
                                    "$ref": "#/definitions/UAUApi.Models.DocumentosDigitais.DocumentoEnvelopeRequest"
                                }
                            },
                            "Mensagem": {
                                "type": "string"
                            },
                            "CodigoDoSistema": {
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
            >>> api = DocumentosDigitaisIntegracao()
            >>> response = api._enviar_envelope_de_documento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/DocumentosDigitais/EnviarEnvelopeDeDocumento"
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

    def consultar_documentos_enviados(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Rota de consulta de documentos enviados da Docusign atraves do numero de identificação do envelope
        
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        Parametros:
        - Codigo identificador do envelope
        
        Endpoint: `/api/v{version}/DocumentosDigitais/ConsultarDocumentosEnviados`
        HTTP Method: `POST`
        
        Implementation Notes:
        Essa rota faz consulta ao documentos enviados da Docusign atraves do numero de identificação do envelope
        
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
                            "NumeroDoEnvelope": {
                                "format": "int32",
                                "description": "Numero identificador do envelope",
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
            >>> api = DocumentosDigitaisIntegracao()
            >>> response = api._consultar_documentos_enviados(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/DocumentosDigitais/ConsultarDocumentosEnviados"
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

    def consultar_assinaturas_enviadas(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Rota de consulta de assinaturas enviadas da Docusign atraves do numero de identificação do envelope <br />
        Passos:
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        Parametros:
        - Codigo identificador do envelope
        
        Endpoint: `/api/v{version}/DocumentosDigitais/ConsultarAssinaturasEnviadas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Essa rota faz consulta a assinatura envidas da Docusign atraves do numero de identificação do envelope
        
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
                            "NumeroDoEnvelope": {
                                "format": "int32",
                                "description": "Numero identificador do envelope",
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
            >>> api = DocumentosDigitaisIntegracao()
            >>> response = api._consultar_assinaturas_enviadas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/DocumentosDigitais/ConsultarAssinaturasEnviadas"
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

    def consulta_documentos_digitais_ativos(
        self,
        version: str,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Rota de consulta de documentos digitais ativos e configurados no sistema. <br />
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario 
        Retorno do metodo é o codigo e nome dos sistemas configurados para assinatura digital
        
        Endpoint: `/api/v{version}/DocumentosDigitais/ConsultaDocumentosDigitaisAtivos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Rota de consulta de documentos digitais ativos e configurados no sistema
        
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
            >>> api = DocumentosDigitaisIntegracao()
            >>> response = api._consulta_documentos_digitais_ativos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/DocumentosDigitais/ConsultaDocumentosDigitaisAtivos"
        kwargs = {
            "Authorization": authorization,
            "X-INTEGRATION-Authorization": x_integration_authorization,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        response = self.api.post(
            path,
            json=params
        )
        return response

    def consultar_envelope_documentos_codigo_externo(
        self,
        version: str,
        request: Optional[Dict] = None,
        authorization: Optional[str] = None,
        x_integration_authorization: Optional[str] = None
    ) -> requests.Response:
        """
        Rota de consulta de envelopes da Docusign apenas pelo codigo externo do evelope. <br />
        O código externo é o código identificador do envelope na Docusign <br />
        Passos: 
        1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        2. Preencher os parâmetros de request para uso do método.
        Parametros:
        - Codigo externo do envelope
        
        Endpoint: `/api/v{version}/DocumentosDigitais/ConsultarEnvelopeDocumentosCodigoExterno`
        HTTP Method: `POST`
        
        Implementation Notes:
        Esta rota faz consulta de envelopes da Docusign apenas pelo codigo externo (o código externo é o código identificador do envelope na Docusign)
        
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
                            "EnvelopeId": {
                                "description": "Codigo externo do envelope",
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
            >>> api = DocumentosDigitaisIntegracao()
            >>> response = api._consultar_envelope_documentos_codigo_externo(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = f"/api/v{version}/DocumentosDigitais/ConsultarEnvelopeDocumentosCodigoExterno"
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

