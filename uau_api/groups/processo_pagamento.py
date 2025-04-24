"""This module contains auto-generated API class.

DO NOT EDIT MANUALLY.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from ..requestsapi import RequestsApi

class ProcessoPagamento:
    """Auto-generated API class"""

    def __init__(self, api):
        """Initialize with API client

        Args:
            api: The authenticated API client instance
        """
        if not hasattr(api, "is_authenticated") or not api.is_authenticated:
            raise ValueError("API client must be authenticated")
        self.api = RequestsApi(api.base_url, session=api.get_session())

    def aprovar_dvq(
        self,
        dvq: Optional[str] = None,
        aprovar: Optional[bool] = None,
        usuario: Optional[str] = None,
        sobrepor_aprovacoes_de_outros_usuarios: Optional[bool] = None,
        parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """Realiza a aprovação DVQ de uma ou várias parcelas.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
  Permite a aprovação DVQ de parcelas específicas.

No request [dvq] deve ser informado qual a letra que será aprovada ou não.
Os seguintes parâmetros obrigatórios para aprovação da letra "D":  Confirmação de data
usrConfirmou
codigoEmpresa
codigoObra
numeroProcesso
numeroParcela 


Os seguintes parâmetros obrigatórios para aprovação da letra "V" : Confirmação do valor
usrConfirmou
codigo_empresa
codigo_obra
numero_processo
codigo_departamento
numero_parcela
status_processo
valor_parcela      


Os seguintes parâmetros obrigatórios para aprovação da letra "Q" : Confirmação da quantidade
usrConfirmou
codigo_empresa
codigo_obra
numero_processo
numero_parcela
status_processo
tipo_Docprocesso
adiantamento_parcela       




Será validado as permissões do usuário informado. Verifique as permissões caso esteja sendo retornado erro na requisição;
FID : Permissão para aprovar "D"
FIV : Permissão para aprovar "V"
FIQ : Permissão para aprovar "Q"


