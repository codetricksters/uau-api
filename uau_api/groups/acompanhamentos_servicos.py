"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class AcompanhamentosServicos:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def acompanhar_contrato(
        self,
        empresa: Optional[str] = None,
        obra: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        descricao_servico: Optional[str] = None,
        mes: Optional[datetime] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        usuario: Optional[str] = None,
        qtde: Optional[int] = None,
        sequencia: Optional[str] = None,
        codigo_estrutura: Optional[str] = None,
        orcamento: Optional[int] = None,
        contrato_vinculado: Optional[int] = None,
        ordem: Optional[int] = None,
        etapa: Optional[str] = None,
        observacao: Optional[str] = None,
        aplicacao_material: Optional[List[Dict]] = None
    ) -> dict:
        """Grava o acompanhamento de contrato vinculado a um planejamento ou orçamento

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Grava o acompanhamento de contrato vinculado a um planejamento ou orçamento

Informar os parâmetros dependendo do vinculo com orçamento ou planejamento


        """
        path = "AcompanhamentosServicos/AcompanharContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "produto": produto,
                "contrato": contrato,
                "item": item,
                "servico": servico,
                "descricaoServico": descricao_servico,
                "mes": mes,
                "dataInicio": data_inicio,
                "dataFim": data_fim,
                "usuario": usuario,
                "qtde": qtde,
                "sequencia": sequencia,
                "codigoEstrutura": codigo_estrutura,
                "orcamento": orcamento,
                "contratoVinculado": contrato_vinculado,
                "ordem": ordem,
                "etapa": etapa,
                "observacao": observacao,
                "aplicacaoMaterial": aplicacao_material,
            }
        )

    def acompanhar_servico_pl(
        self,
        empresa: Optional[str] = None,
        obra: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None,
        usuario: Optional[str] = None,
        qtde: Optional[int] = None,
        sequencia: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None,
        aprova_contrato: Optional[bool] = None,
        contrato_vinculado: Optional[int] = None,
        descricao_servico: Optional[str] = None,
        ordem: Optional[int] = None,
        etapa: Optional[str] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """Acompanhamento de Serviços do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio: 
  Acompanhar serviço do planejamento solicitado.

Valida se o usuário está cadastrado no sistema e ativo.
Valida se já existe acompanhamento para o código externo de integração solicitado.
Verifica se o fechamento do acompanhamento não foi realizado.


        """
        path = "AcompanhamentosServicos/AcompanharServicoPL"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "produto": produto,
                "contrato": contrato,
                "item": item,
                "servico": servico,
                "mes": mes,
                "usuario": usuario,
                "qtde": qtde,
                "sequencia": sequencia,
                "codExternoIntegracao": cod_externo_integracao,
                "aprovaContrato": aprova_contrato,
                "contratoVinculado": contrato_vinculado,
                "descricaoServico": descricao_servico,
                "ordem": ordem,
                "etapa": etapa,
                "observacao": observacao,
            }
        )

    def acompanhar_servico_orcado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        servico: Optional[str] = None,
        item: Optional[str] = None,
        orcamento: Optional[int] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None,
        usuario_logado: Optional[str] = None,
        sequencia: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None,
        aprova_contrato: Optional[bool] = None,
        contrato_vinculado: Optional[int] = None,
        descricao_servico: Optional[str] = None,
        ordem: Optional[int] = None,
        etapa: Optional[str] = None,
        mes: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """Acompanhar serviços de orçamento.

        Implementation Notes:
        Definição técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Permite consultar e portanto acompanhar os serviços que foram orçados de acordo com os parâmentros passados na requisição.

Deve montar uma estrutura seguindo o modelo.
Valida se o usuário está cadastrado.
Valida se o serviço não possui estruturas.
Valida se possui distribuição no periodo acompanhado.
Valida o saldo do orçamento que será acompanhado.


        """
        path = "AcompanhamentosServicos/AcompanharServicoOrcado"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "servico": servico,
                "item": item,
                "orcamento": orcamento,
                "periodo": periodo,
                "quantidade": quantidade,
                "usuario_logado": usuario_logado,
                "sequencia": sequencia,
                "codExternoIntegracao": cod_externo_integracao,
                "aprovaContrato": aprova_contrato,
                "contratoVinculado": contrato_vinculado,
                "descricaoServico": descricao_servico,
                "ordem": ordem,
                "etapa": etapa,
                "mes": mes,
                "produto": produto,
                "contrato": contrato,
                "observacao": observacao,
            }
        )

    def acompanhar_servico_contrato(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        contrato_servico: Optional[int] = None,
        item_contrato: Optional[int] = None,
        servico: Optional[str] = None,
        data_inicio: Optional[str] = None,
        data_fim: Optional[str] = None,
        mes_pl: Optional[str] = None,
        quantidade: Optional[int] = None,
        porcentagem_acomp: Optional[int] = None,
        observacoes: Optional[str] = None,
        etapa: Optional[str] = None,
        cod_estrutura: Optional[str] = None,
        sequencia: Optional[str] = None,
        usuario_logado: Optional[str] = None,
        cod_acomp: Optional[int] = None,
        orcamento: Optional[int] = None,
        item_orcamento: Optional[str] = None,
        aplicacao_material: Optional[List[Dict]] = None
    ) -> dict:
        """Acompanhar serviços de contrato.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método do acordo com o modelo.

Definição de Negócio:
  Permite consultar e portanto acompanhar serviços referentes aos contratos.

Valida usuário.
Valida prazo de validade do contrato.


        """
        path = "AcompanhamentosServicos/AcompanharServicoContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "contrato_servico": contrato_servico,
                "item_contrato": item_contrato,
                "servico": servico,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
                "mes_pl": mes_pl,
                "quantidade": quantidade,
                "porcentagem_acomp": porcentagem_acomp,
                "observacoes": observacoes,
                "etapa": etapa,
                "cod_estrutura": cod_estrutura,
                "sequencia": sequencia,
                "usuario_logado": usuario_logado,
                "cod_acomp": cod_acomp,
                "orcamento": orcamento,
                "itemOrcamento": item_orcamento,
                "aplicacaoMaterial": aplicacao_material,
            }
        )

    def excluir_acompanhamento_servico_pl(
        self,
        empresa: Optional[str] = None,
        obra: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None,
        usuario: Optional[str] = None,
        qtde: Optional[int] = None,
        sequencia: Optional[str] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """Excluir acompanhamento de Serviços do planejamento.

        Implementation Notes:
        Definição Técnica:
  Permite excluir acompanhamento de Serviços do planejamento.

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio: 
  Acompanhar serviço do planejamento solicitado.

Valida se existe acompanhamento para o código informado.
Valida se existe acompanhamento para o registro informado.
Valida se o acompanhamento se encontra aberto.
Valida a quantidade informada para exclusão.


        """
        path = "AcompanhamentosServicos/ExcluirAcompanhamentoServicoPL"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "produto": produto,
                "contrato": contrato,
                "item": item,
                "servico": servico,
                "mes": mes,
                "usuario": usuario,
                "qtde": qtde,
                "sequencia": sequencia,
                "codExternoIntegracao": cod_externo_integracao,
            }
        )

    def excluir_acompanhamento_servico_orcado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        servico: Optional[str] = None,
        item: Optional[str] = None,
        orcamento: Optional[int] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None,
        sequencia: Optional[str] = None,
        num_acomp: Optional[int] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """Excluir acompanhamento de serviço orçado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite excluir acompanhamento de serviço orçado.

Valida se a exclusão pode ser realizada.


        """
        path = "AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcado"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "servico": servico,
                "item": item,
                "orcamento": orcamento,
                "periodo": periodo,
                "quantidade": quantidade,
                "sequencia": sequencia,
                "numAcomp": num_acomp,
                "codExternoIntegracao": cod_externo_integracao,
            }
        )

    def alterar_acompanhamento_servico_contrato(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        contrato_servico: Optional[int] = None,
        item_contrato: Optional[int] = None,
        servico: Optional[str] = None,
        data_inicio: Optional[str] = None,
        data_fim: Optional[str] = None,
        mes_pl: Optional[str] = None,
        quantidade: Optional[int] = None,
        porcentagem_acomp: Optional[int] = None,
        observacoes: Optional[str] = None,
        etapa: Optional[str] = None,
        cod_estrutura: Optional[str] = None,
        sequencia: Optional[str] = None,
        usuario_logado: Optional[str] = None,
        cod_acomp: Optional[int] = None,
        orcamento: Optional[int] = None,
        item_orcamento: Optional[str] = None,
        aplicacao_material: Optional[List[Dict]] = None
    ) -> dict:
        """Alterar acompanhamento de serviços de contrato.

        Implementation Notes:
        Definição técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Permite consultar e portanto acompanhar os serviços que foram orçados de acordo com os parâmentros passados na requisição.

Deve montar uma estrutura seguindo o modelo.
Valida se o usuário é cadastrado e se tem permissão para realizar a alteração.
Valida se o serviço é controlado por tipologia de produção.
Valida se a quantidade a acompanhar excede o saldo a acompanhar.
Valida se o contrato é valido para aletrações.
Valida o prazo de validade do contrato.


        """
        path = "AcompanhamentosServicos/AlterarAcompanhamentoServicoContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "contrato_servico": contrato_servico,
                "item_contrato": item_contrato,
                "servico": servico,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
                "mes_pl": mes_pl,
                "quantidade": quantidade,
                "porcentagem_acomp": porcentagem_acomp,
                "observacoes": observacoes,
                "etapa": etapa,
                "cod_estrutura": cod_estrutura,
                "sequencia": sequencia,
                "usuario_logado": usuario_logado,
                "cod_acomp": cod_acomp,
                "orcamento": orcamento,
                "itemOrcamento": item_orcamento,
                "aplicacaoMaterial": aplicacao_material,
            }
        )

    def excluir_acompanhamento_servico_de_contrato(
        self,
        empresa: Optional[int] = None,
        contrato_servico: Optional[int] = None,
        item_contrato: Optional[int] = None,
        servico: Optional[str] = None,
        quantidade: Optional[int] = None,
        sequencia: Optional[str] = None,
        codigo_estrutura: Optional[str] = None,
        usuario_logado: Optional[str] = None,
        cod_aec: Optional[int] = None
    ) -> dict:
        """Excluir acompanhamento de serviço de contrato.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Exclui o acompanhamento de serviço no contrato.

Valida se o usuário tem permissão para excluir um acompanhamento.
Valida se possui estrutura e se o status do acompanhamento está como "aberto". Neste caso não será excluido.


        """
        path = "AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContrato"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "contrato_servico": contrato_servico,
                "item_contrato": item_contrato,
                "servico": servico,
                "quantidade": quantidade,
                "sequencia": sequencia,
                "codigo_estrutura": codigo_estrutura,
                "usuario_logado": usuario_logado,
                "codAec": cod_aec,
            }
        )

    def excluir_acompanhamento_servico_orcado_por_chave(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        servico: Optional[str] = None,
        item: Optional[str] = None,
        orcamento: Optional[int] = None,
        periodo: Optional[str] = None,
        quantidade: Optional[int] = None,
        sequencia: Optional[str] = None,
        num_acomp: Optional[int] = None,
        cod_externo_integracao: Optional[str] = None
    ) -> dict:
        """Excluir acompanhamento de serviço orçado por chave.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Exclui o acompanhamento de serviço oraçado de acordo com a chave informada.

Valida se o acompanhamento informado existe.
Valida se a exclusão pode ser realizada.


        """
        path = "AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoPorChave"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "servico": servico,
                "item": item,
                "orcamento": orcamento,
                "periodo": periodo,
                "quantidade": quantidade,
                "sequencia": sequencia,
                "numAcomp": num_acomp,
                "codExternoIntegracao": cod_externo_integracao,
            }
        )

    def consultar_acompanhamento_contrato_servico_por_servico(
        self,
        empresa: Optional[int] = None,
        servico: Optional[str] = None
    ) -> dict:
        """Acompanhar contrato de serviço por empresa e serviço.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Consulta acompanhamento de contrato de serviço filtrando por serviço.

        """
        path = "AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorServico"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Servico": servico,
            }
        )

    def consultar_acompanhamento_contrato_servico_por_contrato_eservico(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        servico: Optional[str] = None
    ) -> dict:
        """Acompanhar contrato de serviço por empresa, contrato e serviço.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
  Definição de Negócio:
  Permite acompanhar contratos filtrando por:
Empresa
Contrato
Serviço




        """
        path = "AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorContratoEServico"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Contrato": contrato,
                "Servico": servico,
            }
        )

