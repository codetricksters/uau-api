"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Planejamento:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def atualizar_item_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        descricao_item: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Atualizar item do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/AtualizarItemPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "DescricaoItem": descricao_item,
                "Usuario": usuario,
            }
        )

    def consultar_item_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None
    ) -> dict:
        """Consultar item do planejamento de acordo com a chave do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarItemPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
            }
        )

    def consultar_saldo_siplanejada(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[int] = None,
        contrato: Optional[int] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes_pl: Optional[str] = None,
        insumo: Optional[str] = None
    ) -> dict:
        """Realiza consulta de valores aprovados e saldos das SIs do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Necessário permissão de consulta no programa OBPLNOBR


        """
        path = "Planejamento/ConsultarSaldoSIPlanejada"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "MesPl": mes_pl,
                "Insumo": insumo,
            }
        )

    def inserir_servico_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        tipo_de_custo: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Inserir serviços no planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/InserirServicoPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "TipoDeCusto": tipo_de_custo,
                "Usuario": usuario,
            }
        )

    def exportar_planejamento_produto(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        contrato: Optional[int] = None,
        produto: Optional[int] = None
    ) -> dict:
        """Exportar planejamento de um produto

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ExportarPlanejamentoProduto"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Contrato": contrato,
                "Produto": produto,
            }
        )

    def atualizar_insumos_planejamento(
        self,
        insumos: Optional[List[Dict]] = None,
        justificativa_aprovacao_pl: Optional[str] = None
    ) -> dict:
        """Alterar valores

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Necessário permissão de alteração no programa OBPLNOBR


        """
        path = "Planejamento/AtualizarInsumosPlanejamento"
        return self.api.post(
            path,
            json={
                "Insumos": insumos,
                "justificativaAprovacaoPl": justificativa_aprovacao_pl,
            }
        )

    def atualizar_servico_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        qtde: Optional[int] = None,
        data_inicio: Optional[str] = None,
        data_termino: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Atualizar serviço do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/AtualizarServicoPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "Qtde": qtde,
                "DataInicio": data_inicio,
                "DataTermino": data_termino,
                "Usuario": usuario,
            }
        )

    def consultar_servico_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None
    ) -> dict:
        """Consultar serviços do planejamento de acordo com a chave do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarServicoPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
            }
        )

    def consultar_solicitacao_insumo_pl(
        self,
        num_solicitacao: Optional[int] = None
    ) -> dict:
        """Consultar as solicitações de alteração de insumos do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarSolicitacaoInsumoPL"
        return self.api.post(
            path,
            json={
                "numSolicitacao": num_solicitacao,
            }
        )

    def inserir_estrutura_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        sequencia: Optional[str] = None,
        codigo_item: Optional[str] = None,
        tipo: Optional[int] = None,
        qtde: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Inserir estrutura no planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/InserirEstruturaPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "Sequencia": sequencia,
                "CodigoItem": codigo_item,
                "Tipo": tipo,
                "Qtde": qtde,
                "Usuario": usuario,
            }
        )

    def consultar_solicitacao_servico_pl(
        self,
        num_solicitacao: Optional[int] = None
    ) -> dict:
        """Consultar as solicitações de alteração de serviço do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarSolicitacaoServicoPL"
        return self.api.post(
            path,
            json={
                "numSolicitacao": num_solicitacao,
            }
        )

    def inserir_servico_planejamento_mes(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None,
        qtde: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Inserir serviço do planejamento de acordo com o mês.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/InserirServicoPlanejamentoMes"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "Mes": mes,
                "Qtde": qtde,
                "Usuario": usuario,
            }
        )

    def aprovar_solicitacao_planejamento(
        self,
        num_solicitacao: Optional[int] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """Aprovar a solicitação de aprovação de planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Exemplo do json de request:
 {
 "NumSolicitacao" 622,
   "Usuario": "root",
   "Departamento": "FIN",
   "Cargo": "10"
   }



        """
        path = "Planejamento/AprovarSolicitacaoPlanejamento"
        return self.api.post(
            path,
            json={
                "NumSolicitacao": num_solicitacao,
                "Usuario": usuario,
                "Departamento": departamento,
                "Cargo": cargo,
            }
        )

    def atualizar_estrutura_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        sequencia: Optional[str] = None,
        qtde: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Atualizar estrutura no planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/AtualizarEstruturaPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "Sequencia": sequencia,
                "Qtde": qtde,
                "Usuario": usuario,
            }
        )

    def consultar_estrutura_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        sequencia: Optional[str] = None
    ) -> dict:
        """Consultar estrutura do planejamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarEstruturaPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "Sequencia": sequencia,
            }
        )

    def atualizar_servico_planejamento_mes(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None,
        qtde: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Atualizar serviço do planejamento de acordo com o mês.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/AtualizarServicoPlanejamentoMes"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "Mes": mes,
                "Qtde": qtde,
                "Usuario": usuario,
            }
        )

    def consultar_desembolso_planejamento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        mes_inicial: Optional[str] = None,
        mes_final: Optional[str] = None
    ) -> dict:
        """Consultar desembolso (Projetado, A pagar e Pago) por obra e período.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
O mês inicial e final deverão ser informados no formato MM/YYYY. Exemplo: 01/2019, 12/2019.

Definição de Negócio:
  Status:

Projetado: Considera a data de pagamento (DtaRef) para realizar o cálculo dos valores.
A pagar: Considera a data de prorrogação da parcela (DtaRef) para realizar o cálculo dos valores.
Pago: Considera a data de pagamento da parcela (DtaRef) para realizar o cálculo dos valores.


        """
        path = "Planejamento/ConsultarDesembolsoPlanejamento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "MesInicial": mes_inicial,
                "MesFinal": mes_final,
            }
        )

    def consultar_servico_planejamento_mes(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        mes: Optional[str] = None
    ) -> dict:
        """Consultar serviço do planejamento de acordo com o mês.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarServicoPlanejamentoMes"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "Mes": mes,
            }
        )

    def consultar_servico_planejamento_por_obra(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """Consultar serviço do planejamento por obra.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarServicoPlanejamentoPorObra"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
            }
        )

    def inserir_servico_planejamento_integrado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        produto: Optional[str] = None,
        contrato: Optional[str] = None,
        item: Optional[str] = None,
        servico: Optional[str] = None,
        tipo_de_custo: Optional[str] = None,
        codigo_externo: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Inserir serviços no planejamento integrado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/InserirServicoPlanejamentoIntegrado"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Produto": produto,
                "Contrato": contrato,
                "Item": item,
                "Servico": servico,
                "TipoDeCusto": tipo_de_custo,
                "CodigoExterno": codigo_externo,
                "Usuario": usuario,
            }
        )

    def recusar_solicitacao_planejamento_geral(
        self,
        num_solicitacao: Optional[int] = None,
        num_solicitacoes: Optional[List[Dict]] = None,
        ids_itens_solicitacao: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """Recusar a solicitação de planejamento, como também os itens da solicitação.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/RecusarSolicitacaoPlanejamentoGeral"
        return self.api.post(
            path,
            json={
                "NumSolicitacao": num_solicitacao,
                "NumSolicitacoes": num_solicitacoes,
                "IdsItensSolicitacao": ids_itens_solicitacao,
                "Usuario": usuario,
                "Departamento": departamento,
                "Cargo": cargo,
            }
        )

    def aprovar_solicitacao_planejamento_em_lote(
        self,
        num_solicitacoes: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """Aprovar várias solicitações de aprovação de planejamento em uma única requisição.

        Implementation Notes:
         Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Exemplo do json de request:
 {
 "NumSolicitacoes" [
       625, 626
   ],
   "Usuario": "root",
   "Departamento": "FIN",
   "Cargo": "10"
  }



        """
        path = "Planejamento/AprovarSolicitacaoPlanejamentoEmLote"
        return self.api.post(
            path,
            json={
                "NumSolicitacoes": num_solicitacoes,
                "Usuario": usuario,
                "Departamento": departamento,
                "Cargo": cargo,
            }
        )

    def atualizar_servico_planejamento_integrado(
        self,
        codigo_externo: Optional[str] = None,
        qtde: Optional[int] = None,
        data_inicio: Optional[str] = None,
        data_termino: Optional[str] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Atualizar serviço do planejamento integrado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/AtualizarServicoPlanejamentoIntegrado"
        return self.api.post(
            path,
            json={
                "CodigoExterno": codigo_externo,
                "Qtde": qtde,
                "DataInicio": data_inicio,
                "DataTermino": data_termino,
                "Usuario": usuario,
            }
        )

    def consultar_servico_planejado_desintegrado(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None
    ) -> dict:
        """Consultar serviço planejado desintegrado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarServicoPlanejadoDesintegrado"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
            }
        )

    def consultar_servico_planejamento_integrado(
        self,
        codigo_externo: Optional[str] = None
    ) -> dict:
        """Consultar serviço do planejamento integrado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarServicoPlanejamentoIntegrado"
        return self.api.post(
            path,
            json={
                "CodigoExterno": codigo_externo,
            }
        )

    def consultar_aprovacao_pl_pendente_por_usuario(
        self,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        empresas_obras: Optional[str] = None,
        tipo_consulta_aprovacao: Optional[str] = None,
        numero_dias: Optional[int] = None
    ) -> dict:
        """Realiza consulta das aprovações pendentes para o usuário.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarAprovacaoPlPendentePorUsuario"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "departamento": departamento,
                "cargo": cargo,
                "empresasObras": empresas_obras,
                "tipoConsultaAprovacao": tipo_consulta_aprovacao,
                "numero_dias": numero_dias,
            }
        )

    def recusar_solicitacao_planejamento_geral_em_lote(
        self,
        num_solicitacao: Optional[int] = None,
        num_solicitacoes: Optional[List[Dict]] = None,
        ids_itens_solicitacao: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """Recusar a solicitação de planejamento em lote, como também os itens da solicitação.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/RecusarSolicitacaoPlanejamentoGeralEmLote"
        return self.api.post(
            path,
            json={
                "NumSolicitacao": num_solicitacao,
                "NumSolicitacoes": num_solicitacoes,
                "IdsItensSolicitacao": ids_itens_solicitacao,
                "Usuario": usuario,
                "Departamento": departamento,
                "Cargo": cargo,
            }
        )

    def aprovar_solicitacao_planejamento_insumos_em_lote(
        self,
        ids_itens_solicitacao: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """Aprovar a solicitação de aprovação de planejamento de insumos em lotes de solicitações. Passando como parâmetro o número dos itens das solicitações.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Exemplo do json de request:
{
 "IdsItensSolicitacao" [
       1615, 1616, 1617            
   ],
   "Usuario": "root",
   "Departamento": "FIN",
   "Cargo": "10"
  }



        """
        path = "Planejamento/AprovarSolicitacaoPlanejamentoInsumosEmLote"
        return self.api.post(
            path,
            json={
                "IdsItensSolicitacao": ids_itens_solicitacao,
                "Usuario": usuario,
                "Departamento": departamento,
                "Cargo": cargo,
            }
        )

    def aprovar_solicitacao_planejamento_servicos_em_lote(
        self,
        num_solicitacao: Optional[int] = None,
        chaves_servico: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None
    ) -> dict:
        """Aprovar a solicitação de aprovação de planejamento de serviços em lotes de solicitações.

        Implementation Notes:
         Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Exemplo do json de request:
{
"NumSolicitacao": 630,
  "ChavesServico": [
      {
          "empresa": 1,
          "obra": "00000",
          "produto": 7,
          "contrato": 1,
          "item": "01.01.01.02",
          "servico": "020201P",
          "data": "01/09/2005"
      },
      {
          "empresa": 1,
          "obra": "00000",
          "produto": 7,
          "contrato": 1,
          "item": "01.01.01.03",
          "servico": "030109P",
          "data": "01/09/2005"
      }
  ],
  "Usuario": "root",
  "Departamento": "FIN",
  "Cargo": "10"
  }



        """
        path = "Planejamento/AprovarSolicitacaoPlanejamentoServicosEmLote"
        return self.api.post(
            path,
            json={
                "NumSolicitacao": num_solicitacao,
                "ChavesServico": chaves_servico,
                "Usuario": usuario,
                "Departamento": departamento,
                "Cargo": cargo,
            }
        )

    def consultar_quantidade_aprovacao_pl_pendente_por_usuario(
        self,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        empresas_obras: Optional[str] = None,
        tipo_consulta_aprovacao: Optional[str] = None,
        numero_dias: Optional[int] = None
    ) -> dict:
        """Realiza a busca da quantidade de solicitação pendente para o usuário.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Planejamento/ConsultarQuantidadeAprovacaoPlPendentePorUsuario"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "departamento": departamento,
                "cargo": cargo,
                "empresasObras": empresas_obras,
                "tipoConsultaAprovacao": tipo_consulta_aprovacao,
                "numero_dias": numero_dias,
            }
        )