O usuário autenticado precisa ter acesso a empresa e a obra da qual está fazendo a requisição.   
Será apenas validado a aprovação DVQ das parcelas informadas. Recomendado utilizar a API [RetornarParcelasDVQ] para retornar as informações das parcelas.


        """
        path = "ProcessoPagamento/AprovarDVQ"
        return self.api.post(
            path,
            json={
                "dvq": dvq,
                "aprovar": aprovar,
                "usuario": usuario,
                "sobreporAprovacoesDeOutrosUsuarios": sobrepor_aprovacoes_de_outros_usuarios,
                "parcelas": parcelas,
            }
        )

    def gerar_processo(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        codigo_fornecedor: Optional[int] = None,
        tipo_processo: Optional[int] = None,
        controlar_estoque: Optional[int] = None,
        acompanha_entrega: Optional[int] = None,
        data_previsao_entrega: Optional[datetime] = None,
        tipo_item: Optional[int] = None,
        historico_lanc_contabil: Optional[str] = None,
        historico_lanc_contabil_pago: Optional[str] = None,
        categoria_movimentacao_financeira: Optional[str] = None,
        numero_contrato: Optional[int] = None,
        parametro: Optional[Dict] = None,
        parcelas: Optional[List[Dict]] = None,
        itens: Optional[List[Dict]] = None,
        desconto_vinculado: Optional[List[Dict]] = None,
        solicitacao_caixa_obra: Optional[Dict] = None,
        permite_boleto_vencido: Optional[bool] = None
    ) -> dict:
        """Gera um processo de pagamento.

        Args:
            empresa: Código da empresa
            obra: Código da obra
            codigo_fornecedor: Código do fornecedor
            tipo_processo: Tipo do processo (1: Processo de Pagamento, 11: Compra de patrimônio, 13: Adiantamento de caixa de obra)
            controlar_estoque: Flag de controle de estoque
            acompanha_entrega: Flag de acompanhamento de entrega
            data_previsao_entrega: Data prevista para entrega
            tipo_item: Tipo do item
            historico_lanc_contabil: Histórico do lançamento contábil
            historico_lanc_contabil_pago: Histórico do lançamento contábil pago
            categoria_movimentacao_financeira: Categoria da movimentação financeira
            numero_contrato: Número do contrato
            parametro: Parâmetros do processo no formato:
                {
                    "CodigoDepartamento": str,
                    "TaxaJuros": int,
                    "TaxaMulta": int,
                    "TipoJuros": int,
                    "Retroagir": int,
                    "IndiceReajuste": str,
                    "DataIncioReajuste": str (formato: "YYYY-MM-DDThh:mm:ss.sssZ"),
                    "CodigoMunicipio": int,
                    "VincularDocFiscalTodosProcessos": bool
                }
            parcelas: Lista de parcelas no formato:
                [{
                    "Datavencimento": str (formato: "YYYY-MM-DDThh:mm:ss.sssZ"),
                    "Valor": float,
                    "Descontos": [{
                        "Descricao": str,
                        "Valor": float,
                        "DataVencimento": str (formato: "YYYY-MM-DDThh:mm:ss.sssZ"),
                        "Cap": str,
                        "HistoricoLancamentoContabil": str
                    }],
                    "DocumentoFiscal": {
                        "NumeroNota": int,
                        "SerieNota": str,
                        "EspecieNota": str,
                        "TipoNota": int,
                        "NFEletronica": int,
                        "ChaveNFe": str
                    },
                    "Banco": str,
                    "Conta": str,
                    "Convenio": str,
                    "TipoEmissao": str,
                    "FormaPagamento": str,
                    "TipoPagamento": str,
                    "CodigoDeBarras": str,
                    "PixCopiaCola": str,
                    "TXID": str
                }]
            itens: Lista de itens no formato:
                [{
                    "Item": str,
                    "Quantidade": float,
                    "Preco": float,
                    "Cap": str,
                    "CategoriaMovimentacaoFinanceira": str,
                    "Unidade": str,
                    "VinculoPL": [{
                        "Item": str,
                        "CodigoProduto": int,
                        "Contrato": int,
                        "Servico": str,
                        "Insumo": str,
                        "MesPlanejamento": str (formato: "YYYY-MM-DDThh:mm:ss.sssZ"),
                        "Quantidade": float,
                        "Preco": float,
                        "NumeroItemContrato": int
                    }],
                    "CodJustificativa": int,
                    "Justificativa": str
                }]
            desconto_vinculado: Lista de descontos vinculados no formato:
                [{
                    "Descricao": str,
                    "DataVencimento": str (formato: "YYYY-MM-DDThh:mm:ss.sssZ"),
                    "Valor": float,
                    "Cap": str,
                    "CodigoFornecedor": int,
                    "Nominal": str,
                    "ItemProcesso": str,
                    "ObraFiscal": str,
                    "HistoricoLancamentoContabilPagar": str,
                    "HistoricoLancamentoContabilPago": str,
                    "CategoriaMovimentacaoFinanceira": str
                }]
            solicitacao_caixa_obra: Dados da solicitação de caixa obra no formato:
                {
                    "NumeroSolicitacao": int,
                    "UsuarioAprovacao": str,
                    "Empresa": int,
                    "Obra": str,
                    "NumeroProcesso": int
                }
            permite_boleto_vencido: Permite boleto vencido

        Implementation Notes:
            Definição Técnica:
            Dados básicos para o funcionamento da API.

            Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario
            Preencher os parâmetros de request para uso do método.

            Definição de Negócio:
            Gera um processo de pagamento.

            É obrigatório informar os dados básicos do processo de pagamento.
            O usuário autenticado precisa ter acesso à empresa e obra que está fazendo a requisição.
            O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.
            Só aceita os tipos de processo de pagamento: composições e insumos, insumos planejados, adiantamento de caixa de obra, patrimônio vinculado ao planejamento.
            Você pode vincular documento fiscal ao processo de pagamento, informe os dados da nota no objeto de DocumentoFiscal.
            
        Returns:
            dict: O resultado da criação do processo
        """
        path = "ProcessoPagamento/GerarProcesso"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "CodigoFornecedor": codigo_fornecedor,
                "TipoProcesso": tipo_processo,
                "ControlarEstoque": controlar_estoque, 
                "AcompanhaEntrega": acompanha_entrega,
                "DataPrevisaoEntrega": data_previsao_entrega,
                "TipoItem": tipo_item,
                "HistoricoLancContabil": historico_lanc_contabil,
                "HistoricoLancContabilPago": historico_lanc_contabil_pago,
                "CategoriaMovimentacaoFinanceira": categoria_movimentacao_financeira,
                "NumeroContrato": numero_contrato,
                "Parametro": parametro,
                "Parcelas": parcelas,
                "Itens": itens,
                "DescontoVinculado": desconto_vinculado,
                "SolicitacaoCaixaObra": solicitacao_caixa_obra,
                "PermiteBoletoVencido": permite_boleto_vencido
            }
        )

    def gerar_nota_fiscal(
        self,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        numero_processo: Optional[int] = None,
        parcela: Optional[int] = None,
        tiponf: Optional[int] = None,
        especie: Optional[str] = None,
        serie: Optional[str] = None,
        nf_eletronica: Optional[bool] = None,
        chave_nfe: Optional[str] = None,
        numero_nota_fiscal: Optional[str] = None,
        codigo_remetente: Optional[int] = None,
        data_emissao: Optional[datetime] = None,
        data_de_emissao_maior_que_cadastro: Optional[bool] = None,
        data_entrada: Optional[datetime] = None,
        data_de_entrada_maior_que_cadastro: Optional[bool] = None,
        modelonf: Optional[int] = None,
        arq_nota_fiscal: Optional[str] = None,
        caminho_origem_arquivo_local: Optional[str] = None,
        caminho_destino_arquivo: Optional[str] = None,
        nome_arquivo: Optional[str] = None,
        copiar_arquivo: Optional[bool] = None,
        vinculara_descontos: Optional[bool] = None
    ) -> dict:
        """Gerar nota fiscal com base nos dados do processo informado. A nota será vinculada ao processo.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Gerar nota fiscal de entrada de acordo com os dados do processo

