# ModeloVenda

## POST `/api/v{version}/ModeloVenda/BuscarPlanoIndexador`

**Seleciona os dados do plano Indexador de um modelo de venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta o plano indexador vinculado ao modelo da venda.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ModeloVenda.BuscarPlanoIndexadorRequest`](#uauapimodelsmodelovendabuscarplanoindexadorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ModeloVenda/ConsultarModeloDeVenda`

**Consulta o modelo de venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta o modelo da venda filtrando os parâmetros informados na request.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ModeloVenda.ConsultarModeloDeVendaRequest`](#uauapimodelsmodelovendaconsultarmodelodevendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ModeloVenda/ConsultarModeloDeVendaSeguroPorChave`

**Consulta o seguro do modelo de venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta o mo seguro do modelo de venda filtrando pela chave/número do modelo.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ModeloVenda.ConsultarModeloDeVendaSeguroPorChaveRequest`](#uauapimodelsmodelovendaconsultarmodelodevendaseguroporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ModeloVenda/ConsultarModeloVenda`

**Consultar o modelo de venda por chave**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta o modelo de vendo filtrando pelo código do modelo.

Tipos de Caps:

Tipo Parcelamento: 0 - Contrato                  
1. 0 - Principal                                 
2. 1 - Corr. por atraso                          
3. 2 - Juros contratual                          
4. 3 - Correção                                  
5. 4 - Multa por atraso                          
6. 5 - Juros por atraso                          
7. 6 - Acrescimo                                 
8. 7 - Desconto                                  
9. 8 - Desconto por antecipação                  
10. 9 - Taxa de boleto                           
11. 10 - Desconto custas                         
12. 11 - Repasse                                 
13. 12 - Desconto condicional                    

Tipo Parcelamento: 1 - Custas | 3 - Honorário
1. 0 - Principal
2. 1 - Juros contratual
3. 2 - Correção
4. 3 - Multa por atraso
5. 4 - Juros por atraso
6. 5 - Corr. por atraso
7. 6 - Acréscimo
8. 7 - Desconto
9. 8 - Desconto por antecipação
10. 9 - Taxa de boleto
11. 10 - Desconto custa
12. 11 - Repasse
13. 12 - Desconto condicional

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ModeloVenda.ConsultarModeloVendaRequest`](#uauapimodelsmodelovendaconsultarmodelovendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar modelo de venda | [`UAUApi.Models.ModeloVenda.ConsultarDadosModeloVenda`](#uauapimodelsmodelovendaconsultardadosmodelovenda) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ModeloVenda/ConsultarParcelasModeloVenda`

**Consultar parcelas do modelo de vendas


De to´do tipo de parcelamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consultar todos os tipo de parcelas do modelo de venda filtrando pela chave/número do modelo.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ModeloVenda.ConsultarParcelasModeloVendaRequest`](#uauapimodelsmodelovendaconsultarparcelasmodelovendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ModeloVenda/GerarParcelasProposta`

