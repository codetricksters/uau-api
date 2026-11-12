# PedidoCompra

## POST `/api/PedidoCompra/GravaPedidoDeCompra`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `tipo` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 6, 9, 10, 11, 12, 13, 15, 16 | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: object

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |

---

## POST `/api/PedidoCompra/ValidarPermissaoAssistentePedidoServico`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `tipoPedido` | query | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 6, 9, 10, 11, 12, 13, 15, 16 | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: object

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |

---

## POST `/api/v{version}/PedidoCompra/AprovarPedidoCompraMaterialApp`

**Aprovar o item do pedido de material**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Aprovar um item do pedido de material realizado.
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.AprovarPedidoCompraMaterialAppRequest`](#uauapimodelspedidocompraaprovarpedidocompramaterialapprequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/AprovarPedidoCompraServicoApp`

**Aprovar o item do pedido serviço**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Aprovar um item do pedido do tipo serviço.
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.AprovarPedidoCompraServicoAppRequest`](#uauapimodelspedidocompraaprovarpedidocompraservicoapprequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/ConfirmarRecebimentoOrdemCompraFornecedor`

**Método com finalidade de confirmar a cotação.**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
Regras Básicas:

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.ConfirmarRecebimentoOrdemCompraFornecedorRequest`](#uauapimodelspedidocompraconfirmarrecebimentoordemcomprafornecedorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Enviar ordem de compra | array de [`UAUApi.Models.PedidoCompra.ConfirmarRecebimentoOrdemCompraFornecedorResponse`](#uauapimodelspedidocompraconfirmarrecebimentoordemcomprafornecedorresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoAdiantamento`

**Gera um novo pedido de compra do tipo "1 -Adiantamento de Contrato"**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo adiantamento (1).
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoAdiantamentoRequest`](#uauapimodelspedidocompragerarpedidodecompradotipoadiantamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoComplemento`

**Gravar novo pedido de compra do tipo "10 - Complemento"**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo complemento (10).
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoComplementoRequest`](#uauapimodelspedidocompragerarpedidodecompradotipocomplementorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoContratoMaterial`

**Gera um novo pedido de compra do tipo "4 - Contrato de Material"**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo Contrato de material (4).
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoContratoMaterialRequest`](#uauapimodelspedidocompragerarpedidodecompradotipocontratomaterialrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoEmergencial`

**Gera um novo pedido de compra do tipo "6 - Emergêncial"**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo emergêncial (6).
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoEmergencialRequest`](#uauapimodelspedidocompragerarpedidodecompradotipoemergencialrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoMaterial`

**Gravar novo pedido de compra do tipo "0 - Material"**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo material (0).
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoMaterialRequest`](#uauapimodelspedidocompragerarpedidodecompradotipomaterialrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoPatrimonio`

**Gera um novo pedido de compra do tipo "3 - Patrimônio"**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo Patrimônio (3).
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoPatrimonioRequest`](#uauapimodelspedidocompragerarpedidodecompradotipopatrimoniorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoRegularizacao`

**Gravar novo pedido de compra do tipo "9 - Regularização"**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso o pedido não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo regularização (9).
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoRegularizacaoRequest`](#uauapimodelspedidocompragerarpedidodecompradotiporegularizacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServico`

**Gera um novo pedido de compra do tipo "2 - Serviço".**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo Serviço (2).
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoRequest`](#uauapimodelspedidocompragerarpedidodecompradotiposervicorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoAdiantamento`

**Gera um novo pedido de compra do tipo "15 - Serviço adiantamento de contrato".**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo 15 - Serviço adiantamento de contrato.
2. Valida as entradas dos pedidos de compras.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoAdiantamentoRequest`](#uauapimodelspedidocompragerarpedidodecompradotiposervicoadiantamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoComplemento`

**Gera um novo pedido de compra do tipo "13 - Pedido serviço complemento".**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo 13 - Serviço complemento.
2. Valida as entradas dos pedidos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoComplementoRequest`](#uauapimodelspedidocompragerarpedidodecompradotiposervicocomplementorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoContrato`

**Gera um novo pedido de compra do tipo "16 - Serviço contrato".**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo 16 - Serviço contrato.
2. Valida as entradas dos pedidos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoContratoRequest`](#uauapimodelspedidocompragerarpedidodecompradotiposervicocontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoEmergencial`

