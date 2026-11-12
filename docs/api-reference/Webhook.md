# Webhook

## POST `/api/v{version}/Webhook/AtualizarPedidoRec`

**Atualizar o pedido de recebimento no UAU de acordo com o retorno da venda ou proposta de venda(recebimento) pela maquininha de cartão**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `request.cpfCnpj` | query | string |  | CPF/CNPJ |
| `request.intencaoVendaId` | query | string |  | ID da intenção de venda |
| `request.intencaoVendaReferencia` | query | string |  | Referência da intenção de venda |
| `request.pedidoId` | query | integer (int32) |  | ID do pedido |
| `request.pedidoReferencia` | query | string |  | Referência do pedido |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Webhook/AtualizarRecebimentoPix`

**Webhook Banco ITAU, para baixa de cobrança PIX**

Definição Técnica:
Definição de Negócio:

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Webhook.PixNotificacaoRecebimentoItauRequest`](#uauapimodelswebhookpixnotificacaorecebimentoitaurequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Webhook.PixNotificacaoRecebimentoItauRequest`](#uauapimodelswebhookpixnotificacaorecebimentoitaurequest) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## GET `/api/v{version}/Webhook/ConfirmarRecebimentoOrdemCompra/{token}`

**Recebe um token da ordem de compra e o decodifica para atualizar o status da ordem de compra automaticamente.**

Alteração : Alexandre Mendes         Data: 19/09/2022
Projeto   : 427564 - Sprint 5 - Engenhanria
Manutenção: Alterado para extrair do token o tipo de resposta, sendo 1 = Aceito ou 3 = Recusado.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `token` | path | string | ✓ |  |
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Webhook.PixNotificacaoRecebimentoItauRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `endToEndId` | string | ✓ |  |
| `txid` | string | ✓ |  |
| `valor` | string | ✓ |  |
| `horario` | string (date-time) | ✓ |  |
| `infoPagador` | string |  |  |
| `devolucoes` | [`Globaltec.UAU.Cobranca.Services.Interfaces.Itau.PixNotificacaoDevolucaoItau`](#globaltecuaucobrancaservicesinterfacesitaupixnotificacaodevolucaoitau) |  |  |
| `pagador` | [`Globaltec.UAU.Cobranca.Services.Interfaces.Itau.IPixNotificacaoPagadorItau`](#globaltecuaucobrancaservicesinterfacesitauipixnotificacaopagadoritau) |  |  |

### Globaltec.UAU.Cobranca.Services.Interfaces.Itau.IPixNotificacaoPagadorItau

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf` | string |  |  |
| `cnpj` | string |  |  |
| `nome` | string |  |  |

### Globaltec.UAU.Cobranca.Services.Interfaces.Itau.PixNotificacaoDevolucaoItau

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id` | string |  |  |
| `rtrId` | string |  |  |
| `valor` | string |  |  |
| `horario` | [`Globaltec.UAU.Cobranca.Services.Interfaces.Itau.IPixNotificacaoHorarioItau`](#globaltecuaucobrancaservicesinterfacesitauipixnotificacaohorarioitau) |  |  |
| `status` | string |  |  |

### Globaltec.UAU.Cobranca.Services.Interfaces.Itau.IPixNotificacaoHorarioItau

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `solicitacao` | string (date-time) |  |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |
