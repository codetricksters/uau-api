# CobrancaPix

## POST `/api/v{version}/Pix/ConsultarPixStatus`

**Consulta o status do registro PIX junto a instituição bancária**

Definição técnica:
- O objetivo desta rota de API e permitir a consulta do status do PIX 

Instituições bancárias suportadas: 
 - 341 = Banco Itaú
 - 246 = Banco Abc
 - 341 = Banco Itaú
 - 756 = Banco Sicoob
 - 237 = Banco Bradesco

Pré requisito:
- Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
    - URL + /api/v{version}/Pix/GerarCobrancaPIX 
Anexos:
- Exemplo Postman: [ALTERAR EXEMPLO]

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: array de [`UAUApi.Models.Venda.ConsultaPixRequest`](#uauapimodelsvendaconsultapixrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consulta realizada com sucesso. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IResultado`](#globaltecuaucobrancaservicesinterfacesiresultado) |
| 400 | Não foi possível realizar suas requisições. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IResultado`](#globaltecuaucobrancaservicesinterfacesiresultado) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pix/GerarCobrancaProposta`

**Solicita o registro de cobrança por PIX de uma ou mais parcelas da venda junto a instituição bancária**

Definição técnica:
- O objetivo desta rota de API é permitir o registro de cobrança por PIX junto a instituição financeira 
- O BASE64 gerado é somente o QRCODE do PIX

Instituições bancárias suportadas: 
 - 341 = Banco Itaú
 - 756 = Banco Sicoob
 - 237 = Banco Bradesco
 - 246 = Banco Abc

Pré requisito:
- Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
    - URL + /api/v{version}/Venda/GerarCobrancaPIX

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.CobrancaPixPropostaRequest`](#uauapimodelsvendacobrancapixpropostarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Registros realizados com sucesso. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IResultado`](#globaltecuaucobrancaservicesinterfacesiresultado) |
| 400 | Não foi possível realizar suas requisições. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IResultado`](#globaltecuaucobrancaservicesinterfacesiresultado) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pix/GerarCobrancaVenda`

**Solicita o registro de cobrança por PIX de uma ou mais parcelas da venda junto a instituição bancária.**

<b>Definição Técnica:</b>
<list type="bullet">
  <item>1. O objetivo desta rota de API é permitir o registro de cobrança por PIX junto à instituição financeira.</item>
  <item>2. O BASE64 gerado é somente o QR Code do PIX.</item>
  <item>3. Instituições bancárias suportadas:</item>
  <list type="bullet">
    <item> - 341 Banco Itaú</item>
    <item> - 756 Banco Sicoob</item>
    <item> - 237 Banco Bradesco</item>
    <item> - 246 Banco ABC</item>
  </list>
</list>
<b>Pré Requisitos:</b>
<list type="bullet">
  <item>1. Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:</item>
  <list type="bullet">
    <item>URL + /api/v{version}/Venda/GerarCobrancaPIX</item>
  </list>
</list>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.CobrancaPixRequest`](#uauapimodelsvendacobrancapixrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Registros realizados com sucesso. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IResultado`](#globaltecuaucobrancaservicesinterfacesiresultado) |
| 400 | Não foi possível realizar suas requisições. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IResultado`](#globaltecuaucobrancaservicesinterfacesiresultado) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pix/PixPorParcelas`

**Retorna as informações do PIX com base na chave de uma ou mais parcelas**

Definição técnica:
- O objetivo desta rota de API é permitir a consulta e retorno das informações dos PIX gerados para uma determinada parcela ou lista de parcelas
- Serão retornados os dados do PIX, caso tenha sido gerado para a(s) parcela(s) requisitada(s)
- Limite máximo de 50 parcelas por requisição

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: array de [`UAUApi.Models.Venda.PixParcelaVendaRequest`](#uauapimodelsvendapixparcelavendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consulta realizada com sucesso. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IResultado`](#globaltecuaucobrancaservicesinterfacesiresultado) |
| 400 | Não foi possível realizar suas requisições. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IResultado`](#globaltecuaucobrancaservicesinterfacesiresultado) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pix/ReimpressaoPix`

**Retorna as informações de impreesão do PIX com o PDF, QRCode e Pix Copia e Cola**

Definição técnica:
- O objetivo desta rota de API é permitir a consulta e retorno das informações do pix de modo que o usuário possa fazer a impressão 
  dos dados de cobrança.
- Será retornado o PDF completo e o QRCode em base64.
- Será retornado o texto do Pix Copia e Cola.

Instituições bancárias suportadas: 
 - 341 = Banco Itaú
 
 - 756 = Banco Sicoob
 
 - 237 = Banco Bradesco

 - 246 = Banco Abc

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultaPixRequest`](#uauapimodelsvendaconsultapixrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Reimpressão do pix realizada com sucesso. | [`Globaltec.UAU.Cobranca.Services.Interfaces.IReimpressao`](#globaltecuaucobrancaservicesinterfacesireimpressao) |
| 400 | Não foi possível realizar suas requisições. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### Globaltec.UAU.Cobranca.Services.Interfaces.IReimpressao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Txid` | string |  |  |
| `RelatorioPDF` | string |  |  |
| `QRCode` | string |  |  |
| `PixCopiaECola` | string |  |  |

### UAUApi.Models.Venda.PixParcelaVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `NumeroVenda` | integer (int32) | ✓ | Número da venda |
| `NumeroParcela` | integer (int32) | ✓ | Número da parcela |
| `TipoParcela` | string | ✓ | Tipo da parcela |
| `NumeroParcelaGeral` | integer (int32) | ✓ | Número geral da parcela |

### UAUApi.Models.Venda.CobrancaPixRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `DataDeCalculo` | string (date-time) | ✓ | Data de cálculo |
| `Antecipar` | boolean | ✓ | Se irá antecipar ou não as parcelas |
| `UsarPadraoPixAvulso` | boolean | ✓ | Se irá usar o padrão de pix avulso cadastrado na obra <list type="bullet"><item>1. Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão de PIX informado,  esse padrão irá sobrepor o padrão da obra, mantendo da configuração de grupo de cobrança.</item></list> |
| `AgruparParcelas` | boolean | ✓ | Se irá agrupar ou não as parcelas |
| `PadraoCobranca` | integer (int32) |  | Número do padrão de cobrança que deve ser utilizado. Se informado, irá desconsiderar o da obra e o da parcela <list type="bullet"><item>1. Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão de PIX informado,  esse padrão irá sobrepor o padrão informado no JSON, o da obra e o da parcela, mantendo da configuração de grupo de cobrança.</item></list> |
| `Parcelas` | array de [`UAUApi.Models.Venda.ParcelaPixVendaRequest`](#uauapimodelsvendaparcelapixvendarequest) | ✓ | Lista com as parcelas para gerar a cobrança |

### UAUApi.Models.Venda.ParcelaPixVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `NumeroVenda` | integer (int32) | ✓ | Número da venda |
| `NumeroParcela` | integer (int32) | ✓ | Número da parcela |
| `TipoParcela` | string | ✓ | Tipo da parcela |
| `NumeroParcelaGeral` | integer (int32) | ✓ | Número geral da parcela |
| `ValorDesconto` | number (double) |  | Valor do desconto. |

### UAUApi.Models.Venda.CobrancaPixPropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `DataDeCalculo` | string (date-time) | ✓ | Data de cálculo das parcelas |
| `Antecipar` | boolean | ✓ | Se irá antecipar ou não as parcelas |
| `UsarPadraoPixAvulso` | boolean | ✓ | Se irá usar o padrão de pix avulso cadastrado na obra |
| `AgruparParcelas` | boolean | ✓ | Se irá agrupar ou não as parcelas |
| `PadraoCobranca` | integer (int32) |  | Número do padrão de cobrança que deve ser utilizado. Se informado, irá desconsiderar o da obra e o da parcela |
| `Parcelas` | array de [`UAUApi.Models.Venda.ParcelaPixPropostaRequest`](#uauapimodelsvendaparcelapixpropostarequest) | ✓ | Lista com as parcelas para gerar a cobrança |

### UAUApi.Models.Venda.ParcelaPixPropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `NumeroProposta` | integer (int32) | ✓ | Número da proposta |
| `NumeroParcela` | integer (int32) | ✓ | Número da parcela |
| `TipoParcela` | string | ✓ | Tipo da parcela |
| `NumeroParcelaGeral` | integer (int32) | ✓ | Número geral da parcela |
| `ValorDesconto` | number (double) | ✓ | Valor do desconto. |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### Globaltec.UAU.Cobranca.Services.Interfaces.IResultado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Sucesso` | boolean |  |  |
| `Status` | integer (int32) |  |  |
| `StatusRetBanco` | string |  |  |
| `Codigo` | integer (int32) |  |  |
| `GrupoParcela` | integer (int32) |  |  |
| `TxId` | string |  |  |
| `Mensagens` | object |  |  |
| `pixLink` | string |  |  |
| `emv` | string |  |  |
| `imagemBase64` | string |  |  |
| `NotificacaoDeErros` | object |  |  |

### UAUApi.Models.Venda.ConsultaPixRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `TxId` | string | ✓ | Identificador da transação PIX |
