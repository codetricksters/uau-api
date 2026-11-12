# Shopping

## POST `/api/v{version}/Shopping/ConsultarRendimentoLojista`

**Método que consulta para lançamentos de rendimento de lojista e auditor.**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Shopping.ConsultarRendimentoLojistaRequest`](#uauapimodelsshoppingconsultarrendimentolojistarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Shopping/GravaRendimentos`

**Consulta a situação das vendas dos lojistas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Shopping.GravaRendimentosRequest`](#uauapimodelsshoppinggravarendimentosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Shopping/ImportacaoDeParcelas`

**Importar parcelas de venda tipo Aluguel Shopping.**

Definição Técnica:
1. Importação de parcelas a receber/recebida para vendas do tipo Aluguel Shopping:
 - URI + /api/v{version}/Shopping/ImportacaoDeParcelas
 
Definição de Negócio:
1. Permite importar parcelas a receber/recebida para vendas do tipo Aluguel Shopping com as seguintes regras:
 - Para importação de parcelas A RECEBER, os seguintes campos devem ser desconsiderados ou não preenchidos:
ValorJurosContrato,ValorCorrecao,ValorMulta,ValorCorrecaoAtraso,ValorJurosAtraso,ValorDesconto,ValorAcrescimo,DataRecebimento,
DataCalculoReajuste,ValorRecebimento,BancoDeposito,ContaDeposito,Depositado,DataDeposito,Conciliado,DataConciliacao,ValorDescontoCondicional
 - O campo ParcelaRecebida deve estar com o valor '0', indicando que a parcela não foi recebida.

1. Para importação de parcelas RECEBIDAS, a maioria dos campos devem estar preenchidos, exceto nos casos de Parcela tipo Custa, Parcela Depositada ou Conciliada.
 - O campo ParcelaRecebida deve estar com o valor '1', indicando que a parcela foi recebida.
  - Caso a parcela seja do tipo Custa, os campos TipoDaCusta, ObservacaoCusta, OrigemCusta devem estar preenchidos.
  - Caso o campo Depositado seja '1', os campos ValorRecebimento,BancoDeposito,ContaDeposito e DataDeposito devem estar preenchidos.
  - Caso o campo Conciliado seja '1', os campos ValorRecebimento,BancoDeposito,ContaDeposito,DataDeposito e DataConciliacao devem estar preenchidos.

