"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class ContratoMaterialServico:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def consultar_itens_contrato(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """Consultar itens de contrato

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consultar itens presentes em um contrato.


        """
        path = "ContratoMaterialServico/ConsultarItensContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
            }
        )

    def consultar_contrato_por_chave(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """Consultar contrato

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna os dados do contrato.

Definição de Negócio:

Consulta contrato filtrando pela chave.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

        """
        path = "ContratoMaterialServico/ConsultarContratoPorChave"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato": contrato,
            }
        )

    def consultar_contrato_por_fornecedor(
        self,
        fornecedor: Optional[int] = None
    ) -> dict:
        """Consultar contratos por fornecedor

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta os contratos de um fornecedor.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

        """
        path = "ContratoMaterialServico/ConsultarContratoPorFornecedor"
        return self.api.post(
            path,
            json={
                "fornecedor": fornecedor,
            }
        )

    def consultar_contrato_por_servico_material(
        self,
        empresa: Optional[int] = None,
        servico_material: Optional[str] = None
    ) -> dict:
        """Consultar contrato por serviço/material e empresa

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta contrato filtrando por:
Empresa;
Serviço ou material;



Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

        """
        path = "ContratoMaterialServico/ConsultarContratoPorServicoMaterial"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "servicoMaterial": servico_material,
            }
        )

    def consultar_itens_vinculo_orcamento_servico(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        orcamento: Optional[int] = None,
        somente_contratos_aprovados: Optional[bool] = None
    ) -> dict:
        """Consultar os itens  do vinculo com o orçamento - SERVIÇOS

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna os dados dos itens de contratos vinculados a um determinado orçamento de serviço.

Definição de Negócio:

Consultar os itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço.
Para retornar apenas os itens de contratos que estejam aprovados, o parâmetro "somenteContratosAprovados" deve ser passado como TRUE.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

        """
        path = "ContratoMaterialServico/ConsultarItensVinculoOrcamentoServico"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "item": item,
                "servico": servico,
                "orcamento": orcamento,
                "somenteContratosAprovados": somente_contratos_aprovados,
            }
        )

    def consultar_saldo_reajustado_por_item_contrato(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        contratos: Optional[List[Dict]] = None,
        situacoes: Optional[List[Dict]] = None
    ) -> dict:
        path = "ContratoMaterialServico/ConsultarSaldoReajustadoPorItemContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "contratos": contratos,
                "situacoes": situacoes,
            }
        )

    def consultar_itens_vinculo_planejamento_servico(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None
    ) -> dict:
        """Consultar os itens  do vinculo com o planejamento - SERVIÇOS
        """
        path = "ContratoMaterialServico/ConsultarItensVinculoPlanejamentoServico"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "item": item,
                "servico": servico,
                "produto": produto,
                "contrato": contrato,
            }
        )

    def consultar_contratos_itens_vinculado_orcamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        orcamento: Optional[int] = None,
        somente_contratos_aprovados: Optional[bool] = None
    ) -> dict:
        """Consultar os contratos e itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.
Retorna os dados dos itens de contratos vinculados a um determinado orçamento de serviço.

Definição de Negócio:

Consultar os contratos e itens de contratos de material/serviço que estejam vinculados a um determinado orçamento de serviço.
Para retornar apenas os itens de contratos que estejam aprovados, o parâmetro "somenteContratosAprovados" deve ser passado como TRUE.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/contrato-de-materiais-e-servicos/

        """
        path = "ContratoMaterialServico/ConsultarContratosItensVinculadoOrcamento"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "orcamento": orcamento,
                "somenteContratosAprovados": somente_contratos_aprovados,
            }
        )

