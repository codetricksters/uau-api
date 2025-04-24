"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Recebiveis:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_meios_preferenciais_recebimento(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta o meio preferencial de recebimento do cliente.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
  Permite consultar os meios preferenciais de recebimento que estão ativos.

        """
        path = "Recebiveis/ConsultarMeiosPreferenciaisRecebimento"
        return self.api.get(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def by_numpadraocobranca(
        self,
        id_empresa: str,
        num_padrao_cobranca: str,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retorna as chaves pix cadastradas ao CPF/CNPJ informado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:

É necessário que exista uma empresa cadastrada.
Numero do padrão de cobrança 0 busca todos os padrões de cobrança.


        """
        path = f"Recebiveis/PadraoDeCobranca/{idempresa}/{numpadraocobranca}"
        return self.api.get(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def parcelas_ecobrancas_do_cliente(
        self,
        cpf: Optional[str] = None,
        valor_reajustado: Optional[bool] = None,
        qtde_parcelas: Optional[int] = None,
        data_inicio_vencimento: Optional[datetime] = None,
        data_fim_vencimento: Optional[datetime] = None,
        pesquisa_por_nao_titulares: Optional[bool] = None
    ) -> dict:
        """Consulta as parcelas e cobranças do cliente.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Definição de Negócio:

Busca parcelas e cobranças em aberto do cliente, informando o CPF.
O parametro PesquisaPorNaoTitulares não é obrigatório, se não informado no request ou informado false, buscará somente dos clientes da venda que possuam o tipo 0 - Titular. Caso informado true buscará de todos os clientes da venda independente do tipo.


        """
        path = "Recebiveis/ParcelasECobrancasDoCliente"
        return self.api.post(
            path,
            json={
                "Cpf": cpf,
                "ValorReajustado": valor_reajustado,
                "QtdeParcelas": qtde_parcelas,
                "DataInicioVencimento": data_inicio_vencimento,
                "DataFimVencimento": data_fim_vencimento,
                "PesquisaPorNaoTitulares": pesquisa_por_nao_titulares,
            }
        )

    def alterar_meio_preferencial_de_recebimento_da_parcela(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        numero_parcela: Optional[int] = None,
        tipo_parcela: Optional[str] = None,
        numero_parcela_geral: Optional[int] = None,
        meio_preferencial_recebimento: Optional[int] = None
    ) -> dict:
        """Altera o meio preferencial de recebimento do cliente.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
  Permite alteração na parcela do meio preferencial de recebimento.
  Permite consultar a alteração realizada na parcela.

        """
        path = "Recebiveis/AlterarMeioPreferencialDeRecebimentoDaParcela"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Venda": venda,
                "NumeroParcela": numero_parcela,
                "TipoParcela": tipo_parcela,
                "NumeroParcelaGeral": numero_parcela_geral,
                "MeioPreferencialRecebimento": meio_preferencial_recebimento,
            }
        )