Anexos:
1. Link para download de exemplos para Postman:
- Exemplo de parcela a receber: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcela-a-Receber.postman_collection.zip
- Exemplo de parcela recebida: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcela-Recebida.postman_collection.zip

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Shopping.ImportacaoDeParcelasShoppingRequest`](#uauapimodelsshoppingimportacaodeparcelasshoppingrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Shopping.ImportacaoDeParcelasShoppingRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Parcelas` | array de [`UAUApi.Models.Shopping.Parcelas.ParcelaShoppingRequest`](#uauapimodelsshoppingparcelasparcelashoppingrequest) | ✓ | Lista de Parcelas a receber/recebidas. |

### UAUApi.Models.Shopping.Parcelas.ParcelaShoppingRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa. |
| `Obra` | string | ✓ | Código da obra. |
| `Numero` | integer (int32) | ✓ | Número da venda. |
| `NumeroParcela` | integer (int32) |  | Numeração da parcela. |
| `TipoParcela` | string | ✓ | Código do tipo da parcela. |
| `NumeroParcelaGeral` | integer (int32) |  | Numeração única da parcela dentro da venda. |
| `DataVencimento` | string (date-time) | ✓ | Data de vencimento da parcela. |
| `ParcelaRecebida` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se a parcela foi recebida. 0 - Não 1 - Sim |
| `ValorPrincipal` | number (double) | ✓ | Valor principal da parcela. |
| `ValorJurosContrato` | number (double) |  | Valor de juros contratual da parcela recebida. |
| `ValorCorrecao` | number (double) |  | Valor de correção da parcela recebida. |
| `ValorMulta` | number (double) |  | Valor de multa por atraso da parcela recebida. |
| `ValorCorrecaoAtraso` | number (double) |  | Valor de correção por atraso da parcela recebida. |
| `ValorJurosAtraso` | number (double) |  | Valor de juros por atraso da parcela recebida. |
| `ValorDesconto` | number (double) |  | Valor de desconto da parcela recebida. |
| `ValorAcrescimo` | number (double) |  | Valor de acréscimo da parcela recebida. |
| `DataRecebimento` | string (date-time) |  | Data de recebimento da parcela. |
| `TaxaPrimeiroJuros` | number (double) | ✓ | Taxa do primeiro juros da parcela. |
| `FrequenciaVencimento` | string | ✓ | Frequência de vencimento utilizada na parcela. |
| `IndiceReajuste` | string | ✓ | Código do índice de reajuste da parcela |
| `Amortizacao` | integer (int32) — valores possíveis: 0, 1, 2, 3 | ✓ | Código do tipo de amortização de juros utilizado na parcela. 0 - Gradiente 1 - Price 2 - SAC 3 - Simples |
| `BeginEndPrice` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se irá utilizar referência Begin ou End quando utilizar o tipo de amortização Price. 0 - Begin 1 - End Caso o campo Amortizacao possua valor diferente de 1 (Price), utilizar sempre o valor 1 (End). |
| `DataInicioReajuste` | string (date-time) | ✓ | Data de inicio de reajuste da parcela. |
| `DataInicioPrimeiroJuros` | string (date-time) | ✓ | Data de início da cobrança do primeiro juros da parcela. |
| `TotalParcelasDoGrupoInformado` | integer (int32) | ✓ | Quantidade de parcelas do grupo da parcela informado pelo usuário. |
| `DataPrimeiraParcelaGrupo` | string (date-time) | ✓ | Data de vencimento da primeira parcela do grupo da parcela. |
| `GrupoPlanoIndexador` | integer (int32) | ✓ | Código do grupo de plano indexador utilizado na parcela. |
| `CobrarJurosPrimeiroPeriodo` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se as parcelas que possuem amortização Price ou SAC terão juros calculo nos casos que a data de vencimento esteja no mesmo mês(frequências mensais ou anuais) ou dia(frequência diária) da data de início de juros. 0 - Não 1 - Sim |
| `DataCalculoReajuste` | string (date-time) |  | Data de cálculo utilizada para calcular o valor de reajuste de uma parcela recebida. |
| `PadraoCobranca` | integer (int32) | ✓ | Código do padrão de cobrança utilizado na parcela. |
| `ValorRecebimento` | number (double) |  | Valor do deposito |
| `BancoDeposito` | integer (int32) |  | Banco do depósito do recebimento. |
| `ContaDeposito` | string |  | Conta do depósito do recebimento. |
| `Depositado` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o recebimento está depositado. 0 - Não 1 - Sim |
| `DataDeposito` | string (date-time) |  | Data de realização do depósito do recebimento. |
| `Conciliado` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o recebimento está conciliado. 0 - Não 1 - Sim |
| `DataConciliacao` | string (date-time) |  | Data de conciliação do depósito do recebimento. |
| `ValorResiduo` | number (double) | ✓ | Valor de resíduo gerado para a parcela. |
| `DataInicioSegundoJuros` | string (date-time) |  | Data de início da cobrança do segundo juros da parcela. |
| `TaxaSegundoJuros` | number (double) | ✓ | Taxa do segundo juros da parcela. |
| `CobrarCorrecaoCusta` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se irá haver cobrança de correção na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarImpostoCusta` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se irá haver cobrança de imposto na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarJurosAtrasoCusta` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se irá haver cobrança de juros por atraso na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarMultaCusta` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se irá haver cobrança de multa por atraso na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarTaxaAdministracaoCusta` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se irá haver cobrança de taxa de administração na parcela Do tipo custa específica. 0 - Não 1 - Sim |
| `TipoDaCusta` | integer (int32) |  | Código do tipo de custa para parcelas do tipo Custas. |
| `ObservacaoCusta` | string |  | Observação da parcela do tipo custa específica. |
| `OrigemCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se a origem da custa é pela obra ou administrativa. 0 - Obra 1 - Administração |
| `RepassarValorLocadorCusta` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se irá haver repasse ao locador para a parcela do tipo custa específica. 0 - Não 1 - Sim |
| `DiasCarenciaMultaJurosAtraso` | integer (int32) | ✓ | Quantidade de dias de carência na cobrança de multa e juros por atraso da parcela. |
| `DiasCarenciaCorrecaoAtraso` | integer (int32) | ✓ | Quantidade de dias de carência na cobrança de correção por atraso da parcela. |
| `CobrarJurosProRata` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se o cálculo do reajuste da parcela será realizado de forma pró-rata.  0 - Não   1 - Sim |
| `TipoSeguro` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica o tipo de seguro para parcelas do tipo seguro. 0 - MIP 1 - DFI |
| `CobrarJurosProRataPrimeiroMes` | integer (int32) — valores possíveis: 0, 1 | ✓ | Indica se o cálculo do reajuste do primeiro mês da parcela será realizado de forma pró-rata.  0 - Não   1 - Sim |
| `ValorDescontoCondicional` | number (double) |  | Valor de desconto condicional da parcela recebida. |
| `DataInicioPeriodoAluguel` | string (date-time) | ✓ | Data de competência da parcela. |
| `HistoricoPadraoDeposito` | string |  | Histórico padrão do depósito. |
| `MeioPreferencialDeRecebimento` | integer (int32) |  | Meio preferencial de recebimento da parcela |

### UAUApi.Models.Shopping.GravaRendimentosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dia` | string (date-time) |  |  |
| `lojista` | boolean |  |  |
| `empresa` | integer (int32) |  |  |
| `obra` | string |  |  |
| `venda` | integer (int32) |  |  |
| `valor_lancamento` | number (double) |  |  |
| `usuario` | string |  |  |
| `tipo_usuario` | integer (int32) |  |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Shopping.ConsultarRendimentoLojistaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_empresa` | integer (int32) |  | Código da empresa que possui a obra com controle de rendimento de lojista e auditor |
| `cod_obra` | string |  |  |
| `num_venda` | integer (int32) |  |  |
| `ini_lancamento` | string (date-time) |  | Data inicial de lançamento da venda registrada com rendimento de lojista e auditor |
| `fim_lancamento` | string (date-time) |  | Data final de lançamento da venda registrada com rendimento de lojista e auditor |
