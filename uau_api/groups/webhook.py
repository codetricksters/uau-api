"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Webhook:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def by_token(
        self,
        token: str,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Recebe um token da ordem de compra e o decodifica para atualizar o status da ordem de compra automaticamente.

        Implementation Notes:
        Alteração : Alexandre Mendes         Data: 19/09/2022
  Projeto   : 427564 - Sprint 5 - Engenhanria
  Manutenção: Alterado para extrair do token o tipo de resposta, sendo 1 = Aceito ou 3 = Recusado.

        """
        path = f"Webhook/ConfirmarRecebimentoOrdemCompra/{token}"
        return self.api.get(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def atualizar_recebimento_pix(
        self,
        end_to_end_id: Optional[str] = None,
        txid: Optional[str] = None,
        valor: Optional[str] = None,
        horario: Optional[datetime] = None,
        info_pagador: Optional[str] = None,
        devolucoes: Optional[Dict] = None,
        pagador: Optional[Dict] = None
    ) -> dict:
        """Webhook Banco ITAU, para baixa de cobrança PIX

        Implementation Notes:
        Definição Técnica:
  Definição de Negócio:

        """
        path = "Webhook/AtualizarRecebimentoPix"
        return self.api.post(
            path,
            json={
                "endToEndId": end_to_end_id,
                "txid": txid,
                "valor": valor,
                "horario": horario,
                "infoPagador": info_pagador,
                "devolucoes": devolucoes,
                "pagador": pagador,
            }
        )

    def atualizar_pedido_rec(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Atualizar o pedido de recebimento no UAU de acordo com o retorno da venda ou proposta de venda(recebimento) pela maquininha de cartão
        """
        path = "Webhook/AtualizarPedidoRec"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