É obrigatório informar os dados básicos da nota fiscal.
O usuário autenticado precisa ter acesso a empresa e obra que está fazendo a requisição;
O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção;
Serão utilizadas as informações fiscais de tributo cadastradas no produto ou na empresa.
Especies disponíveis para geração do documento fiscal (NF - Nota fiscal, CT - Conhecimento de transporte, RE - Recibo, OU - Outros, CF - Cupom fiscal)


        """
        path = "ProcessoPagamento/GerarNotaFiscal"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Obra": obra,
                "NumeroProcesso": numero_processo,
                "Parcela": parcela,
                "TipoNF": tiponf,
                "Especie": especie,
                "Serie": serie,
                "NFEletronica": nf_eletronica,
                "ChaveNfe": chave_nfe,
                "NumeroNotaFiscal": numero_nota_fiscal,
                "CodigoRemetente": codigo_remetente,
                "DataEmissao": data_emissao,
                "DataDeEmissaoMaiorQueCadastro": data_de_emissao_maior_que_cadastro,
                "DataEntrada": data_entrada,
                "DataDeEntradaMaiorQueCadastro": data_de_entrada_maior_que_cadastro,
                "ModeloNF": modelonf,
                "ArqNotaFiscal": arq_nota_fiscal,
                "CaminhoOrigemArquivoLocal": caminho_origem_arquivo_local,
                "CaminhoDestinoArquivo": caminho_destino_arquivo,
                "NomeArquivo": nome_arquivo,
                "CopiarArquivo": copiar_arquivo,
                "VincularADescontos": vinculara_descontos,
            }
        )

    def aprovar_processos(
        self,
        processos: Optional[List[Dict]] = None
    ) -> dict:
        """Realiza a aprovação de parcelas de um processo de pagamento.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:

