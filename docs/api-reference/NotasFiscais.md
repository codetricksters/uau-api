# NotasFiscais

## POST `/api/v{version}/NotasFiscais/ConsultarNFEntrada`

**Listagem de nota fiscal**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Ao menos uma chave de pesquisa deve ser preenchida sendo elas ([CodigoEmpresa],
[CnpjFornecedor], [CodigoFornecedor], [DataInicial], [ListaNFEntrada]).
2. Caso tenha informado a propriedade da Obra, a Empresa torna-se obrigatória.
3. Preenchimento da [DataInicial] torna [DataFinal] obrigatória.
4. Preenchimento da [DataFinal] torna [DataInicial] obrigatória.
5. Obra só vai achar informação se a nota estiver vinculada a um processo.
6. [ListaNFEntrada] Cada objeto deve ter obrigatoriamente o [CodigoEmpresa] e o [NumeroNotaFiscal ou NumeroNotaFiscalEletronica]
6.1 NumeroNotaFiscal = Número de controle da nota fiscal (Obs: no retorno dos dados esse valor fica no campo Numero)
6.2 NumeroNotaFiscalEletronica = Número da nota fiscal eletrônica, informado na DANFE ou NFS-e (Obs: no retorno dos dados esse valor fica no campo NumeroNotaFiscal)

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.UAUApi.Models.ConsultarNFEntradaRequest`](#uauapimodelsuauapimodelsconsultarnfentradarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.UAUApi.Models.NotaFiscalEntrada`](#uauapimodelsuauapimodelsnotafiscalentrada) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/NotasFiscais/SalvarArquivoXMLnotafiscalEntrada`

**Salvar o arquivo XML das notas fiscais para importação no sistema.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario.
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Poderá ser enviado uma lista de arquivos XML.
2. Será permitido no máximo uma lista com 20 arquivos.
3. Tipo do arquivo XML [TipoXML]
    0 para NF-e
    1 para CT-e
    2 para NFS-e,
4. Arquivo XML da nota fiscal (Texto do arquivo) [ArquivoXML].

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: array de [`UAUApi.Models.NotasFiscais.SalvarArquivoXMLnotafiscalEntradaRequest`](#uauapimodelsnotasfiscaissalvararquivoxmlnotafiscalentradarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 206 | Requisição realizada em parte. Verifique as mensagens de retorno. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.NotasFiscais.SalvarArquivoXMLnotafiscalEntradaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `TipoXML` | integer (int32) | ✓ | Tipo do arquivo XML - preencher com: 0, 1 ou 2. Sendo 0 para NF-e, 1 para CT-e e 2 para NFS-e. |
| `ArquivoXML` | string | ✓ | Arquivo XML da nota fiscal (Texto do arquivo). |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.UAUApi.Models.NotaFiscalEntrada

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Número da empresa |
| `Numero` | integer (int32) |  | Número de controle interno da nota |
| `Serie` | string |  | Série da nota fiscal |
| `CodigoFornecedor` | integer (int32) |  | Cód. do fornecedor |
| `CNPJCPFFornecedor` | string |  | CNPJ/CPF Fornecedor |
| `Especie` | string |  | Espécie do documento |
| `NumeroNotaFiscal` | string |  | Número da Nota Fiscal |
| `Usuario` | string |  | Usuário que cadastrou a nota |
| `Tipo` | integer (int32) |  | (0)-Estadual; (1)-Municipal |
| `Cfop` | string |  | Código fiscal da operação |
| `IESubstituto` | string |  | Número da insc. Estadual do substituto tributário |
| `DataEmissao` | string (date-time) |  | Data da emissão da nota |
| `DataSaidaEntrada` | string (date-time) |  | Data da entrada ou saida da nota |
| `PracaPagamento` | string |  | Praça de pagamento (cidade) |
| `UFPagamento` | string |  | UF da praça de pagamento |
| `ValorTotalNota` | number (double) |  | Valor da notaFiscal |
| `UF` | string |  | Estado da Nota Fiscal |
| `Observacao` | string |  | Observação da Nota Fiscal de Entrada |
| `Status` | integer (int32) |  | identificar se a NF Munic. Esta Pendente ou Conferida |
| `CodigoServicoAuxiliar` | string |  | Código do serviço para o imposto de São Paulo DES |
| `DataCadastro` | string (date-time) |  | Data de cadastro da nota no sistema |
| `UsuarioCadastroStatus` | string |  | Usuário que conferiu a nota fiscal |
| `DataCadastroStatus` | string (date-time) |  | Data de conferencia |
| `EmpresaEscritura` | integer (int32) |  | Codigo da empresa que está recebendo essa nota fiscal. Onde ela será escriturada. |
| `EspecieAuxiliar` | string |  | Especie da nota fiscal utilizado em alguns livros eletrônicos (ex.: DES) |
| `SerieAuxiliar` | string |  | Série auxiliar, utizado em alguns livros eletrônicos. Ex.: DES |
| `NumeroManufatura` | integer (int32) |  | Chave do modelo de nota fiscal |
| `NotaFiscalEletronica` | boolean |  | Define se a nota fiscal cadastrada é uma nota eletrônica; |
| `NaturezaOperacaoAuxiliar` | string |  | A natureza da operação auxiliar |
| `OptanteSimplesNacional` | integer (int32) |  | Indicação de optante da simples nacional |
| `SPEDPisCofins` | boolean |  | Se irá enviar a nota fiscal para o SPED PIS/COFINS ao gerar o arquivo |
| `ObraRelacaoAdministrativa` | string |  | Código da obra do relatório de administração de obra. |
| `NumeroRelacaoAdministrativa` | integer (int32) |  | Número do relatório por empresa e obra. |
| `ChaveNotaFiscalEletronica` | string |  | Chave da Nfe gerada para identificação e código de barras do DANFE |
| `NumeroCidade` | integer (int32) |  | Código da cidade |
| `ClasseConsumo` | string |  | Classe do consumo |
| `TipoLigacao` | integer (int32) |  | Tipo da ligação |
| `GrupoTensao` | string |  | Grupo tensão |
| `TipoAssinante` | integer (int32) |  | Tipo assinante |
| `Anexos` | integer (int32) |  | Anexos |
| `NotaFiscalEletronicaPropria` | boolean |  | Se a NF-e é de emissão própria: 0 - Não, 1 - Sim |
| `CodigoFiscal` | string |  | Código fiscal |
| `NumeroCsf` | integer (int32) |  | Número do CSF |
| `NumeroApd` | integer (int32) |  | Número de apitidão |
| `EnviarSPEDReinf` | boolean |  | Se irá enviar a nota fiscal para o SPED REINF |
| `CodigoTtsr` | string |  | Código do tipo de serviço para a REINF [TabTipoServicoREINF] |
| `CodigoTnrr` | string |  | Código da natureza de rendimento do REINF [TabNaturezaRendimentoREINF] |
| `Obra` | string |  | Código da obra vinculada a nota fiscal, será preenchida com a obra do processo de pagamento vínculado. |
| `Processos` | array de [`UAUApi.Models.UAUApi.Models.NotfiscProc`](#uauapimodelsuauapimodelsnotfiscproc) |  | Processos da nota fiscal |
| `Enderecos` | array de [`UAUApi.Models.UAUApi.Models.NotaFiscalEndereco`](#uauapimodelsuauapimodelsnotafiscalendereco) |  | Endereços da nota fiscal |
| `NotaFiscalEntTotalServico` | [`UAUApi.Models.UAUApi.Models.NotaFiscalEntTotalServico`](#uauapimodelsuauapimodelsnotafiscalenttotalservico) |  | NotaFiscalEntTotalServico |
| `ItensNotaFiscalEntProdutos` | array de [`UAUApi.Models.UAUApi.Models.ItensNotaFiscalEntProduto`](#uauapimodelsuauapimodelsitensnotafiscalentproduto) |  | ItensNotaFiscalEntProduto |
| `ItensNotaFiscalEnt` | array de [`UAUApi.Models.UAUApi.Models.ItensNotaFiscalEnt`](#uauapimodelsuauapimodelsitensnotafiscalent) |  | Cód. do fornecedor |
| `NotaFiscalEntTotalProduto` | [`UAUApi.Models.UAUApi.Models.NotaFiscalEntTotalProduto`](#uauapimodelsuauapimodelsnotafiscalenttotalproduto) |  | Cód. do fornecedor |

### UAUApi.Models.UAUApi.Models.NotaFiscalEntTotalProduto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa |
| `Numero` | integer (int32) |  | Contador de documento fiscal por empresa. |
| `ValorTotalProduto` | number (double) |  | Valor total dos produtos |
| `ValorBaseICMS` | string |  | Valor Base de Cálculo de ICMS |
| `ValorBaseICMSSub` | number (double) |  | ValorBaseICMSSub |
| `ValorICMSSub` | number (double) |  | Valor do icms substituto |
| `ValorFrete` | number (double) |  | Valor do frete |
| `ValorSeguro` | number (double) |  | Valor do seguro |
| `ValorIPI` | number (double) |  | Valor do IPI |
| `SomaTotalNFIcmsSub` | boolean |  | Se o valor do Frete irá ser somado ao total da nota. |
| `IncideICMSFrete` | boolean |  | Se irá incidir o ICMS sobre o valor do frete. |
| `SomaTotNFIcmsSub` | boolean |  | Se o valor do ICMS substituição tributária irá ser somado ao total da nota. |
| `IncideICMSSeguro` | boolean |  | Se irá incidir o ICMS sobre o valor do seguro |
| `SomaTotalNotaFiscalSeguro` | boolean |  | Se o valor do Seguro irá ser somado ao total da nota. |
| `IncideICMSDespesaAcesso` | boolean |  | Se irá incidir o ICMS sobre o valor das despesas acessórias (outros). |
| `SomaTotalNotaFiscalDespesaAcesso` | boolean |  | Se o valor da despesa acessória irá ser somado ao total da nota. |
| `ValorDesconto` | number (double) |  | Valor do desconto aplicado na nota fiscal |
| `ValorDespesaAcesso` | number (double) |  | Valor de outras despesas acessórias |
| `ValorBaseIPI` | number (double) |  | Valor da base de cálculo do IPI |
| `ValorBasePISCredito` | number (double) |  | Valor total da base de cálculo do PIS referente ao crédito do imposto |
| `ValorPISCredito` | number (double) |  | Valor total do PIS referente ao crédito do imposto |
| `ValorBaseCofinsCredito` | number (double) |  | Valor total da base de cálculo de COFINS referente ao crédito do imposto |
| `ValorCofinsCredito` | number (double) |  | Valor total do COFINS referente ao crédito do imposto |
| `IncideIPIFrete` | boolean |  | IncideIPIFrete |
| `IncideIPISeguro` | boolean |  | IncideIPISeguro |
| `IncideIPIDespesaAcesso` | boolean |  | IncideIPIDespesaAcesso |
| `IncideIPIDesconto` | boolean |  | IncideIPIDesconto |
| `ValIcms` | number (double) |  | Valor do ICMS |
| `ValBaseIcmsSub` | number (double) |  | Valor Base de Cálculo de ICMS Substituto |
| `SomaTotalNotafiscalFrete` | boolean |  | SomaTotalNotafiscalFrete |
| `ValorBaseCBSIBS` | number (double) |  | Valor da Base de Cálculo do CBS (Contribuição sobre Bens e Serviços) |
| `ValorCBS` | number (double) |  | Valor do CBS (Contribuição sobre Bens e Serviços) |
| `ValorIBSUF` | number (double) |  | Valor do IBS da UF (Imposto sobre Bens e Serviços - Estadual) |
| `ValorIBSMunicipio` | number (double) |  | Valor do IBS Municipal (Imposto sobre Bens e Serviços - Municipal) |

### UAUApi.Models.UAUApi.Models.ItensNotaFiscalEnt

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa |
| `Item` | integer (int32) |  | (Contador) Nº do item na nota fiscal |
| `Valor` | number (double) |  | Valor do item |
| `Numero` | integer (int32) |  | Contador de documento fiscal por empresa. |
| `NumeroServico` | string |  | Número do serviço |
| `DescricaoServico` | string |  | Descrição do serviço |
| `Unidade` | string |  | Unidade do serviço |
| `Quantidade` | number (double) |  | Qtde do serviço |
| `ValorUnitario` | number (double) |  | Valor unitário do serviço |
| `CalculoImposto` | integer (int32) |  | Se o valor do serviço será utilizado para base de cálculo dos impostos. |
| `CFOP` | string |  | Código  fiscal da operação (CFOP) |
| `Tipo` | string |  | Tipo do item: 00 – Mercadoria para Revenda; 01 – Matéria-Prima; 02 – Embalagem; 03 – Produto em Processo; 04 – Produto Acabado; 05 – Subproduto; 06 – Produto Intermediário; 07 – Material de Uso e Consumo; 08 – Ativo Imobilizado; 09 – Serviços; 10 – Outros insumos; 99 – Outras |
| `NumeroSTPis` | integer (int32) |  | Contador da tabela |
| `NumeroSTCofins` | integer (int32) |  | Contador da tabela |
| `ValorBasePisCredito` | number (double) |  | Valor da base de cálculo de PIS referente a crédito do imposto |
| `PorcentagemPisCredito` | number (double) |  | Taxa de PIS referente a crédito do imposto |
| `ValorPisCredito` | number (double) |  | Valor do PIS referente a crédito do imposto |
| `ValorBaseCofinsCredito` | number (double) |  | Valor da base de cálculo de COFINS referente a crédito do imposto |
| `PorcentagemCofinsCredito` | number (double) |  | Taxa de Cofins referente a crédito do imposto |
| `ValorCofinsCredito` | number (double) |  | Valor do COFINS referente a crédito do imposto |
| `NaturezaCredito` | string |  | Natureza do crédito de PIS/COFINS, código da base de cálculo do crédito |
| `NumeroApi` | integer (int32) |  | Código da aplicação do produto |
| `NumeroMscPlc` | integer (int32) |  | Empresa (Empresa Ativa) |
| `AnoPlc` | integer (int32) |  | Ano fiscal (Cada ano irá possuir um plano de contas) |
| `ContaPlc` | string |  | Numero da conta contábil, já com a máscara da conta |
| `STCofins` | string |  | STCofins |

### UAUApi.Models.UAUApi.Models.ItensNotaFiscalEntProduto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Número da empresa |
| `NumeroProduto` | string |  | Número do produto |
| `Numero` | integer (int32) |  | Número interno da nota |
| `NumItem` | string |  | Contador de item da nota. |
| `DescricaoProduto` | string |  | Descrição do produto |
| `Unidade` | string |  | Unidade do produto |
| `Quantidade` | number (double) |  | Quantidade do produto |
| `ValorUnitario` | number (double) |  | Valor unitário do produto |
| `PorcentagemDescricaoProduto` | number (double) |  | Porcentagem de desconto sobre o total do produto. |
| `ValorTotalProduto` | number (double) |  | Valor total do produto |
| `PorcentagemIPI` | number (double) |  | Taxa de IPI do Item |
| `ValorIPI` | number (double) |  | Valor do IPI do produto |
| `IPIIncideICMS` | integer (int32) |  | Se irá incidir ICMS sobre o total do IPI |
| `PorcentagemICMS` | number (double) |  | Taxa de ICMS |
| `PorcentagemReducao` | number (double) |  | Porcentagem de Redução do ICMS |
| `ValorBaseICMS` | number (double) |  | Base de Cálculo do ICMS |
| `ValorICMSProduto` | number (double) |  | Valor do ICMS do produto |
| `SituacaoTributaria` | string |  | Situação tributária formato (00) |
| `ClassificacaoFiscal` | string |  | Classificação fiscal |
| `ValorOutras` | number (double) |  | Valor de outras do produto. |
| `ValorIsenta` | number (double) |  | Valor isento de imposto do produto. |
| `NCM` | string |  | Nomenclatura Comum do Mercosul - O Sistema Harmonizado de Designação e de Codificação de Mercadorias, ou simplesmente Sistema Harmonizado (SH), é um método internacional de classificação de mercadorias, baseado em uma estrutura de códigos e respectivas descrições. |
| `CFOP` | string |  | Código  fiscal da operação (CFOP) |
| `CreditaIPI` | boolean |  | Se irá possuir crédito de IPI. |
| `PorcentagemReducaoIPI` | number (double) |  | Porcentagem de Redução do IPI |
| `ValorBaseIPI` | number (double) |  | Base de Cálculo do IPI |
| `ValorOutrasIPI` | number (double) |  | Valor de outras do IPI do produto. |
| `ValorIsentaIPI` | number (double) |  | Valor de isentas do IPI do produto. |
| `ValorFrete` | number (double) |  | Valor do frete |
| `ValorSeguro` | number (double) |  | Valor do seguro |
| `ValorDespesaAcesso` | number (double) |  | Valor da despesa do acesso |
| `ValorDesconto` | number (double) |  | Valor do desconto |
| `ValorBaseICMSFrete` | number (double) |  | Valor da base de cálculo do INSS adicional |
| `ValorICMSFrete` | number (double) |  | Valor base do ICMS(Frete) |
| `ValorOutrasFrete` | number (double) |  | ValorOutrasFrete |
| `ValorIsentaFrete` | number (double) |  | ValorIsentaFrete |
| `ValorBaseICMSSeguro` | number (double) |  | ValorBaseICMSSeguro |
| `ValorICMSSeguro` | number (double) |  | ValorICMSSeguro |
| `ValorOutrasSeguro` | number (double) |  | ValorOutrasSeguro |
| `ValorIsentaSeguro` | number (double) |  | ValorIsentaSeguro |
| `ValorBaseICMSDespesaAcesso` | number (double) |  | ValorBaseICMSDespesaAcesso |
| `ValorICMSDespesaAcesso` | number (double) |  | ValorICMSDespesaAcesso |
| `ValorOutrasDespesaAcesso` | number (double) |  | ValorOutrasDespesaAcesso |
| `ValorIsentaDespesaAcesso` | number (double) |  | Valor isento de imposto do produto. |
| `ValorBaseICMSSub` | number (double) |  | Base de Cálculo do ICMS substituição tributária |
| `ValorICMSSub` | number (double) |  | Valor do ICMS do produto substituição tributária |
| `PorcentagemICMSSub` | number (double) |  | Porcentagem de ICMS referente a Substituição tributária |
| `Tipo` | string |  | Tipo do item: 00 – Mercadoria para Revenda; 01 – Matéria-Prima; 02 – Embalagem; 03 – Produto em Processo; 04 – Produto Acabado; 05 – Subproduto; 06 – Produto Intermediário; 07 – Material de Uso e Consumo; 08 – Ativo Imobilizado; 09 – Serviços; 10 – Outros insumos; 99 – Outras |
| `NumSTPis` | integer (int32) |  | Contador da tabela |
| `STCofins` | string |  | STCofins |
| `NumSTIcms` | integer (int32) |  | NumSTIcms |
| `ValTotBaseICMS` | number (double) |  | ValorTotalBaseICMS |
| `ValTotICMS` | number (double) |  | ValorTotalICMS |
| `ValTotOutras` | number (double) |  | ValorTotalOutras |
| `ValTotIsenta` | number (double) |  | ValorTotalIsenta |
| `CodigoEAN` | string |  | GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras |
| `ModalidadeBaseICMS_infep` | integer (int32) |  | Modalidade de determinação da BC do ICMS ST: 0 – Preço tabelado ou máximo  sugerido; 1 - Lista Negativa (valor); 2 - Lista Positiva (valor); 3 - Lista Neutra (valor); 4 - Margem Valor Agregado (%); 5 - Pauta (valor); |
| `ModalidadeBaseICMSSub_infep` | integer (int32) |  | Modalidade de determinação da BC do ICMS ST: 0 – Preço tabelado ou máximo  sugerido; 1 - Lista Negativa (valor); 2 - Lista Positiva (valor); 3 - Lista Neutra (valor); 4 - Margem Valor Agregado (%); 5 - Pauta (valor); |
| `PorcMargemICMSSub_infep` | number (double) |  | Percentual da Margem de Valor Adicionado ICMS Substituição Tributária |
| `PorcReducICMSSub_infep` | number (double) |  | Percentual de redução da Base de cálculo do ICMS Substituição tributária |
| `StIPI_infep` | string |  | Situação tributária do IPI |
| `MotivoDesoneracaoICMS_infep` | integer (int32) |  | Motivo da desoneração do ICMS: 1 – Táxi; 2 – Deficiente Físico; 3 – Produtor Agropecuário; 4 – Frotista/Locadora; 5 – Diplomático/Consular; 6 – Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio (Resolução 714/88 e 790/94 – CONTRAN |
| `CodNatOper_infep` | string |  | Código da natureza da operação/prestação |
| `NumSTIpi_infep` | integer (int32) |  | Contador da tabela |
| `NumeroAPI` | integer (int32) |  | Código da aplicação do produto |
| `CEST` | string |  | CEST |
| `NumCSOSN` | integer (int32) |  | NumCSOSN |
| `CSOSN` | string |  | CSOSN |
| `OrigemProduto` | integer (int32) |  | OrigemProduto |
| `PorcentagemCreditoSimplesNacional` | number (double) |  | PorcCreditoSimplesNacional |
| `ValorCreditoSimplesNacional` | number (double) |  | ValorCreditoSimplesNacional |
| `ValorBaseIPIFrete` | number (double) |  | ValorBaseIPIFrete |
| `ValorIPIFrete` | number (double) |  | ValorIPIFrete |
| `ValorOutrasIPIFrete` | number (double) |  | ValorOutrasIPIFrete |
| `ValorIsentaIPIFrete` | number (double) |  | ValorIsentaIPIFrete |
| `ValorBaseIPISeguro` | number (double) |  | ValorBaseIPISeguro |
| `ValorIPISeguro` | number (double) |  | ValorIPISeguro |
| `ValorOutrasIPISeguro` | number (double) |  | ValorOutrasIPISeguro |
| `ValorIsentaIPISeguro` | number (double) |  | ValorIsentaIPISeguro |
| `ValorBaseIPIDespesaAcesso` | number (double) |  | ValorBaseIPIDespesaAcesso |
| `ValorIPIDespesaAcesso` | number (double) |  | ValorIPIDespesaAcesso |
| `ValorOutrasIPIDespesasAcesso` | number (double) |  | ValorOutrasIPIDespesaAcesso |
| `ValorIsentaIPIDespesaAcesso` | number (double) |  | ValorIsentaIPIDespesaAcesso |
| `ValorTotalBaseIPI` | number (double) |  | ValorTotalBaseIPI |
| `ValorTotalIPI` | number (double) |  | ValorTotalIPI |
| `ValorTotalOutrasIPI` | number (double) |  | ValorTotalOutrasIPI |
| `ValorTotalIsentaIPI` | number (double) |  | ValorTotalIsentaIPI |
| `NumMscPlc` | integer (int32) |  | Empresa (Empresa Ativa) |
| `AnoPlc` | integer (int32) |  | Ano fiscal (Cada ano irá possuir um plano de contas) |
| `ContaPlc` | string |  | Numero da conta contábil, já com a máscara da conta |
| `STCBS_infep` | string |  | Situação tributária da CBS |
| `ClassTribCBS_infep` | string |  | Classificação tributária da CBS |
| `PorcentReducaoCBS_infep` | number (double) |  | Percentual de redução do CBS (Imposto sobre Valor Agregado) |
| `PorcentReducaoIBS_infep` | number (double) |  | Percentual de redução do IBS (Imposto sobre Valor Agregado) |
| `PorcCBS_infep` | number (double) |  | Percentual da CBS |
| `PorcCBSEfetiva_infep` | number (double) |  | Percentual efetivo da CBS |
| `PorcIBSUF_infep` | number (double) |  | Percentual do IBS da UF (Unidade Federativa) |
| `PorcIBSUFEfetiva_infep` | number (double) |  | Percentual efetivo do IBS da UF (Unidade Federativa) |
| `PorcIBSMunicipio_infep` | number (double) |  | Percentual do IBS do Município |
| `PorcIBSMunicipioEfetiva_infep` | number (double) |  | Percentual efetivo do IBS do Município |
| `ValBaseCBSIBS_infep` | number (double) |  | Valor da base de cálculo da CBS |
| `ValCBS_infep` | number (double) |  | Valor da CBS |
| `ValIBSUF_infep` | number (double) |  | Valor do IBS da UF (Unidade Federativa) |
| `ValIBSMunicipio_infep` | number (double) |  | Valor do IBS do Município |

### UAUApi.Models.UAUApi.Models.NotaFiscalEntTotalServico

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Número da empresa |
| `NumeroNotaFiscalEletronica` | integer (int32) |  | Contador de documento fiscal por empresa. |
| `ISSNota` | integer (int32) |  | Se vai ser o ISSQN no total da Nota Fiscal |
| `PorcentagemISS` | number (double) |  | Alíquota do issqn |
| `ValorTotalServico` | number (double) |  | Valor total dos serviços |
| `OrigemBaseCalculocISS` | integer (int32) |  | Origem da base de cálculo do ISS |
| `ValorISS` | number (double) |  | Valor o ISSQN da nota fiscal |
| `DeduzirNotaFiscalISS` | boolean |  | Se irá deduzir o valor do ISS do campo Total com deduções. |
| `PorcentagemIRRF` | number (double) |  | Alíquota do IRRF |
| `OrigemBaseCalculoIRRF` | integer (int32) |  | Origem da base de cálculo do IRRF |
| `ValorIRRF` | number (double) |  | Valor o IRRF da nota fiscal |
| `DeduzirNotaFiscalIRRF` | boolean |  | Se irá deduzir o valor do IRRF do campo Total com deduções. |
| `PorcentagemIRPJ` | number (double) |  | Alíquota do IRPJ |
| `OrigemBaseCalculoIRPJ` | integer (int32) |  | Origem da base de cálculo do IRPJ |
| `ValorIRPJ` | number (double) |  | Valor o IRPJ da nota fiscal |
| `DeduzirNotaFiscalIRPJ` | boolean |  | Se irá deduzir o valor do IRPJ do campo Total com deduções. |
| `PorcentagemPIS` | number (double) |  | Alíquota do PIS |
| `OrigemBaseCalculoPIS` | integer (int32) |  | Origem da base de cálculo do PIS |
| `ValorPIS` | number (double) |  | Valor do  PIS da nota fiscal |
| `DeduzirNotaFiscalPIS` | boolean |  | Se irá deduzir o valor do PIS do campo Total com deduções. |
| `PorcentagemCOFINS` | number (double) |  | Alíquota do COFINS |
| `OrigemBaseCalculoCOFINS` | integer (int32) |  | Origem da base de cálculo do COFINS |
| `ValorCOFINS` | number (double) |  | Valor do COFINS da nota fiscal |
| `DeduzirNotaFiscalCOFINS` | boolean |  | Se irá deduzir o valor do COFINS do campo Total com deduções. |
| `PorcentagemCSSL` | number (double) |  | Alíquota da Contribuição social |
| `OrigemBaseCalculoCSSL` | integer (int32) |  | Origem da base de cálculo da Contribuição social |
| `ValorCSSL` | number (double) |  | Valor da Contribuição social da nota fiscal |
| `DeduzirNotaFiscalCSSL` | boolean |  | Se irá deduzir o valor da Contribuição social do campo Total com deduções. |
| `PorcentagemINSS` | number (double) |  | Alíquota do INSS |
| `OrigemBaseCalcINSS_nfets` | integer (int32) |  | Origem da base de cálculo do INSS |
| `ValorINSS` | number (double) |  | Valor do INSS da nota fiscal |
| `DeduzirNotaFiscalINSS` | boolean |  | Se irá deduzir o valor do INSS do campo Total com deduções. |
| `ValorBenSociais` | number (double) |  | Valor dos benefícios sociais |
| `CodigoImpostoIRRF` | string |  | Código do imposto perante SRF |
| `CodigoImpostoIRPJ` | string |  | Código do imposto perante SRF |
| `CodigoImpostoPIS` | string |  | Código do imposto perante SRF |
| `CodigoImpostoCOFINS` | string |  | Código do imposto perante SRF |
| `CodigoImpostoCSSL` | string |  | Código do imposto perante SRF |
| `CodigoImpostoINSS` | string |  | Código do imposto perante SRF |
| `CodigoImpostoISS` | string |  | Código do imposto perante SRF |
| `PorcentagemBaseCalculoISS` | number (double) |  | Porcentagem do total dos serviços, que cobrará imposto, que será utilizado como base para cálculo do ISS |
| `ValorBaseCalculoISS` | number (double) |  | Valor da base de cálculo do ISS |
| `PorcentagemBaseCalculoIRRF` | number (double) |  | Porcentagem do total dos serviços, que cobrará imposto, que será utilizado como base para cálculo do IRRF |
| `ValorBaseCalculoIRRF` | number (double) |  | Valor da base de cálculo DO IRRF |
| `PorcentagemBaseCalculoIRPJ` | number (double) |  | Porcentagem do total dos serviços, que cobrará imposto, que será utilizado como base para cálculo do IRPJ |
| `ValorBaseCalculoIRPJ` | number (double) |  | Valor da base de cálculo do IRPJ |
| `PorcentagemBaseCalculoPIS` | number (double) |  | Porcentagem do total dos serviços, que cobrará imposto, que será utilizado como base para cálculo do PIS |
| `ValorBaseCalculoPIS` | number (double) |  | Valor da base de cálculo do PIS |
| `PorcentagemBaseCalculoCOFINS` | number (double) |  | Porcentagem do total dos serviços, que cobrará imposto, que será utilizado como base para cálculo do COFINS |
| `ValorBaseCalculoCOFINS` | number (double) |  | Valor da base de cálculo do COFINS |
| `PorcentagemBaseCalculoCSSL` | number (double) |  | Porcentagem do total dos serviços, que cobrará imposto, que será utilizado como base para cálculo do CSSL |
| `ValorBaseCalculoCSSL` | number (double) |  | Valor da base de cálculo do CSSL |
| `PorcentagemBaseCalculoINSS` | number (double) |  | Porcentagem do total dos serviços, que cobrará imposto, que será utilizado como base para cálculo do INSS |
| `ValorBaseCalculoINSS` | number (double) |  | Valor da base de cálculo do INSS |
| `ValorParcelaDeduzirIRRF` | number (double) |  | Armazenar o valor da dedução do imposto de renda pessoa fisica |
| `ValorBasePisCredito` | number (double) |  | Valor total da base de cálculo de PIS referente ao crédito do imposto |
| `ValorPisCredito` | number (double) |  | Valor total do PIS referente ao crédito do imposto |
| `ValorBaseCofinsCredito` | number (double) |  | Valor total da base de cálculo de COFINS referente ao crédito do imposto |
| `ValorCofinsCredito` | number (double) |  | Valor do COFINS referente ao crédito do imposto |
| `NumeroCimpISS` | integer (int32) |  | NumeroCimpISS |
| `NumeroCimpIRRF` | integer (int32) |  | NumeroCimpIRRF |
| `NumeroCimpIRPJ` | integer (int32) |  | NumeroCimpIRPJ |
| `NumeroCimpPIS` | integer (int32) |  | NumeroCimpPIS |
| `NumeroCimpCOFINS` | integer (int32) |  | NumeroCimpCOFINS |
| `NumeroCimpCSLL` | integer (int32) |  | NumeroCimpCSLL |
| `NumeroCimpINSS` | integer (int32) |  | NumeroCimpINSS |
| `OrigemBaseCalculoINSSAdicional` | integer (int32) |  | Origem da base de cálculo do INSS adicional |
| `PorcentagemBaseCalculoINSSAdicional` | number (double) |  | Porcentagem da base de cálculo do INSS adicional |
| `PorcentagemINSSAdicional` | number (double) |  | Alíquota de INSS adicional |
| `DeduzirNotaFiscalINSSAdicional` | boolean |  | Se irá deduzir da nota o valor do INSS adiconal |
| `TipoINSSAdicional` | integer (int32) |  | Tipo do INSS adicional: |
| `ValorINSSAdicional` | number (double) |  | Valor do INSS da nota fiscal adicional |
| `ValorBaseCalculoINSSAdicional` | number (double) |  | Valor da base de cálculo do INSS adicional |

### UAUApi.Models.UAUApi.Models.NotaFiscalEndereco

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Numero da empresa da nota fiscal |
| `Numero` | integer (int32) |  | Número de controle interno da nota fiscal |
| `Tipo` | integer (int32) |  | Tipo do endereço: 0-Emitente da nf; 1-Destinatário da nf; |
| `NumeroBairro` | integer (int32) |  | Número do bairro |
| `NumeroLogradouro` | integer (int32) |  | Número do logradouro |
| `NumeroEndereco` | string |  | Numero do endereço |
| `Complemento` | string |  | Complemento do endereço |
| `CNPJ` | string |  | CNPJ/CPF do Emitente da nf; Destinatário da nf ou do Local de retirada da mercadoria |
| `InscrituraEstadual` | string |  | Nº da inscrição estadual do Emitente da nf; Destinatário da nf |
| `InscrituraMunicipal` | string |  | Nº da inscrição municipal do Emitente da nf; Destinatário da nf |
| `TipoPessoa` | integer (int32) |  | Tipo do do 0-Emitente da nf; 1-Destinatário da nf ou do Local de retirada de mercadoria. 0-Física  1-Jurídica |

### UAUApi.Models.UAUApi.Models.NotfiscProc

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Numero da empresa |
| `Numero` | integer (int32) |  | Número do Processo |
| `NumeroParcela` | integer (int32) |  | Número da Parcela |
| `Obra` | string |  | Obra do Processo |
| `DataVencimento` | string (date-time) |  | Data de vencimento da parcela |
| `DataProrrogacao` | string (date-time) |  | Data de prorrogação da parcela |
| `ValorParcela` | number (double) |  | Valor da parcela |
| `ValorAcrescimos` | number (double) |  | Valor dos acréscimos da parcela |
| `ValorDescontos` | number (double) |  | Valor dos descontos da parcela |
| `CodigoBanco` | string |  | Número do banco |
| `ContaBanco` | string |  | Número da conta |
| `ConvenioBanco` | string |  | Convênio do banco |

### UAUApi.Models.UAUApi.Models.ConsultarNFEntradaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ListaNFEntrada` | array de [`UAUApi.Models.UAUApi.Models.NFEntrada`](#uauapimodelsuauapimodelsnfentrada) |  | Lista com notas fiscais especificas para busca. |
| `CodigoEmpresa` | integer (int32) |  | Código da empresa onde foi lançada a nota. |
| `CodigoObra` | string |  | Código da obra *Obra do processo vinculado a nota. |
| `CnpjFornecedor` | string |  | CNPJ/CPF do fornecedor. |
| `CodigoFornecedor` | string |  | Código da pessoa (fornecedor) no UAU. |
| `DataInicial` | string (date-time) |  | Data inicial para busca de notas em um período. |
| `DataFinal` | string (date-time) |  | Data final para busca de notas em um período. |
| `TipoPeriodo` | integer (int32) — valores possíveis: 1, 2 |  | Indica por qual tipo de data irá ser feito o filtro 1 - Entrada ou 2 - Emissão |

### UAUApi.Models.UAUApi.Models.NFEntrada

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoEmpresa` | integer (int32) |  | Código da empresa |
| `NumeroNotaFiscal` | integer (int32) |  | Número de controle da nota fiscal (interno) |
| `NumeroNotaFiscalEletronica` | string |  | Número da nota fiscal eletrônica |
