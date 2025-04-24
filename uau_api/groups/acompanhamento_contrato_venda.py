"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class AcompanhamentoContratoVenda:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gravar_acompanhamento(
        self,
        num_acompanhamento: Optional[int] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_contrato: Optional[str] = None,
        periodo_inicio: Optional[datetime] = None,
        periodo_fim: Optional[datetime] = None,
        lista_de_produtos: Optional[List[Dict]] = None,
        responsavel: Optional[int] = None,
        status: Optional[int] = None,
        observacao_para_entrega: Optional[str] = None,
        motorista: Optional[int] = None,
        caminhao_placa: Optional[str] = None,
        uf_placa: Optional[str] = None
    ) -> dict:
        """Método responsável por gravar o acompanhamento de contrato de vendas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Retorna json com as informações de empresa, obra, número do contrato e número do acompanhamento.

Definição de Negócio:

Permite inserir ou alterar um acompanhamento de contrato de venda. 
O usuário autenticado deve ter permissão de inclusão ou alteração em OBACOMPVENDA, a depender do objetivo (inserir ou editar acompanhamento).
O sistema identifica que é uma edição no acompanhamento quando a propriedade [NumAcompanhamento] está preenchida. Em caso de não informação deste campo, será gravado um novo acompanhamento.
O usuário autenticado deve ter permissão de inclusão em OBMEDICAOVENDA.
Em caso de manutenção de um acompanhamento, as informações serão sobrescritas e as quantidades "Qtde medida" e "Qtde falta medir" calculadas a partir da propriedade [QtdeAMedir] informada.


        """
        path = "AcompanhamentoContratoVenda/GravarAcompanhamento"
        return self.api.post(
            path,
            json={
                "NumAcompanhamento": num_acompanhamento,
                "Empresa": empresa,
                "Obra": obra,
                "NumContrato": num_contrato,
                "PeriodoInicio": periodo_inicio,
                "PeriodoFim": periodo_fim,
                "ListaDeProdutos": lista_de_produtos,
                "Responsavel": responsavel,
                "Status": status,
                "ObservacaoParaEntrega": observacao_para_entrega,
                "Motorista": motorista,
                "CaminhaoPlaca": caminhao_placa,
                "UFPlaca": uf_placa,
            }
        )

