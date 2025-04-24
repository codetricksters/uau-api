"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Usuarios:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_usuarios_ativos(
        self,
        login_usuario: Optional[str] = None
    ) -> dict:
        """Retorna a relação de usuários ativos

        Implementation Notes:
        Se não informar o parâmetro “login_usuario”, vai está retornando todos os usuários ativos disponíveis.
Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.       

Parâmetros da request

login_usuario: Nome do login usuario.


        """
        path = "Usuarios/ConsultarUsuariosAtivos"
        return self.api.post(
            path,
            json={
                "login_usuario": login_usuario,
            }
        )

    def consultar_grupos_de_usuario(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Realiza consulta de grupos de usuário.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario


        """
        path = "Usuarios/ConsultarGruposDeUsuario"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

