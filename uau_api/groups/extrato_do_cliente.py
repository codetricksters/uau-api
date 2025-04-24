"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class ExtratoDoCliente:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gerar_pdfextrato_cliente(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        tipo_ordenacao: Optional[int] = None,
        valor_antecipado: Optional[bool] = None,
        data_prorrogacao: Optional[bool] = None,
        ocultar_personalizacao: Optional[bool] = None,
        ocultar_usuario: Optional[bool] = None,
        data_calculo: Optional[datetime] = None,
        residuo_ira_compor_valor_total: Optional[bool] = None
    ) -> dict:
        """Método utilizado gerar os extratos em arquivos PDF e converte-los para string base64.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Preencher as opções de visualização do extrato nos módulos Vendas/Shopping, menu Utilitários, submenu Configurações extrato da venda (Visão Cliente)

Obs.: Parâmetros para impressão deste extrato são configurados na tela descrita neste virtuau: https://ajuda.globaltec.com.br/virtuau/configuracao-extrato-de-vendas-visao-cliente

        """
        path = "ExtratoDoCliente/GerarPDFExtratoCliente"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "numVenda": num_venda,
                "tipoOrdenacao": tipo_ordenacao,
                "valorAntecipado": valor_antecipado,
                "dataProrrogacao": data_prorrogacao,
                "ocultarPersonalizacao": ocultar_personalizacao,
                "ocultarUsuario": ocultar_usuario,
                "dataCalculo": data_calculo,
                "residuoIraComporValorTotal": residuo_ira_compor_valor_total,
            }
        )

    def gerar_pdfextrato_cliente_v2(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        tipo_ordenacao: Optional[int] = None,
        valor_antecipado: Optional[bool] = None,
        data_prorrogacao: Optional[bool] = None,
        ocultar_personalizacao: Optional[bool] = None,
        ocultar_usuario: Optional[bool] = None,
        data_calculo: Optional[datetime] = None,
        residuo_ira_compor_valor_total: Optional[bool] = None
    ) -> dict:
        """Método utilizado gerar os extratos em arquivos PDF e converte-los para string base64.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Preencher as opções de visualização do extrato nos módulos Vendas/Shopping, menu Utilitários, submenu Configurações extrato da venda (Visão Cliente)

Obs.: Parâmetros para impressão deste extrato são configurados na tela descrita neste virtuau: https://ajuda.globaltec.com.br/virtuau/configuracao-extrato-de-vendas-visao-cliente

        """
        path = "ExtratoDoCliente/GerarPDFExtratoClienteV2"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "numVenda": num_venda,
                "tipoOrdenacao": tipo_ordenacao,
                "valorAntecipado": valor_antecipado,
                "dataProrrogacao": data_prorrogacao,
                "ocultarPersonalizacao": ocultar_personalizacao,
                "ocultarUsuario": ocultar_usuario,
                "dataCalculo": data_calculo,
                "residuoIraComporValorTotal": residuo_ira_compor_valor_total,
            }
        )

    def consultar_saldo_cessoes_direito_anteriores(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None
    ) -> dict:
        """Consulta as vendas anteriores a essa, gerada por cessão de direito, retornando o saldo já pago nas vendas anteriores

        Implementation Notes:
        Retorna o somatório do saldo já pago das vendas anteriores de cessão de direito

        """
        path = "ExtratoDoCliente/ConsultarSaldoCessoesDireitoAnteriores"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_venda": num_venda,
            }
        )

    def consultar_dados_demonstrativo_pagto_cliente(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        tipos_parc: Optional[str] = None,
        tipo_ordenacao: Optional[int] = None,
        mostrara_pagas: Optional[bool] = None,
        princ_juros: Optional[bool] = None,
        descontopor_adiantamento: Optional[bool] = None,
        valor_antecipado: Optional[bool] = None,
        nome_fantasia: Optional[bool] = None,
        ocultapref_custas: Optional[bool] = None,
        data_calculo: Optional[datetime] = None,
        exibir_data_deposito: Optional[bool] = None
    ) -> dict:
        """Consulta os dados das parcelas pagas, informações do cliente e as unidades/produtos de uma determinada venda.
  Contém as chamadas dos métodos ConsultarItensRecebidas e ConsultarParcelasRecebidasCliente retornando um dataset e suas tabelas.
  OBS.: A instruçãoa [tipos_parc] se refere à parcelas que não devem ser mostradas no extrato do cliente, se enviar vazio, vai mostrar todas.

        Implementation Notes:
        Retorna informações das parcelas pagas, informações do cliente e unidades/produtos de uma determinada venda.

        """
        path = "ExtratoDoCliente/ConsultarDadosDemonstrativoPagtoCliente"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_venda": num_venda,
                "tipos_parc": tipos_parc,
                "tipo_ordenacao": tipo_ordenacao,
                "mostrara_pagas": mostrara_pagas,
                "princ_juros": princ_juros,
                "descontopor_adiantamento": descontopor_adiantamento,
                "valor_antecipado": valor_antecipado,
                "nome_fantasia": nome_fantasia,
                "ocultapref_custas": ocultapref_custas,
                "dataCalculo": data_calculo,
                "exibirDataDeposito": exibir_data_deposito,
            }
        )

