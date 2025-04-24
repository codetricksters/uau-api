"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Venda:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def renegociar_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        parc_geradas: Optional[List[Dict]] = None,
        parc_sel_reneg: Optional[List[Dict]] = None,
        val_desc_reneg: Optional[int] = None,
        val_acresc_reneg: Optional[int] = None,
        valor_reajustado: Optional[int] = None,
        numero_padrao_cobranca: Optional[int] = None,
        tabelaplano_idx: Optional[List[Dict]] = None,
        data_calculo: Optional[str] = None
    ) -> dict:
        """Realiza a renegociação de parcelas de uma venda realizando as validações necessárias.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método

Definição de Negócio:
  Permite renegociar parcelas de uma venda

O usuário deverá estar autenticado e validado
Informar os dados da venda
Informar as parcelas a serem geradas
Informar as parcelas escolhidas para renegociação
Informar o plano de indexação
Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
  retorna mensagem informando a inconsistência encontrada para que seja analisada
Após as validações realiza a renegociação das parcelas
Será registrado comentário na venda sobre a renegociação realizada
Lista de planos indexadores
Caso não informe a lista de planos indexadores, serão considerados os planos que já existem na venda. 
Caso informe a lista de planos indexadores, a lista informada será considerada.
Caso um grupo informado de plano indexador já exista na venda, ele não será inserido novamente.
Para verificar se os planos já existem, serão considerados os grupos. Se para um grupo informado, já existir os mesmos indíces e datas na venda, ele não será adicionado.




Padrão de Cobrança

Padrão de Cobrança Informado no JSON. (Se o tipo de parcela tiver um padrão de cobrança vinculado, esse padrão será priorizado.)
    Exemplo:
    Padrão de cobrança informado: 4
    Parcela: P, Padrão de cobrança: 2
    Parcela: J, Não possui padrão de cobrança
    Parcelas geradas:
    Parcela: P, Padrão de cobrança: 2
    Parcela: J, Padrão de cobrança: 4

-Padrão de Cobrança Não Informado no JSON:
- Se o padrão de cobrança não for informado no JSON, ele será consultado pela obra.
  
  - Se o número do padrão de cobrança não for informado no JSON e na obra não estiver cadastrado, será utilizado o padrão de cobrança da primeira parcela
  que foi selecionada para renegociação. Esse padrão de cobrança será então preenchido em todas as parcelas.
  

VirtUau:

https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso


        """
        path = "Venda/RenegociarVenda"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Venda": venda,
                "Parc_Geradas": parc_geradas,
                "ParcSel_Reneg": parc_sel_reneg,
                "ValDesc_reneg": val_desc_reneg,
                "ValAcresc_reneg": val_acresc_reneg,
                "Valor_Reajustado": valor_reajustado,
                "NumeroPadraoCobranca": numero_padrao_cobranca,
                "Tabelaplano_idx": tabelaplano_idx,
                "DataCalculo": data_calculo,
            }
        )

    def busca_parc_reneg_web(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_ven: Optional[int] = None,
        exibirparcenv_cob: Optional[bool] = None,
        somenteparc_atraso: Optional[bool] = None,
        parcelasenviadas_banco: Optional[bool] = None
    ) -> dict:
        """Buscar parcelas calculadas na data atual

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Possibilita buscar parcelas calculadas para a data atual (dia da requisição).

        """
        path = "Venda/BuscaParcRenegWeb"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_ven": num_ven,
                "exibirparcenv_cob": exibirparcenv_cob,
                "somenteparc_atraso": somenteparc_atraso,
                "parcelasenviadas_banco": parcelasenviadas_banco,
            }
        )

    def exclusao_de_boletos(
        self,
        lista_boletos_excluir: Optional[List[Dict]] = None
    ) -> dict:
        """Faz a exclusão dos boletos informados

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Possibilita excluir boletos que estão com o status de normal.
Será permitido a exclusão de no máximo 20 boletos por requisição.


        """
        path = "Venda/ExclusaoDeBoletos"
        return self.api.post(
            path,
            json={
                "listaBoletosExcluir": lista_boletos_excluir,
            }
        )

    def exportar_vendas_xml(
        self,
        dados_vendas: Optional[Dict] = None
    ) -> dict:
        """Busca as vendas informadas ou as vendas inseridas/alteradas no periodo informado.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os dados das contas contábeis com a URI + /api/v{version}/Venda/ExportarVendasXml
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite exportar os registros de uma ou mais vendas do UAU para um arquivo XML no formato esperado para realização de importação de vendas.

Deve informar a venda ou o período para que seja realizada a consulta.
Pode informar as chaves de Venda que são [Empresa, Obra, Venda].
Valida as datas e campos inseridos.
O perído informado buscará vendas considerando a data de cadastro, a data de manutenção e a data de quitação.
O item "listaVendas" permite informar empresa, obra e venda que serão adicionados ao retorno da consulta. 
  Não será filtrado exclusivamente por esta lista de vendas, mas serão acrescidas ao resultado do período informado.

VirtUau:

http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Venda/Venda_ExportarVendasXml
Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/777060/ 
Arquivo de Retorno: https://ajuda.globaltec.com.br/download/777060/


        """
        path = "Venda/ExportarVendasXml"
        return self.api.post(
            path,
            json={
                "dados_vendas": dados_vendas,
            }
        )

    def importacao_de_venda(
        self,
        xml_vendas: Optional[str] = None,
        alterarnumerodas_vendas: Optional[bool] = None
    ) -> dict:
        """Importar vendas para o UAU via XML

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Número máximo de importações por vez: 50.
Para obter retorno de sucesso ou falha na importação consulte o endpoint:
URI + /api/v1.0/Venda/ImportacaoVendaComRetorno



Validação:

Arquivo XSD: https://ajuda.globaltec.com.br/wp-content/uploads/2021/01/Manual-de-integracao-de-Vendas_versao1006_2.zip

Dicionário de dados: https://ajuda.globaltec.com.br/wp-content/uploads/2021/01/Venda.zip


Definição de Negócio:
Permite importar vendas para o UAU via XML.

Valida quantidade de importações por requisição.
Caso ocorra erro em uma venda, todas as outras importações são canceladas.


        """
        path = "Venda/ImportacaoDeVenda"
        return self.api.post(
            path,
            json={
                "xml_vendas": xml_vendas,
                "alterarnumerodas_vendas": alterarnumerodas_vendas,
            }
        )

    def aprov_desaprov_reneg(
        self,
        cod_empresa: Optional[int] = None,
        cod_obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        aprov_desaprov: Optional[bool] = None
    ) -> dict:
        """Aprovar ou desaprovar renegociações

        Implementation Notes:
        Definição técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de negócio

A rota aprova ou desaprova uma renegociação de venda.
É realizada uma validação da Alçada.
Os anexos são atualizados conforme a operação solicitada.

Pré requisito:

É necessário ter permissão de aprovação em FIMNTVENRENCON

Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:

URL + /api/v{version}/Venda/AprovDesaprovReneg




        """
        path = "Venda/AprovDesaprovReneg"
        return self.api.post(
            path,
            json={
                "codEmpresa": cod_empresa,
                "codObra": cod_obra,
                "numVenda": num_venda,
                "aprovDesaprov": aprov_desaprov,
            }
        )

    def buscar_tipos_de_custas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar a lista de tipos de custas ativos.

        Implementation Notes:
        Definição Técnica:

Busca a lista de status de cobrança ativos do sistema:

URI + /api/v{version}/Venda/BuscarTiposDeCustas


Formato dos dados retornados:

Codigo(String):Código do tipo de custa
Descricao(String):Descrição do status de cobrança




        """
        path = "Venda/BuscarTiposDeCustas"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_historicos(
        self,
        vendas: Optional[List[Dict]] = None,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        tipo_manutencao: Optional[str] = None
    ) -> dict:
        """Consultar os históricos de uma ou mais vendas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
O preenchimento da lista de vendas, devem ser preenchidos de forma padronizada, ou preenche todas as vendas com o número da venda, ou todas com apenas empresa e obra.
Para o preenchimento dos tipos de manutenção, o valor de tipo de manutenção deve ser numérico e caso tenha mais de um, devem ser separados por vírgula. Exemplo: 1,2,4.
Recomendável buscar períodos curtos ou uma venda específica para evitar timeout.

Definição de Negócio:
  Consultar os históricos de uma ou mais vendas selecionadas.
  Para buscar os históricos das vendas um dos parâmetros devem estar preenchidos, ou a lista de vendas ou o período da manutenção.

As classes abaixo não serão preenchidas no objeto de retorno porque essas informações não possuem histórico:
Comissoes
Comentarios
AluguelShopping
VendaVinculada
DescontosDeCusta
Recebimentos
Prorrogacoes




        """
        path = "Venda/ConsultarHistoricos"
        return self.api.post(
            path,
            json={
                "Vendas": vendas,
                "DataInicio": data_inicio,
                "DataFim": data_fim,
                "TipoManutencao": tipo_manutencao,
            }
        )

    def excluir_parcela_custa(
        self,
        excluir_parcela_no_banco: Optional[bool] = None,
        lista: Optional[List[Dict]] = None
    ) -> dict:
        """Reliza a exclusão de Parcela de Custa.
        """
        path = "Venda/ExcluirParcelaCusta"
        return self.api.post(
            path,
            json={
                "ExcluirParcelaNoBanco": excluir_parcela_no_banco,
                "Lista": lista,
            }
        )

    def gerar_boleto_bancario(
        self,
        parcelas: Optional[List[Dict]] = None,
        data_calculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        reajustar: Optional[bool] = None,
        excluirboleto_expirado: Optional[bool] = None,
        formaarquivo_cobranca: Optional[int] = None,
        boletosacado_detalhado: Optional[bool] = None,
        carnetres_vias: Optional[bool] = None,
        naovalidardados_pendentes: Optional[bool] = None,
        acrescentar_residuo: Optional[bool] = None,
        usarpadraoboleto_avulso: Optional[bool] = None,
        agrupar_parcelas: Optional[bool] = None,
        formaagruparpor_vendas: Optional[bool] = None,
        valor_boleto: Optional[int] = None,
        padrao_cobranca: Optional[int] = None,
        excluir_boletos_existentes: Optional[bool] = None,
        reaproveitar_boleto: Optional[bool] = None,
        valor_taxa_boleto: Optional[int] = None
    ) -> dict:
        """Gravar o arquivo de remessa para geração do boleto bancario ou carne

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Permite gerar o boleto bancário ou carnê.
O usuário autenticado deve ter permissão de inclusão no programa de permissão VEBOLETOAVULSO.
Para gerar boleto parcial é necessário informar a propriedade ValorBoleto.
Não pode ser um valor negativo nem inferior a 0,01 centavo.
Se informar um valor igual ao valor total das parcelas enviadas, será gerado um boleto normal.
Se informar um valor menor que o valor total das parcelas enviadas, será gerado um boleto parcial.
Apenas uma parcela das enviadas deverá ser parcial
Não será gerado boleto caso informe um valor que não cubra todas as parcelas enviadas
A ordem de envio das parcelas deve ser a mesma ordem de seleção das parcelas ao gerar o boleto pela tela de recebimento avulso.
  Exemplo: Na tela de recebimento avulso, selecionei as parcelas 360, 359 e 358. Ao gerar pela API, as parcelas devem ser enviadas
  na mesma sequência selecionada.
Irá validar se as parcelas enviadas podem gerar o boleto parcial de acordo com a regra de dias para vencimento.


Será possível gerar boleto parcial somente para parcelas de uma única empresa, obra e venda.
Só é possível gerar boleto parcial para mais de uma parcela quando for antecipação.
É obrigatório reajustar ao gerar o boleto parcial.


