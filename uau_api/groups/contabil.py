"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Contabil:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_saldo_de_contas(
        self,
        empresa: Optional[int] = None,
        mes_ano: Optional[datetime] = None,
        tipo: Optional[str] = None
    ) -> dict:
        """Consulta o saldo de contas contábeis do UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os saldo das contas conbaeis com a URI + /api/v{version}/Contabil/SaldoDeContas
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Pode-se consultar o saldo das contas contábeis do UAU, podendo fazer filtros pela empresa, 
  tipo, ano e mês, com isso é possível fazer a integração da parte de saldos contábeis com o UAU

Deve informar obrigatoriamente todos os parâmetros da request.

VirtUau:

http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Contabil/Contabil_ConsultarSaldoDeContas

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/777058/


        """
        path = "Contabil/ConsultarSaldoDeContas"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "MesAno": mes_ano,
                "Tipo": tipo,
            }
        )

    def consultar_contas_contabeis(
        self,
        empresa: Optional[int] = None,
        ano: Optional[int] = None,
        conta: Optional[str] = None,
        descricao_conta: Optional[str] = None,
        limitar_retorno_em: Optional[int] = None
    ) -> dict:
        """Consulta os dados de contas contábeis do UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os dados das contas contábeis com a URI + /api/v{version}/Contabil/ConsultarContasContabeis
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Consulta os dados de contas contábeis do UAU, podendo fazer filtros pela empresa,
  ano, conta ou descrição da conta, com o intuito de buscar informações de uma conta contábil.

Deve informar obrigatoriamente o código da empresa, ano da máscara de plano de contas e o a propriedade limitarRetornoEm.
Pode informar opcionalmente o código da conta ou a descrição da conta.
Os parâmetros (DescricaoConta, Conta) podem conter o sinal de porcentagem (%), 
  caso necessite fazer a consulta a partir de um caractere curinga. Exemplos: %UAU, %UAU%, UAU%.

VirtUau:

http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Contabil/Contabil_ConsultarContasContabeis

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/777058/


        """
        path = "Contabil/ConsultarContasContabeis"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Ano": ano,
                "Conta": conta,
                "DescricaoConta": descricao_conta,
                "LimitarRetornoEm": limitar_retorno_em,
            }
        )