**Gerar parcelas da proposta baseado em parametros de parcelas. Pode ser usado para propostas e vendas.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Gera parcelas da proposta baseado nos parametros de parcelas informado.
2. Valida os campos passados na request.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ModeloVenda.GerarParcelasPropostaRequest`](#uauapimodelsmodelovendagerarparcelaspropostarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.ModeloVenda.PropostaParcelasGeradas`](#uauapimodelsmodelovendapropostaparcelasgeradas) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ModeloVenda/MontarModeloRenegociacao`

**Monta modelo de renegociação com os parâmetros das parcelas e as parcelas.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:

Permite gerar parâmetros do modelo e as parcelas para uma renegociação.
1. Somente usuários autenticados podem ter acesso a essa rota.
2. As informações recebidas no request devem existirem no UAU.
3. O modelo de venda deve estar aprovado para ser utilizado.
4. O modelo de venda informada está vinculado a empresa/obra informada.
5. Os valores de custas, seguros e contratos devem estar configurados para o modelo.

Atenção:
1. Os campos DtIdxParc e DtJurParc são postos como o dia atual da venda caso o modelo esteja configurada para receber a data da venda.

Anexos:

- Exemplo Postman: https://ajuda.globaltec.com.br/download/777189/
- Exemplo Retorno: https://ajuda.globaltec.com.br/download/777192/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ModeloVenda.MontarModeloRenegociacaoRequest`](#uauapimodelsmodelovendamontarmodelorenegociacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Modelo de renegociação gerado com sucesso. | [`UAUApi.Models.ModeloRenegociacao.ModeloRenegociacao`](#uauapimodelsmodelorenegociacaomodelorenegociacao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.ModeloRenegociacao.ModeloRenegociacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `parametroParcelas` | array de [`UAUApi.Models.ModeloVenda.PropostaParamModeloVenda`](#uauapimodelsmodelovendapropostaparammodelovenda) |  | Lista dos modelos de negociação |
| `Parc_Geradas` | array de [`UAUApi.Models.Venda.RenegociarVenda.ParcelaRenegociacaoRequest`](#uauapimodelsvendarenegociarvendaparcelarenegociacaorequest) |  | Lista de parcelas geradas. |

### UAUApi.Models.Venda.RenegociarVenda.ParcelaRenegociacaoRequest

Dados das parcelas renegociados pela API

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumParc_pg` | integer (int32) | ✓ | Número da parcela |
| `NumParcGer_pg` | integer (int32) | ✓ | Número geral da parcela (identificador) |
| `Tipo_pg` | string | ✓ | Tipo da parcela |
| `Valor_pg` | number (double) | ✓ | Valor principal |
| `Data_pg` | string (date-time) | ✓ | Data de vencimento |
| `DtParc_pg` | string (date-time) | ✓ | Data da primeira parcela do grupo Preencher com a data de vencimento da primeira parcela |
| `AmortParc_pg` | integer (int32) | ✓ | Tipo de amortização 0-Gradiente 1-Price 2-SAC 3-Simples |
| `BeginEndParc_pg` | integer (int32) | ✓ | 0-Begin ou 1-End (quando for amortização PRICE) |
| `GrupoParc_pg` | integer (int32) | ✓ | Número do grupo que a parcela pertence |
| `TotParcGrupo_pg` | integer (int32) | ✓ | Total de parcelas do grupo |
| `ComoParc_pg` | string | ✓ | Frequência de vencimento (mensal, semestral, anual etc...) |
| `DtJurParc_pg` | string (date-time) | ✓ | Data de início de cobrança da 1ª taxa de juros contratuais |
| `JurosParc_pg` | number (double) | ✓ | 1ª Taxa de juros contratual |
| `DataSegJuros_pg` | string (date-time) |  | Data de início de cobrança da 2ª taxa de juros contratuais |
| `PorcSegJuros_pg` | number (double) |  | 2ª Taxa de juros contratual |
| `DtIdxParc_pg` | string (date-time) | ✓ | Data do início da correção indexada |
| `IdxReaj_pg` | string | ✓ | Código do índice de reajuste |
| `GrupoIdx_pg` | integer (int32) | ✓ | Número do plano indexador utilizado no cálculo |
| `DtJurosComJuros_pg` | integer (int32) | ✓ | Cobrar juros no mês/dia da data de juros |
| `CobrarJurosProRata_pg` | integer (int32) | ✓ | Cobrar juros pró-rata |
| `CobrarJurosProRataPrimeiroMes_pg` | integer (int32) | ✓ | Cobrar juros pró-rata 1º mês |
| `CarenciaAtraso_pg` | integer (int32) | ✓ | Dias de carência para multa e juros por atraso |
| `CarenciaAtrasoCorrecao_pg` | integer (int32) | ✓ | Dias de carência para cobrar correção atraso |
| `DataCompetencia_pg` | string (date-time) |  | Data do início do período de aluguel |
| `CobrarMulta_pg` | integer (int32) | ✓ | Cobrar multa (parcela de custas) 0-Não 1-Sim |
| `CobrarJurosAtr_pg` | integer (int32) | ✓ | Cobrar juros por atraso (parcela de custas) 0-Não 1-Sim |
| `CobrarCorrecao_pg` | integer (int32) | ✓ | Cobrar correçao (parcela de custas) 0-Não 1-Sim |
| `CobrarTxAdm_pg` | integer (int32) | ✓ | Cobrar taxa de administração (parcela de custas) 0-Não 1-Sim |
| `CobrarImposto_pg` | integer (int32) | ✓ | Cobrar imposto (parcela de custas) 0-Não 1-Sim |
| `CobrarCPMF_pg` | integer (int32) | ✓ | Cobrar CPMF (parcela de custas) 0-Não 1-Sim |
| `OrigemCusta_pg` | integer (int32) | ✓ | Origem da custa [0 - Obra / 1 - Administração] (parcela de custas) |
| `RepassarLocador_pg` | integer (int32) | ✓ | Repassar locador (parcela de custas) 0-Não 1-Sim |
| `NumCtp_pg` | integer (int32) |  | Tipo da custa [Honorários, IPTU, etc.. cadastro sistema] (parcela de custas) |
| `TipoSeguro_pg` | integer (int32) |  | Tipo de seguro [0 - MIP / 1 - DFI] (parcelas de seguro) |
| `TotParc_pg` | integer (int32) | ✓ | Total de parcelas |
| `Cap_pg` | string | ✓ | Cap principal |
| `CapAcrescimo_pg` | string | ✓ | Cap de acréscimo |
| `CapDesconto_pg` | string | ✓ | Cap de desconto |
| `CapDescontoCusta_pg` | string | ✓ | Cap de desconto de custas |
| `CapDescontoAntec_pg` | string | ✓ | Cap de desconto de antecipação |
| `CapCorrecao_pg` | string | ✓ | Cap de correção |
| `CapCorrecaoAtr_pg` | string | ✓ | Cap de correção por atraso |
| `CapDescontoCondicional_pg` | string | ✓ | Cap de desconto condicional |
| `CapJuros_pg` | string | ✓ | Cap de juros contratual |
| `CapJurosAtr_pg` | string | ✓ | Cap de juros por atraso |
| `CapMulta_pg` | string | ✓ | Cap de multa |
| `CapRepasse_pg` | string | ✓ | Cap de repasse |
| `CapTaxaBol_pg` | string | ✓ | Cap de taxa de boleto |

### UAUApi.Models.ModeloVenda.PropostaParamModeloVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numParametro` | integer (int32) | ✓ | número do prametro do modelo de venda |
| `numParcela` | integer (int32) | ✓ | quantidade de parcelas |
| `valorParcela` | number (double) |  | valor da parcela |
| `valorTotalParcela` | number (double) |  | valor total da parcela |
| `percentualParcela` | number (double) |  | percentual da parcela |
| `dataParcela` | string (date-time) | ✓ | data de cadastro da parcela |
| `dataReajuste` | string (date-time) | ✓ | data de inicio do reajuste |
| `dataJuros` | string (date-time) | ✓ | data de inicio do juros |
| `juros` | number (double) |  | valor do juros |
| `dataSegundoJuros` | string (date-time) |  | data de inicio do segundo juros |
| `percentualSegundoJuros` | number (double) |  | percentual segundo juros |
| `tipoParcela` | string | ✓ | tipo de parcela |
| `frequencia` | string | ✓ | código frequencia |
| `amortizacao` | integer (int32) |  | amortização da parcela 0 - Gradiente, 1 - Price, 2 - SAC ou 3 - Simples. |
| `beginEnd` | integer (int32) |  | 0 - Begin  1 - End |
| `reajuste` | string | ✓ | índice de reajuste da parcela quando não for utilizar um plano indexador |
| `JurosComJuros` | integer (int32) |  | Aceita valores de 0 e 1. Indica se as parcelas que possuem amortização Price ou SAC terão juros calculados nos casos que a data de vencimento esteja no mesmo mês(frequências mensais ou anuais) ou dia(frequência diária) da data de início de juros |
| `planoIndexParcela` | integer (int32) |  | plano indexador da parcela, quando não tiver plano informar 1. |
| `tipoValor` | integer (int32) |  | tipo do valor da parcela (0 - percentual, 1 - valor) |
| `carenciaAtraso` | integer (int32) |  | quantidade de dias carência por atraso |
| `carenciaAtrasoCorrecao` | integer (int32) |  | quantidade de dias de carência para cobrança de correção por atraso |
| `cobrarJurosProRata` | integer (int32) |  | juros pro rata |
| `cobrarJurosProRataPrimeiroMes` | integer (int32) |  | realizar o cálculo de juros no primeiro mês como pró-rata. (0 - Não,  1 - Sim") |
| `competencia` | integer (int32) |  | Qual a competência da parcela: 0 - Mês anterior, 1 - Mês atual ou 2 - Mês de geração. |
| `numModeloVenda` | integer (int32) |  | Número do modelo de venda. |
| `tipoContrato` | integer (int32) |  | Tipo de contrato: 0 - Contrato, 1 - Custas, 2 - Seguro, 3 - Honorarios |
| `cap` | string |  | Cap do valor principal da parcela |
| `capCorrecaoAtraso` | string |  | Cap do valor de correção por atraso da parcela |
| `capJuros` | string |  | Cap do valor de juros da parcela |
| `capCorrecao` | string |  | Cap do valor de correção/reajuste da parcela |
| `capMulta` | string |  | Cap do valor de multa da parcela |
| `capJurosAtraso` | string |  | Cap do valor de juros por atraso da parcela |
| `capAcrescimo` | string |  | Cap do valor de acréscimo da parcela |
| `capDesconto` | string |  | Cap do valor de desconto da parcela |
| `capDescontoAntecipado` | string |  | Cap do valor de desconto antecipado (do juros) da parcela |
| `capTaxaBoleto` | string |  | Cap do valor de taxa de boleto da parcela |
| `capDescontoCusta` | string |  | Cap do valor de desconto de custas da parcela |
| `capRepasse` | string |  | Cap do repasse da parcela |
| `capDescontoCondicional` | string |  | Cap do valor de desconto condicional da parcela |
| `tipoParcelamento` | integer (int32) |  | tipo de parcelamento     0 - Contrato     1 - Custas     2 - Seguro     3 - Honorário |
| `NumCtp` | integer (int32) |  | Tipo de custas |
| `OrigemCusta` | integer (int32) |  | Tipo da origem de custas |
| `cobrarMulta` | integer (int32) |  | Cobrar multa ou não para custas |
| `cobrarJurosAtraso` | integer (int32) |  | Cobrar juros por atraso ou não para custas |
| `cobrarImposto` | integer (int32) |  | Cobrar imposto ou não para custas |
| `cobrarCorrecao` | integer (int32) |  | Cobrar correção/reajuste para custas |
| `cobrarCPMF` | integer (int32) |  | cobrar CPMF para custas |
| `repassarLocador` | integer (int32) |  | Repassar ao locador valor das custas |
| `tipoSeguro` | integer (int32) |  | Tipo de seguro |
| `CobrarTaxaAdm` | integer (int32) |  | Cobrar taxa administrativa de aluguel |

### UAUApi.Models.ModeloVenda.MontarModeloRenegociacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codModeloVenda` | integer (int32) | ✓ | Código do modelo de renegociação |
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra da empresa |
| `numVenda` | integer (int64) | ✓ | Número da venda |
| `ValorRenegContrato` | number (double) |  | Valor da renegociação do contrato |
| `ValorRenegCustas` | number (double) |  | Valor da renegociação das custas |
| `ValorRenegSeguroMIP` | number (double) |  | Valor da renegociação do seguro MIP |
| `ValorRenegSeguroDFI` | number (double) |  | Valor da renegociação do seguro DFI |

### UAUApi.Models.ModeloVenda.PropostaParcelasGeradas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `chaveParcelaGerada` | integer (int32) |  | chave da parcela gerada |
| `numeroParcela` | integer (int32) |  | número da parcela gerada |
| `dataVencimento` | string (date-time) |  | data de vencimento da parcela |
| `valorParcela` | number (double) |  | valor da parcela |
| `tipoParcela` | string |  | tipo de parcela |
| `planoIndexReajuste` | string |  | plano indexador para reajueste |
| `jurosParcela` | number (double) |  | valor do juros da parcela |
| `dataJurosParcela` | string (date-time) |  | data de inicio do juros da parcela |
| `dataPlanoIndexParcela` | string (date-time) |  | data inicio do plano indexador da parcela |
| `valorReajustadoParcela` | number (double) |  | valor reajustado da parcela |
| `tipoVencimentoParcela` | string |  | tipo de vencimento da parcela |
| `amortizacaoParcela` | integer (int32) |  | amortização da parcela |
| `beginEndParcela` | integer (int32) |  | 0 - Begin  1 - End da parcela |
| `qtdTotalParcela` | integer (int32) |  | quantidade total de parcela |
| `dataIncioParcela` | string (date-time) |  | data de incio da parcela |
| `planoIndexParcela` | integer (int32) |  | plano indexador da parcela |
| `grupoParcela` | integer (int32) |  | código do grupo de parcela |
| `qtdTotalGrupo` | number (double) |  | quantidade total de parcelas do grupo |
| `jurosComJuros` | integer (int32) |  | Cobrar juros caso a parcelas esteja no mesmo mês ou no mesmo dia da data de inicio do juros |
| `dataSegundoJuros` | string (date-time) |  | data de incio do segundo juros |
| `percentualSegundoJuros` | number (double) |  | percentual do sengundo juros |
| `carenciaAtraso` | integer (int32) |  | quantidade de dias carência por atraso |
| `carenciaAtrasoCorrecao` | integer (int32) |  | quantidade de dias de carência para cobrança de correção por atraso |
| `cobrarJurosProRata` | integer (int32) |  | cobrar juros pro rata |
| `cobrarJurosProRataPrimeiroMes` | integer (int32) |  | cobrar juros no primeiro mês como pró-rata. (0 - Não,  1 - Sim") |
| `dataInicioAluguel` | string (date-time) |  | data de competência do aluguel |
| `cobrarTaxaAdministrativa` | integer (int32) |  | cobrar taxa administrativa |
| `cap` | string |  | Cap do valor de principal da parcela |
| `capCorrecaoAtraso` | string |  | Cap do valor de correção por atraso da parcela |
| `capJuros` | string |  | Cap do valor de juros da parcela |
| `capCorrecao` | string |  | Cap do valor de correção da parcela |
| `capMulta` | string |  | Cap do valor de multa da parcela |
| `capJurosAtraso` | string |  | Cap do valor de juros por atraso da parcela |
| `capAcrescimo` | string |  | Cap do valor de acréscimo da parcela |
| `capDesconto` | string |  | Cap do valor de desconto da parcela |
| `capDescontoAntecipado` | string |  | Cap do valor de desconto antecipado (juros) da parcela |
| `capTaxaBoleto` | string |  | Cap do valor de taxa de boleto da parcela |
| `capDescontoCusta` | string |  | Cap do valor de desconto de custa da parcela |
| `capRepasse` | string |  | Cap do repasse da parcela |
| `capDescontoCondicional` | string |  | Cap do valor de desconto condicional da parcela |
| `tipoParcelamento` | integer (int32) |  | 0 - Contrato 1 - Custas 2 - Seguro 3 - Honorário |
| `NumCtp` | integer (int32) |  | Tipo da custa |
| `OrigemCusta` | integer (int32) |  | Tipo da origem de custas |
| `cobrarMulta` | integer (int32) |  | Cobrar multa por atraso em parcela de custa |
| `cobrarJurosAtraso` | integer (int32) |  | Cobrar juros por atraso em parcela de custa |
| `cobrarImposto` | integer (int32) |  | Cobrar imposto em parcela de custa |
| `cobrarCorrecao` | integer (int32) |  | Cobrar correção/reajuste em parcela de custa |
| `cobrarCPMF` | integer (int32) |  | Cobrar CPMF em parcela de custa |
| `repassarLocador` | integer (int32) |  | Repassar valor da custa para o locador no repasse |
| `tipoSeguro` | integer (int32) |  | Tipo de seguro da parcela de seguro |
| `meioPreferencialRecebimento` | integer (int32) |  | Meio preferencial de recebimento |

### UAUApi.Models.ModeloVenda.GerarParcelasPropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `parametromodelovenda` | array de [`UAUApi.Models.ModeloVenda.PropostaParamModeloVenda`](#uauapimodelsmodelovendapropostaparammodelovenda) | ✓ | Lista com os parametro para gerar as parcelas |
| `codigoEmpresa` | integer (int32) | ✓ | Código do modelo de venda |
| `codigoObra` | string | ✓ | Código da obra |
| `redistribuirValor` | boolean |  | Irá redistribuir valor da parcela |
| `utilizarCap` | boolean |  | Irá utlizar cap para gerar as parcelas |
| `tipoVenda` | integer (int32) |  | Tipo da venda |

### UAUApi.Models.ModeloVenda.ConsultarParcelasModeloVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nummodelo_venda` | integer (int32) | ✓ | Número do modelo de vendas |

### UAUApi.Models.ModeloVenda.ConsultarDadosModeloVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `modeloVenda` | [`UAUApi.Models.ModeloVenda.ModeloVenda`](#uauapimodelsmodelovendamodelovenda) |  | Modelo da venda |

### UAUApi.Models.ModeloVenda.ModeloVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numModeloVenda` | integer (int32) |  | código do modelo de venda |
| `descricao` | string |  | descrição do modelo de venda |
| `gerarResiduo` | integer (int32) |  | vai gerar resíduo |
| `reajusteAnual` | integer (int32) |  | possui reajuste anual |
| `correcaoAtraso` | integer (int32) |  | vai cobrar correção por atraso |
| `qtdDiasRetroagir` | integer (int32) |  | quantidade de dias que vai retroagir |
| `cobrarJurosContrato` | integer (int32) |  | em caso de atraso vai cobrar juros contratual |
| `correcaoProRata` | integer (int32) |  | o calculo do reajuste será Pro-Rata |
| `tipoAntecipacao` | integer (int32) |  | o tipo de antecipação será pro-rata |
| `multa` | number (double) |  | valor da multa |
| `juros` | number (double) |  | valor do juros |
| `diasCarencia` | integer (int32) |  | quantidade de dias de carencia |
| `planoIndexador` | integer (int32) |  | o contrato possui plano indexador |
| `usuarioCad` | string |  | usuário que cadastrou o modelo de venda |
| `dataCadastro` | string (date-time) |  | data que cadastrou o modelo de venda |
| `statusModeloVenda` | integer (int32) |  | status do modelo de venda( 0 - Ativo / 1 - Inativo) |
| `possuiAniversarioContrato` | integer (int32) |  | o modelo de venda possui aniversário de contrato. |
| `cobrarTaxaBoleto` | integer (int32) |  | cobrar taxa de boleto (0 - Não cobrar taxa 1 - Cobrar taxa) |
| `capProvisaoCurtoPrazo` | string |  | código do CAP provisão curto prazo |
| `capProvisaoLongoPrazo` | string |  | código do CAP provisão longo prazo |
| `cobrarCorrecaoAtrasoCarencia` | integer (int32) |  | cobrar a correção por atraso apenas após acarência definida nesse campo |
| `antecipaCorrecao` | integer (int32) |  | cobrado correção diária nas parcelas antecipadas para contrato que possui correção anual |
| `cobrarJurosRecebidaDataJuros` | integer (int32) |  | cobrar juros para parcelas recebida após a data que inciou o juros |
| `multaFracionada` | boolean |  | a multa será fracionada diáriamente (false-Não fracionada, true-fracionada) |
| `antecipaJurosLinear` | boolean |  | vai antecipar juros linear |
| `periodoMesReajuste` | integer (int32) |  | frequencia da correção será anual ou semestral (12 meses, 6 meses) |
| `zerarCorrecaoNegativa` | boolean |  | vai zarer correção negativa |
| `juroAtrasoMensal` | boolean |  | cobrar juros por atraso mensal |
| `correcaoCrescente` | boolean |  | cobrar correção crescente |
| `correcaoAtrasoPerson` | boolean |  | cobrar correção dos dias de atraso, será cobrado a correção do mês mais os dias de atraso |
| `diaRepasseAluguel` | integer (int32) |  | dia do mês que será repassado o valor do aluguel. |
| `anexos` | integer (int32) |  | anexos do modelo de venda |
| `modeloVendaAprovado` | boolean |  | modelo venda está aprovado |
| `jurosAnual` | integer (int32) |  | o juros serão mensais (0 - Mensais, 1 - Não Mensais) |
| `periodoMesJuros` | integer (int32) |  | período do juros caso não seja mensal (12 - Anual, 6 - Semestral) |
| `buscarDataBaseResiduo` | integer (int32) |  | vai buscar data base de resíduo por: 0 - Data base de resíduo informada 1 - Data base de resíduo deve ser igual a data do ato da venda. 2 - Busca uma diferença de meses entre a data da venda. |
| `dataBaseResiduo` | string (date-time) |  | informar data base de resíduo |
| `difMesesBaseResiduo` | integer (int32) |  | diferença da quantidade de meses em relação a data base de resíduo e a data da venda. |
| `correcaoAntecProxAnivContrato` | boolean |  | calcular a correção por antecipação apenas no próximo aniversário de contrato. (0 - Não 1 - Sim) |
| `histLancVenda` | string |  | historico do lançamento da venda |
| `histLancRecebidas` | string |  | historico do lançamento para parcelas recebidas |
| `histLancProvJurosCorrecao` | string |  | historico do lançamento de provisão de juros e correção |
| `histLancImposto` | string |  | historico do lançamento de imposto |
| `cobrarHonorario` | boolean |  | cobrar honorário (0 - Não, 1 - Sim) |
| `percentHonorarioRenegociacao` | number (double) |  | valor em percentual do honorário cobrado sobre o saldo renegociado |
| `modeloVendaParcela` | array de [`UAUApi.Models.ModeloVenda.ModVenParcela`](#uauapimodelsmodelovendamodvenparcela) |  | Informações do parcelamento do modelo de venda |
| `modeloVendaSeguro` | array de [`UAUApi.Models.ModeloVenda.ModeloVendaSeguro`](#uauapimodelsmodelovendamodelovendaseguro) |  | Informações do seguro do modelo de venda |
| `modeloVendaImposto` | array de [`UAUApi.Models.ModeloVenda.ModeloVendaImposto`](#uauapimodelsmodelovendamodelovendaimposto) |  | Informações do imposto do modelo de venda |
| `modeloVendaPlanoIdx` | array de [`UAUApi.Models.ModeloVenda.ModVenPlanoIdx`](#uauapimodelsmodelovendamodvenplanoidx) |  | Informações do plano indexador do modelo de venda |
| `modeloVendaCap` | array de [`UAUApi.Models.ModeloVenda.ModVenCap`](#uauapimodelsmodelovendamodvencap) |  | Informações dos CAPS do modelo de venda |
| `modeloVendaObra` | array de [`UAUApi.Models.ModeloVenda.ModVenObr`](#uauapimodelsmodelovendamodvenobr) |  | Informações das obras vinculadas ao modelo de venda |
| `TipoContratoRec` | integer (int32) |  |  |
| `MetodoAmortizacao` | integer (int32) |  |  |
| `IndicePrecoPreObra` | integer (int32) |  |  |
| `IndicePrecoPosObra` | integer (int32) |  |  |

### UAUApi.Models.ModeloVenda.ModVenObr

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numModeloVenda` | integer (int32) |  | número do modelo venda |
| `empresa` | integer (int32) |  | código da empresa |
| `obra` | string |  | código da obra |
| `usuario` | string |  | usúario vinculou o modelo de venda a obra |
| `data` | string (date-time) |  | data de vinculo o modelo de venda a obra |
| `observacao` | string |  | bservções do modelo de venda vinculado a obra |
| `tipo` | boolean |  | tipo de modelo de venda vinculado a obra |

### UAUApi.Models.ModeloVenda.ModVenCap

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numModeloVenda` | integer (int32) |  | número do modelo de venda |
| `tipoCap` | integer (int32) |  | tipo de cap |
| `tipoParcelamento` | integer (int32) |  | tipo de parcelamento     0 - Contrato     1 - Custas     2 - Seguro     3 - Honorário |
| `codCap` | string |  | código do cap |

### UAUApi.Models.ModeloVenda.ModVenPlanoIdx

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numModeloVenda` | integer (int32) |  | número do modelo de venda |
| `numPlanoIdx` | integer (int32) |  | número do plano indexador |
| `codPlanoIdx` | string |  | código do Plano Indexador |
| `buscaDataContrato` | integer (int32) |  | buscar a data da inicio da data do contrato |
| `data` | string (date-time) |  | data de ínicio de incidência do índice |
| `difQtdMesDataContrato` | integer (int32) |  | diferença da quantidade de meses em relação a data de início do índice e a data do contrato. |

### UAUApi.Models.ModeloVenda.ModeloVendaImposto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numModeloVenda` | integer (int32) |  | número do modelo de venda |
| `codDesconto` | string |  | código do imposto |
| `codCap` | string |  | código do cap do imposto |

### UAUApi.Models.ModeloVenda.ModeloVendaSeguro

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numModeloVenda` | integer (int32) |  | número do modelo de venda |
| `tipoSeguro` | integer (int32) |  | tipo do seguro(0 - MIP (Morte e invalidez permanente do mutuário), 1 - DFI (Danos físicos ao imóvel) |
| `taxaSaldoDevedor` | boolean |  | o valor do seguro é uma taxa em relação ao saldo devedor do contrato |
| `valorSeguro` | number (double) |  | valor do seguro |
| `usuario` | string |  | usúario que cadastrou o seguro |
| `data` | string (date-time) |  | data de cadastro do seguro |
| `codCap` | string |  | código do cap do seguro |

### UAUApi.Models.ModeloVenda.ModVenParcela

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numModeloVenda` | integer (int32) |  | número do modelo de venda |
| `numParcela` | integer (int32) |  | número da parcela |
| `tipoParcela` | string |  | tipo da parcela |
| `qtdParcela` | integer (int32) |  | quantidade de parcela |
| `reajusteParcela` | string |  | tipo de reajuste da parcela |
| `planoIdxParcela` | integer (int32) |  | plano indexador da parcela |
| `jurosParcela` | number (double) |  | valor do juros da parcela |
| `amortizacaoParcela` | integer (int32) |  | amortização da parcela |
| `possuiCorrecaoParcela` | integer (int32) |  | possui correção na parcela |
| `frequenciaParcela` | string |  | frequencia da parcela |
| `porcentagemParcela` | number (double) |  | Porcentagen da parcela |
| `dtJurosComJurosParcela` | integer (int32) |  | calcular juros caso a parcelas esteja no mesmo mês ou no mesmo dia da data de inicio do juros |
| `dataParcela` | string (date-time) |  | data de cadastro da parcela |
| `buscaDtContratoParcela` | integer (int32) |  | a data inicial da parcela será a data do contrato. |
| `dataReajusteParcela` | string (date-time) |  | data de inicio da correção |
| `buscaDtReajusteContrato` | integer (int32) |  | a data inicial de correção será a data do contrato |
| `tipoValorParcela` | boolean |  | o grupo de parcelas possui valor fixo.(0 - Valor Percentual 1 - Valor Fixo) |
| `qtdParcelaCalculado` | boolean |  | a quantidade de parcelas será calculada da data de início de parcela até a data de início de juros (0 - Quantidade fixa 1 - Quantidade variável) |
| `dataJurosParcela` | string (date-time) |  | data de inicio do juros |
| `buscaDtJurosContrato` | integer (int32) |  | a data inicial de juros será a data do contrato. |
| `porcSegundoJuros` | number (double) |  | percentual do segundo juros |
| `dataSegundoJuros` | string (date-time) |  | data de inicio do segundo juros |
| `diasCarenciaJurosMulta` | integer (int32) |  | quantidade de dias de carência para cobrança de juros por atraso e multa |
| `diasCarenciaAtrasoCorrecao` | integer (int32) |  | quantidade de dias de carência para cobrança de correção por atraso |
| `cobrarJurosProRata` | integer (int32) |  | juros  pro rata |
| `qtdDifMesesReajusteContrato` | integer (int32) |  | diferença da quantidade de meses em relação a data de início de reajuste e a data do contrato. |
| `qtdDifMesesJurosContrato` | integer (int32) |  | diferença da quantidade de meses em relação a data de início de juros e a data do contrato. |
| `qtdDifMesesContrato` | integer (int32) |  | diferença da quantidade de meses em relação a data de início da parcela e a data do contrato. |
| `cobrarJurosProRataPrimeiroMes` | boolean |  | realizar o cálculo de juros no primeiro mês como pró-rata. (0 - Não,  1 - Sim") |
| `competenciaParcela` | integer (int32) |  | Tipo de competência da parcela |
| `tipoParcelamentoContrato` | integer (int32) |  | Tipo de parcelamento(0 - Contrato, 1 - Custas, 2 - Seguro, 3 - Honorarios) |
| `tipoCusta` | integer (int32) |  | tipo de custa |
| `origemCusta` | integer (int32) |  | Origem da custa (0 - Obra, 1 - Administração) |
| `cobrarMulta` | integer (int32) |  | cobrar multa |
| `cobrarJurosAtraso` | integer (int32) |  | cobrar juros por atraso |
| `cobrarTaxaAdm` | integer (int32) |  | cobrar taxa administrativa |
| `cobrarImposto` | integer (int32) |  | cobrar honorário (0 - Não, 1 - Sim) |
| `cobrarCorrecao` | integer (int32) |  | cobrar correção |
| `cobrarCpmf` | integer (int32) |  | cobrar CPMF |
| `repassarLocador` | integer (int32) |  | irá realizar repasse a locador |
| `beginEndParcela` | integer (int32) |  | begin/end da parcela |

### UAUApi.Models.ModeloVenda.ConsultarModeloVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codModeloVenda` | integer (int32) |  | Código modelo de venda |

### UAUApi.Models.ModeloVenda.ConsultarModeloDeVendaSeguroPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nummodelo_venda` | integer (int32) | ✓ | Número do modelo de vendas |

### UAUApi.Models.ModeloVenda.ConsultarModeloDeVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `obra` | string | ✓ | Código da obra |
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `nummodelo_venda` | integer (int32) | ✓ | Código do Modelo de venda |
| `eat_inat` | integer (int32) — valores possíveis: 0, 1, 2 |  | Status 0-Ativos 1-Inativos 2-Ambos |
| `campos_retornados` | string |  | Nome dos campos a serem retornados |
| `tipo` | integer (int32) | ✓ | Tipo do modelo de venda 0 - Venda 1 - Renegociação |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.ModeloVenda.BuscarPlanoIndexadorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nummodelo_venda` | integer (int32) | ✓ | Número do modelo de venda |
