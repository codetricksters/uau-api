"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Espelho:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def alterar_status_unidade(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None,
        novo_status_unidade: Optional[int] = None,
        motivo_alteracao: Optional[str] = None,
        categoria_status_personalizacao: Optional[int] = None
    ) -> dict:
        """Atualizar unidade personalizada do produto

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Espelho/AlterarStatusUnidade"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoProduto": codigo_produto,
                "numeroPersonalizacao": numero_personalizacao,
                "novoStatusUnidade": novo_status_unidade,
                "motivoAlteracao": motivo_alteracao,
                "categoriaStatusPersonalizacao": categoria_status_personalizacao,
            }
        )

    def consultar_espelhos_venda(
        self,
        usuario_logado: Optional[str] = None
    ) -> dict:
        """Consulta espelhos de venda as empresas que o usuário tem permissão.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Espelho/ConsultarEspelhosVenda"
        return self.api.post(
            path,
            json={
                "usuario_logado": usuario_logado,
            }
        )

    def retornar_menor_preco_person(
        self,
        tipo_contrato: Optional[int] = None,
        cod_produto: Optional[int] = None,
        cod_categ_preco: Optional[str] = None,
        numero_person: Optional[int] = None,
        empresa: Optional[int] = None,
        data_categ_preco_produto: Optional[datetime] = None,
        porc_preco_minimo: Optional[int] = None
    ) -> dict:
        """Busca o valor do menor preço que pode ser inserido em um produto.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Espelho/RetornarMenorPrecoPerson"
        return self.api.post(
            path,
            json={
                "tipoContrato": tipo_contrato,
                "codProduto": cod_produto,
                "codCategPreco": cod_categ_preco,
                "numeroPerson": numero_person,
                "empresa": empresa,
                "dataCategPrecoProduto": data_categ_preco_produto,
                "porcPrecoMinimo": porc_preco_minimo,
            }
        )

    def atualizar_campos_customizados(
        self,
        campos_custom: Optional[Dict] = None
    ) -> dict:
        """Rotina responsável por atualizar campos customizados

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Espelho/AtualizarCamposCustomizados"
        return self.api.post(
            path,
            json={
                "campos_custom": campos_custom,
            }
        )

    def consultar_unidade_per_por_chave(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None
    ) -> dict:
        """Consultar unidade personalizada do produto

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Espelho/ConsultarUnidadePerPorChave"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoProduto": codigo_produto,
                "numeroPersonalizacao": numero_personalizacao,
            }
        )

    def busca_unidades_de_acordo_com_where(
        self,
        where: Optional[str] = None,
        retorna_venda: Optional[bool] = None
    ) -> dict:
        """Rotina responsável por buscar os dados das unidades de acordo com o WHERE passado por parâmetro.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Espelho/BuscaUnidadesDeAcordoComWhere"
        return self.api.post(
            path,
            json={
                "where": where,
                "retorna_venda": retorna_venda,
            }
        )

    def alterar_data_entrega_chaves_unidade(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_produto: Optional[int] = None,
        numero_personalizacao: Optional[int] = None,
        data_entrega_chaves: Optional[datetime] = None,
        observacao: Optional[str] = None
    ) -> dict:
        """Alterar a data de entrega das chaves da unidade

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Espelho/AlterarDataEntregaChavesUnidade"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoProduto": codigo_produto,
                "numeroPersonalizacao": numero_personalizacao,
                "dataEntregaChaves": data_entrega_chaves,
                "observacao": observacao,
            }
        )

    def consultar_personalizacoes_com_precos(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        num_produto: Optional[int] = None,
        cod_obra: Optional[str] = None,
        num_personalizacao: Optional[int] = None,
        consultarapenasnao_vendidos: Optional[bool] = None,
        tipo_contrato: Optional[int] = None,
        datatabela_preco: Optional[datetime] = None,
        campos_person: Optional[str] = None,
        status_person: Optional[str] = None,
        num_espelho: Optional[int] = None,
        tipocontrato_grafico: Optional[int] = None
    ) -> dict:
        """Consulta uma personalização com preços.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.


        """
        path = "Espelho/ConsultarPersonalizacoesComPrecos"
        return self.api.post(
            path,
            json={
                "usuario": usuario,
                "empresa": empresa,
                "num_produto": num_produto,
                "cod_obra": cod_obra,
                "num_personalizacao": num_personalizacao,
                "consultarapenasnao_vendidos": consultarapenasnao_vendidos,
                "tipo_contrato": tipo_contrato,
                "datatabela_preco": datatabela_preco,
                "campos_person": campos_person,
                "status_person": status_person,
                "num_espelho": num_espelho,
                "tipocontrato_grafico": tipocontrato_grafico,
            }
        )

    def busca_unidades_de_acordo_com_where_detalhado(
        self,
        where: Optional[str] = None,
        retorna_venda: Optional[bool] = None,
        data_tabela_preco: Optional[datetime] = None
    ) -> dict:
        """Consultar unidades de aacordo com o "where" informado

        Implementation Notes:
        
parâmetros de request da classe BuscaUnidadesDeAcordoComWhereDetalhadoRequest


        """
        path = "Espelho/BuscaUnidadesDeAcordoComWhereDetalhado"
        return self.api.post(
            path,
            json={
                "where": where,
                "retorna_venda": retorna_venda,
                "data_tabela_preco": data_tabela_preco,
            }
        )

