# BoletoServices

## POST `/api/v{version}/BoletoServices/AlterarDataVencimento`

**Altera a data de vencimento do boleto**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio: Permite alterar a data de vencimento de um boleto cadastrado no UAU.
1. Não é permitido alterar a data de vencimento para um boleto excluído.
2. Não é permitido alterar a data de vencimento para um boleto antecipado.
3. Não é permito alterar data de vencimento de um boleto gerado via intermediario digital.
4. Para manutenção de boleto, o campo Nosso Número não pode estar vazio.
5. A nova data de vencimento do boleto não pode ser menor que a data original.
6. Não é permitido alterar a data de vencimento para um boleto dos bancos 246-ABC, 353-SANTANDER e 425-SOCINAL.
7. Não é permitido alterar a data de vencimento para um boleto com tipo de cobrança "Débito Automático" nos bancos; 1 (carteira 2), 341 (carteira 2) e 104 (carteira 5).
8. Para boletos do banco "341 - Itau", "01 - Banco do Brasil", "425 - Banco Socinal"  ou "104 - Caixa Econômica Federal" débito automático, carteira "00 - Débito automático" só é permitido a ação "1 - Cancelamento".
9. Alguns bancos não possuem a opção de alteração de vencimento implementada. A API informará se não puder realizar a alteração.


