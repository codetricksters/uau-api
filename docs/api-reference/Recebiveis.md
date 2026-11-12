# Recebiveis

## POST `/api/v{version}/Recebiveis/AlterarMeioPreferencialDeRecebimentoDaParcela`

**Altera o meio preferencial de recebimento do cliente.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
Permite alteração na parcela do meio preferencial de recebimento.
Permite consultar a alteração realizada na parcela.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Recebiveis.AlterarMeioPreferencialRequest`](#uauapimodelsrecebiveisalterarmeiopreferencialrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Recebiveis.MeioPreferencialRecebimentoResponse`](#uauapimodelsrecebiveismeiopreferencialrecebimentoresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## GET `/api/v{version}/Recebiveis/ConsultarMeiosPreferenciaisRecebimento`

**Consulta o meio preferencial de recebimento do cliente.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
Permite consultar os meios preferenciais de recebimento que estão ativos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Recebiveis.MeiosRecebimentoResponse`](#uauapimodelsrecebiveismeiosrecebimentoresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## GET `/api/v{version}/Recebiveis/PadraoDeCobranca/{IdEmpresa}/{NumPadraoCobranca}`

**Retorna as chaves pix cadastradas ao CPF/CNPJ informado.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:
1. É necessário que exista uma empresa cadastrada.
2. Numero do padrão de cobrança 0 busca todos os padrões de cobrança.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `IdEmpresa` | path | integer (int32) | ✓ |  |
| `NumPadraoCobranca` | path | integer (int32) | ✓ |  |
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Recebiveis.PadraoCobranca`](#uauapimodelsrecebiveispadraocobranca) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Recebiveis/ParcelasECobrancasDoCliente`

**Consulta as parcelas e cobranças do cliente.**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
 Definição de Negócio:
 1. Busca parcelas e cobranças em aberto do cliente, informando o CPF/CNPJ.
 2. O parametro PesquisaPorNaoTitulares não é obrigatório, se não informado no request ou informado false, buscará somente dos clientes da venda que possuam o tipo 0 - Titular. Caso informado true buscará de todos os clientes da venda independente do tipo.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Recebiveis.ParcelasECobrancasDoClienteRequest`](#uauapimodelsrecebiveisparcelasecobrancasdoclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Recebiveis.RecebiveisResponse`](#uauapimodelsrecebiveisrecebiveisresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Recebiveis.RecebiveisResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Vendas` | array de [`UAUApi.Models.Recebiveis.Venda`](#uauapimodelsrecebiveisvenda) |  | Lista de vendas |

### UAUApi.Models.Recebiveis.Venda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Empresa da venda |
| `Obra` | string |  | Obra da venda |
| `Venda` | integer (int32) |  | Número da venda |
| `ItensVenda` | array de [`UAUApi.Models.Recebiveis.ItensVenda`](#uauapimodelsrecebiveisitensvenda) |  | Itens da venda |
| `ParcelasVenda` | array de [`UAUApi.Models.Recebiveis.ParcelasVenda`](#uauapimodelsrecebiveisparcelasvenda) |  | Parcelas da venda |

### UAUApi.Models.Recebiveis.ParcelasVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumParcela` | integer (int32) |  | Número da parcela |
| `TipoParcela` | string |  | Tipo da parcela |
| `NumGeralParcela` | integer (int32) |  | Número geral da parcela |
| `ValorParcela` | number (double) |  | Valor da parcela. Caso não esteja informado como valor reajustado, irá buscar o valor principal |
| `DataVencimento` | string (date-time) |  | Data de vencimento da parcela |
| `BoletoParcela` | array de [`UAUApi.Models.Recebiveis.BoletosVenda`](#uauapimodelsrecebiveisboletosvenda) |  | Boletos gerados para a parcela |
| `PixParcela` | array de [`UAUApi.Models.Recebiveis.PixVenda`](#uauapimodelsrecebiveispixvenda) |  | Pix gerados para a parcela |

### UAUApi.Models.Recebiveis.PixVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Banco` | integer (int32) |  | Banco emissor do pix |
| `Txid` | string |  | TXID do pix (chave para qualquer busca) |
| `DataVencimento` | string (date-time) |  | Data de vencimento da cobrança pix |
| `ValorPix` | number (double) |  | Valor do pix gerado |
| `Agrupado` | boolean |  | False - Pix normal | True - Pix agrupado (tem duas ou mais parcelas vinculadas ao pix) |

### UAUApi.Models.Recebiveis.BoletosVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodBanco` | integer (int32) |  | Código do banco |
| `SeuNumero` | integer (int32) |  | Seu número do boleto |
| `DataVencimento` | string (date-time) |  | Data de vencimento do boleto |
| `ValorBoleto` | number (double) |  | Valor do boleto |
| `Bolecode` | boolean |  | False - Boleto normal | True - Bolecode (possui pix junto do boleto) |
| `Agrupado` | boolean |  | False - Boleto normal | True - Boleto agrupado (tem duas ou mais parcelas vinculadas no boleto) |

### UAUApi.Models.Recebiveis.ItensVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoProduto` | integer (int32) |  | Código do Produto |
| `DescProduto` | string |  | Descrição do produto |
| `CodigoPersonalizacao` | integer (int32) |  | Código da personalização |
| `Identificador` | string |  | Identificador do item |

### UAUApi.Models.Recebiveis.ParcelasECobrancasDoClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Cpf` | string | ✓ | CPF/CNPJ do cliente |
| `ValorReajustado` | boolean | ✓ | False - Não reajustar | True - Reajustar valores |
| `QtdeParcelas` | integer (int32) |  | Quantidade de parcelas a serem retornadas na venda, a contar da mais antiga a receber |
| `DataInicioVencimento` | string (date-time) |  | Periodo inicial de busca dos vencimentos das parcelas |
| `DataFimVencimento` | string (date-time) |  | Periodo final de busca dos vencimentos das parcelas |
| `PesquisaPorNaoTitulares` | boolean |  | Informa se a busca deverá ser realizada informando o CPF de qualquer cliente ou apenas de titulares da venda |

### UAUApi.Models.Recebiveis.PadraoCobranca

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoEmpresa` | integer (int32) |  | Código da empresa vinculada ao padrão de cobrança conforme cadastro no UAU |
| `CNPJ` | string |  | CNPJ da empresa vinculada ao padrão de cobrança conforme cadastro no UAU |
| `DescricaoEmpresa` | string |  | Descrição da empresa vinculada ao padrão de cobrança conforme cadastro no UAU |
| `NumPadraoCobranca` | integer (int32) |  | Número do padrão de cobrança retornado. Número único por empresa. |
| `DescPadraoCobranca` | string |  | Descrição do padrão de cobrança retornado conforme cadastrado pelo usuário. Descrição livre. |
| `Status` | integer (int32) |  | Status do Padrão de Cobrança. Ativo ou Inativo |
| `CodBanco` | integer (int32) |  | Código do banco conforme Banco Central |
| `DescBanco` | string |  | Nome do Banco |
| `Conta` | string |  | Código da conta |
| `DescConta` | string |  | Descrição da conta |
| `Agencia` | string |  | Código da agência |
| `TipoCobranca` | integer (int32) |  | Tipo de cobrança do padrão. Existe uma tabela que grava os tipos de cobrança disponíveis. São os registros que mostram na visão Tipo da tela de padrão de cobrança |
| `DescTipoCobranca` | string |  | Descrição do tipo de cobrança |
| `Carteira` | string |  | Código da carteira utilizado pelo usuário |
| `ImprimirBoleto` | boolean |  | Informa se o boleto será para impressão ou não. Identifica se após a geração do boleto, mostrará a visualização do PDF do boleto. |
| `IntermediarioDigital` | boolean |  | Indica se este boleto permite operação de intermediação digital |
| `UsaPIX` | string |  | Chave Pix informada para padrão de cobrança que permite emissão de cobrança Pix |
| `BoletoHibrido` | boolean |  | Indica se este padrão de cobrança permite emissão de boleto híbrido (Código de Barras de Boleto + QRCode do Pix) |

### UAUApi.Models.Recebiveis.MeiosRecebimentoResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  | Código do meio de recebimento |
| `Descricao` | string |  | Descrição do meio de recebimento |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Recebiveis.MeioPreferencialRecebimentoResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Empresa |
| `Obra` | string |  | Obra |
| `Venda` | integer (int32) |  | Número da venda |
| `NumeroParcela` | integer (int32) |  | Número da parcela |
| `NumeroParcelaGeral` | integer (int32) |  | Número geral da parcela |
| `TipoParcela` | string |  | Tipo de parcela |
| `MeioPreferencialRecebido` | integer (int32) |  | Código do meio preferencial de recebimento enviado pelo request |
| `MeioPreferencialRecebidoAnterior` | integer (int32) |  | Código do meio preferencial de recebimento anterior |
| `DescricaoMeioPreferencialRecebidoAnterior` | string |  | Descrição do meio preferencial de recebimento anterior |
| `MeioPreferencialRecebidoAtual` | integer (int32) |  | Código do meio preferencial de recebimento |
| `DescricaoMeioPreferencialRecebidoAtual` | string |  | Descrição do meio preferencial de recebimento |

### UAUApi.Models.Recebiveis.AlterarMeioPreferencialRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Empresa |
| `Obra` | string | ✓ | Obra |
| `Venda` | integer (int32) | ✓ | Número da venda |
| `NumeroParcela` | integer (int32) | ✓ | Número da parcela |
| `TipoParcela` | string | ✓ | Tipo de parcela |
| `NumeroParcelaGeral` | integer (int32) | ✓ | Número geral da parcela |
| `MeioPreferencialRecebimento` | integer (int32) | ✓ | Código do novo meio preferencial de recebimento |
