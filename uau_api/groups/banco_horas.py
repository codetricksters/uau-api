"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class BancoHoras:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def lancar_banco_horas_funcionario(
        self,
        lista_banco_horas: Optional[List[Dict]] = None
    ) -> dict:
        """Gravar lançamentos de banco de horas para o funcionário

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Gravar lançamento de horas no banco de horas para o funcionário.


        """
        path = "BancoHoras/LancarBancoHorasFuncionario"
        return self.api.post(
            path,
            json={
                "ListaBancoHoras": lista_banco_horas,
            }
        )

