"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class CobrancaPix:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def pix_por_parcelas(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """Retorna as informações do PIX com base na chave de uma ou mais parcelas

        Implementation Notes:
        Definição técnica:

O objetivo desta rota de API é permitir a consulta e retorno das informações dos PIX gerados para uma determinada parcela ou lista de parcelas
Serão retornados os dados do PIX, caso tenha sido gerado para a(s) parcela(s) requisitada(s)
Limite máximo de 50 parcelas por requisição


        """
        path = "Pix/PixPorParcelas"
        return self.api.post(
            path,
            json=parameters if parameters is not None else {}
        )

    def reimpressao_pix(
        self,
        tx_id: Optional[str] = None
    ) -> dict:
        """Retorna as informações de impreesão do PIX com o PDF, QRCode e Pix Copia e Cola

        Implementation Notes:
        Definição técnica:

O objetivo desta rota de API é permitir a consulta e retorno das informações do pix de modo que o usuário possa fazer a impressão 
  dos dados de cobrança.
Será retornado o PDF completo e o QRCode em base64.
Será retornado o texto do Pix Copia e Cola.

Instituições bancárias suportadas: 

341 = Banco Itaú

756 = Banco Sicoob

237 = Banco Bradesco

246 = Banco Abc



        """
        path = "Pix/ReimpressaoPix"
        return self.api.post(
            path,
            json={
                "TxId": tx_id,
            }
        )

    def consultar_pix_status(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """Consulta o status do registro PIX junto a instituição bancária

        Implementation Notes:
        Definição técnica:

O objetivo desta rota de API e permitir a consulta do status do PIX 

Instituições bancárias suportadas: 

341 = Banco Itaú
246 = Banco Abc
341 = Banco Itaú
756 = Banco Sicoob
237 = Banco Bradesco

Pré requisito:

Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
URL + /api/v{version}/Pix/GerarCobrancaPIX 
  Anexos:


Exemplo Postman: [ALTERAR EXEMPLO]


        """
        path = "Pix/ConsultarPixStatus"
        return self.api.post(
            path,
            json=parameters if parameters is not None else {}
        )

    def gerar_cobranca_venda(
        self,
        data_de_calculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        usar_padrao_pix_avulso: Optional[bool] = None,
        agrupar_parcelas: Optional[bool] = None,
        padrao_cobranca: Optional[int] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """Solicita o registro de cobrança por PIX de uma ou mais parcelas da venda junto a instituição bancária.

        Implementation Notes:
        Definição Técnica:

O objetivo desta rota de API é permitir o registro de cobrança por PIX junto à instituição financeira.
O BASE64 gerado é somente o QR Code do PIX.
Instituições bancárias suportadas:

341 Banco Itaú
756 Banco Sicoob
237 Banco Bradesco
246 Banco ABC



Pré Requisitos:

Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
URL + /api/v{version}/Venda/GerarCobrancaPIX



        """
        path = "Pix/GerarCobrancaVenda"
        return self.api.post(
            path,
            json={
                "DataDeCalculo": data_de_calculo,
                "Antecipar": antecipar,
                "UsarPadraoPixAvulso": usar_padrao_pix_avulso,
                "AgruparParcelas": agrupar_parcelas,
                "PadraoCobranca": padrao_cobranca,
                "Parcelas": parcelas,
            }
        )

    def gerar_cobranca_proposta(
        self,
        data_de_calculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        usar_padrao_pix_avulso: Optional[bool] = None,
        agrupar_parcelas: Optional[bool] = None,
        padrao_cobranca: Optional[int] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """Solicita o registro de cobrança por PIX de uma ou mais parcelas da venda junto a instituição bancária

        Implementation Notes:
        Definição técnica:

O objetivo desta rota de API é permitir o registro de cobrança por PIX junto a instituição financeira 
O BASE64 gerado é somente o QRCODE do PIX

Instituições bancárias suportadas: 

341 = Banco Itaú
756 = Banco Sicoob
237 = Banco Bradesco
246 = Banco Abc

Pré requisito:

Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
URL + /api/v{version}/Venda/GerarCobrancaPIX




        """
        path = "Pix/GerarCobrancaProposta"
        return self.api.post(
            path,
            json={
                "DataDeCalculo": data_de_calculo,
                "Antecipar": antecipar,
                "UsarPadraoPixAvulso": usar_padrao_pix_avulso,
                "AgruparParcelas": agrupar_parcelas,
                "PadraoCobranca": padrao_cobranca,
                "Parcelas": parcelas,
            }
        )

