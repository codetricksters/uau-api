# Fiscal

## POST `/api/v{version}/Fiscal/BuscarCAPs`

**Retornar a lista de CAPs ativos**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Formato dos dados retornados:
 - Codigo (String): Código do CAP
 - Descricao (String): Descrição do CAP
 - Tipo (Integer): Tipo do CAP
        - 0: Geral
        - 1: Acresc/Desc

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Fiscal.CapDTO`](#globaltecuaufiscalcapdto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Fiscal/BuscarCodigoServicoFiscal`

**Consulta a lista de cógidos de serviços fiscais**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta os códigos de serviços fiscais ativos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Fiscal.CodigoServicoFiscalDTO`](#globaltecuaufiscalcodigoservicofiscaldto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Fiscal/ImportarLancamentosContabeis`

**Importa lançamentos fiscais e/ou societários - Formato novo**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Utiliza o novo formato do XML na string passada como parâmetro.

Definição de Negócio:
1. Importa lançamentos fiscais e/ou societários.
2. Valida o XML passado no request.
3. Valida usuário e suas permissões.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Fiscal.ImportarLancamentosContabeisRequest`](#uauapimodelsfiscalimportarlancamentoscontabeisrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Fiscal/ImportarLancamentosFiscais`

**Importa lançamentos fiscais e/ou societários - Formato antigo**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.
3. Recebe string no formato XML com os dados do lançamento para importação.
4. Utiliza o formato antigo do XML na string passada como parâmetro.

Definição de Negócio:
1. Importa lançamentos fiscais e/ou societários.
2. Valida o XML passado no request.
3. Valida o usuário e suas permissões.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Fiscal.ImportarLancamentosFiscaisRequest`](#uauapimodelsfiscalimportarlancamentosfiscaisrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Fiscal.ImportarLancamentosFiscaisRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadoslacamentos_xml` | string |  | Contem uma string com os dados do lançamento em formato de documento xml |

### UAUApi.Models.Fiscal.ImportarLancamentosContabeisRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dadoslacamentos_xml` | string |  | Contem uma string com os dados do lancamento em formato de documento xml |

### Globaltec.UAU.Fiscal.CodigoServicoFiscalDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### Globaltec.UAU.Fiscal.CapDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |
| `Tipo` | integer (int32) |  |  |
