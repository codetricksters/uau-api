"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Folha:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gravar_alocacao_mao_obra(
        self,
        lista_alocacao: Optional[List[Dict]] = None
    ) -> dict:
        """Objetivo: Incluir/Alterar alocação de mão de obra para funcionários do UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método GravarAlocacaoMaoObra.

Definição de Negócio:

Efetua a inclusão ou alteração(caso o registro já exista) na alocação de mão de obra para funcionários do UAU.
Deve informar obrigatoriamente os campos:
Código da empresa de lotação do funcionário
Matrícula do funcionário
Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY
Código da empresa que o funcionário será alocado
Código da obra que o funcionário será alocado
Quantidade de dias que o funcionário está sendo alocado



VirtUau:

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-a-importacao-de-alocação-de-mão-de-obra
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/alocacao-de-mao-de-obra-de-funcionarios/


        """
        path = "Folha/GravarAlocacaoMaoObra"
        return self.api.post(
            path,
            json={
                "ListaAlocacao": lista_alocacao,
            }
        )

    def gravar_movimentacao_mensal_obra(
        self,
        lista_movimentacao_obra: Optional[List[Dict]] = None
    ) -> dict:
        """Objetivo: Incluir/Alterar movimentação mensal por obra dos funcionários do UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método GravarMovimentacaoMensalObra.

Definição de Negócio:

Efetua a inclusão ou alteração(caso o registro já exista) na movimentação mensal por obra dos funcionários do UAU.
Deve informar obrigatoriamente os campos:
Código da empresa de lotação do funcionário
Matrícula do funcionário
Código da rubrica a ser rateada na empresa/obra
Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY
Código da empresa de rateio dos cálculos do funcionário
Código da obra de rateio dos cálculos do funcionário
Quantidade ou valor da proporção definida para a empresa/obra de rateio



VirtUau:

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-a-importacao-de-movimentacao-mensal-e-movimentacao-por-obra/
Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-calculo-da-folha-de-pagamento-com-rateio


        """
        path = "Folha/GravarMovimentacaoMensalObra"
        return self.api.post(
            path,
            json={
                "ListaMovimentacaoObra": lista_movimentacao_obra,
            }
        )

