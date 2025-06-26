from typing import Dict, Any, List, Optional
from datetime import datetime
from uau_api.requestsapi import RequestsApi

import requests
class DocumentosDigitaisIntegracao:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

    def enviar_envelope_de_documento(
        self,
        lista_de_pessoas: Optional[List[Dict]] = None,
        lista_de_documentos: Optional[List[Dict]] = None,
        mensagem: Optional[str] = None,
        codigo_do_sistema: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `DocumentosDigitais/EnviarEnvelopeDeDocumento`
        HTTP Method: `POST`
        
        Implementation Notes:
         Definição Técnica:
           Rota de envio de documentos digitais para assinatura atraves dos sistemas configurados. 
           Sendo possivel utilizar Docusign ou Clicksign 
           Passos: 
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
          Parametros:
        ListaDePessoas
        Nome_enva =>  Nome da pessoa
        Ordem_enva => Ordem de assinatura (Apenas para Docusign)
        Email_enva => Email da pessoa 
        
        
        ListaDeDocumentos
        DocumentoBase64_envd => Documento em base64
        Nome_envd => nome do documento 
        Ordem_envd => ordem de envio do documento (Apenas para Docusign)
        Extensao_envd => Extensão do arquivo em formato: *.extensao exemplo: *.pdf
        
        
        Mensagem (Apenas para ClickSign)
        CodigoDoSistema => Codigo do Sistema Utilizado 
          Obs. Consulta utilizando a rota de ConsultaDocumentosDigitaisAtivos
        
        
        
        Args:
            ListaDePessoas (List[Dict[str, Any]]): The lista de pessoas
            ListaDeDocumentos (List[Dict[str, Any]]): The lista de documentos
            Mensagem (str): The mensagem
            CodigoDoSistema (int): The codigo do sistema
        
        Parameter Structure:
        
            {
                "ListaDePessoas": [
                    {
                        "Email_enva": "string",
                        "Nome_enva": "string",
                        "Ordem_enva": 0
                    }
                ],
                "ListaDeDocumentos": [
                    {
                        "DocumentoBase64_envd": "string",
                        "Extensao_envd": "string",
                        "Nome_envd": "string",
                        "Ordem_envd": 0
                    }
                ],
                "Mensagem": "string",
                "CodigoDoSistema": 0
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
        path = "DocumentosDigitais/EnviarEnvelopeDeDocumento"
        kwargs = {
            "ListaDePessoas": lista_de_pessoas,
            "ListaDeDocumentos": lista_de_documentos,
            "Mensagem": mensagem,
            "CodigoDoSistema": codigo_do_sistema,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_documentos_enviados(
        self,
        numero_do_envelope: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `DocumentosDigitais/ConsultarDocumentosEnviados`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
          Rota de consulta de documentos enviados da Docusign atraves do numero de identificação do envelope
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
          Parametros:
        Codigo identificador do envelope
        
        
        
        Args:
            NumeroDoEnvelope (int): The numero do envelope
        
        Parameter Structure:
        
            {
                "NumeroDoEnvelope": 0
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
        path = "DocumentosDigitais/ConsultarDocumentosEnviados"
        kwargs = {
            "NumeroDoEnvelope": numero_do_envelope,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_assinaturas_enviadas(
        self,
        numero_do_envelope: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `DocumentosDigitais/ConsultarAssinaturasEnviadas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica: 
          Rota de consulta de assinaturas enviadas da Docusign atraves do numero de identificação do envelope 
          Passos:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
          Parametros:
        Codigo identificador do envelope
        
        
        
        Args:
            NumeroDoEnvelope (int): The numero do envelope
        
        Parameter Structure:
        
            {
                "NumeroDoEnvelope": 0
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
        path = "DocumentosDigitais/ConsultarAssinaturasEnviadas"
        kwargs = {
            "NumeroDoEnvelope": numero_do_envelope,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consulta_documentos_digitais_ativos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `DocumentosDigitais/ConsultaDocumentosDigitaisAtivos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica: 
          Rota de consulta de documentos digitais ativos e configurados no sistema. 
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario 
          Retorno do metodo é o codigo e nome dos sistemas configurados para assinatura digital
        
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
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
        path = "DocumentosDigitais/ConsultaDocumentosDigitaisAtivos"
        kwargs = {
            "Detalhe": detalhe,
            "Mensagem": mensagem,
            "Descricao": descricao,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

    def consultar_envelope_documentos_codigo_externo(
        self,
        envelope_id: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `DocumentosDigitais/ConsultarEnvelopeDocumentosCodigoExterno`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica: 
          Rota de consulta de envelopes da Docusign apenas pelo codigo externo do evelope. 
          O código externo é o código identificador do envelope na Docusign 
          Passos: 
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
          Parametros:
        Codigo externo do envelope
        
        
        
        Args:
            EnvelopeId (str): The envelope id
        
        Parameter Structure:
        
            {
                "EnvelopeId": "string"
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
        path = "DocumentosDigitais/ConsultarEnvelopeDocumentosCodigoExterno"
        kwargs = {
            "EnvelopeId": envelope_id,
        }
        params = {k: v for k, v in kwargs.items() if v is not None}
        try:
            response = self.api.post(
                path,
                json=params
            )
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return response.text