Padrão de cobrança    
Não é obrigatório informá-lo.
Caso informado, o sistema irá desconsiderar a configuração do parâmetro usarpadraoboleto_avulso e irá gerar o boleto pelo padrão informado.
Caso informado, será desconsiderado o padrão de cobrança de todas as parcelas, incluindo custas administrativas, e boleto será gerado com o padrão de cobrança informado.
Apenas os padrões de cobrança ativos serão aceitos.
Será possivel gerar boleto com o padrão de informado somente para parcelas de uma única empresa.


Excluir Boletos Existentes
Não é obrigatório informar o parâmetro ExcluirBoletosExistentes.
Caso não seja informado será mantido a opção padrão de não excluir.
Caso informado, irá executar as mesmas ações que a configuração 'Excluir boletos já emitidos ao gerar um novo boleto para a parcela' no cadastro de empresas > config. vendas.


Reaproveitar boleto
Não é obrigatório informar o parâmetro ReaproveitarBoleto
Caso não seja informado será mantida a opção padrão de não reaproveitar o boleto,
Caso informado, irá tentar reaproveitar algum boleto que já exista para uma das parcelas enviadas.
Somente válido para bancos e/ou tipos de cobrança que permitem a manutenção do boleto.
Somente para parcelas de uma única empresa, obra e venda. Caso envie parcelas de vendas diferentes, a opção de reaproveitar boleto será desconsiderada e irá gerar um novo boleto.
Será gerado arquivo de alteração de vencimento ou valor do boleto.
Não será possivel reaproveitar caso não exista boleto gerado ou o agrupamento das parcelas gere mais de um boleto.


Sempre homologue junto ao banco antes de usar!


Valor taxa boleto
Não é obrigatório informar o parâmetro ValorTaxaBoleto
Essa taxa será utilizada independente do parâmetro de reaproveitar boleto for true e a venda cobrar taxa de boleto.
Caso informado, irá desconsiderar o valor da taxa cadastrado na empresa e aplicar o valor informado.
Caso não seja informado ou seja informado zero, irá aplicar o valor da taxa cadastrado na empresa do boleto reaproveitado.




        """
        path = "Venda/GerarBoletoBancario"
        return self.api.post(
            path,
            json={
                "parcelas": parcelas,
                "data_calculo": data_calculo,
                "antecipar": antecipar,
                "reajustar": reajustar,
                "excluirboleto_expirado": excluirboleto_expirado,
                "formaarquivo_cobranca": formaarquivo_cobranca,
                "boletosacado_detalhado": boletosacado_detalhado,
                "carnetres_vias": carnetres_vias,
                "naovalidardados_pendentes": naovalidardados_pendentes,
                "acrescentar_residuo": acrescentar_residuo,
                "usarpadraoboleto_avulso": usarpadraoboleto_avulso,
                "agrupar_parcelas": agrupar_parcelas,
                "formaagruparpor_vendas": formaagruparpor_vendas,
                "ValorBoleto": valor_boleto,
                "PadraoCobranca": padrao_cobranca,
                "ExcluirBoletosExistentes": excluir_boletos_existentes,
                "ReaproveitarBoleto": reaproveitar_boleto,
                "ValorTaxaBoleto": valor_taxa_boleto,
            }
        )

    def gerar_pdfresumo_venda(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        data_correcao: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        parcelas: Optional[List[Dict]] = None,
        aplicar_desconto_geral: Optional[bool] = None,
        percentual_desconto_geral: Optional[int] = None,
        aplicar_desconto_antecipacao: Optional[bool] = None,
        desconto_antecipacao: Optional[Dict] = None
    ) -> dict:
        """Gerar PDF do relatório do resumo da venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.

Definição de Negócio:
  Gera boleto PDF do resumo da venda em formato Base64.