Anexos:
1. Exemplo Postman: https://ajuda.globaltec.com.br/wp-content/uploads/2019/06/BoletoUAU.postman_collection.zip
2. Exemplo Retorno: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/AlterarDataVencimento.retorno.zip

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.AlterarDataVencimentoRequest`](#uauapimodelsboletoservicesalterardatavencimentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.BoletoServices.AlterarDataVencimentoResponse`](#uauapimodelsboletoservicesalterardatavencimentoresponse) |
| 400 | Parâmetros inválidos. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/ConsultarBoletosDoCliente`

**Consulta boletos de cliente

Consulta os boletos de um determinado cliente exibindo ou não boletos vencidos.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Consulta ou não boletos vencidos.

Definição de Negócio:

Consulta boletos por cliente.
1. Consulta boletos por cliente.
2. Ao definir que não irá mostrar boletos vencidos, serão retornados apenas os boletos a vencer.
3. Ao definir que deve mostrar boletos vencidos, serão retornados boletos vencidos e a vencer.
4. Parcelas que possuem mais de um boleto ativo, não terão os boletos trazidos na consulta, 
   devido a quem For obter/utilizar o retorno, não saber qual dos boletos deve ser impresso e pago.
5. Parcelas que possuem um único boleto ativo, terão os boletos trazidos na consulta.
6. Os boletos serão listados em ordem crescente de vencimento.
7. Os boletos que não tiverem o Nosso número banco preenchidos mão serão mostrados.
8. Serão mostrados somente os boletos que estiverem com os status a seguir:
    - 0 - Normal
    - 1 - Pendente de confirmação de alteração de vencimento
    - 2 - Pendente de cancelamento de boleto
    - 3 - Confirmada alteração de vencimento/cancelamento
    - 4 - Confirmada alteração de vencimento
    - 6 - Registrado online
    - 10 - Pendente para confirmação de alteração de valor do boleto
    - 11 - Confirmada alteração de valor do boleto

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.ConsultarBoletosDoClienteRequest`](#uauapimodelsboletoservicesconsultarboletosdoclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.BoletoServices.BoletoCliente`](#uauapimodelsboletoservicesboletocliente) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/ConsultarBoletosReimpressao`

**Consultar boletos disponíveis para reimpressão**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio: Consultar boletos disponíveis para reimpressão.
1. Valida usuário logado do tipo (pessoa/cliente).
2. Valida código do usuário.
3. Parcelas que possuem mais de um boleto ativo, não terão os boletos trazidos na consulta, 
   devido a quem for obter/utilizar o retorno, não saber qual dos boletos deve ser impresso e pago.
4. Parcelas que possuem um único boleto ativo, terão os boletos trazidos na consulta.
5. Os boletos serão listados em ordem crescente de vencimento'

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.ConsultarBoletosReimpressaoRequest`](#uauapimodelsboletoservicesconsultarboletosreimpressaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Implementado apenas para usuários Do tipo pessoa! - Não existe pessoa cadastrada para acesso ao UAU Web com o login: XXX - Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/ConsultarDadosDoBoleto`

**Busca os dados vinculados a um boleto (inclui boletos agrupados)**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta informações contidas no boleto.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.ConsultarDadosDoBoletoRequest`](#uauapimodelsboletoservicesconsultardadosdoboletorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/ConsultarStatusBoleto`

**Consulta status do boleto**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Possibilita consulta status do boleto.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.ConsultarStatusBoletoRequest`](#uauapimodelsboletoservicesconsultarstatusboletorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.BoletoServices.BoletoStatusRequest`](#uauapimodelsboletoservicesboletostatusrequest) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/GerarPDFBoleto`

**Gerar boleto**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Utilize em conversor de string Base64 para PDF.

Definição de Negócio:
Permite gerar boleto.

1. O parâmetro booleano (true ou false) "ocultar_dados_pessoais" determina se <br />
os dados pessoais do cliente (nome completo e endereço) serão exibidos no PDF do boleto gerado.
2. O parâmetro inteiro "cod_banco" deve ser informado sem zeros a esquerda por se tratar de um número inteiro <br />

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.GerarPDFBoletoRequest`](#uauapimodelsboletoservicesgerarpdfboletorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/GerarPDFCarne`

**Retorna os carnês em formato base64 conforme os dados informados.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request com os dados do usuário para uso do método.
3. O retorno será um base64. Para poder visualizar os carnês, é necessário fazer uma conversão para PDF.

Regras de Negócio:
1. Para realizar a requisição, informar apenas um filtro. Caso o filtro de chaves do boleto for informado, o filtro de venda remessa, não deve ser informado. O mesmo para o caso contrário.
2. CarneTresBoletosPaginaNaVertical, irá gerar três boletos por página
3. CarneDoisBoletosPaginaNaHorizontal irá gerar dois boletos por página na horizontal
4. Informar apenas um dos parametros de layout de carnê por página como true, caso um seja true, o outro deverá ser informado como false.
5. No filtro de venda remessa, caso não deseje passar o numeroRemessa, não o inclua na chave ou passe o valor como 0.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.PDFCarneRequest`](#uauapimodelsboletoservicespdfcarnerequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.PDFCarne.PDFCarneResponse`](#uauapimodelspdfcarnepdfcarneresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/ObterCodigoDeBarras`

**Monta o valor do código de barras do boleto**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Busca o número do código de barras do boleto informado.
2. Caso boleto que deseja consultar seja gerado via intermediário digital informar: código do banco e seu número

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.ObterCodigoDeBarrasRequest`](#uauapimodelsboletoservicesobtercodigodebarrasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/ObterLinhaDigitavel`

**Monta a linha digitável descrição número do código de barras**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta a linha digitável do código de barras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.ObterLinhaDigitavelRequest`](#uauapimodelsboletoservicesobterlinhadigitavelrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/BoletoServices/ObterMensagemDoBoleto`

**Consulta a mensagem do boleto**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta a mensagem do boleto informado nos parâmetros da request.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BoletoServices.ObterMensagemDoBoletoRequest`](#uauapimodelsboletoservicesobtermensagemdoboletorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.BoletoServices.ObterMensagemDoBoletoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `seu_numero` | integer (int64) |  | Seu número do boleto |
| `cod_banco` | integer (int32) |  | Código do banco |
| `cod_empresa` | integer (int32) |  | Código da empresa |
| `instrucao` | string |  | Instrução do boleto |
| `carteira` | string |  | Carteira utilizada |

### UAUApi.Models.BoletoServices.ObterLinhaDigitavelRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigode_barras` | string |  | Código de barras |

### UAUApi.Models.BoletoServices.ObterCodigoDeBarrasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_banco` | string |  | Identificação do Banco |
| `seu_numero` | string |  | Identificação do Boleto seu número |
| `data_venc` | string (date-time) |  | Data de Vencimento do boleto |
| `valor_nominal` | number (double) |  | Valor Nominal do título |
| `campo_livre` | string |  | Campo livre utilizado de acordo com a especificação interna do banco emissor |

### UAUApi.Models.PDFCarne.PDFCarneResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `carne` | string |  | Carnê gerado em base64 |

### UAUApi.Models.BoletoServices.PDFCarneRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `filtroChavesBoleto` | array de [`UAUApi.Models.BoletoServices.FiltroChaveBoleto`](#uauapimodelsboletoservicesfiltrochaveboleto) |  | Filtro de chaves do boleto |
| `filtroVendaRemessa` | [`UAUApi.Models.BoletoServices.FiltroVendaRemessa`](#uauapimodelsboletoservicesfiltrovendaremessa) |  | Filtro de venda e remessa |
| `CarneTresBoletosPaginaNaVertical` | boolean | ✓ | Indica se o carnê terá três boletos por página na vertical |
| `CarneDoisBoletosPaginaNaHorizontal` | boolean | ✓ | Indica se o carnê terá dois boletos por página na horizontal |

### UAUApi.Models.BoletoServices.FiltroVendaRemessa

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `numeroRemessa` | integer (int32) |  | Número da remessa |
| `obra` | string | ✓ | Código da obra |
| `venda` | integer (int32) | ✓ | Código da venda |

### UAUApi.Models.BoletoServices.FiltroChaveBoleto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `banco` | integer (int32) | ✓ | Código do banco |
| `seuNumero` | integer (int32) | ✓ | Seu número |

### UAUApi.Models.BoletoServices.GerarPDFBoletoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_banco` | integer (int32) |  | Número do banco |
| `seu_numero` | integer (int64) |  | Seu número do boleto |
| `ocultar_dados_pessoais` | boolean |  | Ocultar informações do pagador |

### UAUApi.Models.BoletoServices.BoletoStatusRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoBanco` | integer (int32) |  | Número do banco |
| `seuNumero` | integer (int64) |  | Seu número do boleto |
| `status` | integer (int32) |  | Status do boleto (0 - Normal, 1 - Excluída, 2 - Recebida, 3 - Não encontrado) |
| `descricaoStatus` | string |  | Descrição do status(Normal, Excluída,Recebida, Não encontrado) |
| `ocorrencia` | integer (int32) |  | Status da ocorrência do boleto  0 - Emitido para banco                                 1 - Recebimento eletrônico                                 2 - Assistente recebimento                                 3 - Manutenção de venda                                 4 - Boleto excluído                                 5 - Venda excluída                                 6 - Recebimento de parcelas                                 7 - Lançamento de custas                                 8 - Desconto de imposto                                 9 - Acerto final                                 10 - Boleto expirado                                 11 - Excluído pela alteração de vencimento                                 12 - Excluído pela confirmação de cancelamento no arquivo de retorno                                 13 - Excluído pela alteração de nosso número                                 14 - Proposta vendida com boleto válido |
| `descricaoOcorrencia` | string |  | Descrição da ocorrência do boleto |

### UAUApi.Models.BoletoServices.ConsultarStatusBoletoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoBanco` | integer (int32) |  | Número do banco |
| `seuNumero` | integer (int64) |  | Seu número do boleto |

### UAUApi.Models.BoletoServices.ConsultarDadosDoBoletoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_banco` | string |  | Número do Banco |
| `seu_numero` | string |  | Seu Número - Uma das chaves para o boleto |

### UAUApi.Models.BoletoServices.ConsultarBoletosReimpressaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `obra` | string |  | Código da obra |
| `num_venda` | integer (int32) |  | Número da venda/compra realizada pelo cliente |
| `naomostraboleto_vencido` | boolean |  | Indica se irá trazer boletos vencidos ou não True  - Exibe somente os boletos vencidos na data atual ou a vencer False - Exibe todos os boletos |
| `mostrarApenasUltimoBoleto` | boolean |  | Opcional Indica se irá trazer último boleto para parcelas com mais de um boleto True  - Exibe somente o último boleto gerado de cada parcela False - Não exibe boletos de parcelas com mais de um boleto gerado |

### UAUApi.Models.BoletoServices.BoletoCliente

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dataEmissao` | string (date-time) |  | Data de emissão do boleto |
| `valorDocumento` | number (double) |  | Valor do boleto |
| `codBanco` | integer (int32) |  | Código do banco |
| `seuNumero` | integer (int64) |  | Seu número do boleto |
| `dataVencimento` | string (date-time) |  | Data de vencimento do boleto |
| `localPgto` | string |  | Local onde deve efetuar o pagamento |
| `linhaDigitavel` | string |  | linha digitavel do beleto |
| `dataGeracao` | string (date-time) |  | data de geração do boleto |
| `agCodCedente` | string |  | Código do cedente |
| `nossoNumero` | string |  | Nosso número do boleto |
| `instrucao` | string |  | Instrução do preenchimento do boleto |
| `carteira` | string |  | Número da carteira |
| `campoLivre` | string |  | Campo livre do boleto |
| `nomeBanco` | string |  | Nome do banco |
| `descricaoEmpresa` | string |  | Descrição da empresa |
| `descricaoObra` | string |  | Descrição da obra |
| `codEmpresa` | integer (int32) |  | Código da empresa |
| `obraParcela` | string |  | Código da obra da parcela |
| `numeroVenda` | integer (int32) |  | Número da venda ou da proposta de venda |
| `dataEnvioPorEmail` | string (date-time) |  | Data de envio do boleto por email |
| `dataReenvioPorEmail` | string (date-time) |  | Data de reenvio do boleto por email |
| `boletoEnviado` | string |  | Boleto foi enviado |
| `numeroRemessa` | integer (int32) |  | N° da Remessa |

### UAUApi.Models.BoletoServices.ConsultarBoletosDoClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codPessoa` | integer (int32) | ✓ | Código da pessoa |
| `naoMostraBoletoVencido` | boolean |  | Consultar boletos vencidos True  - Não consulta boletos que estiverem vencidos retorna somente os boletos a vencer False - Retorna os boletos vencidos e a vencer, obedecendo a regra de ter somente um boleto por parcela |
| `usuario` | string |  | Login do usuário |
| `tipo_usuario` | integer (int32) |  | Tipo do usuário 0 = USUÁRIO UAU, 1 = USUÁRIO CLIENTE. |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.BoletoServices.AlterarDataVencimentoResponse

Classe usada na resposta do método AlterarDataVencimento da API de boletos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dataEmissao` | string (date-time) |  | Data de emissão do boleto |
| `valorDocumento` | number (double) |  | Valor do documento com multa e juros, se houve |
| `codBanco` | integer (int32) |  | Código do banco do boleto corresponde ao COMPE, também conhecido como Código das Instituições Bancárias na Compensação. |
| `seuNumero` | integer (int64) |  | Seu número do boleto |
| `dataVencimento` | string (date-time) |  | Data do vencimento do boleto |
| `localPgto` | string |  | Informações sobre os locais onde o boleto poderá ser pago |
| `linhaDigitavel` | string |  | Representação numérica do código de barras, porém os números não estão na mesma ordem |
| `dataGeracao` | string (date-time) |  | Data em que o boleto foi gerado ou emitido |
| `agCodCedente` | string |  | Código da agência bancária + Código do cedente da conta bancária |
| `nossoNumero` | string |  | Identificação única do boleto no software emissor deste documento |
| `instrucao` | string |  | Informações para o caixa no momento do pagamento, como por exemplo as taxas de juros e multas que devem ser cobrados |
| `carteira` | string |  | Indica se o boleto é registrado ou não, ele varia conforme cada banco |
| `campoLivre` | string |  | Campo livre utilizado de acordo com a especificação interna do banco emissor |

### UAUApi.Models.BoletoServices.AlterarDataVencimentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `seuNumero` | integer (int64) | ✓ | Seu número do boleto |
| `codBanco` | integer (int32) | ✓ | Código do banco do boleto |
| `codEmpresa` | integer (int64) | ✓ | Código da empresa cadastrada no UAU |
| `novaDataVenc` | string (date-time) | ✓ | Nova data de vencimento do boleto |
