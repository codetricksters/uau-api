"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class AcompanharEntrega:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_processos(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """Método com finalidade de consultar processos do acompanhamento de entrega.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras Básicas:

Retorna os processos e itens que estão com o acompanhamento de entrega pendente para uma dada empresa e obra informada.


        """
        path = "AcompanharEntrega/ConsultarProcessos"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
            }
        )

    def acompanhar_pre_entrega(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        chave_nota_fiscal: Optional[str] = None,
        chave_nota_fiscal_frete: Optional[str] = None,
        codigo_do_boleto: Optional[str] = None,
        codigo_do_boleto_frete: Optional[str] = None,
        itens: Optional[List[Dict]] = None
    ) -> dict:
        """Método com finalidade de acompanhar pre entrega

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Regras Básicas:

O usuário deve possuir acesso na empresa e obra informada.
O usuário deve possuir permissão de alteração no programa FIANALISE.
O número do processo deve ser um processo existente.
A NF e NF de frete devem ser númericos e válidos.
O código de barras deve ser númerico e possuir no mínimo 36 caracteres.


        """
        path = "AcompanharEntrega/AcompanharPreEntrega"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Processo": processo,
                "ChaveNotaFiscal": chave_nota_fiscal,
                "ChaveNotaFiscalFrete": chave_nota_fiscal_frete,
                "CodigoDoBoleto": codigo_do_boleto,
                "CodigoDoBoletoFrete": codigo_do_boleto_frete,
                "Itens": itens,
            }
        )

