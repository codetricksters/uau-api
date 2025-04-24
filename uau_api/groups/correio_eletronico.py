"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class CorreioEletronico:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def enviar_mail_interno_uau(
        self,
        mensagem_envio: Optional[str] = None,
        usuariosuau_destino: Optional[str] = None,
        usuariouau_envio: Optional[str] = None,
        assunto: Optional[str] = None
    ) -> dict:
        """Enviar email interno para o usuário root

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint

Definição de Negócio:

Possibilita envio de email interno para o usuário root.
Valida as informaçõe passadas no request.


        """
        path = "CorreioEletronico/EnviarMailInternoUau"
        return self.api.post(
            path,
            json={
                "mensagem_envio": mensagem_envio,
                "usuariosuau_destino": usuariosuau_destino,
                "usuariouau_envio": usuariouau_envio,
                "assunto": assunto,
            }
        )