Validações a nível de usuário.


        """
        path = "Venda/GerarPDFResumoVenda"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "numeroVenda": numero_venda,
                "dataCalculo": data_calculo,
                "dataCorrecao": data_correcao,
                "antecipar": antecipar,
                "parcelas": parcelas,
                "aplicarDescontoGeral": aplicar_desconto_geral,
                "percentualDescontoGeral": percentual_desconto_geral,
                "aplicarDescontoAntecipacao": aplicar_desconto_antecipacao,
                "descontoAntecipacao": desconto_antecipacao,
            }
        )

    def buscar_status_cobranca(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar a lista de status de cobrança ativos.

        Implementation Notes:
        Definição Técnica:

Busca a lista de status de cobrança ativos do sistema:

URI + /api/v{version}/Venda/BuscarStatusCobranca


Formato dos dados retornados:

Codigo(Integer):Código do status de cobrança
Descricao(String):Descrição do status de cobrança




        """
        path = "Venda/BuscarStatusCobranca"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_resumo_venda(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        data_correcao: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        parcelas: Optional[List[Dict]] = None,
        aplicar_desconto_geral: Optional[bool] = None,
        percentual_desconto_geral: Optional[int] = None,
        aplicar_desconto_antecipacao: Optional[bool] = None,
        desconto_antecipacao: Optional[Dict] = None
    ) -> dict:
        """Consultar resumo da venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Obtêm informações referentes a venda consultada.

        """
        path = "Venda/ConsultarResumoVenda"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "numeroVenda": numero_venda,
                "dataCalculo": data_calculo,
                "dataCorrecao": data_correcao,
                "antecipar": antecipar,
                "parcelas": parcelas,
                "aplicarDescontoGeral": aplicar_desconto_geral,
                "percentualDescontoGeral": percentual_desconto_geral,
                "aplicarDescontoAntecipacao": aplicar_desconto_antecipacao,
                "descontoAntecipacao": desconto_antecipacao,
            }
        )

    def gerar_venda_de_proposta(
        self,
        numero_proposta: Optional[int] = None,
        atualiza_datas_da_venda: Optional[bool] = None,
        data_venda: Optional[datetime] = None,
        atualiza_inicio_primeiro_juros: Optional[bool] = None,
        atualiza_inicio_reajuste: Optional[bool] = None,
        atualiza_inicio_segundo_juros: Optional[bool] = None,
        atualiza_base_residuo: Optional[bool] = None,
        atualiza_plano_indexador: Optional[bool] = None,
        data_primeiro_juros: Optional[datetime] = None,
        data_segundo_juros: Optional[datetime] = None,
        data_reajuste: Optional[datetime] = None,
        data_base_residuo: Optional[datetime] = None,
        lista_plano_indexador: Optional[List[Dict]] = None,
        desconsiderar_nao_titulares_avalista: Optional[bool] = None,
        dias_prorrogacao_parc_vencidas: Optional[int] = None,
        usuario_cad_venda: Optional[str] = None,
        lista_nao_titular_avalista: Optional[List[Dict]] = None
    ) -> dict:
        """Efetua a venda da proposta informada e retorna o Objeto Venda da mesma

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Realiza venda de acordo com a proposta informada.

Validações serão realizadas para efetuar a operação.
Todas alterações informadas no request apenas afetarão a venda gerada.
A opção de desconsiderar não titulares avalistas, serve para o caso onde queriam gravar uma venda sem titular avalista, que possa está configurado na proposta.
Se informar o lista de não titulares, o sistema vai desconsiderar os da proposta e utilizar os informados no request.
A lista de não titulares deve conter o código das pessoas no UAU.


        """
        path = "Venda/GerarVendaDeProposta"
        return self.api.post(
            path,
            json={
                "numeroProposta": numero_proposta,
                "atualizaDatasDaVenda": atualiza_datas_da_venda,
                "dataVenda": data_venda,
                "atualizaInicioPrimeiroJuros": atualiza_inicio_primeiro_juros,
                "atualizaInicioReajuste": atualiza_inicio_reajuste,
                "atualizaInicioSegundoJuros": atualiza_inicio_segundo_juros,
                "atualizaBaseResiduo": atualiza_base_residuo,
                "atualizaPlanoIndexador": atualiza_plano_indexador,
                "dataPrimeiroJuros": data_primeiro_juros,
                "dataSegundoJuros": data_segundo_juros,
                "dataReajuste": data_reajuste,
                "dataBaseResiduo": data_base_residuo,
                "listaPlanoIndexador": lista_plano_indexador,
                "desconsiderarNaoTitularesAvalista": desconsiderar_nao_titulares_avalista,
                "diasProrrogacaoParcVencidas": dias_prorrogacao_parc_vencidas,
                "usuarioCadVenda": usuario_cad_venda,
                "listaNaoTitularAvalista": lista_nao_titular_avalista,
            }
        )

    def buscar_tipos_de_parcelas(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar a lista de tipos de parcelas ativos

        Implementation Notes:
        Definição Técnica:

Busca a lista de status de cobrança ativos do sistema:

URI + /api/v{version}/Venda/BuscarTiposDeParcelas


Formato dos dados retornados:

Tipo(String):Código do tipo de parcela
Descricao(String):Descrição do tipo de parcela




        """
        path = "Venda/BuscarTiposDeParcelas"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def finalizar_renegociacao(
        self,
        usuario_logado: Optional[str] = None,
        parc_geradas_json: Optional[str] = None,
        parcsel_reneg_json: Optional[str] = None,
        grupo_parcelas_json: Optional[str] = None,
        valdesc_reneg: Optional[int] = None,
        valacresc_reneg: Optional[int] = None,
        val_reneg: Optional[int] = None,
        pendentevalidar_alcada: Optional[bool] = None,
        venda: Optional[int] = None,
        obra: Optional[str] = None,
        empresa: Optional[int] = None,
        tabelaplano_idx_json: Optional[str] = None
    ) -> dict:
        """Finalizar uma negociação

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Possibilita finalizar determinada negociação.

        """
        path = "Venda/FinalizarRenegociacao"
        return self.api.post(
            path,
            json={
                "usuario_logado": usuario_logado,
                "parc_geradas_json": parc_geradas_json,
                "parcsel_reneg_json": parcsel_reneg_json,
                "grupo_parcelas_json": grupo_parcelas_json,
                "valdesc_reneg": valdesc_reneg,
                "valacresc_reneg": valacresc_reneg,
                "val_reneg": val_reneg,
                "pendentevalidar_alcada": pendentevalidar_alcada,
                "venda": venda,
                "obra": obra,
                "empresa": empresa,
                "tabelaplano_idx_json": tabelaplano_idx_json,
            }
        )

    def gravar_ocorrencia_anexo(
        self,
        ocorrencias: Optional[List[Dict]] = None
    ) -> dict:
        """Anexar uma ocorrência

        Implementation Notes:
        Definição técnica:

Adiciona uma ou várias ocorrências vinculada de anexo de acordo com os parâmetros passados na requisição.

Parâmetros da request

Chave: Chave para consulta.
Campos: 
Campos obrigatórios para a chave="Venda" (empresa, obra, venda, codigo ocorrencia, usuario). 
Campos obrigatórios para a chave="Parcela" (empresa, obra, venda, número parcela, número geral da parcela, tipo da parcela, codigo ocorrência, usuario)




        """
        path = "Venda/GravarOcorrenciaAnexo"
        return self.api.post(
            path,
            json={
                "Ocorrencias": ocorrencias,
            }
        )

    def alterar_data_prorrogacao(
        self,
        dados_prorrogacao: Optional[Dict] = None
    ) -> dict:
        path = "Venda/AlterarDataProrrogacao"
        return self.api.post(
            path,
            json={
                "dados_prorrogacao": dados_prorrogacao,
            }
        )

    def buscar_parcelas_areceber(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_ven: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        valor_presente: Optional[bool] = None
    ) -> dict:
        """Buscar parcelas a receber calculadas para a data atual

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Possibilita a busca de parcelas a receber na data atual.

        """
        path = "Venda/BuscarParcelasAReceber"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_ven": num_ven,
                "data_calculo": data_calculo,
                "valor_presente": valor_presente,
            }
        )

    def buscar_parametro_cobranca(
        self,
        empresa: Optional[int] = None,
        banco: Optional[int] = None
    ) -> dict:
        """Retornar a lista com parâmetros de cobranças

        Implementation Notes:
        Definição Técnica:

Busca a lista de parâmetros de cobrança ativos do sistema:

URI + /api/v{version}/Venda/BuscarParametroCobranca


Formato dos dados retornados:

Banco     (String) : Número do banco
NomeBanco (String) : Nome do banco
Conta     (String) : Número da conta
Agencia   (String) : Código da agência do banco
Carteira  (String) : Código da carteira do convênio com banco
Codigo    (String) : Código do parâmetro de cobrança no sistema
Descricao (String) : Descrição do parâmetro de cobrança no sistema
Empresa   (String) : Código da empresa
Cedente   (String) : Código do cedente da remessa de cobrança



Definição de negócio:

Para buscar todos os padrões de cobrança ativos, usar null nos parâmetros da requisição ou não enviar os campos.


        """
        path = "Venda/BuscarParametroCobranca"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "banco": banco,
            }
        )

    def buscar_parcelas_recebidas(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_ven: Optional[int] = None
    ) -> dict:
        """Buscar parcelas recebidas da venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Possibilita buscar parcelas que foram recebidas.

        """
        path = "Venda/BuscarParcelasRecebidas"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_ven": num_ven,
            }
        )

    def buscar_status_de_escritura(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Retornar a lista de Status de escritura ativos.

        Implementation Notes:
        Definição Técnica:

Busca a lista de Status de escritura ativos do sistema:

URI + /api/v{version}/Venda/BuscarStatusDeEscritura


Formato dos dados retornados:

Codigo(Integer):Código de Status de escritura
Descricao(String):Descrição do Status de escritura




        """
        path = "Venda/BuscarStatusDeEscritura"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_parcelas_da_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        boleto_antecipado: Optional[bool] = None,
        somente_parcelas_aptas_boleto: Optional[bool] = None
    ) -> dict:
        """Consultar parcelas da venda calculadas para a data informada

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite consultar as parcelas de uma venda.

Ao enviar somenteParcelasAptasBoleto como TRUE, irá validar se a venda possui bloqueio ou manutenção pendente e se a empresa está configurada
  para "Não permitir enviar para banco parcelas com status [em banco]"
Caso a venda possua bloqueio ou esteja em manutenção, não irá retornar nenhuma parcela da venda.
Caso esteja configurado para não enviar parcelas com status em banco, não irá retornar as parcelas que já tenham boletos gerados.




        """
        path = "Venda/ConsultarParcelasDaVenda"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_venda": num_venda,
                "data_calculo": data_calculo,
                "boleto_antecipado": boleto_antecipado,
                "somenteParcelasAptasBoleto": somente_parcelas_aptas_boleto,
            }
        )

    def gerar_pdfevolucao_contrato(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None
    ) -> dict:
        """Gerar PDF do relatório da evolução do contrato

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.

Definição de Negócio:
  Gera PDF da evolução do contrato em string do tipo Base64.

Validações a nível de usuário.


        """
        path = "Venda/GerarPDFEvolucaoContrato"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "numeroVenda": numero_venda,
            }
        )

    def buscar_recebimentos_da_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        parcelasnao_conciliadas: Optional[bool] = None
    ) -> dict:
        """Consulta os recebimentos de uma venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Permite consultar os reecebimentos de uma venda, ou seja, o que já foi recebido.
Caso o campo "parcelasnao_conciliadas" esteja marcado como "true" as parcelas não conciliadas também serão retornadas.


        """
        path = "Venda/BuscarRecebimentosDaVenda"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "venda": venda,
                "parcelasnao_conciliadas": parcelasnao_conciliadas,
            }
        )

    def exportar_pessoas_da_venda_xml(
        self,
        lista_vendas: Optional[List[Dict]] = None
    ) -> dict:
        """Busca as pessoas vinculadas às vendas informadas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Possibilita acesso às pessoas que estão relacionadas com a venda informada.

Valida a existência da venda.


        """
        path = "Venda/ExportarPessoasDaVendaXml"
        return self.api.post(
            path,
            json={
                "lista_vendas": lista_vendas,
            }
        )

    def gravar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_contrato: Optional[int] = None,
        estabelecimento: Optional[str] = None,
        forma_pgto: Optional[int] = None,
        qtde_parcelas: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        valor_liquido: Optional[int] = None,
        tipo_recebimento: Optional[int] = None,
        antecipacao: Optional[bool] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """Gravar pedido de recebimento junto a NTK

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

É obrigatório ter o ambiente de integração com a PAYGO configurado, só após o registro junto a eles que o registro será gerado no UAU.
É necessário ter permissão de inclusão no programa VEPEDIDORECEBIMENTO


        """
        path = "Venda/GravarPedidoDeRecebimento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "NumContrato": num_contrato,
                "Estabelecimento": estabelecimento,
                "FormaPgto": forma_pgto,
                "QtdeParcelas": qtde_parcelas,
                "DataCalculo": data_calculo,
                "ValorLiquido": valor_liquido,
                "TipoRecebimento": tipo_recebimento,
                "Antecipacao": antecipacao,
                "Parcelas": parcelas,
            }
        )

    def importacao_venda_com_retorno(
        self,
        xml_vendas: Optional[str] = None,
        alterarnumerodas_vendas: Optional[bool] = None
    ) -> dict:
        """Importar vendas para o UAU via XML com retorno de venda importada

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Número máximo de importações por vez: 50.

Definição de Negócio:
  Possibilita importa vendas via XML para o UAU e receber como retorno as vendas importadas.

Valida quantidade de importações por requisição.
Caso ocorra erro em uma venda, todas as outras importações são canceladas e terá um retorno com informações da venda que falhou.


        """
        path = "Venda/ImportacaoVendaComRetorno"
        return self.api.post(
            path,
            json={
                "xml_vendas": xml_vendas,
                "alterarnumerodas_vendas": alterarnumerodas_vendas,
            }
        )

    def manter_status_cobranca_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        numero_parcela: Optional[int] = None,
        numero_parcela_geral: Optional[int] = None,
        tipo_parcela: Optional[str] = None,
        status_cobranca: Optional[List[Dict]] = None
    ) -> dict:
        """Alterar status de cobrança da venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Possibilita alterar o status de cobrança referentes a determinada venda.
  Validações serão realizadas para efetuar a operação:

Se os parâmetros forem da parcela, o ocorrência será gravada na parcela correspondente.
Se os parâmetros forem da venda, o ocorrência será gravada na venda correspondente.
Caso seja informado o parâmetro numeroParcela, numeroParcelaGeral ou tipoParcela, os três serão obrigatórios.
O parâmetro 'código' deverá ser do tipo numérico.
Os status de cobrança da venda ou parcela, serão substituídos pelos status informados.


        """
        path = "Venda/ManterStatusCobrancaVenda"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "venda": venda,
                "numeroParcela": numero_parcela,
                "numeroParcelaGeral": numero_parcela_geral,
                "tipoParcela": tipo_parcela,
                "statusCobranca": status_cobranca,
            }
        )

    def venda_valida_para_manutencao(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        usr_logado: Optional[str] = None,
        mensagem_securitizacao: Optional[str] = None
    ) -> dict:
        """Valida se a venda pode ser renegociada pela tela de renegociação na Web.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Valida a possibilidade de realizar a renegociação da venda, para tal tarefa a venda não pode ter restrições.

Os campos inseridos na request serão utilizado para buscar e verificar disponibilidade de renegociação.


        """
        path = "Venda/VendaValidaParaManutencao"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "venda": venda,
                "usr_logado": usr_logado,
                "mensagem_securitizacao": mensagem_securitizacao,
            }
        )

    def consultar_contas_receber_calc(
        self,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        tipos_parcela: Optional[str] = None,
        vendas: Optional[List[Dict]] = None
    ) -> dict:
        """Consulta de parcelas de contas a receber já calculadas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Possibilita Consultar as parcelas de contas a receber já calculadas com retorno a lista de parcelas.
Nenhuma propriedade é obrigatória, porém é obrigatório ser enviado pelo menos um tipo de filtro para consultar os dados.
Na propriedade vendas, é obrigatório apenas o parâmetro empresa.
É indispensável que o PROUAU esteja rodando diariamente o cálculo de parcelas para que os resultados estejam sempre corretos.
O Filtro de período filtrará pela data de vencimento da parcela.
O filtro por tipo de parcelas pode aceitar mais de um tipo, é obrigatório colocar entre aspas simples cada código de parcela e separadas por virgula. Ex.: 'P', 'M'


        """
        path = "Venda/ConsultarContasReceberCalc"
        return self.api.post(
            path,
            json={
                "DataInicio": data_inicio,
                "DataFim": data_fim,
                "TiposParcela": tipos_parcela,
                "Vendas": vendas,
            }
        )

    def importacao_parcelas_de_custas(
        self,
        custas: Optional[List[Dict]] = None
    ) -> dict:
        """Importar parcelas do tipo Custa

        Implementation Notes:
        Definição Técnica:

Importação de parcelas do tipo Custas:
URI + /api/v{version}/Venda/ImportacaoParcelasDeCustas



Definição de Negócio:

Permite importar parcelas do tipo Custas com as seguintes regras:

Os campos: Observacao, CobrarJurosAtraso, CobrarMulta, CobrarCorrecao, CobrarImposto, CobrarTxAdm, CobrarRepasseLocador, Competencia, NUMEROPARCELA e MeioPreferencialDeRecebimento são opcionais.


Referente a propriedade de CAPs:

Caso não sejam informados os CAPs para uma ou mais parcelas de custas, para essas parcelas, será utilizada a configuração padrão de CAPs da empresa;
Será possível utilizar em uma mesma requisição parcelas com CAPs definidos no JSON e parcelas com CAPs padrão da empresa (não informado no JSON);
Será validada a existência dos CAPs informado e só será possível utilizar CAPs ativos;
Caso seja informado um CAP para uma determinada parcela, todos os demais CAPs daquela parcela, serão obrigatórios;



Anexos:

Link para download de exemplos:
Exemplo de parcela tipo Custa: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcelas-de-Custas.postman_collection.zip


        """
        path = "Venda/ImportacaoParcelasDeCustas"
        return self.api.post(
            path,
            json={
                "custas": custas,
            }
        )

    def buscar_campanha_desconto_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None
    ) -> dict:
        """Buscar a campanha de desconto disponível para uma campanha

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método

Definição de Negócio:
  Permite renegociar parcelas de uma venda

O usuário deverá estar autenticado e validado
Informar os dados da venda
Informar as parcelas a serem geradas
Informar as parcelas escolhidas para renegociação
Informar o plano de indexação
Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
  retorna mensagem informando a inconsistência encontrada para que seja analisada
Após as validações realiza a renegociação das parcelas
Será registrado comentário na venda sobre a renegociação realizada

VirtUau:

https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso


        """
        path = "Venda/BuscarCampanhaDescontoVenda"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Venda": venda,
                "DataCalculo": data_calculo,
            }
        )

    def cancelar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """Cancelar o pedido de recebimento junto a NTK

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Pedidos que já tiveram um recebimento parcial junto a NTK, não são cancelados. (trava na NTK).
É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO


        """
        path = "Venda/CancelarPedidoDeRecebimento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Pedido": pedido,
            }
        )

    def atualizar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """Atualizar o(s) pedido(s) de recebimento junto a NTK

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Serão atualizadas as parcelas do pedido que ainda estão com status: 0 - Em aberto 
Valida usuário e permissões
Valida outras informações passadas no request


        """
        path = "Venda/AtualizarPedidoDeRecebimento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Pedido": pedido,
            }
        )

    def consultar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """Consultar o pedido de recebimento junto a NTK

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Possibilita consultar pedido de recebimento junto a NTK
As informações retornadas serão informações do pedido na NTK.
É necessário ter permissão de consulta em VEPEDIDORECEBIMENTO


        """
        path = "Venda/ConsultarPedidoDeRecebimento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Pedido": pedido,
            }
        )

    def processar_recebimento_parcelas(
        self,
        recebimento: Optional[Dict] = None,
        forma_pagamento: Optional[Dict] = None
    ) -> dict:
        """Processa o recebimento de parcelas realizados por outros sistemas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Responsável por processar recebimentos de parcelas com os dados de recebimento e forma de pagamento.

A origem do recebimento das parcelas DEVE sempre ser 0.
Serão realizadas várias validações para realização da requisição.
O valor do desconto aplicado ao recebimento será sempre do objeto de recebimento, o valor do desconto da parcela será aplicado somente pela tela de recebimento avulso.


        """
        path = "Venda/ProcessarRecebimentoParcelas"
        return self.api.post(
            path,
            json={
                "recebimento": recebimento,
                "formaPagamento": forma_pagamento,
            }
        )

    def manter_status_escrituracao_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        status_escrituracao: Optional[List[Dict]] = None
    ) -> dict:
        """Alterar status da escrituração da venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Valida usuário e suas permissões


        """
        path = "Venda/ManterStatusEscrituracaoVenda"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "venda": venda,
                "statusEscrituracao": status_escrituracao,
            }
        )

    def retorna_chaves_vendas_por_periodo(
        self,
        data_inicio: Optional[datetime] = None,
        data_fim: Optional[datetime] = None,
        status_escrituracao: Optional[bool] = None,
        status_venda: Optional[str] = None,
        lista_empresa_obra: Optional[List[Dict]] = None
    ) -> dict:
        """Consulta as chaves das vendas e comentários de status de escrituração de acordo com o período informado

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.   
Formatação das chaves de resposta: "Empresa-Obra/Venda, Empresa-Obra/Venda, Empresa-Obra/Venda"
   "01705-B1705/00159,01705-B1705/00160,01705-B1705/00161"
  

Definição de Negócio:

Permite consultar as chaves das vendas que foram inseridas, tiveram manutenção ou foram quitadas no período informado.
Se o campo "status_escrituracao" do request for marcado como "true" serão retonadas as chaves que tiveram alterações no status de escrituração.
Parâmetro opcional para request: statusVenda.  0 - Normal, 1 - Cancelada, 3 - Quitado, 4 - Em acerto, 5 Aluguel antecipado.
Parâmetros opcionais para request: codigoEmpresa e codigoObra.


        """
        path = "Venda/RetornaChavesVendasPorPeriodo"
        return self.api.post(
            path,
            json={
                "data_inicio": data_inicio,
                "data_fim": data_fim,
                "status_escrituracao": status_escrituracao,
                "statusVenda": status_venda,
                "listaEmpresaObra": lista_empresa_obra,
            }
        )

    def consultar_demonstrativo_correcao(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None,
        numero_parcela: Optional[int] = None,
        numero_parcela_geral: Optional[int] = None,
        tipo_parcela: Optional[str] = None,
        data_calculo: Optional[datetime] = None,
        data_correcao: Optional[datetime] = None,
        valor_antecipado: Optional[bool] = None
    ) -> dict:
        """Consultar demonstrativo de correção da parcela da venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite consultar demonstrativo de correção da parcela da venda.

Valida usuário e suas permissões.
Valida existência da venda.
Valida existência das parcelas.


        """
        path = "Venda/ConsultarDemonstrativoCorrecao"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "venda": venda,
                "numeroParcela": numero_parcela,
                "numeroParcelaGeral": numero_parcela_geral,
                "tipoParcela": tipo_parcela,
                "dataCalculo": data_calculo,
                "dataCorrecao": data_correcao,
                "valorAntecipado": valor_antecipado,
            }
        )

    def consultar_plano_indexadores_venda(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        venda: Optional[int] = None
    ) -> dict:
        """Consulta o plano indexador da venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Retorna informações pertinentes ao plano indexador da venda.

        """
        path = "Venda/ConsultarPlanoIndexadoresVenda"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "venda": venda,
            }
        )

    def gravar_num_contrato_financiamento(
        self,
        codg_empresa: Optional[int] = None,
        codg_obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        codg_usuario: Optional[str] = None,
        num_contrato: Optional[str] = None
    ) -> dict:
        """Altera numero de contrato da venda

        Implementation Notes:
        Definição técnica:

Altera número de contrato para uma venda.

Pré requisito:

Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
URL + /api/v{version}/Venda/GravarNumContratoFinanciamento 
  Anexos:


Exemplo Postman: [ALTERAR EXEMPLO]


        """
        path = "Venda/GravarNumContratoFinanciamento"
        return self.api.post(
            path,
            json={
                "codgEmpresa": codg_empresa,
                "codgObra": codg_obra,
                "numVenda": num_venda,
                "codgUsuario": codg_usuario,
                "numContrato": num_contrato,
            }
        )

    def consultar_empreendimentos_cliente(
        self,
        codigo_usuario: Optional[int] = None
    ) -> dict:
        """Consulta os empreendimentos que o cliente possui contrato em aberto

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Consulta os empreendimento que o cliente possui e está com situação em aberto.

        """
        path = "Venda/ConsultarEmpreendimentosCliente"
        return self.api.post(
            path,
            json={
                "codigo_usuario": codigo_usuario,
            }
        )

    def consultar_pedido_de_recebimento_uau(
        self,
        numerontk: Optional[int] = None,
        numero_pedido: Optional[int] = None
    ) -> dict:
        """Consultar o pedido de recebimento no UAU

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:

Possibilita consultar pedido de recebimento registrado no UAU por número do pedido junto a NTK ou pelo número do pedido no UAU.
As informações retornadas são referentes a como o UAU registrou o pedido internamente.
É necessário ter permissão de consulta em VEPEDIDORECEBIMENTO


        """
        path = "Venda/ConsultarPedidoDeRecebimentoUAU"
        return self.api.post(
            path,
            json={
                "NumeroNTK": numerontk,
                "NumeroPedido": numero_pedido,
            }
        )

    def consultar_unidades_compradas_por_cpf(
        self,
        cpf_cnpj: Optional[str] = None
    ) -> dict:
        """Consulta unidades compradas pelo número de CPF

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
  Possibilita consultar unidades que foram compradas por determinado CPF/CNPJ

Valida se o usuário está autenticado (logado) no sitema.
Verifica se o Cpf/Cnpj informado existe cadastrado no sistema.


        """
        path = "Venda/ConsultarUnidadesCompradasPorCPF"
        return self.api.post(
            path,
            json={
                "CpfCnpj": cpf_cnpj,
            }
        )

    def calcular_desconto_campanha_antecipacao(
        self,
        campanha_de_desconto: Optional[Dict] = None,
        parcelas_calculadas: Optional[List[Dict]] = None,
        data_calculo: Optional[datetime] = None
    ) -> dict:
        """Buscar a campanha de desconto disponível para uma campanha

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método

Definição de Negócio:
  Permite renegociar parcelas de uma venda

O usuário deverá estar autenticado e validado
Informar os dados da venda
Informar as parcelas a serem geradas
Informar as parcelas escolhidas para renegociação
Informar o plano de indexação
Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
  retorna mensagem informando a inconsistência encontrada para que seja analisada
Após as validações realiza a renegociação das parcelas
Será registrado comentário na venda sobre a renegociação realizada

VirtUau:

https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/
Anexos:

Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso


        """
        path = "Venda/CalcularDescontoCampanhaAntecipacao"
        return self.api.post(
            path,
            json={
                "CampanhaDeDesconto": campanha_de_desconto,
                "ParcelasCalculadas": parcelas_calculadas,
                "DataCalculo": data_calculo,
            }
        )

    def consultar_campanha_desconto_disponivel(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None,
        data_calculo: Optional[datetime] = None,
        data_correcao: Optional[datetime] = None
    ) -> dict:
        """Consultar campanha de desconto disponível para a venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Consulta a campanha de desconto disponível para utilização.

Valida usuário logado e permissões


        """
        path = "Venda/ConsultarCampanhaDescontoDisponivel"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "numeroVenda": numero_venda,
                "dataCalculo": data_calculo,
                "dataCorrecao": data_correcao,
            }
        )

    def consultar_desconto_antecipacao_parcela(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        num_venda: Optional[int] = None,
        num_parc: Optional[int] = None,
        numparc_ger: Optional[int] = None,
        tipo_parc: Optional[str] = None,
        data_calculo: Optional[datetime] = None,
        valor_parcela: Optional[int] = None,
        data_vencimento: Optional[datetime] = None,
        data_prorrogacao: Optional[datetime] = None,
        totalparcelas_sel: Optional[int] = None,
        antecipado: Optional[bool] = None,
        totalpara_quitacao: Optional[int] = None
    ) -> dict:
        """Calcular desconto por antecipação da parcela

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de negócio:
  Consulta o valor do desconto caso a parcela seja paga antecipadamente.

        """
        path = "Venda/ConsultarDescontoAntecipacaoParcela"
        return self.api.post(
            path,
            json={
                "empresa": empresa,
                "obra": obra,
                "num_venda": num_venda,
                "num_parc": num_parc,
                "numparc_ger": numparc_ger,
                "tipo_parc": tipo_parc,
                "data_calculo": data_calculo,
                "valor_parcela": valor_parcela,
                "data_vencimento": data_vencimento,
                "data_prorrogacao": data_prorrogacao,
                "totalparcelas_sel": totalparcelas_sel,
                "antecipado": antecipado,
                "totalpara_quitacao": totalpara_quitacao,
            }
        )

    def consultar_unidades_compradas_usr_logado(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Consulta unidades compradas pelo usuário que está logado

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
  Possibilita consultar unidades que foram compradas por determinado usuário.

Valida se o usuário está autenticado (logado) no sitema.
Usuário só pode ser do tipo pessoa.
Valida se o usuário está cadastrado para acesso no UAUWeb.


        """
        path = "Venda/ConsultarUnidadesCompradasUsrLogado"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def consultar_unidades_compradas_por_cpfcnpj(
        self,
        cpf_cnpj: Optional[str] = None
    ) -> dict:
        """Consulta unidades compradas pelo número de CPF ou CNPJ

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
  Possibilita consultar unidades que foram compradas por determinado CPF/CNPJ

Valida se o usuário está autenticado (logado) no sitema.
Verifica se o Cpf/Cnpj informado existe cadastrado no sistema.


        """
        path = "Venda/ConsultarUnidadesCompradasPorCPFCNPJ"
        return self.api.post(
            path,
            json={
                "CpfCnpj": cpf_cnpj,
            }
        )

    def gerar_pdfevolucao_saldo_devedor_financiamento(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_venda: Optional[int] = None,
        tipo_relatorio: Optional[int] = None
    ) -> dict:
        """Gerar PDF do relatório de evolução do saldo devedor do financiamento imobiliário

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.

Definição de Negócio:
  Gerar PDF do relatório de evolução do saldo devedor do financiamento imobiliário da venda em formato Base64.

        """
        path = "Venda/GerarPDFEvolucaoSaldoDevedorFinanciamento"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "numeroVenda": numero_venda,
                "tipoRelatorio": tipo_relatorio,
            }
        )