**Gera um novo pedido de compra do tipo "11 - Pedido serviço emergencial".**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo 11 - Serviço emergencial.
2. Valida as entradas dos pedidos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoEmergencialRequest`](#uauapimodelspedidocompragerarpedidodecompradotiposervicoemergencialrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/PedidoCompra/GravarPedidoDeCompraDoTipoServicoRegularizacao`

**Gera um novo pedido de compra do tipo "12 - Pedido serviço regularização".**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Retorna uma lista de string com os dados do pedido gerado ou uma mensagem de alerta caso não seja gerado corretamente.
    - Posição 0 = Numero do pedido;
    - Posição 1 = mensagem de erro (Caso o pedido não seja gerado corretamente);

Definição de Negócio:
1. Gerar um novo pedido de compra do tipo 12 - Serviço regularização.
2. Valida as entradas dos pedidos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoRegularizacaoRequest`](#uauapimodelspedidocompragerarpedidodecompradotiposervicoregularizacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoRegularizacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido de serviço regularização. |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico`](#uauapimodelspedidocompradadositempedidocompraservico) | ✓ | Lista com todos os serviços que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoServico` | string | ✓ | Codigo do serviço do pedido |
| `quantidade` | number (double) | ✓ | Quantidade do serviço do pedido |
| `precoOrcado` | number (double) |  | Preço orçado do serviço do pedido |
| `unidade` | string | ✓ | Unidade do serviço do pedido |
| `origemServico` | integer (int32) | ✓ | Origem do serviço do pedido 0 - composiçõesGerais / 1 = planilhaOrcamentaria / 2 - planejamentoObra |
| `numOrcamento` | integer (int32) |  | Numero do orçamento, quando a origem do serviço for de planilha orçamentária |
| `itemOrcamento` | string |  | Item do orçamento, quando a origem do serviço for de planilha orçamentária |
| `mesPl` | string |  | Mês do vinculo com o planejamento, quando a origem do serviço for do planejamento da obra Obs.: informar a data no formato Dia/Mês/Ano |
| `itemPl` | string |  | Item do vinculo com o planejamento, quando a origem do serviço for do planejamento da obra |
| `produtoPl` | integer (int32) |  | Produto do vinculo com o planejamento, quando a origem do serviço for do planejamento da obra |
| `contratoPl` | integer (int32) |  | Contrato do vinculo com o planejamento, quando a origem do serviço for do planejamento da obra |
| `CAP` | string | ✓ | CAP do serviço do pedido |
| `CategoriaMovimentacaoFinanceira` | string |  | Categoria de movimentação financeira do item. |
| `dataInicio` | string (date-time) | ✓ | Data de início do serviço do pedido Obs.: informar a data no formato Mês/Dia/Ano |
| `especificacao` | string |  | Especificação do serviço Obs.: Para gravar uma especificação com quebra de linha utilize o comando ''\r\n'' |
| `observacao` | string |  | Observação do serviço do pedido Obs.: Para gravar uma especificação com quebra de linha utilize o comando ''\r\n'' |
| `listaVinculo` | array de [`UAUApi.Models.PedidoCompra.DadosVinculoItemPedidoCompra`](#uauapimodelspedidocompradadosvinculoitempedidocompra) |  | Lista dos vinculos de SI do pedido |
| `categoria` | string |  |  |

### UAUApi.Models.PedidoCompra.DadosVinculoItemPedidoCompra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `produtoPl` | integer (int32) | ✓ | Codigo do produto da SI do vinculo ao planejamento |
| `contratoPl` | integer (int32) | ✓ | Codigo do contrato da SI do vinculo ao planejamento |
| `itemPl` | string | ✓ | Codigo do Item da SI do vinculo ao planejamento |
| `servicoPl` | string | ✓ | Codigo do serviço da SI do vinculo ao planejamento |
| `mesPl` | string | ✓ | Mês de referência do vinculo ao planejamento obs.: informar a data no formato Mês/Ano (MM/YYYY) |
| `codigoInsumoPl` | string | ✓ | Codigo da SI do vinculo do planejamento |
| `quantidadeVinculo` | number (double) | ✓ | Quantidade do vinculo ao planejamento Obs.: informar a quantidade de considerando que a unidade da Si é a mesma do itemdo pedido. O sistema irá realizar a conversão entre as unidades, caso haja conversão cadastrada entre as unidades. |
| `numeroItemContrato` | integer (int32) |  | Numero do item do contrato de material que deseja vincular a SI, quando o pedido for de adiantamento de contrato. |

### UAUApi.Models.PedidoCompra.DadosPedidoCompra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) | ✓ | Codigo da empresa do pedido |
| `codigoObra` | string | ✓ | Codigo da obra do pedido |
| `considerarVinculoSemSaldoMes` | boolean |  | Considerar vínculo sem saldo no mês de planejamento informado True - Permite vincular SI's que não possuem saldo de planejamento no mês PL informado, mas que possuem saldo em algum mês posterior. False - Não permitir vincular SI's que não possuem saldo de planejamento no mês PL informado. |
| `codigoObraFiscal` | string | ✓ | Codigo da obra fiscal do pedido |
| `usuario` | string | ✓ | Usuario que irá realizar o pedido |
| `observacao` | string |  | Observação geral do pedido Obs.: Para gravar uma observação com quebra de linha utilize o comando ''\r\n'' |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoEmergencialRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido de serviço emergencial. |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico`](#uauapimodelspedidocompradadositempedidocompraservico) | ✓ | Lista com todos os serviços que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido de serviço. |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServicoContrato`](#uauapimodelspedidocompradadositempedidocompraservicocontrato) | ✓ | Lista com todos os serviços que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServicoContrato

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoServico` | string | ✓ | Codigo do serviço do pedido |
| `quantidade` | number (double) | ✓ | Quantidade do serviço do pedido |
| `precoOrcado` | number (double) |  | Preço orçado do serviço do pedido |
| `unidade` | string | ✓ | Unidade do serviço do pedido |
| `CAP` | string | ✓ | CAP do serviço do pedido |
| `CategoriaMovimentacaoFinanceira` | string |  | Categoria de movimentação financeira do item. |
| `dataInicio` | string (date-time) | ✓ | Data de início do serviço do pedido Obs.: informar a data no formato Mês/Dia/Ano |
| `especificacao` | string |  | Especificação do serviço Obs.: Para gravar uma especificação com quebra de linha utilize o comando ''\r\n'' |
| `observacao` | string |  | Observação do serviço do pedido Obs.: Para gravar uma especificação com quebra de linha utilize o comando ''\r\n'' |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoComplementoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido de serviço complemento. |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico`](#uauapimodelspedidocompradadositempedidocompraservico) | ✓ | Lista com todos os serviços que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoAdiantamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido de serviço. |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServicoAdiantamento`](#uauapimodelspedidocompradadositempedidocompraservicoadiantamento) | ✓ | Lista com todos os serviços que serão inseridos no pedido |
| `numeroContrato` | integer (int32) | ✓ | Numero do contrato de serviço que terá o pedido vinculado. |

### UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServicoAdiantamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoServico` | string | ✓ | Codigo do serviço do pedido |
| `quantidade` | number (double) | ✓ | Quantidade do serviço do pedido |
| `precoOrcado` | number (double) |  | Preço orçado do serviço do pedido |
| `unidade` | string | ✓ | Unidade do serviço do pedido |
| `origemServico` | integer (int32) | ✓ | Origem do serviço do pedido 0 - composiçõesGerais / 1 = planilhaOrcamentaria / 2 - planejamentoObra |
| `numOrcamento` | integer (int32) |  | Numero do orçamento, quando a origem do serviço for de planilha orçamentária |
| `itemOrcamento` | string |  | Item do orçamento, quando a origem do serviço for de planilha orçamentária |
| `mesPl` | string |  | Mês do vinculo com o planejamento, quando a origem do serviço for do planejamento da obra Obs.: informar a data no formato Dia/Mês/Ano |
| `itemPl` | string |  | Item do vinculo com o planejamento, quando a origem do serviço for do planejamento da obra |
| `produtoPl` | integer (int32) |  | Produto do vinculo com o planejamento, quando a origem do serviço for do planejamento da obra |
| `contratoPl` | integer (int32) |  | Contrato do vinculo com o planejamento, quando a origem do serviço for do planejamento da obra |
| `CAP` | string | ✓ | CAP do serviço do pedido |
| `CategoriaMovimentacaoFinanceira` | string |  | Categoria de movimentação financeira do item. |
| `dataInicio` | string (date-time) | ✓ | Data de início do serviço do pedido Obs.: informar a data no formato Mês/Dia/Ano |
| `especificacao` | string |  | Especificação do serviço Obs.: Para gravar uma especificação com quebra de linha utilize o comando ''\r\n'' |
| `observacao` | string |  | Observação do serviço do pedido Obs.: Para gravar uma especificação com quebra de linha utilize o comando ''\r\n'' |
| `listaVinculo` | array de [`UAUApi.Models.PedidoCompra.DadosVinculoItemPedidoCompra`](#uauapimodelspedidocompradadosvinculoitempedidocompra) | ✓ | Lista dos vinculos de SI do pedido |
| `categoria` | string |  |  |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoServicoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido de serviço. |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompraServico`](#uauapimodelspedidocompradadositempedidocompraservico) | ✓ | Lista com todos os serviços que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoRegularizacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Informações do pedido de regularizacao |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompra`](#uauapimodelspedidocompradadositempedidocompra) | ✓ | Lista com todos os itens de regularizacao que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.DadosItemPedidoCompra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoInsumo` | string | ✓ | Codigo do insumo do pedido |
| `CAP` | string | ✓ | CAP do insumo do pedido |
| `CategoriaMovimentacaoFinanceira` | string |  | Categoria de movimentação financeira do item. |
| `unidade` | string | ✓ | Unidade do insumo do pedido |
| `controleEstoque` | integer (int32) | ✓ | Define se o insumo do pedido irá controlar estoque 0 - Não / 1 - Sim |
| `dataEntrega` | string (date-time) | ✓ | Data da entrega do insumo do pedido obs.: informar a data no formato Mês/Dia/Ano |
| `quantidade` | number (double) | ✓ | Quantidade do insumo do pedido |
| `precoOrcado` | number (double) |  | Preço orçado do insumo do pedido |
| `observacao` | string |  | Observação do insumo do pedido Obs.: Para gravar uma observação com quebra de linha utilize o comando ''\r\n'' |
| `especificacao` | string |  | Especificação do insumo do pedido Obs.: Para gravar uma especificação com quebra de linha utilize o comando ''\r\n'' |
| `codDepreciacao` | string |  | Codigo de depreciação do insumo do pedido (opcional) - Usado quando o pedido for do tipo de patrimônio. |
| `listaVinculo` | array de [`UAUApi.Models.PedidoCompra.DadosVinculoItemPedidoCompra`](#uauapimodelspedidocompradadosvinculoitempedidocompra) | ✓ | Lista dos vinculos do insumo do pedido |
| `codJustificativa` | integer (int32) |  | Código da justificativa para insumo com quantidade/valor extrapolado em relação ao controle físico. |
| `justificativa` | string |  | Descrição da justificativa para insumo com quantidade/valor extrapolado em relação ao controle físico. Parâmetro opcional, sendo que na ausência dessa informação o sistema irá considerar a descrição da justificativa cadastrada no sistema de acordo com o código da justificativa informado. |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoPatrimonioRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido de patrimônio |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompra`](#uauapimodelspedidocompradadositempedidocompra) | ✓ | Lista com todos os itens de patriônio que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoMaterialRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Informações do pedido de material |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompra`](#uauapimodelspedidocompradadositempedidocompra) | ✓ | Lista com todos os itens de material que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoEmergencialRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido emergencial |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompra`](#uauapimodelspedidocompradadositempedidocompra) | ✓ | Lista com todos os itens emergenciais que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoContratoMaterialRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Dados do pedido de contrato de material |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompraContratoMaterial`](#uauapimodelspedidocompradadositempedidocompracontratomaterial) | ✓ | Lista com todos os itens de contrato de material que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.DadosItemPedidoCompraContratoMaterial

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoInsumo` | string | ✓ | Codigo do insumo do pedido |
| `CAP` | string | ✓ | CAP do insumo do pedido |
| `CategoriaMovimentacaoFinanceira` | string |  | Categoria de movimentação financeira do item. |
| `unidade` | string | ✓ | Unidade do insumo do pedido |
| `controleEstoque` | integer (int32) | ✓ | Define se o insumo do pedido irá controlar estoque 0 - Não / 1 - Sim |
| `dataEntrega` | string (date-time) | ✓ | Data da entrega do insumo do pedido obs.: informar a data no formato Mês/Dia/Ano |
| `quantidade` | number (double) | ✓ | Quantidade do insumo do pedido |
| `precoOrcado` | number (double) |  | Preço orçado do insumo do pedido |
| `observacao` | string |  | Observação do insumo do pedido |
| `especificacao` | string |  | Especificação do insumo do pedido Obs.: Para gravar uma especificação com quebra de linha utilize o comando ''\r\n'' |
| `categoria` | string |  | Código da categoria do insumo |
| `codJustificativa` | integer (int32) |  | Código da justificativa para insumo com quantidade/valor extrapolado em relação ao controle físico. |
| `justificativa` | string |  | Descrição da justificativa para insumo com quantidade/valor extrapolado em relação ao controle físico. Parâmetro opcional, sendo que na ausência dessa informação o sistema irá considerar a descrição da justificativa cadastrada no sistema de acordo com o código da justificativa informado. |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoComplementoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Informações do pedido de complemento |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompra`](#uauapimodelspedidocompradadositempedidocompra) | ✓ | Lista com todos os itens de complemento que serão inseridos no pedido |

### UAUApi.Models.PedidoCompra.GerarPedidoDeCompraDoTipoAdiantamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadosPedido` | [`UAUApi.Models.PedidoCompra.DadosPedidoCompra`](#uauapimodelspedidocompradadospedidocompra) | ✓ | Informações do pedido de adiantamento de contrato |
| `listaDadosItemPedido` | array de [`UAUApi.Models.PedidoCompra.DadosItemPedidoCompra`](#uauapimodelspedidocompradadositempedidocompra) | ✓ | Lista com todos os itens de adiantamento de compra que serão inseridos no pedido |
| `numeroContrato` | integer (int32) | ✓ | Numero do contrato de material que terá o pedido vinculado. |

### UAUApi.Models.PedidoCompra.ConfirmarRecebimentoOrdemCompraFornecedorResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nomeFornecedor` | string |  | Nome do fornecedor do pedido |
| `codigoEmpresa` | integer (int32) |  | Empresa do pedido |
| `codigoObra` | string |  | Obra do pedido |
| `ordemDeCompra` | integer (int32) |  | Número da ordem de compra do pedido |

### UAUApi.Models.PedidoCompra.ConfirmarRecebimentoOrdemCompraFornecedorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nomeFornecedor` | string |  | Nome do fornecedor do pedido |
| `codigoEmpresa` | integer (int32) |  | Empresa do pedido |
| `codigoObra` | string |  | Obra do pedido |
| `ordemDeCompra` | integer (int32) |  | Número da ordem de compra do pedido |
| `tipoResposta` | integer (int32) |  | Tipo da resposta do fornecedor ao email do followUp. 1 = Aceito 3 = Recusado |
| `observacao` | string |  | Observação do fornecedor |

### UAUApi.Models.PedidoCompra.AprovarPedidoCompraServicoAppRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_empresa` | integer (int32) | ✓ | Código da empresa |
| `codigo_obra` | string | ✓ | Código da obra |
| `servico` | string | ✓ | Código do servico |
| `num_pedido` | integer (int32) | ✓ | Númedo do pedido |
| `mensagem_retorno` | string |  | Mensagem retornada do método de aprovação |
| `departamento` | string |  | Departamento da aprovação |
| `cargo` | string |  | Cargo da aprovação |
| `cod_justificativa` | integer (int32) |  | Código da justificativa de aprovação |
| `obs_justificativa` | string |  | Observação da justificativa de aprovação |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.PedidoCompra.AprovarPedidoCompraMaterialAppRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_empresa` | integer (int32) | ✓ | Código da empresa |
| `codigo_obra` | string | ✓ | Código da obra |
| `insumo` | string | ✓ | Código do insumo do pedido |
| `item_ped` | integer (int32) | ✓ | Código do item do pedido |
| `num_pedido` | integer (int32) | ✓ | Númedo do pedido |
| `mensagem_retorno` | string |  | Mensagem retornada do método de aprovação |
| `departamento` | string |  | Departamento da aprovação |
| `cargo` | string |  | Cargo da aprovação |
| `cod_justificativa` | integer (int32) |  | Código da justificativa de aprovação |
| `obs_justificativa` | string |  | Observação da justificativa de aprovação |

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |
