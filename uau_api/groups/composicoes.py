"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Composicoes:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def inserir_composicoes(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        prod_equipe: Optional[int] = None,
        tipo_custo: Optional[str] = None,
        civil_pes: Optional[int] = None,
        status: Optional[int] = None,
        categoria: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        codigo_servico_fiscal: Optional[str] = None,
        controlafvs: Optional[bool] = None,
        confirmado: Optional[int] = None,
        porc_qtde_excedida_entrega: Optional[str] = None,
        porc_preco_excedido_entrega: Optional[str] = None,
        porc_preco_reduzido_entrega: Optional[str] = None
    ) -> dict:
        path = "Composicoes/InserirComposicoes"
        return self.api.post(
            path,
            json={
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade,
                "prodEquipe": prod_equipe,
                "tipoCusto": tipo_custo,
                "civilPes": civil_pes,
                "status": status,
                "categoria": categoria,
                "categoriaMovFin": categoria_mov_fin,
                "CAP": cap,
                "CAPEstorno": cap_estorno,
                "CAPTransacaoFinanceira": cap_transacao_financeira,
                "NCM": ncm,
                "CEST": cest,
                "aplicacao": aplicacao,
                "codigoServicoFiscal": codigo_servico_fiscal,
                "controlaFVS": controlafvs,
                "confirmado": confirmado,
                "porcQtdeExcedidaEntrega": porc_qtde_excedida_entrega,
                "porcPrecoExcedidoEntrega": porc_preco_excedido_entrega,
                "porcPrecoReduzidoEntrega": porc_preco_reduzido_entrega,
            }
        )

    def atualizar_composicoes(
        self,
        lista_composicoes_atualizar: Optional[List[Dict]] = None
    ) -> dict:
        path = "Composicoes/AtualizarComposicoes"
        return self.api.post(
            path,
            json={
                "listaComposicoesAtualizar": lista_composicoes_atualizar,
            }
        )

    def consultar_todas_composicoes(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Método responsável por retornar todas as composições gerais.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Composicoes/ConsultarTodasComposicoes"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_composicoes_por_chave(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        status: Optional[int] = None,
        prod_equipe: Optional[int] = None,
        tipo_custo: Optional[str] = None,
        civil_pes: Optional[int] = None,
        categoria: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        codigo_servico_fiscal: Optional[str] = None,
        controlafvs: Optional[bool] = None,
        confirmado: Optional[int] = None,
        porc_qtde_excedida_entrega: Optional[str] = None,
        porc_preco_excedido_entrega: Optional[str] = None,
        porc_preco_reduzido_entrega: Optional[str] = None
    ) -> dict:
        path = "Composicoes/ConsultarComposicoesPorChave"
        return self.api.post(
            path,
            json={
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade,
                "status": status,
                "prodEquipe": prod_equipe,
                "tipoCusto": tipo_custo,
                "civilPes": civil_pes,
                "categoria": categoria,
                "categoriaMovFin": categoria_mov_fin,
                "CAP": cap,
                "CAPEstorno": cap_estorno,
                "CAPTransacaoFinanceira": cap_transacao_financeira,
                "NCM": ncm,
                "CEST": cest,
                "aplicacao": aplicacao,
                "codigoServicoFiscal": codigo_servico_fiscal,
                "controlaFVS": controlafvs,
                "confirmado": confirmado,
                "porcQtdeExcedidaEntrega": porc_qtde_excedida_entrega,
                "porcPrecoExcedidoEntrega": porc_preco_excedido_entrega,
                "porcPrecoReduzidoEntrega": porc_preco_reduzido_entrega,
            }
        )

    def consultar_insumos_da_composicao(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        status: Optional[int] = None,
        prod_equipe: Optional[int] = None,
        tipo_custo: Optional[str] = None,
        civil_pes: Optional[int] = None,
        categoria: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        codigo_servico_fiscal: Optional[str] = None,
        controlafvs: Optional[bool] = None,
        confirmado: Optional[int] = None,
        porc_qtde_excedida_entrega: Optional[str] = None,
        porc_preco_excedido_entrega: Optional[str] = None,
        porc_preco_reduzido_entrega: Optional[str] = None
    ) -> dict:
        path = "Composicoes/ConsultarInsumosDaComposicao"
        return self.api.post(
            path,
            json={
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade,
                "status": status,
                "prodEquipe": prod_equipe,
                "tipoCusto": tipo_custo,
                "civilPes": civil_pes,
                "categoria": categoria,
                "categoriaMovFin": categoria_mov_fin,
                "CAP": cap,
                "CAPEstorno": cap_estorno,
                "CAPTransacaoFinanceira": cap_transacao_financeira,
                "NCM": ncm,
                "CEST": cest,
                "aplicacao": aplicacao,
                "codigoServicoFiscal": codigo_servico_fiscal,
                "controlaFVS": controlafvs,
                "confirmado": confirmado,
                "porcQtdeExcedidaEntrega": porc_qtde_excedida_entrega,
                "porcPrecoExcedidoEntrega": porc_preco_excedido_entrega,
                "porcPrecoReduzidoEntrega": porc_preco_reduzido_entrega,
            }
        )

    def alterar_insumo_composicoes_geral(
        self,
        cod_composicao: Optional[str] = None,
        cod_insumo: Optional[str] = None,
        tipo_item: Optional[int] = None,
        coeficiente: Optional[int] = None,
        preco: Optional[int] = None
    ) -> dict:
        path = "Composicoes/AlterarInsumoComposicoesGeral"
        return self.api.post(
            path,
            json={
                "codComposicao": cod_composicao,
                "codInsumo": cod_insumo,
                "tipoItem": tipo_item,
                "coeficiente": coeficiente,
                "preco": preco,
            }
        )

    def inserir_insumo_composicoes_geral(
        self,
        cod_composicao: Optional[str] = None,
        cod_insumo: Optional[str] = None,
        tipo_item: Optional[int] = None,
        coeficiente: Optional[int] = None,
        preco: Optional[int] = None
    ) -> dict:
        path = "Composicoes/InserirInsumoComposicoesGeral"
        return self.api.post(
            path,
            json={
                "codComposicao": cod_composicao,
                "codInsumo": cod_insumo,
                "tipoItem": tipo_item,
                "coeficiente": coeficiente,
                "preco": preco,
            }
        )

    def consultar_composicoes_por_descricao(
        self,
        descricao: Optional[str] = None
    ) -> dict:
        """Consultar a tabela Composicoes pela sua descrição

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Composicoes/ConsultarComposicoesPorDescricao"
        return self.api.post(
            path,
            json={
                "descricao": descricao,
            }
        )

    def consultar_composicoes_com_filtro_livre(
        self,
        filtro: Optional[str] = None
    ) -> dict:
        """Consultar registros de composições gerais utilizando um filtro livre com qualquer um dos campos desta

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Permite consultar os registros de composições gerais utilizando um filtro livre com qualquer um dos campos existentes
Exemplo de filtro a ser utilizado: 

