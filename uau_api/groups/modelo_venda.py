"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class ModeloVenda:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def buscar_plano_indexador(
        self,
        nummodelo_venda: Optional[int] = None
    ) -> dict:
        """Seleciona os dados do plano Indexador de um modelo de venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta o plano indexador vinculado ao modelo da venda.


        """
        path = "ModeloVenda/BuscarPlanoIndexador"
        return self.api.post(
            path,
            json={
                "nummodelo_venda": nummodelo_venda,
            }
        )

    def consultar_modelo_venda(
        self,
        cod_modelo_venda: Optional[int] = None
    ) -> dict:
        """Consultar o modelo de venda por chave

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta o modelo de vendo filtrando pelo código do modelo.

Tipos de Caps:
Tipo Parcelamento: 0 - Contrato                  

0 - Principal                                 
1 - Corr. por atraso                          
2 - Juros contratual                          
3 - Correção                                  
4 - Multa por atraso                          
5 - Juros por atraso                          
6 - Acrescimo                                 
7 - Desconto                                  
8 - Desconto por antecipação                  
9 - Taxa de boleto                           
10 - Desconto custas                         
11 - Repasse                                 
12 - Desconto condicional                    

Tipo Parcelamento: 1 - Custas | 3 - Honorário

0 - Principal
1 - Juros contratual
2 - Correção
3 - Multa por atraso
4 - Juros por atraso
5 - Corr. por atraso
6 - Acréscimo
7 - Desconto
8 - Desconto por antecipação
9 - Taxa de boleto
10 - Desconto custa
11 - Repasse
12 - Desconto condicional


        """
        path = "ModeloVenda/ConsultarModeloVenda"
        return self.api.post(
            path,
            json={
                "codModeloVenda": cod_modelo_venda,
            }
        )

    def gerar_parcelas_proposta(
        self,
        parametromodelovenda: Optional[List[Dict]] = None,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        redistribuir_valor: Optional[bool] = None,
        utilizar_cap: Optional[bool] = None,
        tipo_venda: Optional[int] = None
    ) -> dict:
        """Gerar parcelas da proposta baseado em parametros de parcelas. Pode ser usado para propostas e vendas.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Gera parcelas da proposta baseado nos parametros de parcelas informado.
Valida os campos passados na request.


        """
        path = "ModeloVenda/GerarParcelasProposta"
        return self.api.post(
            path,
            json={
                "parametromodelovenda": parametromodelovenda,
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "redistribuirValor": redistribuir_valor,
                "utilizarCap": utilizar_cap,
                "tipoVenda": tipo_venda,
            }
        )

    def consultar_modelo_de_venda(
        self,
        obra: Optional[str] = None,
        empresa: Optional[int] = None,
        nummodelo_venda: Optional[int] = None,
        eat_inat: Optional[int] = None,
        campos_retornados: Optional[str] = None,
        tipo: Optional[int] = None
    ) -> dict:
        """Consulta o modelo de venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta o modelo da venda filtrando os parâmetros informados na request.


        """
        path = "ModeloVenda/ConsultarModeloDeVenda"
        return self.api.post(
            path,
            json={
                "obra": obra,
                "empresa": empresa,
                "nummodelo_venda": nummodelo_venda,
                "eat_inat": eat_inat,
                "campos_retornados": campos_retornados,
                "tipo": tipo,
            }
        )

    def montar_modelo_renegociacao(
        self,
        cod_modelo_venda: Optional[int] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        valor_reneg_contrato: Optional[int] = None,
        valor_reneg_custas: Optional[int] = None,
        valor_reneg_seguromip: Optional[int] = None,
        valor_reneg_segurodfi: Optional[int] = None
    ) -> dict:
        """Monta modelo de renegociação com os parâmetros das parcelas e as parcelas.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite gerar parâmetros do modelo e as parcelas para uma renegociação.

Somente usuários autenticados podem ter acesso a essa rota.
As informações recebidas no request devem existirem no UAU.
O modelo de venda deve estar aprovado para ser utilizado.
O modelo de venda informada está vinculado a empresa/obra informada.
Os valores de custas, seguros e contratos devem estar configurados para o modelo.

Atenção:

Os campos DtIdxParc e DtJurParc são postos como o dia atual da venda caso o modelo esteja configurada para receber a data da venda.

Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/777189/
Exemplo Retorno: https://ajuda.globaltec.com.br/download/777192/


        """
        path = "ModeloVenda/MontarModeloRenegociacao"
        return self.api.post(
            path,
            json={
                "codModeloVenda": cod_modelo_venda,
                "empresa": empresa,
                "obra": obra,
                "numVenda": num_venda,
                "ValorRenegContrato": valor_reneg_contrato,
                "ValorRenegCustas": valor_reneg_custas,
                "ValorRenegSeguroMIP": valor_reneg_seguromip,
                "ValorRenegSeguroDFI": valor_reneg_segurodfi,
            }
        )

    def consultar_parcelas_modelo_venda(
        self,
        nummodelo_venda: Optional[int] = None
    ) -> dict:
        """Consultar parcelas do modelo de vendas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consultar todos os tipo de parcelas do modelo de venda filtrando pela chave/número do modelo.


        """
        path = "ModeloVenda/ConsultarParcelasModeloVenda"
        return self.api.post(
            path,
            json={
                "nummodelo_venda": nummodelo_venda,
            }
        )

    def consultar_modelo_de_venda_seguro_por_chave(
        self,
        nummodelo_venda: Optional[int] = None
    ) -> dict:
        """Consulta o seguro do modelo de venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Consulta o mo seguro do modelo de venda filtrando pela chave/número do modelo.


        """
        path = "ModeloVenda/ConsultarModeloDeVendaSeguroPorChave"
        return self.api.post(
            path,
            json={
                "nummodelo_venda": nummodelo_venda,
            }
        )

