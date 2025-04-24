"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Shopping:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def grava_rendimentos(
        self,
        dia: Optional[datetime] = None,
        lojista: Optional[bool] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        valor_lancamento: Optional[int] = None,
        usuario: Optional[str] = None,
        tipo_usuario: Optional[int] = None
    ) -> dict:
        """Consulta a situação das vendas dos lojistas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Shopping/GravaRendimentos"
        return self.api.post(
            path,
            json={
                "dia": dia,
                "lojista": lojista,
                "empresa": empresa,
                "obra": obra,
                "venda": venda,
                "valor_lancamento": valor_lancamento,
                "usuario": usuario,
                "tipo_usuario": tipo_usuario,
            }
        )

    def importacao_de_parcelas(
        self,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """Importar parcelas de venda tipo Aluguel Shopping.

        Implementation Notes:
        Definição Técnica:

Importação de parcelas a receber/recebida para vendas do tipo Aluguel Shopping:
URI + /api/v{version}/Shopping/ImportacaoDeParcelas



Definição de Negócio:

Permite importar parcelas a receber/recebida para vendas do tipo Aluguel Shopping com as seguintes regras:

Para importação de parcelas A RECEBER, os seguintes campos devem ser desconsiderados ou não preenchidos:
  ValorJurosContrato,ValorCorrecao,ValorMulta,ValorCorrecaoAtraso,ValorJurosAtraso,ValorDesconto,ValorAcrescimo,DataRecebimento,
  DataCalculoReajuste,ValorRecebimento,BancoDeposito,ContaDeposito,Depositado,DataDeposito,Conciliado,DataConciliacao,ValorDescontoCondicional
O campo ParcelaRecebida deve estar com o valor '0', indicando que a parcela não foi recebida.


Para importação de parcelas RECEBIDAS, a maioria dos campos devem estar preenchidos, exceto nos casos de Parcela tipo Custa, Parcela Depositada ou Conciliada.

O campo ParcelaRecebida deve estar com o valor '1', indicando que a parcela foi recebida.
Caso a parcela seja do tipo Custa, os campos TipoDaCusta, ObservacaoCusta, OrigemCusta devem estar preenchidos.
Caso o campo Depositado seja '1', os campos ValorRecebimento,BancoDeposito,ContaDeposito e DataDeposito devem estar preenchidos.
Caso o campo Conciliado seja '1', os campos ValorRecebimento,BancoDeposito,ContaDeposito,DataDeposito e DataConciliacao devem estar preenchidos.



Anexos:

Link para download de exemplos para Postman:
Exemplo de parcela a receber: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcela-a-Receber.postman_collection.zip
Exemplo de parcela recebida: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcela-Recebida.postman_collection.zip


        """
        path = "Shopping/ImportacaoDeParcelas"
        return self.api.post(
            path,
            json={
                "Parcelas": parcelas,
            }
        )

    def consultar_rendimento_lojista(
        self,
        cod_empresa: Optional[int] = None,
        cod_obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        ini_lancamento: Optional[datetime] = None,
        fim_lancamento: Optional[datetime] = None
    ) -> dict:
        """Método que consulta para lançamentos de rendimento de lojista e auditor.
        """
        path = "Shopping/ConsultarRendimentoLojista"
        return self.api.post(
            path,
            json={
                "cod_empresa": cod_empresa,
                "cod_obra": cod_obra,
                "num_venda": num_venda,
                "ini_lancamento": ini_lancamento,
                "fim_lancamento": fim_lancamento,
            }
        )

