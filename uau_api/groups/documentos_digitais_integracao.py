"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class DocumentosDigitaisIntegracao:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def enviar_envelope_de_documento(
        self,
        lista_de_pessoas: Optional[List[Dict]] = None,
        lista_de_documentos: Optional[List[Dict]] = None,
        mensagem: Optional[str] = None,
        codigo_do_sistema: Optional[int] = None
    ) -> dict:
        """Esta rota faz o envio de documentos digitais para assinatira digital

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


        """
        path = "DocumentosDigitais/EnviarEnvelopeDeDocumento"
        return self.api.post(
            path,
            json={
                "ListaDePessoas": lista_de_pessoas,
                "ListaDeDocumentos": lista_de_documentos,
                "Mensagem": mensagem,
                "CodigoDoSistema": codigo_do_sistema,
            }
        )

    def consultar_documentos_enviados(
        self,
        numero_do_envelope: Optional[int] = None
    ) -> dict:
        """Essa rota faz consulta ao documentos enviados da Docusign atraves do numero de identificação do envelope

        Implementation Notes:
        Definição Técnica:
  Rota de consulta de documentos enviados da Docusign atraves do numero de identificação do envelope

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
  Parametros:
Codigo identificador do envelope


        """
        path = "DocumentosDigitais/ConsultarDocumentosEnviados"
        return self.api.post(
            path,
            json={
                "NumeroDoEnvelope": numero_do_envelope,
            }
        )

    def consultar_assinaturas_enviadas(
        self,
        numero_do_envelope: Optional[int] = None
    ) -> dict:
        """Essa rota faz consulta a assinatura envidas da Docusign atraves do numero de identificação do envelope

        Implementation Notes:
        Definição Técnica: 
  Rota de consulta de assinaturas enviadas da Docusign atraves do numero de identificação do envelope 
  Passos:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
  Parametros:
Codigo identificador do envelope


        """
        path = "DocumentosDigitais/ConsultarAssinaturasEnviadas"
        return self.api.post(
            path,
            json={
                "NumeroDoEnvelope": numero_do_envelope,
            }
        )

    def consulta_documentos_digitais_ativos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Rota de consulta de documentos digitais ativos e configurados no sistema

        Implementation Notes:
        Definição Técnica: 
  Rota de consulta de documentos digitais ativos e configurados no sistema. 

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario 
  Retorno do metodo é o codigo e nome dos sistemas configurados para assinatura digital


        """
        path = "DocumentosDigitais/ConsultaDocumentosDigitaisAtivos"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_envelope_documentos_codigo_externo(
        self,
        envelope_id: Optional[str] = None
    ) -> dict:
        """Esta rota faz consulta de envelopes da Docusign apenas pelo codigo externo (o código externo é o código identificador do envelope na Docusign)

        Implementation Notes:
        Definição Técnica: 
  Rota de consulta de envelopes da Docusign apenas pelo codigo externo do evelope. 
  O código externo é o código identificador do envelope na Docusign 
  Passos: 

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
  Parametros:
Codigo externo do envelope


        """
        path = "DocumentosDigitais/ConsultarEnvelopeDocumentosCodigoExterno"
        return self.api.post(
            path,
            json={
                "EnvelopeId": envelope_id,
            }
        )