O Usuário informado precisa ter a permissão [FICHEQUE] para aprovar as parcelas do processo.
A(s) parcela(s) precisam estar no "Emissão de Pagamentos" para serem aprovadas.
Todos os parâmetros são obrigatórios.


        """
        path = "ProcessoPagamento/AprovarProcessos"
        return self.api.post(
            path,
            json={
                "processos": processos,
            }
        )

    def consultar_processos(
        self,
        processos: Optional[List[Dict]] = None,
        empresa_obra_periodo: Optional[Dict] = None,
        fornecedor_periodo: Optional[Dict] = None
    ) -> dict:
        """Consultar processos de pagamento por empresa(s), obra(s) e número(s) do(s) processo(s) e/ou empresa, obra e período(data de cadastro do processo) e/ou CNPJ do fornecedor e período(data de cadastro do processo).

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
  Permite que você consulte o(s) processo(s) de pagamento por um número e/ou período específico.

Você pode consultar informando uma lista dos números dos processos de pagamento, código da empresa e código da obra cadastrados no UAU.
Você pode consultar processos de pagamento informado uma lista de código da empresa e código da obra cadastrado no UAU por um determinado período.
Você pode consultar processos de pagamento informado uma lista de fornecedores cadastrado no UAU por um determinado período.
O usuário autenticado precisa ter acesso as empresas e obras das quais ele está fazendo a requisição.   
Caso consulte vários processos ou informe um longo período, sugerimos que consulte o serviço de maneira assíncrona. 
NovoBeneficiario: O campo Parametro/NovoBeneficiario sempre retornará o valor null. A informação é retornada no campo Parcelas/NovoBeneficiario.
Caso passe uma mistura de todos os filtros, o filtro de data que será utilizado será o do busca por cnpj a frente do busca por empresas e obras.
  7.1 Caso queria buscar por períodos diferentes recomendamos utilizar requests separados para respeitar os períodos por grupo separado.


        """
        path = "ProcessoPagamento/ConsultarProcessos"
        return self.api.post(
            path,
            json={
                "Processos": processos,
                "EmpresaObraPeriodo": empresa_obra_periodo,
                "FornecedorPeriodo": fornecedor_periodo,
            }
        )

    def manutencao_processo(
        self,
        numero: Optional[int] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        codigo_fornecedor: Optional[int] = None,
        codigo_novo_beneficiario: Optional[int] = None,
        antecipado: Optional[bool] = None,
        retroacao: Optional[int] = None,
        codigo_departamento: Optional[str] = None,
        tipo_juros: Optional[int] = None,
        taxa_juros_atraso: Optional[int] = None,
        taxa_multa_atraso: Optional[int] = None,
        chave_nfe: Optional[str] = None,
        parcela: Optional[Dict] = None,
        numero_protocolo: Optional[int] = None,
        permite_boleto_vencido: Optional[bool] = None
    ) -> dict:
        """Executa manutenção básica em uma etapa do processo de pagamento.

        Implementation Notes:
        Definição Técnica:
Dados básicos para o funcionamento da API.

Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario
Consultar os dados de um processo de pagamento: URI + /api/v{version}/ProcessoPagamento/ConsultarProcessos
Preencher os parâmetros de request para uso do método.
Documentação API - Manutenção de Processo (Clique Aqui)

Definição de Negócio:
Permite ajustar informações básicas do processo de pagamento, como vencimento, data de prorrogação, novo beneficiário, fornecedor, etc.
   Consulte a documentação do objeto de request.

É obrigatório informar os dados básicos do processo de pagamento.
Para alterar informações da parcela do processo, preencha o objeto de Parcelas.
Todas as alterações gerarão um comentário de alteração no processo.
O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a alteração.
O parâmetro CodigoNovoBeneficiario altera todas as parcelas a pagar do processo informado, independentemente da parcela informada.
  Ao informar esse valor no processo, na resposta da request o valor será null, mas estará indicado nas parcelas. Isso ocorre porque esse campo pertence à parcela.
O parâmetro NovoBeneficiario altera apenas a parcela informada, se ela estiver a pagar.
  Se preencher o parâmetro de beneficiário no processo e na parcela, o parâmetro do processo será desconsiderado, alterando apenas os beneficiários das parcelas informadas.
