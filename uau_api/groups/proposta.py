from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

import requests
class Proposta:
    def __init__(self, api: RequestsApi):
        """Initialize with API client

        Args:
            api: The API client instance
        """
        self.api = api

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
        """
        
        Endpoint: `Proposta/GerarBoleto`
        HTTP Method: `POST`
        
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
        
        
        
        
        
        Args:
            parcelas (List[Dict[str, Any]]): The parcelas
            datacalculo (datetime): The datacalculo
            antecipar (int): The antecipar
            reajustar (int): The reajustar
            excluirboletoexpirado (int): The excluirboletoexpirado
            formacobranca (int): The formacobranca
            boletosacadodetalhado (int): The boletosacadodetalhado
            carnetresvias (int): The carnetresvias
            validardadospendentes (int): The validardadospendentes
            acrescentarresiduo (int): The acrescentarresiduo
            usarpadraoboletoavulso (int): The usarpadraoboletoavulso
            agruparparcelas (int): The agruparparcelas
            ValorBoleto (int): The valor boleto
            PadraoCobranca (int): The padrao cobranca
            ExcluirBoletosExistentes (int): The excluir boletos existentes
        
        Parameter Structure:
        
            {
                "parcelas": [
                    {
                        "empresa": 0,
                        "obra": "string",
                        "numproposta": 0,
                        "numparcela": 0,
                        "tipoparcela": "string",
                        "numparcelagerada": 0,
                        "valordescontoantecipacao": 0
                    }
                ],
                "datacalculo": "2025-04-23T13:46:14.143Z",
                "antecipar": true,
                "reajustar": true,
                "excluirboletoexpirado": true,
                "formacobranca": 0,
                "boletosacadodetalhado": true,
                "carnetresvias": true,
                "validardadospendentes": true,
                "acrescentarresiduo": true,
                "usarpadraoboletoavulso": true,
                "agruparparcelas": true,
                "ValorBoleto": 0,
                "PadraoCobranca": 0,
                "ExcluirBoletosExistentes": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._gerar_boleto(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/GerarBoleto"
        try:
            response = self.api.post(
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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def expirar_boletos(
        self,
        detalhe: Optional[str] = None,
        mensagem: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/ExpirarBoletos`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Exclui todos os boletos expirados, propostas e vendas, de acordo com a configuração da empresa.
        
        
        
        Args:
            Detalhe (str): The detalhe
            Mensagem (str): The mensagem
            Descricao (str): The descricao
        
        Parameter Structure:
        
            {
                "Detalhe": "string",
                "Mensagem": "string",
                "Descricao": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._expirar_boletos(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/ExpirarBoletos"
        try:
            response = self.api.post(
                path,
                json={
                    "Detalhe": detalhe,
                    "Mensagem": mensagem,
                    "Descricao": descricao,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

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
        """
        
        Endpoint: `Proposta/GravarProposta`
        HTTP Method: `POST`
        
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
        
        
        
        
        Args:
            proposta (Dict[str, Any]): The proposta
            propostaPacelasGeradas (List[Dict[str, Any]]): The pacelas geradas
            propostaParamModeloParcelas (List[Dict[str, Any]]): The param modelo parcelas
            propostaParamParcelas (List[Dict[str, Any]]): The param parcelas
            propostaComissao (List[Dict[str, Any]]): The comissao
            propostaComissaoParc (List[Dict[str, Any]]): The comissao parc
            propostaItens (List[Dict[str, Any]]): The itens
            propostaCliente (List[Dict[str, Any]]): The cliente
            propostaPlanoIndex (List[Dict[str, Any]]): The plano index
            propostaSeguro (List[Dict[str, Any]]): The seguro
            propostaCustasRetencao (Dict[str, Any]): The custas retencao
            propostaCustasRetencaoParcela (List[Dict[str, Any]]): The custas retencao parcela
            propostaCap (List[Dict[str, Any]]): The cap
            propostaShopping (Dict[str, Any]): The shopping
        
        Parameter Structure:
        
            {
                "proposta": {
                    "numProposta": 0,
                    "codigoEmpresa": 0,
                    "codigoObra": "string",
                    "tipoContrato": 0,
                    "dataProposta": "2025-04-23T13:46:14.152Z",
                    "codigoCliente": 0,
                    "codigoVendedor": 0,
                    "valorTotalProposta": 0,
                    "desconto": 0,
                    "acrescimo": 0,
                    "periodoValidade": 0,
                    "usuarioCadastro": "string",
                    "dataCadastro": "2025-04-23T13:46:14.152Z",
                    "codigoHierarquia": 0,
                    "numComissao": 0,
                    "juros": 0,
                    "multa": 0,
                    "jurosContrato": 0,
                    "reajusteAnual": 0,
                    "gerarResiduo": 0,
                    "qtdeDiasCarenciaAtraso": 0,
                    "numMesRetroagirIdx": 0,
                    "correcaoAtraso": 0,
                    "correcaoProRata": 0,
                    "cobrarTaxaBoleto": 0,
                    "carenciaAtrasoCorrecao": 0,
                    "antecipaCorrecao": 0,
                    "cobrarJurosRecPosChave": 0,
                    "zerarCorrecaoNegativa": true,
                    "antecipaJurosLinear": true,
                    "juroAtrasoMensal": true,
                    "correcaoCrescente": true,
                    "correcaoAtrasoPerson": true,
                    "jurosAnual": 0,
                    "periodoMesJuros": 0,
                    "multaFracionada": true,
                    "periodoMesReajuste": 0,
                    "anteciparCorrecaoAniverCont": true,
                    "hitoricoLancamento": "string",
                    "historicoParcRecebidas": "string",
                    "historicoLancJurosCorrecao": "string",
                    "usurAprovouProposta": "string",
                    "dataAprovouProposta": "2025-04-23T13:46:14.152Z",
                    "usrCancelouProposta": "string",
                    "datacancelamentoProposta": "2025-04-23T13:46:14.152Z",
                    "usrConfirmouProposta": "string",
                    "dataConfirmacaoProposta": "2025-04-23T13:46:14.152Z",
                    "statusAprovacaoProposta": 0,
                    "statusProposta": 0,
                    "planoIndexador": 0,
                    "dataBaseResiduo": "2025-04-23T13:46:14.152Z",
                    "valorProvisaoLongoPrazo": 0,
                    "valorProvisaoCurtoPrazo": 0,
                    "codVeiculoDivulgacao": 0,
                    "numFinalidade": 0,
                    "spedPisCofins": true,
                    "observacao": "string",
                    "procOportunidade": 0,
                    "AteHabiteSe": true,
                    "diaRepasseAluguel": 0,
                    "cobrarImposto": 0,
                    "cobrarTaxaAdmin": 0,
                    "dataIniContrato": "2025-04-23T13:46:14.152Z",
                    "dataFimContrato": "2025-04-23T13:46:14.152Z",
                    "fianca1": "string",
                    "fianca2": "string",
                    "fianca3": "string",
                    "valorFianca": 0,
                    "dataFianca": "2025-04-23T13:46:14.152Z",
                    "nomeSeguradora": "string",
                    "numApoliceSeguroIncendio": "string",
                    "valorSeguroIncendio": 0,
                    "dataSeguroIncendio": "2025-04-23T13:46:14.152Z",
                    "tipoFianca": 0,
                    "atividade": 0,
                    "numContratoCEF": "string",
                    "numPadraoCobranca": 0,
                    "numServicoFiscal": 0,
                    "tributadoRET": true,
                    "numTributacaoRET": 0,
                    "UtilizarDescontoUltimaParc": true,
                    "TipoContratoRec": 0,
                    "MetodoAmortizacaoRec": 0,
                    "IndicePrecoPreObraRec": 0,
                    "IndicePrecoPosObraRec": 0,
                    "AplicacaoJurosRec": 0,
                    "JurosAnualPercentualRec": 0,
                    "TermoReserva": 0
                },
                "propostaPacelasGeradas": [
                    {
                        "chaveParcelaGerada": 0,
                        "numeroParcela": 0,
                        "dataVencimento": "2025-04-23T13:46:14.152Z",
                        "valorParcela": 0,
                        "tipoParcela": "string",
                        "planoIndexReajuste": "string",
                        "jurosParcela": 0,
                        "dataJurosParcela": "2025-04-23T13:46:14.152Z",
                        "dataPlanoIndexParcela": "2025-04-23T13:46:14.152Z",
                        "valorReajustadoParcela": 0,
                        "tipoVencimentoParcela": "string",
                        "amortizacaoParcela": 0,
                        "beginEndParcela": 0,
                        "qtdTotalParcela": 0,
                        "dataIncioParcela": "2025-04-23T13:46:14.152Z",
                        "planoIndexParcela": 0,
                        "grupoParcela": 0,
                        "qtdTotalGrupo": 0,
                        "jurosComJuros": 0,
                        "dataSegundoJuros": "2025-04-23T13:46:14.152Z",
                        "percentualSegundoJuros": 0,
                        "carenciaAtraso": 0,
                        "carenciaAtrasoCorrecao": 0,
                        "cobrarJurosProRata": 0,
                        "cobrarJurosProRataPrimeiroMes": 0,
                        "dataInicioAluguel": "2025-04-23T13:46:14.152Z",
                        "cobrarTaxaAdministrativa": 0,
                        "cap": "string",
                        "capCorrecaoAtraso": "string",
                        "capJuros": "string",
                        "capCorrecao": "string",
                        "capMulta": "string",
                        "capJurosAtraso": "string",
                        "capAcrescimo": "string",
                        "capDesconto": "string",
                        "capDescontoAntecipado": "string",
                        "capTaxaBoleto": "string",
                        "capDescontoCusta": "string",
                        "capRepasse": "string",
                        "capDescontoCondicional": "string",
                        "tipoParcelamento": 0,
                        "NumCtp": 0,
                        "OrigemCusta": 0,
                        "cobrarMulta": 0,
                        "cobrarJurosAtraso": 0,
                        "cobrarImposto": 0,
                        "cobrarCorrecao": 0,
                        "cobrarCPMF": 0,
                        "repassarLocador": 0,
                        "tipoSeguro": 0,
                        "meioPreferencialRecebimento": 0
                    }
                ],
                "propostaParamModeloParcelas": [
                    {
                        "numParametro": 0,
                        "numParcela": 0,
                        "valorParcela": 0,
                        "valorTotalParcela": 0,
                        "percentualParcela": 0,
                        "dataParcela": "2025-04-23T13:46:14.152Z",
                        "dataReajuste": "2025-04-23T13:46:14.152Z",
                        "dataJuros": "2025-04-23T13:46:14.152Z",
                        "juros": 0,
                        "dataSegundoJuros": "2025-04-23T13:46:14.152Z",
                        "percentualSegundoJuros": 0,
                        "tipoParcela": "string",
                        "frequencia": "string",
                        "amortizacao": 0,
                        "beginEnd": 0,
                        "reajuste": "string",
                        "JurosComJuros": 0,
                        "planoIndexParcela": 0,
                        "tipoValor": 0,
                        "carenciaAtraso": 0,
                        "carenciaAtrasoCorrecao": 0,
                        "cobrarJurosProRata": 0,
                        "cobrarJurosProRataPrimeiroMes": 0,
                        "competencia": 0,
                        "numModeloVenda": 0,
                        "tipoContrato": 0,
                        "cap": "string",
                        "capCorrecaoAtraso": "string",
                        "capJuros": "string",
                        "capCorrecao": "string",
                        "capMulta": "string",
                        "capJurosAtraso": "string",
                        "capAcrescimo": "string",
                        "capDesconto": "string",
                        "capDescontoAntecipado": "string",
                        "capTaxaBoleto": "string",
                        "capDescontoCusta": "string",
                        "capRepasse": "string",
                        "capDescontoCondicional": "string",
                        "tipoParcelamento": 0,
                        "NumCtp": 0,
                        "OrigemCusta": 0,
                        "cobrarMulta": 0,
                        "cobrarJurosAtraso": 0,
                        "cobrarImposto": 0,
                        "cobrarCorrecao": 0,
                        "cobrarCPMF": 0,
                        "repassarLocador": 0,
                        "tipoSeguro": 0,
                        "CobrarTaxaAdm": 0
                    }
                ],
                "propostaParamParcelas": [
                    {
                        "NumParametro": 0,
                        "tipoParcela": "string",
                        "numParcela": 0,
                        "valorParcela": 0,
                        "valorTotalParcela": 0,
                        "percentualParcela": 0,
                        "dataParcela": "2025-04-23T13:46:14.152Z",
                        "dataJuros": "2025-04-23T13:46:14.152Z",
                        "dataReajuste": "2025-04-23T13:46:14.152Z",
                        "juros": 0,
                        "dataSegundoJuros": "2025-04-23T13:46:14.152Z",
                        "percentualSegundoJuros": 0,
                        "frequencia": "string",
                        "reajuste": "string",
                        "amortizacao": 0,
                        "beginEnd": 0,
                        "jurosComJuros": 0,
                        "planoIndexParcela": 0,
                        "tipoValor": 0,
                        "carenciaAtraso": 0,
                        "carenciaAtrasoCorrecao": 0,
                        "cobrarJurosProRata": 0,
                        "cobrarJurosProRataPrimeiroMes": 0,
                        "competencia": 0
                    }
                ],
                "propostaComissao": [
                    {
                        "numComissao": 0,
                        "codPessoa": 0,
                        "PorcComissao": 0,
                        "valorComissao": 0,
                        "tipoPagamento": 0,
                        "tipoLancamento": 0,
                        "sobreRecebimento": 0,
                        "regraLiberacao": 0,
                        "gerarProcesso": 0,
                        "indicaCaptador": 0,
                        "codigoCargo": "string",
                        "parteHierarquia": true,
                        "gerarComissao": true,
                        "valorAcrescimo": 0,
                        "usrAcrescimo": "string",
                        "dataAcrescimo": "2025-04-23T13:46:14.152Z",
                        "valorDesconto": 0,
                        "usrDesconto": "string",
                        "dataDesconto": "2025-04-23T13:46:14.152Z"
                    }
                ],
                "propostaComissaoParc": [
                    {
                        "NumComissaoParc": 0,
                        "NumeroParcela": 0,
                        "porcentagemRecebimento": 0,
                        "porcentualComissao": 0,
                        "FormaLiberacao": 0,
                        "NumeroParcelaProposta": 0,
                        "TipoParcela": "string",
                        "CodigoStatusescritura": 0
                    }
                ],
                "propostaItens": [
                    {
                        "codEmpresa": 0,
                        "codProduto": 0,
                        "NumPersonalizacao": 0,
                        "precoProduto": 0,
                        "qtdeProduto": 0,
                        "Contrato": 0,
                        "itemProduto": "string",
                        "valComissaoDireta": 0,
                        "porcentualComissao": 0
                    }
                ],
                "propostaCliente": [
                    {
                        "numCliente": 0,
                        "tipocliente": 0,
                        "porcTitular": 0,
                        "emiteBoleto": true
                    }
                ],
                "propostaPlanoIndex": [
                    {
                        "dataReajuste": "2025-04-23T13:46:14.153Z",
                        "numGrupoPlanoIdx": 0,
                        "codigoPlanoIndexador": "string"
                    }
                ],
                "propostaSeguro": [
                    {
                        "tipoSeguro": 0,
                        "porTaxa": true,
                        "valor": 0,
                        "usuarioCadastro": "string",
                        "dataCadastro": "2025-04-23T13:46:14.153Z",
                        "cap": "string"
                    }
                ],
                "propostaCustasRetencao": {
                    "valorRetencao": 0
                },
                "propostaCustasRetencaoParcela": [
                    {
                        "NumParcela": "string",
                        "codigoCap": "string",
                        "dataVencimento": "2025-04-23T13:46:14.153Z",
                        "valorRetencao": 0,
                        "cobrarTaxaAdm": 0,
                        "CobrarCPMF": 0
                    }
                ],
                "propostaCap": [
                    {
                        "tipoCap": 0,
                        "codigoCAP": "string"
                    }
                ],
                "propostaShopping": {
                    "codigoAtividade": "string",
                    "tipoContrato": 0,
                    "basePercentualAluguel": 0,
                    "area": 0,
                    "frente": 0,
                    "profundidade": 0,
                    "numLocal": 0,
                    "percententualAluguel": 0,
                    "ReceitaInformada": 0,
                    "PercentualFPP": 0
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._gravar_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/GravarProposta"
        try:
            response = self.api.post(
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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def cancelar_proposta(
        self,
        numero_proposta: Optional[int] = None,
        cancelar_vendida: Optional[bool] = None,
        excluir_boletos: Optional[bool] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/CancelarProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        É obrigatório informar o código da proposta.
        Caso ela esteja vendida, deve informar se é para cancela-la ou não.
        A proposta não pode estar cancelada ou expirada
        Ao enviar ExcluirBoletos como TRUE, irá excluir os boletos ativos da proposta e permitir o cancelamento.
        
        
        
        Args:
            numeroProposta (int): The proposta
            cancelarVendida (int): The vendida
            ExcluirBoletos (int): The excluir boletos
        
        Parameter Structure:
        
            {
                "numeroProposta": 0,
                "cancelarVendida": true,
                "ExcluirBoletos": true
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._cancelar_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/CancelarProposta"
        try:
            response = self.api.post(
                path,
                json={
                    "numeroProposta": numero_proposta,
                    "cancelarVendida": cancelar_vendida,
                    "ExcluirBoletos": excluir_boletos,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

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
        """
        
        Endpoint: `Proposta/RenegociarProposta`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            NumProposta (int): The num proposta
            PropostaParcelasGeradas (List[Dict[str, Any]]): The proposta parcelas geradas
            ParcelasSelecionadas (List[Dict[str, Any]]): The parcelas selecionadas
            ValorDesconto (int): The valor desconto
            ValorAcrescimo (int): The valor acrescimo
            NumPadraoCobranca (int): The num padrao cobranca
            TermoReserva (int): The termo reserva
        
        Parameter Structure:
        
            {
                "NumProposta": 0,
                "PropostaParcelasGeradas": [
                    {
                        "Numero": 0,
                        "Tipo": "string",
                        "Valor": 0,
                        "DtVencimento": "2025-04-23T13:46:14.182Z",
                        "DtParc": "2025-04-23T13:46:14.182Z",
                        "Amortizacao": 0,
                        "BeginEnd": 0,
                        "NumGrupo": 0,
                        "TotalParcGrupo": 0,
                        "Frequencia": "string",
                        "DtIniJuros": "2025-04-23T13:46:14.182Z",
                        "TxJuros": 0,
                        "DataSegJuros": "2025-04-23T13:46:14.183Z",
                        "TxSegJuros": 0,
                        "DtIniIdx": "2025-04-23T13:46:14.183Z",
                        "IdxReaj": "string",
                        "GrupoIdx": 0,
                        "DtJurosComJuros": 0,
                        "CobrarJurosProRata": 0,
                        "CobrarJurosProRataPrimeiroMes": 0,
                        "CarenciaAtraso": 0,
                        "CarenciaAtrasoCorrecao": 0,
                        "TotalParc": 0,
                        "MeioPreferencialRecebimento": 0
                    }
                ],
                "ParcelasSelecionadas": [
                    {
                        "NumParc": 0,
                        "NumParcGer": 0,
                        "Tipo": "string"
                    }
                ],
                "ValorDesconto": 0,
                "ValorAcrescimo": 0,
                "NumPadraoCobranca": 0,
                "TermoReserva": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._renegociar_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/RenegociarProposta"
        try:
            response = self.api.post(
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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_proposta_por_id(
        self,
        num_proposta: Optional[int] = None,
        valor_antecipado: Optional[int] = None,
        data_calculo: Optional[datetime] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/ConsultarPropostaPorId`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        Definição de Negócio:
        
        Busca determinada proposta filtrando por ID.
        Valida usuário e suas permissões.
        O campo valorAntecipado e dataCalculo são opcionais, mas caso informado algum deles, precisa informar valor nos dois campos.
        valorAntecipado deve ser preenchido com 0 para falso ou 1 para verdadeiro.
        
        
        
        
        
        Args:
            numProposta (int): The proposta
            valorAntecipado (int): The antecipado
            dataCalculo (datetime): The calculo
        
        Parameter Structure:
        
            {
                "numProposta": 0,
                "valorAntecipado": 0,
                "dataCalculo": "2025-04-23T13:46:14.210Z"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._consultar_proposta_por_id(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/ConsultarPropostaPorId"
        try:
            response = self.api.post(
                path,
                json={
                    "numProposta": num_proposta,
                    "valorAntecipado": valor_antecipado,
                    "dataCalculo": data_calculo,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def vincular_arquivo_proposta(
        self,
        arquivo: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        proposta: Optional[int] = None,
        usuario: Optional[str] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/VincularArquivoProposta`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Realiza a vinculadção de arquivo com determinada proposta.
        
        
        
        Args:
            arquivo (str): The arquivo
            nome_arquivo (str): The nome_arquivo
            proposta (int): The proposta
            usuario (str): The usuario
        
        Parameter Structure:
        
            {
                "arquivo": "string",
                "nome_arquivo": "string",
                "proposta": 0,
                "usuario": "string"
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._vincular_arquivo_proposta(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/VincularArquivoProposta"
        try:
            response = self.api.post(
                path,
                json={
                    "arquivo": arquivo,
                    "nome_arquivo": nome_arquivo,
                    "proposta": proposta,
                    "usuario": usuario,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

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
        """
        
        Endpoint: `Proposta/GravarPedidoDeRecebimento`
        HTTP Method: `POST`
        
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
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            NumContrato (int): The num contrato
            Estabelecimento (str): The estabelecimento
            FormaPgto (int): The forma pgto
            QtdeParcelas (int): The qtde parcelas
            DataCalculo (datetime): The data calculo
            ValorLiquido (int): The valor liquido
            TipoRecebimento (int): The tipo recebimento
            Antecipacao (int): The antecipacao
            Parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "NumContrato": 0,
                "Estabelecimento": "string",
                "FormaPgto": 0,
                "QtdeParcelas": 0,
                "DataCalculo": "2025-04-23T13:46:14.224Z",
                "ValorLiquido": 0,
                "TipoRecebimento": 0,
                "Antecipacao": true,
                "Parcelas": [
                    {
                        "NumeroParcela": 0,
                        "NumeroParcelaGeral": 0,
                        "TipoParcela": "string",
                        "ValorDesconto": 0,
                        "ValorDescontoAntecipado": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._gravar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/GravarPedidoDeRecebimento"
        try:
            response = self.api.post(
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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def cancelar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/CancelarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        
        Pedidos que já tiveram um recebimento parcial junto a NTK, não são cancelados. (trava na NTK).
        É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Pedido (int): The pedido
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Pedido": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._cancelar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/CancelarPedidoDeRecebimento"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Obra": obra,
                    "Pedido": pedido,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_hierarquia_parcelas(
        self,
        codigo: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/ConsultarHierarquiaParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        
        Args:
            codigo (int): The codigo
        
        Parameter Structure:
        
            {
                "codigo": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._consultar_hierarquia_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/ConsultarHierarquiaParcelas"
        try:
            response = self.api.post(
                path,
                json={
                    "codigo": codigo,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def atualizar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/AtualizarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        
        Serão atualizadas as parcelas do pedido que ainda estão com status: 0 - Em aberto 
        É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Pedido (int): The pedido
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Pedido": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._atualizar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/AtualizarPedidoDeRecebimento"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Obra": obra,
                    "Pedido": pedido,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_pedido_de_recebimento(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        pedido: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/ConsultarPedidoDeRecebimento`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        
        Possibilita consultar pedido de recebimento junto a NTK
        As informações retornadas serão informações do pedido na NTK.
        
        
        
        Args:
            Empresa (int): The empresa
            Obra (str): The obra
            Pedido (int): The pedido
        
        Parameter Structure:
        
            {
                "Empresa": 0,
                "Obra": "string",
                "Pedido": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._consultar_pedido_de_recebimento(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/ConsultarPedidoDeRecebimento"
        try:
            response = self.api.post(
                path,
                json={
                    "Empresa": empresa,
                    "Obra": obra,
                    "Pedido": pedido,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def processar_recebimento_parcelas(
        self,
        recebimento: Optional[Dict] = None,
        forma_pagamento: Optional[Dict] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/ProcessarRecebimentoParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Processa as parcelas recebidas
        O valor do desconto aplicado ao recebimento será sempre do objeto de recebimento, o valor do desconto da parcela será aplicado somente pela tela de recebimento avulso.
        Não é possível realizar recebimento para todas as parcelas da proposta! Ao realizar o recebimento de parcelas o sistema verifica se possui boleto gerado e pedido de recebimento para outra parcelas da proposta.
        
        
        
        Args:
            recebimento (Dict[str, Any]): The recebimento
            formaPagamento (Dict[str, Any]): The pagamento
        
        Parameter Structure:
        
            {
                "recebimento": {
                    "Empresa": 0,
                    "Banco": "string",
                    "Conta": "string",
                    "HistContabil": "string",
                    "UsuarioLogado": "string",
                    "TipoRecebimento": 0,
                    "DataRecebimento": "2025-04-23T13:46:14.265Z",
                    "ValorJurosPreDatado": 0,
                    "DataParcelaPreDatada": "2025-04-23T13:46:14.265Z",
                    "ValorLiquidoRecebido": 0,
                    "ValorDesconto": 0,
                    "ValorAcrescimo": 0,
                    "DataCalculo": "2025-04-23T13:46:14.266Z",
                    "Antecipacao": true,
                    "NovaDataVenc": "2025-04-23T13:46:14.266Z",
                    "ReceberResiduo": true,
                    "OrigemRecebimento": 0,
                    "Parcelas": [
                        {
                            "NumParc": 0,
                            "NumParcGer": 0,
                            "NumeroContrato": 0,
                            "Obra": "string",
                            "TipoParc": "string",
                            "ValorDesconto": 0
                        }
                    ]
                },
                "formaPagamento": {
                    "Cheques": [
                        {
                            "Banco": 0,
                            "Agencia": "string",
                            "Conta": "string",
                            "NumCheque": "string",
                            "DataCadastro": "2025-04-23T13:46:14.266Z",
                            "Valor": 0,
                            "Titular": "string",
                            "QuemRecebeu": "string",
                            "Predatado": "2025-04-23T13:46:14.266Z",
                            "ValorDescontoCedido": 0,
                            "ValorAcrescimoCedido": 0,
                            "NumeroControle": 0,
                            "TipoValorJurosPredatado": 0
                        }
                    ],
                    "Bens": [
                        {
                            "NumBem": 0,
                            "Descricao": "string",
                            "Valor": 0,
                            "QuemRecebeu": "string",
                            "QuemRespons": "string",
                            "DataRecebeu": "2025-04-23T13:46:14.266Z"
                        }
                    ],
                    "Dinheiro": [
                        {
                            "NumControle": 0,
                            "Valor": 0,
                            "QuemRecebeu": "string",
                            "DataRecebeu": "2025-04-23T13:46:14.266Z"
                        }
                    ],
                    "CredEletro": [
                        {
                            "NumControle": 0,
                            "Valor": 0,
                            "QuemRecebeu": "string",
                            "DataRecebimento": "2025-04-23T13:46:14.266Z",
                            "DataDeposito": "2025-04-23T13:46:14.266Z",
                            "DataConciliacao": "2025-04-23T13:46:14.266Z"
                        }
                    ],
                    "Cartao": [
                        {
                            "NumControle": 0,
                            "Valor": 0,
                            "QuemRecebeu": "string",
                            "DataRecebimento": "2025-04-23T13:46:14.266Z",
                            "NumTerminal": 0,
                            "NSU": "string",
                            "NumReferencia": "string",
                            "CodAutorizacao": "string",
                            "Modalidade": 0,
                            "TotalParcelas": 0,
                            "Comprovante": "string"
                        }
                    ]
                }
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._processar_recebimento_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/ProcessarRecebimentoParcelas"
        try:
            response = self.api.post(
                path,
                json={
                    "recebimento": recebimento,
                    "formaPagamento": forma_pagamento,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def consultar_pedido_de_recebimento_uau(
        self,
        numerontk: Optional[int] = None,
        numero_pedido: Optional[int] = None
    ) -> dict:
        """
        
        Endpoint: `Proposta/ConsultarPedidoDeRecebimentoUAU`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        
        Definição de Negócio:
        
        Possibilita consultar pedido de recebimento regisrado no UAU por número do pedido junto a NTK ou pelo número do pedido no UAU.
        As informações retornadas são referentes a como o UAU registrou o pedido internamente.
        
        
        
        Args:
            NumeroNTK (int): The numero n t k
            NumeroPedido (int): The numero pedido
        
        Parameter Structure:
        
            {
                "NumeroNTK": 0,
                "NumeroPedido": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._consultar_pedido_de_recebimentouau(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/ConsultarPedidoDeRecebimentoUAU"
        try:
            response = self.api.post(
                path,
                json={
                    "NumeroNTK": numerontk,
                    "NumeroPedido": numero_pedido,
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

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
        """
        
        Endpoint: `Proposta/RetornarValoresEstruturaComissao`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
        
        Realiza cálculos da comissão e retorna os valores
        Parâmetros:
        Grupo de parcelas
        Estrutura de comissão
        
        
        
        
        
        Args:
            codigoEmpresa (int): The empresa
            codigoObra (str): The obra
            codigoVendedor (int): The vendedor
            codigoHierarquia (int): The hierarquia
            codigoComissao (int): The comissao
            valorTotalComissao (int): The total comissao
            valorComissaoDireta (int): The comissao direta
            produtos (List[Dict[str, Any]]): The produtos
            parcelas (List[Dict[str, Any]]): The parcelas
        
        Parameter Structure:
        
            {
                "codigoEmpresa": 0,
                "codigoObra": "string",
                "codigoVendedor": 0,
                "codigoHierarquia": 0,
                "codigoComissao": 0,
                "valorTotalComissao": 0,
                "valorComissaoDireta": 0,
                "produtos": [
                    {
                        "codEmpresa": 0,
                        "codProduto": 0,
                        "NumPersonalizacao": 0,
                        "precoProduto": 0,
                        "qtdeProduto": 0,
                        "Contrato": 0,
                        "itemProduto": "string",
                        "valComissaoDireta": 0,
                        "porcentualComissao": 0
                    }
                ],
                "parcelas": [
                    {
                        "numeroParcela": 0,
                        "valorParcela": 0,
                        "tipoParcela": "string",
                        "quantidadeParcela": 0,
                        "grupoParcela": 0,
                        "tipoValor": 0
                    }
                ]
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._retornar_valores_estrutura_comissao(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/RetornarValoresEstruturaComissao"
        try:
            response = self.api.post(
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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

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
        """
        
        Endpoint: `Proposta/RetornaValorComissaoDeducaoParcelas`
        HTTP Method: `POST`
        
        Implementation Notes:
        Definição Técnica:
        
        Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
        Preencher os parâmetros de request para uso do método.
        
        Definição de Negócio:
          Calcula o valor da comissão deduzido.
        
        
        Args:
            CodigoHierarquia (int): The codigo hierarquia
            CodigoModeloVenda (int): The codigo modelo venda
            ValorTotalProduto (int): The valor total produto
            ValorTotalComissao (int): The valor total comissao
            ValorTotalComissaoDireta (int): The valor total comissao direta
            ParcelasGeradas (List[Dict[str, Any]]): The parcelas geradas
            PorcentagemComissao (int): The porcentagem comissao
            ValorItemProposta (int): The valor item proposta
        
        Parameter Structure:
        
            {
                "CodigoHierarquia": 0,
                "CodigoModeloVenda": 0,
                "ValorTotalProduto": 0,
                "ValorTotalComissao": 0,
                "ValorTotalComissaoDireta": 0,
                "ParcelasGeradas": [
                    {
                        "NumeroParcela": 0,
                        "Valor": 0,
                        "TipoParcela": "string",
                        "QuantidadeParcela": 0,
                        "GrupoParcela": 0,
                        "TipoValor": 0,
                        "Porcentagem": 0
                    }
                ],
                "PorcentagemComissao": 0,
                "ValorItemProposta": 0
            }
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._retorna_valor_comissao_deducao_parcelas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "Proposta/RetornaValorComissaoDeducaoParcelas"
        try:
            response = self.api.post(
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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def traduzir_request_parcelas_geradas(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "Numero": 0,
                    "Tipo": "string",
                    "Valor": 0,
                    "DtVencimento": "2025-04-23T13:46:14.294Z",
                    "DtParc": "2025-04-23T13:46:14.294Z",
                    "Amortizacao": 0,
                    "BeginEnd": 0,
                    "NumGrupo": 0,
                    "TotalParcGrupo": 0,
                    "Frequencia": "string",
                    "DtIniJuros": "2025-04-23T13:46:14.294Z",
                    "TxJuros": 0,
                    "DataSegJuros": "2025-04-23T13:46:14.294Z",
                    "TxSegJuros": 0,
                    "DtIniIdx": "2025-04-23T13:46:14.294Z",
                    "IdxReaj": "string",
                    "GrupoIdx": 0,
                    "DtJurosComJuros": 0,
                    "CobrarJurosProRata": 0,
                    "CobrarJurosProRataPrimeiroMes": 0,
                    "CarenciaAtraso": 0,
                    "CarenciaAtrasoCorrecao": 0,
                    "TotalParc": 0,
                    "MeioPreferencialRecebimento": 0
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._traduzir_request_parcelas_geradas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Proposta/TraduzirRequestParcelasGeradas"
        try:
            response = self.api.post(
                path,
                json=parameters if parameters is not None else {}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

    def traduzir_request_parcelas_selecionadas(
        self,
        parameters: Optional[List[Dict]] = None
    ) -> dict:
        """
        HTTP Method: `POST`
        
        Args:
            parameters (List[Dict]): List of parameter dictionaries for the request
        
        Parameter Structure:
        
            [
                {
                    "NumParc": 0,
                    "NumParcGer": 0,
                    "Tipo": "string"
                }
            ]
        
        Returns:
            dict: The API response
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If required parameters are missing or invalid
        
        Examples:
            >>> api = Proposta()
            >>> response = api._traduzir_request_parcelas_selecionadas(
            ...     parameter1='value1',
            ...     parameter2='value2'
            ... )
        """
        path = "/api/Proposta/TraduzirRequestParcelasSelecionadas"
        try:
            response = self.api.post(
                path,
                json=parameters if parameters is not None else {}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return response.text

