"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class Proposta:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def gerar_boleto(
        self,
        parcelas: Optional[List[Dict]] = None,
        datacalculo: Optional[datetime] = None,
        antecipar: Optional[bool] = None,
        reajustar: Optional[bool] = None,
        excluirboletoexpirado: Optional[bool] = None,
        formacobranca: Optional[int] = None,
        boletosacadodetalhado: Optional[bool] = None,
        carnetresvias: Optional[bool] = None,
        validardadospendentes: Optional[bool] = None,
        acrescentarresiduo: Optional[bool] = None,
        usarpadraoboletoavulso: Optional[bool] = None,
        agruparparcelas: Optional[bool] = None,
        valor_boleto: Optional[int] = None,
        padrao_cobranca: Optional[int] = None,
        excluir_boletos_existentes: Optional[bool] = None
    ) -> dict:
        """Gerar boleto

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Retorna string do tipo Base64. Para obter o boleto utilize um conversor: Base64 para PDF.
Definição de Negócio:

Gera boleto com os dados informados na request.
O usuário autenticado deve ter permissão de inclusão no programa de permissão VEBOLETOAVULSO.
Para gerar boleto parcial é necessário informar a propriedade ValorBoleto.
Não pode ser um valor negativo nem inferior a 0,01 centavo.
Se informar um valor igual ao valor total das parcelas enviadas, será gerado um boleto normal.
Se informar um valor menor que o valor total da parcela enviada, será gerado um boleto parcial.
Apenas uma parcela das enviadas deverá ser parcial
Não será gerado boleto caso informe um valor que não cubra todas as parcelas enviadas
Irá validar se as parcelas enviadas podem gerar o boleto parcial de acordo com a regra de dias para vencimento.


Será possível gerar boleto parcial somente para parcelas de uma única empresa, obra e proposta.
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




        """
        path = "Proposta/GerarBoleto"
        return self.api.post(
            path,
            json={
                "parcelas": parcelas,
                "datacalculo": datacalculo,
                "antecipar": antecipar,
                "reajustar": reajustar,
                "excluirboletoexpirado": excluirboletoexpirado,
                "formacobranca": formacobranca,
                "boletosacadodetalhado": boletosacadodetalhado,
                "carnetresvias": carnetresvias,
                "validardadospendentes": validardadospendentes,
                "acrescentarresiduo": acrescentarresiduo,
                "usarpadraoboletoavulso": usarpadraoboletoavulso,
                "agruparparcelas": agruparparcelas,
                "ValorBoleto": valor_boleto,
                "PadraoCobranca": padrao_cobranca,
                "ExcluirBoletosExistentes": excluir_boletos_existentes,
            }
        )

    def expirar_boletos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """Excluir boletos expirados de proposta e venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Exclui todos os boletos expirados, propostas e vendas, de acordo com a configuração da empresa.


        """
        path = "Proposta/ExpirarBoletos"
        return self.api.post(
            path,
            json={
                "Detalhe": detalhe,
                "Mensagem": mensagem,
                "Descricao": descricao,
            }
        )

    def gravar_proposta(
        self,
        proposta: Optional[Dict] = None,
        proposta_pacelas_geradas: Optional[List[Dict]] = None,
        proposta_param_modelo_parcelas: Optional[List[Dict]] = None,
        proposta_param_parcelas: Optional[List[Dict]] = None,
        proposta_comissao: Optional[List[Dict]] = None,
        proposta_comissao_parc: Optional[List[Dict]] = None,
        proposta_itens: Optional[List[Dict]] = None,
        proposta_cliente: Optional[List[Dict]] = None,
        proposta_plano_index: Optional[List[Dict]] = None,
        proposta_seguro: Optional[List[Dict]] = None,
        proposta_custas_retencao: Optional[Dict] = None,
        proposta_custas_retencao_parcela: Optional[List[Dict]] = None,
        proposta_cap: Optional[List[Dict]] = None,
        proposta_shopping: Optional[Dict] = None
    ) -> dict:
        """Grava os dados da proposta de venda

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Definição de Negócio:

O usuário autenticado deve ter permissão de inclusão e alteração em CRPROPOSTAVENDA.
  1.1 Se não precisar de alterar propostas, basta ter apenas de inclusão.
A alteração de uma proposta é feita respeitando todas informações enviadas, ou seja, deve reeniviar o mesmo objeto da proposta totalmente para alterar apenas 1 campo por exemplo.
  2.1 O sistema identifica que é uma alteração de proposta quando o código da proposta está preenchido [numProposta].
A propriedade de propostaPacelasGeradas, Não precisa ser preenchida pois suas informações serão regeradas pela API.
As validações de propriedades obrigatórias podem validar para o tipo de proposta que está sendo recebido.
  5.1 Os campos marcados como obrigatórios são os campos obrigatórios gerais, para gravar o básico de uma proposta de venda.
  5.1.1 Aluguel, aluguel garantido e aluguel shopping, tem mais propriedades obrigatórias ou até mesmo opcionais.
Mais informações sobre as propriedades e como elas devem ser preenchidas estão na documentação dos models.
Tornou-se obsoleto ó código da hierarquia, agora pelo numeroComissao(modelo) nos iremos achar a hierarquia e validar.
O cálculo da comissão é feito da seguinte forma.
Ao informar a propriedade percentualSegundoJuros ou a propriedade dataSegundoJuros, ambas serão obrigatórias em propostaParamParcelas e propostaParamModeloParcelas.
O parâmetro opcional TermoReserva, quando preenchido, precisa ter o valor 0 ou 1. (0-Não, 1-Sim).
  Obs: Arredondar o valor calculado para duas casas decimais.
Propriedade propostaItens : Valor geral de comissão.
- Valor da comissão = (Preço do produto x quantidade x Porcentual da comissão) / 100.
      - 81831,038 = (492.37 x 2936.17 x 5.660376) / 100.
      - Após o cálculo o valor da comissão é arredondado considerando duas casas decimais depois da virgula. Valor da comissão = 81831.04.
      - O Preço do produto, quantidade e Porcentual da comissão são referentes aos seguintes campos respectivamente 'precoProduto', 'qtdeProduto' e 'porcentualComissao'.
      - Dados referente ao objeto 'propostaItens'.
  Propriedade propostaComissao : Valor da comissão.             
- Valor da comissão = (Valor da comissão x Porcentual da comissão)/100.
      - 27822,5536  = (81831.04 x 34.000000) / 100.
      - O Valor da comissão e Porcentual da comissão são referentes aos seguintes campos respectivamente 'valorComissao' e 'PorcComissao'.
      - Dados referente ao objeto 'propostaComissao'.
  - O resultado do cálculo da comissão é referente ao campo 'valorComissao' e também é o valor que deve ser informado.
  Planilha com exemplo do cálculo do valor total e comissão:
  https://drive.google.com/file/d/14IW7aoBkT91FFOJBB5LVth-eerIxnqLP/view
Anexos:
  Exemplo do body json: 
  https://ajuda.globaltec.com.br/wp-content/uploads/2019/12/exemploGravarProposta.txt



        """
        path = "Proposta/GravarProposta"
        return self.api.post(
            path,
            json={
                "proposta": proposta,
                "propostaPacelasGeradas": proposta_pacelas_geradas,
                "propostaParamModeloParcelas": proposta_param_modelo_parcelas,
                "propostaParamParcelas": proposta_param_parcelas,
                "propostaComissao": proposta_comissao,
                "propostaComissaoParc": proposta_comissao_parc,
                "propostaItens": proposta_itens,
                "propostaCliente": proposta_cliente,
                "propostaPlanoIndex": proposta_plano_index,
                "propostaSeguro": proposta_seguro,
                "propostaCustasRetencao": proposta_custas_retencao,
                "propostaCustasRetencaoParcela": proposta_custas_retencao_parcela,
                "propostaCap": proposta_cap,
                "propostaShopping": proposta_shopping,
            }
        )

    def cancelar_proposta(
        self,
        numero_proposta: Optional[int] = None,
        cancelar_vendida: Optional[bool] = None,
        excluir_boletos: Optional[bool] = None
    ) -> dict:
        """Cancelar determinada proposta

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

É obrigatório informar o código da proposta.
Caso ela esteja vendida, deve informar se é para cancela-la ou não.
A proposta não pode estar cancelada ou expirada
Ao enviar ExcluirBoletos como TRUE, irá excluir os boletos ativos da proposta e permitir o cancelamento.


        """
        path = "Proposta/CancelarProposta"
        return self.api.post(
            path,
            json={
                "numeroProposta": numero_proposta,
                "cancelarVendida": cancelar_vendida,
                "ExcluirBoletos": excluir_boletos,
            }
        )

    def renegociar_proposta(
        self,
        num_proposta: Optional[int] = None,
        proposta_parcelas_geradas: Optional[List[Dict]] = None,
        parcelas_selecionadas: Optional[List[Dict]] = None,
        valor_desconto: Optional[int] = None,
        valor_acrescimo: Optional[int] = None,
        num_padrao_cobranca: Optional[int] = None,
        termo_reserva: Optional[int] = None
    ) -> dict:
        """Realiza a renegociação de parcelas de uma proposta de venda com as validações necessárias

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite renegociar parcelas de uma proposta

O usuário deverá estar autenticado e validado.
Informar os dados da proposta.
Informar as parcelas a serem geradas.
Informar as parcelas escolhidas para renegociação.
Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
  retorna mensagem informando a inconsistência encontrada para que seja analisada.
Após as validações realiza a renegociação das parcelas.
Será registrado comentário na proposta sobre a renegociação realizada.
O parâmetro opcional TermoReserva, quando preenchido, precisa ter o valor 0 ou 1. (0-Não, 1-Sim).


        """
        path = "Proposta/RenegociarProposta"
        return self.api.post(
            path,
            json={
                "NumProposta": num_proposta,
                "PropostaParcelasGeradas": proposta_parcelas_geradas,
                "ParcelasSelecionadas": parcelas_selecionadas,
                "ValorDesconto": valor_desconto,
                "ValorAcrescimo": valor_acrescimo,
                "NumPadraoCobranca": num_padrao_cobranca,
                "TermoReserva": termo_reserva,
            }
        )

    def consultar_proposta_por_id(
        self,
        num_proposta: Optional[int] = None,
        valor_antecipado: Optional[int] = None,
        data_calculo: Optional[datetime] = None
    ) -> dict:
        """Consulta dados da proposta por ID

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Definição de Negócio:

Busca determinada proposta filtrando por ID.
Valida usuário e suas permissões.
O campo valorAntecipado e dataCalculo são opcionais, mas caso informado algum deles, precisa informar valor nos dois campos.
valorAntecipado deve ser preenchido com 0 para falso ou 1 para verdadeiro.




        """
        path = "Proposta/ConsultarPropostaPorId"
        return self.api.post(
            path,
            json={
                "numProposta": num_proposta,
                "valorAntecipado": valor_antecipado,
                "dataCalculo": data_calculo,
            }
        )

    def vincular_arquivo_proposta(
        self,
        arquivo: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        proposta: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """Vincular arquivo a proposta

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Realiza a vinculadção de arquivo com determinada proposta.


        """
        path = "Proposta/VincularArquivoProposta"
        return self.api.post(
            path,
            json={
                "arquivo": arquivo,
                "nome_arquivo": nome_arquivo,
                "proposta": proposta,
                "usuario": usuario,
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
        """Gravar pedido de recebimento  junto a NTK

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

É obrigatório ter o ambiente de integração com a NTK configurado, só após o registro junto a eles que o registro será gerado no UAU.
É necessário ter permissão de inclusão no programa VEPEDIDORECEBIMENTO
Não é possível gerar pedido para receber todas as parcelas de uma proposta, o sistema irá validar juntamente com boletos gerados.
Somente propostas com status 2 - confirmadas podem gerar pedido de recebimento.
É necessário que o prospect esteja migrado para geração do pedido.


        """
        path = "Proposta/GravarPedidoDeRecebimento"
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

Definição de Negócio:

Pedidos que já tiveram um recebimento parcial junto a NTK, não são cancelados. (trava na NTK).
É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO


        """
        path = "Proposta/CancelarPedidoDeRecebimento"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "Pedido": pedido,
            }
        )

    def consultar_hierarquia_parcelas(
        self,
        codigo: Optional[int] = None
    ) -> dict:
        """Consulta parcelas a desconsiderar que estão vinculadas a hierarquia informada

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

        """
        path = "Proposta/ConsultarHierarquiaParcelas"
        return self.api.post(
            path,
            json={
                "codigo": codigo,
            }
        )

    def atualizar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """Atualizar o(s) pedido(s) de recebimento  junto a NTK

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:

Serão atualizadas as parcelas do pedido que ainda estão com status: 0 - Em aberto 
É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO


        """
        path = "Proposta/AtualizarPedidoDeRecebimento"
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
        """Consultar o pedido de recebimento  junto a NTK

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:

Possibilita consultar pedido de recebimento junto a NTK
As informações retornadas serão informações do pedido na NTK.


        """
        path = "Proposta/ConsultarPedidoDeRecebimento"
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
        """Processa o recebimento de parcelas referentes a propostas

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Processa as parcelas recebidas
O valor do desconto aplicado ao recebimento será sempre do objeto de recebimento, o valor do desconto da parcela será aplicado somente pela tela de recebimento avulso.
Não é possível realizar recebimento para todas as parcelas da proposta! Ao realizar o recebimento de parcelas o sistema verifica se possui boleto gerado e pedido de recebimento para outra parcelas da proposta.


        """
        path = "Proposta/ProcessarRecebimentoParcelas"
        return self.api.post(
            path,
            json={
                "recebimento": recebimento,
                "formaPagamento": forma_pagamento,
            }
        )

    def consultar_pedido_de_recebimento_uau(
        self,
        numerontk: Optional[int] = None,
        numero_pedido: Optional[int] = None
    ) -> dict:
        """Consultar o pedido de recebimento no UAU.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:

Possibilita consultar pedido de recebimento regisrado no UAU por número do pedido junto a NTK ou pelo número do pedido no UAU.
As informações retornadas são referentes a como o UAU registrou o pedido internamente.


        """
        path = "Proposta/ConsultarPedidoDeRecebimentoUAU"
        return self.api.post(
            path,
            json={
                "NumeroNTK": numerontk,
                "NumeroPedido": numero_pedido,
            }
        )

    def retornar_valores_estrutura_comissao(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        codigo_vendedor: Optional[int] = None,
        codigo_hierarquia: Optional[int] = None,
        codigo_comissao: Optional[int] = None,
        valor_total_comissao: Optional[int] = None,
        valor_comissao_direta: Optional[int] = None,
        produtos: Optional[List[Dict]] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """Retorna a comissão calculada

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Realiza cálculos da comissão e retorna os valores
Parâmetros:
Grupo de parcelas
Estrutura de comissão




        """
        path = "Proposta/RetornarValoresEstruturaComissao"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "codigoVendedor": codigo_vendedor,
                "codigoHierarquia": codigo_hierarquia,
                "codigoComissao": codigo_comissao,
                "valorTotalComissao": valor_total_comissao,
                "valorComissaoDireta": valor_comissao_direta,
                "produtos": produtos,
                "parcelas": parcelas,
            }
        )

    def retorna_valor_comissao_deducao_parcelas(
        self,
        codigo_hierarquia: Optional[int] = None,
        codigo_modelo_venda: Optional[int] = None,
        valor_total_produto: Optional[int] = None,
        valor_total_comissao: Optional[int] = None,
        valor_total_comissao_direta: Optional[int] = None,
        parcelas_geradas: Optional[List[Dict]] = None,
        porcentagem_comissao: Optional[int] = None,
        valor_item_proposta: Optional[int] = None
    ) -> dict:
        """Retorna o valor da comissão deduzido

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Calcula o valor da comissão deduzido.

        """
        path = "Proposta/RetornaValorComissaoDeducaoParcelas"
        return self.api.post(
            path,
            json={
                "CodigoHierarquia": codigo_hierarquia,
                "CodigoModeloVenda": codigo_modelo_venda,
                "ValorTotalProduto": valor_total_produto,
                "ValorTotalComissao": valor_total_comissao,
                "ValorTotalComissaoDireta": valor_total_comissao_direta,
                "ParcelasGeradas": parcelas_geradas,
                "PorcentagemComissao": porcentagem_comissao,
                "ValorItemProposta": valor_item_proposta,
            }
        )

    def traduzir_request_parcelas_geradas(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        path = "/api/Proposta/TraduzirRequestParcelasGeradas"
        return self.api.post(
            path,
            json=parameters if parameters is not None else {}
        )

    def traduzir_request_parcelas_selecionadas(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        path = "/api/Proposta/TraduzirRequestParcelasSelecionadas"
        return self.api.post(
            path,
            json=parameters if parameters is not None else {}
        )