Se preencher o valor zero ou vazio para o novo beneficiário, a alteração não será considerada. A API não limpa valores de novo beneficiário.


        """
        path = "ProcessoPagamento/ManutencaoProcesso"
        return self.api.post(
            path,
            json={
                "Numero": numero,
                "Empresa": empresa,
                "Obra": obra,
                "CodigoFornecedor": codigo_fornecedor,
                "CodigoNovoBeneficiario": codigo_novo_beneficiario,
                "Antecipado": antecipado,
                "Retroacao": retroacao,
                "CodigoDepartamento": codigo_departamento,
                "TipoJuros": tipo_juros,
                "TaxaJurosAtraso": taxa_juros_atraso,
                "TaxaMultaAtraso": taxa_multa_atraso,
                "ChaveNfe": chave_nfe,
                "Parcela": parcela,
                "NumeroProtocolo": numero_protocolo,
                "PermiteBoletoVencido": permite_boleto_vencido,
            }
        )

    def retornar_parcelas_dvq(
        self,
        usuario: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        numeroproc: Optional[int] = None,
        fornecedor: Optional[str] = None,
        notafiscal: Optional[int] = None,
        inicial: Optional[str] = None,
        final: Optional[str] = None
    ) -> dict:
        """Retorna parcelas com alguma possibilidade de aprovação DVQ.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Os campos empresa, obra e usuário são obrigatórios.
É validado se o usuário existe no banco de dados, e se tem permissão na empresa e obra informada.
Data e Fornecedor devem está vazio ou sem o parâmetro informado na requisição para não serem considerados na consulta.
Número processo(numeroproc) e notafiscal devem está como 0 ou sem o parâmetro informado na requisição para não serem considerados na consulta.
O parâmetro nota fiscal é o número de controle interno da nota fiscal.
Status atual da aprovação status_d, status_v e status_q.
Valor [A]: aprovado
Valor [D]: não aprovado




        """
        path = "ProcessoPagamento/RetornarParcelasDVQ"
        return self.api.post(
            path,
            json={
                "Usuario": usuario,
                "Empresa": empresa,
                "Obra": obra,
                "numeroproc": numeroproc,
                "fornecedor": fornecedor,
                "notafiscal": notafiscal,
                "inicial": inicial,
                "final": final,
            }
        )

    def gerar_processo_medicao(
        self,
        empresa: Optional[int] = None,
        contrato: Optional[int] = None,
        medicao: Optional[int] = None,
        mes_planejamento: Optional[datetime] = None,
        controlar_estoque: Optional[int] = None,
        acompanha_entrega: Optional[int] = None,
        data_previsao_entrega: Optional[datetime] = None,
        historico_lanc_contabil_apagar: Optional[str] = None,
        historico_lanc_contabil_pago: Optional[str] = None,
        historico_lanc_contabil_desc_normal_med: Optional[str] = None,
        categoria_movimentacao_financeira: Optional[str] = None,
        parametro: Optional[Dict] = None,
        documento_fiscal: Optional[Dict] = None,
        parcelas: Optional[List[Dict]] = None,
        itens: Optional[List[Dict]] = None
    ) -> dict:
        """Gerar processo de pagamento de medição de contrato de material/serviço

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Gerar processo de pagamento de medição de contrato de material/serviço

