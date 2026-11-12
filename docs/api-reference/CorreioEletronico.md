# CorreioEletronico

## POST `/api/v{version}/CorreioEletronico/EnviarMailInternoUau`

**Enviar email interno para o usuário root**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint

Definição de Negócio:
1. Possibilita envio de email interno para o usuário root.
2. Valida as informaçõe passadas no request.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.CorreioEletronico.EnviarMailInternoUauRequest`](#uauapimodelscorreioeletronicoenviarmailinternouaurequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.CorreioEletronico.EnviarMailInternoUauRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `mensagem_envio` | string |  | Mensagem que será enviada |
| `usuariosuau_destino` | string |  | Usuário do uau que receberá a mensagem |
| `usuariouau_envio` | string |  | Usuário que está enviando o e-mail |
| `assunto` | string |  | Assunto do mail |