"filtro": "Cod_comp = '10.50'"
"filtro": "Descr_comp LIKE 'TERRAPLANAGEM%'" 
"filtro": "Cod_comp = '10.50' AND Descr_comp LIKE 'TERRAPLANAGEM%'" 
"filtro": "Cod_comp = '10.50' OR Descr_comp LIKE 'TERRAPLANAGEM%'"


        """
        path = "Composicoes/ConsultarComposicoesComFiltroLivre"
        return self.api.post(
            path,
            json={
                "filtro": filtro,
            }
        )

    def alterar_insumo_composicoes_geral_pesada(
        self,
        cod_composicao: Optional[str] = None,
        cod_insumo: Optional[str] = None,
        tipo_item: Optional[int] = None,
        coeficiente: Optional[int] = None,
        preco: Optional[int] = None,
        coef_prod: Optional[int] = None,
        coef_im_prod: Optional[int] = None,
        dmt: Optional[int] = None
    ) -> dict:
        path = "Composicoes/AlterarInsumoComposicoesGeralPesada"
        return self.api.post(
            path,
            json={
                "codComposicao": cod_composicao,
                "codInsumo": cod_insumo,
                "tipoItem": tipo_item,
                "coeficiente": coeficiente,
                "preco": preco,
                "coefProd": coef_prod,
                "coefImProd": coef_im_prod,
                "dMT": dmt,
            }
        )

    def inserir_insumo_composicoes_geral_pesada(
        self,
        cod_composicao: Optional[str] = None,
        cod_insumo: Optional[str] = None,
        tipo_item: Optional[int] = None,
        coeficiente: Optional[int] = None,
        preco: Optional[int] = None,
        coef_prod: Optional[int] = None,
        coef_im_prod: Optional[int] = None,
        dmt: Optional[int] = None
    ) -> dict:
        path = "Composicoes/InserirInsumoComposicoesGeralPesada"
        return self.api.post(
            path,
            json={
                "codComposicao": cod_composicao,
                "codInsumo": cod_insumo,
                "tipoItem": tipo_item,
                "coeficiente": coeficiente,
                "preco": preco,
                "coefProd": coef_prod,
                "coefImProd": coef_im_prod,
                "dMT": dmt,
            }
        )