É obrigatório informar os dados básicos do processo de pagamento;
O usuário autenticado precisa ter acesso a empresa e obra que está fazendo a requisição;
O usuário autenticado precisa ter acesso a aos programas de permissão necessários para fazer a inserção;
Você pode informar uma parcela ou uma lista de parcelas;
Você pode vincular documento fiscal ao processo de pagamento, informe os dados da nota no objeto de “DocumentoFiscal”, o documento deve existir;
Você pode aplicar desconto normal a parcela, informe os dados de desconto no objeto “Descontos”;
Quando o insumo PL for do tipo 1 - quantidade será considerado o preço do item;


        """
        path = "ProcessoPagamento/GerarProcessoMedicao"
        return self.api.post(
            path,
            json={
                "Empresa": empresa,
                "Contrato": contrato,
                "Medicao": medicao,
                "MesPlanejamento": mes_planejamento,
                "ControlarEstoque": controlar_estoque,
                "AcompanhaEntrega": acompanha_entrega,
                "DataPrevisaoEntrega": data_previsao_entrega,
                "HistoricoLancContabilApagar": historico_lanc_contabil_apagar,
                "HistoricoLancContabilPago": historico_lanc_contabil_pago,
                "HistoricoLancContabilDescNormalMed": historico_lanc_contabil_desc_normal_med,
                "CategoriaMovimentacaoFinanceira": categoria_movimentacao_financeira,
                "Parametro": parametro,
                "DocumentoFiscal": documento_fiscal,
                "Parcelas": parcelas,
                "Itens": itens,
            }
        )

    def manutencao_parcelas_processo(
        self,
        codigo_empresa: Optional[int] = None,
        codigo_obra: Optional[str] = None,
        numero_processo: Optional[int] = None,
        data_vencimento: Optional[datetime] = None,
        qtde_parcelas: Optional[int] = None,
        intervalo_parcelas: Optional[int] = None,
        lista_parcelas_manutencao: Optional[List[Dict]] = None,
        lista_valores_novas_parcelas: Optional[List[Dict]] = None,
        lista_valores_acrescimo_novas_parcelas: Optional[List[Dict]] = None,
        lista_data_vencimento_novas_parcelas: Optional[List[Dict]] = None
    ) -> dict:
        """Realiza manutenção em parcelas de processo de pagamento. Será simulado e gerado automaticamente as novas parcelas conforme os parâmetros informados.

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.

Definição de Negócio:
  Permite dar manutenção nas parcelas do processo de pagamento. Ao informar os dados para as novas parcelas, será simulado e gerado automaticamente as novas parcelas
  com novas numerações, valores e data de vencimento. Será excluido a(s) parcela(s) informadas no request, pois foram substituídas pelas novas parcelas geradas.

É obrigatório informar os dados básicos da parcela e do processo de pagamento;
O usuário autenticado precisa ter acesso aos programas de permissão necessários (FIANALISE) para fazer a alteração.


        """
        path = "ProcessoPagamento/ManutencaoParcelasProcesso"
        return self.api.post(
            path,
            json={
                "codigoEmpresa": codigo_empresa,
                "codigoObra": codigo_obra,
                "numeroProcesso": numero_processo,
                "dataVencimento": data_vencimento,
                "qtdeParcelas": qtde_parcelas,
                "intervaloParcelas": intervalo_parcelas,
                "listaParcelasManutencao": lista_parcelas_manutencao,
                "listaValoresNovasParcelas": lista_valores_novas_parcelas,
                "listaValoresAcrescimoNovasParcelas": lista_valores_acrescimo_novas_parcelas,
                "listaDataVencimentoNovasParcelas": lista_data_vencimento_novas_parcelas,
            }
        )

    def gerar_nota_fiscal_produto_pelo_xml(
        self,
        chaven_fe: Optional[str] = None,
        arquivoxml: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        parcela: Optional[int] = None,
        vinculara_descontos: Optional[bool] = None
    ) -> dict:
        """Gerar NF-e com base nos dados informado, xml do diretório.

        Implementation Notes:
        Criação   : Augusto Rabelo Barbosa                 Data: 28/05/2022
  Projeto   : 442112
  Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
  Projeto   : 443200
  Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
Alteração  : Augusto Rabelo Barbosa      data: 04/01/2023
  Projeto    : 443200
  Manutenção  : Alterei o enumerador de importação de nota, passando a utilizar o TiposImportacao do EnumeradoresGerais
Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
  Projeto   : 454022
  Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
Alteração : Juliana Oliveira Souza    Data: 19/06/2023
  Projeto   : 467593
  Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
  Projeto   : 442322 - SPT 10-2024 - US 359545
  Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].

        """
        path = "ProcessoPagamento/GerarNotaFiscalProdutoPeloXML"
        return self.api.post(
            path,
            json={
                "ChaveNFe": chaven_fe,
                "ArquivoXML": arquivoxml,
                "Empresa": empresa,
                "Obra": obra,
                "Processo": processo,
                "Parcela": parcela,
                "VincularADescontos": vinculara_descontos,
            }
        )

    def gerar_nota_fiscal_servico_pelo_xml(
        self,
        codigo_fornecedor: Optional[int] = None,
        numero: Optional[str] = None,
        chavenf_se: Optional[str] = None,
        arquivoxml: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        parcela: Optional[int] = None,
        vinculara_descontos: Optional[bool] = None
    ) -> dict:
        """Gerar NFS-e com base nos dados informado, xml do diretório ou arquivo.

        Implementation Notes:
        Criação   : Augusto Rabelo Barbosa                 Data: 03/11/2022
  Projeto   : 442112
Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
  Projeto   : 443200
  Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
  Projeto   : 454022
  Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
