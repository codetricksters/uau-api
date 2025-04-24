"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Cotacao:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def atualizar_item_cotacao(
        self,
        lista_itens_cotacao: Optional[List[Dict]] = None
    ) -> dict:
        """Atualizar os dados dos itens de cotação de material, cotação de serviço e adiantamento de contrato.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AtualizarItemCotacao
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Permite atualizar os dados dos itens de cotação, seja ela de material ou de serviço.
Para cotações específicas que forem pertencentes à cotação geral, serão alteradas somente a quantidade e a marca (no caso de cotação de material). 
  Os demais valores só serão alterados se a cotação geral for informada na requisição.
Para cotações que forem pertencentes à cotação geral, durante a execução se não existir insumo para um dos itens da cotação informada a execução irá finalizar, efetivando somente a atualização dos itens de cotação anteriores.
Informações de IPI, ICMS e Marca só estão relacionadas às cotações de material, portanto podem ser omitidas na requisição.


        """
        path = "Cotacao/AtualizarItemCotacao"
        return self.api.post(
            path,
            json={
                "listaItensCotacao": lista_itens_cotacao,
            }
        )

    def conta_cotacoes_aprov_mob(
        self,
        usuario: Optional[str] = None
    ) -> dict:
        """Conto as cotações que possuem simulações que o usuário pode aprovar.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/ContaCotacoesMob
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consultar a quantidade de cotações de material e serviço que possuem simulações que o usuário pode aprovar.


        """
        path = "Cotacao/ContaCotacoesAprovMob"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
            }
        )

    def aprovar_simulacoes_compra(
        self,
        simulacoes: Optional[List[Dict]] = None
    ) -> dict:
        """Aprovar simulações de compra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

É necessário permissão de aprovação para o programa ALSIMULCOT


        """
        path = "Cotacao/AprovarSimulacoesCompra"
        return self.api.post(
            path,
            json={
                "Simulacoes": simulacoes,
            }
        )

    def adicionar_fornecedor_cotacao(
        self,
        cod_fornecedor: Optional[int] = None,
        cnpj_fornecedor: Optional[str] = None,
        numero_cotacao: Optional[int] = None,
        numero_cotacao_geral: Optional[int] = None,
        empresa: Optional[int] = None
    ) -> dict:
        """Adicionar fornecedor a uma cotação aberta.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AdicionarFornecedorCotacao
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Permite vincular um fornecedor a uma cotação em aberto de material ou serviço.
Para identificação do fornecedor, são aceitos o código ou CPF/CNPJ deste no sistema.
Para vínculo do fornecedor a uma cotação específica, o código dessa cotação, empresa e, o CPF/CNPJ ou código do fornecedor devem ser informados.
Para vínculo do fornecedor a uma cotação geral, somente o código da cotação geral e, o CPF/CNPJ ou código do fornecedor devem ser informados.


        """
        path = "Cotacao/AdicionarFornecedorCotacao"
        return self.api.post(
            path,
            json={
                "codFornecedor": cod_fornecedor,
                "CNPJFornecedor": cnpj_fornecedor,
                "numeroCotacao": numero_cotacao,
                "numeroCotacaoGeral": numero_cotacao_geral,
                "empresa": empresa,
            }
        )

    def buscar_itens_cotacao_fornecedor(
        self,
        empresa: Optional[int] = None,
        cotacao: Optional[int] = None,
        fornecedor: Optional[int] = None,
        origem: Optional[int] = None
    ) -> dict:
        """Consultar itens de cotação por código do fornecedor.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Cotacao/BuscarItensCotacaoFornecedor
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Permite consultar os dados de itens de cotação de material ou serviço por código do fornecedor.
Somente cotações com status "0 - Criada" são retornadas.


        """
        path = "Cotacao/BuscarItensCotacaoFornecedor"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "cotacao": cotacao,
                "fornecedor": fornecedor,
                "origem": origem,
            }
        )

    def consultar_itens_cotacao_por_obra(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        cotacao: Optional[int] = None
    ) -> dict:
        """Consultar itens cotação por obra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Permite consultar itens da cotação de material ou serviço que esteja aguardando confirmação por obra, filtrando por empresa, obra e número da cotação.


        """
        path = "Cotacao/ConsultarItensCotacaoPorObra"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "cotacao": cotacao,
            }
        )

    def buscar_cotacao_aberta_fornecedor(
        self,
        cnpj: Optional[str] = None
    ) -> dict:
        """Consultar as cotações abertas para o fornecedor, por CNPJ do fornecedor.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio: 

Permite consultar os dados de cotações de material ou serviço que estão disponíveis para o fornecedor. Os tipos de cotações retornadas são:
0 - Cot. material regular
1 - Cot. material adiant. contrato
2 - Cot. serviço regular
3 - Cot. patrimônio
4 - Cot. material contrato
5 - Cot. material emergencial
6 - Cot. manutenção de patrimônio
7 - Cot. material regularização
8 - Cot. material complemento
9 - Cot. serviço emergencial
10 - Cot. serviço regularização
11 - Cot. serviço complemento
12 - Cot. serviço adiant. contrato
13 - Cot. serviço contrato


É obrigatório informar o CNPJ do fornecedor para realizar a consulta.


        """
        path = "Cotacao/BuscarCotacaoAbertaFornecedor"
        return self.api.post(
            path,
            json={
                "cnpj": cnpj,
            }
        )

    def aprovar_confirmacao_cotacao_por_obra(
        self,
        lista_confirmar_aprovacao_cotacao: Optional[List[Dict]] = None
    ) -> dict:
        """Aprovar confirmação de cotação por obra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Possibilita aprovar a confirmação da cotação de material ou serviço por obra.


        """
        path = "Cotacao/AprovarConfirmacaoCotacaoPorObra"
        return self.api.post(
            path,
            json={
                "listaConfirmarAprovacaoCotacao": lista_confirmar_aprovacao_cotacao,
            }
        )

    def remover_aprovacao_simulacoes_compra(
        self,
        simulacoes: Optional[List[Dict]] = None
    ) -> dict:
        """Remover aprovações das simulações de compra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

É necessário permissão de exclusão para o programa ALCONFCOT caso a cotação esteja no fechamento de compra
  e permissão exclusão para o programa ALANALISE caso a cotação esteja na confirmação de cotação por obra.


        """
        path = "Cotacao/RemoverAprovacaoSimulacoesCompra"
        return self.api.post(
            path,
            json={
                "Simulacoes": simulacoes,
            }
        )

    def atualizar_condicao_pagamento_entrega(
        self,
        empresa: Optional[int] = None,
        cotacao: Optional[int] = None,
        numero_cotacao_geral: Optional[int] = None,
        fornecedor: Optional[int] = None,
        dias_entrega: Optional[int] = None,
        quantidade_entrega: Optional[int] = None,
        intervalo_entrega: Optional[int] = None,
        dias_pagamento: Optional[int] = None,
        quantidade_parcela: Optional[int] = None,
        intervalo_parcela: Optional[int] = None,
        tipo_frete: Optional[int] = None,
        tipo_pagamento: Optional[int] = None,
        condicao_pagamento: Optional[str] = None
    ) -> dict:
        """Atualizar as condições de entrega relacionado a cotação.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AtualizarCondicaoPagamentoEntrega
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Permite atualizar os dados de condição de entrega da cotação, bem como dias para entrega, quantidade de parcela, intervalo das parcelas, entre outros.
A condição de pagamento utilizada será sempre SOBRE A ENTREGA.
Para atualizar as condições de pagamento de uma cotação específica, o código dessa cotação e empresa devem ser informados.
Para atualizar as condições de pagamento de uma cotação geral, somente o código da cotação geral deve ser informado.


        """
        path = "Cotacao/AtualizarCondicaoPagamentoEntrega"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "cotacao": cotacao,
                "numeroCotacaoGeral": numero_cotacao_geral,
                "fornecedor": fornecedor,
                "diasEntrega": dias_entrega,
                "quantidadeEntrega": quantidade_entrega,
                "intervaloEntrega": intervalo_entrega,
                "diasPagamento": dias_pagamento,
                "quantidadeParcela": quantidade_parcela,
                "intervaloParcela": intervalo_parcela,
                "tipoFrete": tipo_frete,
                "tipoPagamento": tipo_pagamento,
                "CondicaoPagamento": condicao_pagamento,
            }
        )

    def consultar_aprovacao_da_cotacao_por_obra(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_simulacao: Optional[int] = None,
        numero_cotacao: Optional[int] = None
    ) -> dict:
        """Consultar as aprovações da cotação por obra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

São consultadas as aprovações já realizadas para uma determinada cotação de material ou serviço.


        """
        path = "Cotacao/ConsultarAprovacaoDaCotacaoPorObra"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "numeroSimulacao": numero_simulacao,
                "numeroCotacao": numero_cotacao,
            }
        )

    def reprovar_confirmacoes_cotacao_por_obra(
        self,
        confirmacoes_cotacao: Optional[List[Dict]] = None,
        justificativa_reprovacao: Optional[str] = None
    ) -> dict:
        """Reprovar as confirmações de cotação por obra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

É necessário permissão de exclusão para o programa ALCONFCOT caso a cotação esteja no fechamento de compra
  e permissão exclusão para o programa ALANALISE caso a cotação esteja na confirmação de cotação por obra.


        """
        path = "Cotacao/ReprovarConfirmacoesCotacaoPorObra"
        return self.api.post(
            path,
            json={
                "ConfirmacoesCotacao": confirmacoes_cotacao,
                "justificativaReprovacao": justificativa_reprovacao,
            }
        )

    def consultar_cotacoes_confirmacao_pendente(
        self,
        usuario: Optional[str] = None,
        departamento: Optional[str] = None,
        cargo: Optional[str] = None,
        lista_emp_obras: Optional[List[Dict]] = None,
        cotacao: Optional[int] = None
    ) -> dict:
        """Consultar as cotações com confirmações pendentes

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consulta cotações de material e serviço que estão com as confirmações pendentes.


        """
        path = "Cotacao/ConsultarCotacoesConfirmacaoPendente"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "departamento": departamento,
                "cargo": cargo,
                "listaEmpObras": lista_emp_obras,
                "cotacao": cotacao,
            }
        )

    def consultar_quantidade_cotacao_pendente_por_obra(
        self,
        login_usuario: Optional[str] = None,
        codigo_departamento: Optional[str] = None,
        codigo_cargo: Optional[str] = None,
        lista_emp_obras: Optional[List[Dict]] = None
    ) -> dict:
        """Consultar a quantidade de cotações pendentes de aprovação por obra

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Verifica a quantidade de cotações de material e serviço com pendência na aprovação filtrando por obra.


        """
        path = "Cotacao/ConsultarQuantidadeCotacaoPendentePorObra"
        return self.api.post(
            path,
            json={
                "loginUsuario": login_usuario,
                "codigoDepartamento": codigo_departamento,
                "codigoCargo": codigo_cargo,
                "listaEmpObras": lista_emp_obras,
            }
        )

    def consultar_quantidade_cotacao_pendente_por_obra_mob(
        self,
        login_usuario: Optional[str] = None,
        codigo_departamento: Optional[str] = None,
        codigo_cargo: Optional[str] = None,
        lista_emp_obras: Optional[List[Dict]] = None
    ) -> dict:
        """Consultar a quantidade de cotações pendentes de aprovação para a obra selecionada

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consultar a quantidade de cotações de material e serviço com pendência na aprovação filtrando por obra.


        """
        path = "Cotacao/ConsultarQuantidadeCotacaoPendentePorObraMob"
        return self.api.post(
            path,
            json={
                "loginUsuario": login_usuario,
                "codigoDepartamento": codigo_departamento,
                "codigoCargo": codigo_cargo,
                "listaEmpObras": lista_emp_obras,
            }
        )

    def consultar_justificativas_aprovacao_fora_sequencia(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consultar as justificativas para aprovações de cotação fora da sequência do usuário.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Consultar as justificativas que podem ser utilizadas em aprovações de confirmação de cotação de material ou serviço que esteja fora da sequência do usuário (Controle de aprovações).


        """
        path = "Cotacao/ConsultarJustificativasAprovacaoForaSequencia"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def inserir_altera_coment_forn_frete(
        self,
        empresa: Optional[int] = None,
        codigo_fornecedor: Optional[int] = None,
        cotacao: Optional[int] = None,
        cond_pagto: Optional[int] = None,
        tipo_coment: Optional[int] = None,
        efet_pgto_parc: Optional[int] = None,
        dtvenc_ini: Optional[str] = None,
        qtde_parc: Optional[int] = None,
        intev_parc: Optional[int] = None,
        obs_pgto: Optional[str] = None,
        obs_entrega: Optional[str] = None,
        tipo_pgto: Optional[int] = None,
        tem_frete: Optional[int] = None,
        diaini_venc: Optional[int] = None,
        freteqtde_ent: Optional[int] = None,
        interv_ent: Optional[int] = None,
        dias_entrega: Optional[int] = None
    ) -> dict:
        """Esta rotina inseri um comentario ou atualizar um ja existente."), SoapHeader("TicketAuth

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/InserirAlteraComentFornFrete
Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:

Inserir um comentário ou atualizar um já existente.


        """
        path = "Cotacao/InserirAlteraComentFornFrete"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "codigo_fornecedor": codigo_fornecedor,
                "cotacao": cotacao,
                "cond_pagto": cond_pagto,
                "tipo_coment": tipo_coment,
                "efet_pgto_parc": efet_pgto_parc,
                "dtvenc_ini": dtvenc_ini,
                "qtde_parc": qtde_parc,
                "intev_parc": intev_parc,
                "obs_pgto": obs_pgto,
                "obs_entrega": obs_entrega,
                "tipo_pgto": tipo_pgto,
                "tem_frete": tem_frete,
                "diaini_venc": diaini_venc,
                "freteqtde_ent": freteqtde_ent,
                "interv_ent": interv_ent,
                "diasEntrega": dias_entrega,
            }
        )

