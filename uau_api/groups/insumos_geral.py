"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class InsumosGeral:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def inserir_insumos_geral(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        unidades_insumo: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        status: Optional[int] = None,
        confirmado: Optional[int] = None,
        controlar_preco_meta: Optional[bool] = None,
        dias_de_compra: Optional[int] = None,
        dias_utilizacao: Optional[int] = None,
        numero_de_compras: Optional[int] = None,
        dias_entrega: Optional[int] = None,
        numero_pagamentos: Optional[int] = None,
        tipo_pagamento: Optional[int] = None,
        controle: Optional[int] = None,
        controla_estoque: Optional[int] = None,
        pagamento_sobre: Optional[int] = None,
        preco: Optional[str] = None,
        data_cotacao: Optional[datetime] = None,
        frequencia_compra: Optional[str] = None,
        como_pagar: Optional[str] = None,
        cap: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap_aplicacao_material: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        categoria_do_insumo: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        grupo: Optional[int] = None,
        calc_encargo: Optional[int] = None,
        controlafvm: Optional[bool] = None,
        patrimonio: Optional[int] = None,
        depreciacao: Optional[str] = None,
        grupo_de_insumos: Optional[str] = None,
        rateio_para_mecanicos: Optional[int] = None,
        indicador_util_bem: Optional[int] = None,
        capacidade_diaria_trabalho: Optional[str] = None,
        marca_modelo: Optional[str] = None,
        subgrupo: Optional[int] = None,
        item_manutencao: Optional[bool] = None
    ) -> dict:
        path = "InsumosGeral/InserirInsumosGeral"
        return self.api.post(
            path,
            json={
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade,
                "unidadesInsumo": unidades_insumo,
                "usuario": usuario,
                "status": status,
                "confirmado": confirmado,
                "controlarPrecoMeta": controlar_preco_meta,
                "diasDeCompra": dias_de_compra,
                "diasUtilizacao": dias_utilizacao,
                "numeroDeCompras": numero_de_compras,
                "diasEntrega": dias_entrega,
                "numeroPagamentos": numero_pagamentos,
                "tipoPagamento": tipo_pagamento,
                "controle": controle,
                "controlaEstoque": controla_estoque,
                "pagamentoSobre": pagamento_sobre,
                "preco": preco,
                "dataCotacao": data_cotacao,
                "frequenciaCompra": frequencia_compra,
                "comoPagar": como_pagar,
                "CAP": cap,
                "categoriaMovFin": categoria_mov_fin,
                "CAPAplicacaoMaterial": cap_aplicacao_material,
                "CAPEstorno": cap_estorno,
                "CAPTransacaoFinanceira": cap_transacao_financeira,
                "CategoriaDoInsumo": categoria_do_insumo,
                "NCM": ncm,
                "CEST": cest,
                "Aplicacao": aplicacao,
                "grupo": grupo,
                "calcEncargo": calc_encargo,
                "controlaFVM": controlafvm,
                "patrimonio": patrimonio,
                "depreciacao": depreciacao,
                "grupoDeInsumos": grupo_de_insumos,
                "rateioParaMecanicos": rateio_para_mecanicos,
                "indicadorUtilBem": indicador_util_bem,
                "capacidadeDiariaTrabalho": capacidade_diaria_trabalho,
                "marcaModelo": marca_modelo,
                "subgrupo": subgrupo,
                "itemManutencao": item_manutencao,
            }
        )

    def atualizar_insumos_geral(
        self,
        lista_insumos_atualizar: Optional[List[Dict]] = None
    ) -> dict:
        path = "InsumosGeral/AtualizarInsumosGeral"
        return self.api.post(
            path,
            json={
                "listaInsumosAtualizar": lista_insumos_atualizar,
            }
        )

    def consultar_insumos_geral(
        self,
        codigo_insumo: Optional[str] = None,
        descricao_insumo: Optional[str] = None,
        codigosub_grupo: Optional[int] = None,
        item_manutencao: Optional[int] = None,
        patrimonio: Optional[int] = None
    ) -> dict:
        """Consulta os itens de determinada revisão de um veículo ou equipamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Nenhum parâmetro é obrigatório e os dados são retornados utilizando o LIKE para encontrar as informações.


        """
        path = "InsumosGeral/ConsultarInsumosGeral"
        return self.api.post(
            path,
            json={
                "codigo_insumo": codigo_insumo,
                "descricao_insumo": descricao_insumo,
                "codigosub_grupo": codigosub_grupo,
                "item_manutencao": item_manutencao,
                "patrimonio": patrimonio,
            }
        )

    def consultar_insumos_geral_por_chave(
        self,
        codigo: Optional[str] = None,
        descricao: Optional[str] = None,
        unidade: Optional[str] = None,
        unidades_insumo: Optional[List[Dict]] = None,
        usuario: Optional[str] = None,
        status: Optional[int] = None,
        confirmado: Optional[int] = None,
        controlar_preco_meta: Optional[bool] = None,
        dias_de_compra: Optional[int] = None,
        dias_utilizacao: Optional[int] = None,
        numero_de_compras: Optional[int] = None,
        dias_entrega: Optional[int] = None,
        numero_pagamentos: Optional[int] = None,
        tipo_pagamento: Optional[int] = None,
        controle: Optional[int] = None,
        controla_estoque: Optional[int] = None,
        pagamento_sobre: Optional[int] = None,
        preco: Optional[str] = None,
        data_cotacao: Optional[datetime] = None,
        frequencia_compra: Optional[str] = None,
        como_pagar: Optional[str] = None,
        cap: Optional[str] = None,
        categoria_mov_fin: Optional[str] = None,
        cap_aplicacao_material: Optional[str] = None,
        cap_estorno: Optional[str] = None,
        cap_transacao_financeira: Optional[str] = None,
        categoria_do_insumo: Optional[str] = None,
        ncm: Optional[str] = None,
        cest: Optional[str] = None,
        aplicacao: Optional[str] = None,
        grupo: Optional[int] = None,
        calc_encargo: Optional[int] = None,
        controlafvm: Optional[bool] = None,
        patrimonio: Optional[int] = None,
        depreciacao: Optional[str] = None,
        grupo_de_insumos: Optional[str] = None,
        rateio_para_mecanicos: Optional[int] = None,
        indicador_util_bem: Optional[int] = None,
        capacidade_diaria_trabalho: Optional[str] = None,
        marca_modelo: Optional[str] = None,
        subgrupo: Optional[int] = None,
        item_manutencao: Optional[bool] = None
    ) -> dict:
        path = "InsumosGeral/ConsultarInsumosGeralPorChave"
        return self.api.post(
            path,
            json={
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade,
                "unidadesInsumo": unidades_insumo,
                "usuario": usuario,
                "status": status,
                "confirmado": confirmado,
                "controlarPrecoMeta": controlar_preco_meta,
                "diasDeCompra": dias_de_compra,
                "diasUtilizacao": dias_utilizacao,
                "numeroDeCompras": numero_de_compras,
                "diasEntrega": dias_entrega,
                "numeroPagamentos": numero_pagamentos,
                "tipoPagamento": tipo_pagamento,
                "controle": controle,
                "controlaEstoque": controla_estoque,
                "pagamentoSobre": pagamento_sobre,
                "preco": preco,
                "dataCotacao": data_cotacao,
                "frequenciaCompra": frequencia_compra,
                "comoPagar": como_pagar,
                "CAP": cap,
                "categoriaMovFin": categoria_mov_fin,
                "CAPAplicacaoMaterial": cap_aplicacao_material,
                "CAPEstorno": cap_estorno,
                "CAPTransacaoFinanceira": cap_transacao_financeira,
                "CategoriaDoInsumo": categoria_do_insumo,
                "NCM": ncm,
                "CEST": cest,
                "Aplicacao": aplicacao,
                "grupo": grupo,
                "calcEncargo": calc_encargo,
                "controlaFVM": controlafvm,
                "patrimonio": patrimonio,
                "depreciacao": depreciacao,
                "grupoDeInsumos": grupo_de_insumos,
                "rateioParaMecanicos": rateio_para_mecanicos,
                "indicadorUtilBem": indicador_util_bem,
                "capacidadeDiariaTrabalho": capacidade_diaria_trabalho,
                "marcaModelo": marca_modelo,
                "subgrupo": subgrupo,
                "itemManutencao": item_manutencao,
            }
        )

    def consultar_insumos_geral_por_descricao(
        self,
        descricao: Optional[str] = None
    ) -> dict:
        path = "InsumosGeral/ConsultarInsumosGeralPorDescricao"
        return self.api.post(
            path,
            json={
                "Descricao": descricao,
            }
        )