Alteração : Juliana Oliveira Souza    Data: 19/06/2023
  Projeto   : 467593
  Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
Alteração : Rogério Adriano           Data: 31/07/2023
  Projeto   : 475869
  Manutenção: Foi inserido validação após o preenchimento da classe de nota fiscal
              para verificar se foi preenchido com sucesso, caso contrario irá retornar o erro.
Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
  Projeto   : 442322 - SPT 10-2024 - US 359545
  Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].

        """
        path = "ProcessoPagamento/GerarNotaFiscalServicoPeloXML"
        return self.api.post(
            path,
            json={
                "CodigoFornecedor": codigo_fornecedor,
                "Numero": numero,
                "ChaveNFSe": chavenf_se,
                "ArquivoXML": arquivoxml,
                "Empresa": empresa,
                "Obra": obra,
                "Processo": processo,
                "Parcela": parcela,
                "VincularADescontos": vinculara_descontos,
            }
        )

    def integrar_processo_pagamento_uauws(
        self,
        xml_proc: Optional[str] = None
    ) -> dict:
        """Realizar a integração do processo de pagamento utilizando arquivo XML

        Implementation Notes:
        Definição Técnica:

Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
Preencher os parâmetros de request para uso do método.
Deve seguir arquivo XSD como formato aceito.
Os campos do tipo data devem obedecer o formato específico (yyyy-MM-dd).

Definição de negócio:

Realiza a importação dos dados de processo de pagamento para o UAU de acordo com o arquivo XML.
Será validado os dados do XML para realizar a importação, bem como tipagem de dados, dados obrigatórios, entre outros. 
Virtuau: https://ajuda.globaltec.com.br/virtuau/como-integrar-meus-processos-de-pagamento/

Anexos:

XML: https://ajuda.globaltec.com.br/download/777734/
XSD: https://ajuda.globaltec.com.br/download/777719/
Postman: https://ajuda.globaltec.com.br/download/777737/


        """
        path = "ProcessoPagamento/IntegrarProcessoPagamentoUAUWS"
        return self.api.post(
            path,
            json={
                "xml_proc": xml_proc,
            }
        )

    def gerar_nota_fiscal_transporte_pelo_xml(
        self,
        chavec_te: Optional[str] = None,
        arquivoxml: Optional[str] = None,
        empresa: Optional[int] = None,
        obra: Optional[str] = None,
        processo: Optional[int] = None,
        parcela: Optional[int] = None,
        vinculara_descontos: Optional[bool] = None
    ) -> dict:
        """Gerar CT-e com base nos dados informado, xml do diretório.

        Implementation Notes:
        Criação   : Augusto Rabelo Barbosa                 Data: 03/11/2022
  Projeto   : 442112
Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
  Projeto   : 443200
  Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.
Alteração: Augusto Rabelo Barbosa      data: 04/01/2023
  Projeto: 443200
  Manutenção: Alterei o enumerador de importação de nota, passando a utilizar o TiposImportacao do EnumeradoresGerais
Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
  Projeto   : 454022
  Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.
Alteração : Juliana Oliveira Souza    Data: 19/06/2023
  Projeto   : 467593
  Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário
Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
  Projeto   : 442322 - SPT 10-2024 - US 359545
  Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].

        """
        path = "ProcessoPagamento/GerarNotaFiscalTransportePeloXML"
        return self.api.post(
            path,
            json={
                "ChaveCTe": chavec_te,
                "ArquivoXML": arquivoxml,
                "Empresa": empresa,
                "Obra": obra,
                "Processo": processo,
                "Parcela": parcela,
                "VincularADescontos": vinculara_descontos,
            }
        )

