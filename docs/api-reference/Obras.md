# Obras

## POST `/api/v{version}/Obras/ConsultarObraPorChave`

**Consultar obra por chave**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta dados de uma obra filtrando por chave.
2. Valida os campos passados como parâmetros.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Obras.ObrasRequest`](#uauapimodelsobrasobrasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Obras |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Obras/ObterMesesAbertosPorEmpresaObra`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Obras.MesesAbertosPorObraRequest`](#uauapimodelsobrasmesesabertosporobrarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | mesesAbertos | array de string (date-time) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Obras/ObterObrasAtivas`

**Consulta obras cadastradas e ativas no UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta obras cadastradas e ativas dentro do UAU.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Obras | array de [`UAUApi.Models.Obra`](#uauapimodelsobra) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Obra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Cod_obr` | string |  | Código da Obra |
| `Empresa_obr` | integer (int32) |  | Código da empresa |
| `Descr_obr` | string |  | Descrição da obra |
| `Status_obr` | integer (int32) |  | status da obra |
| `Ender_obr` | string |  | Endereço da obra |
| `Fone_obr` | string |  | número de telefone da obra |
| `Fisc_obr` | string |  | Código da obra fiscal |
| `DtIni_obr` | string (date-time) |  | Data de início da obra |
| `Dtfim_obr` | string (date-time) |  | Data final da obra |
| `TipoObra_obr` | integer (int32) |  | Tipo da obra |
| `EnderEntr_obr` | string |  | Endereço de entrega cadastrado na obra |
| `CEI_obr` | string |  | Campo CEI da obra |
| `DataCad_obr` | string (date-time) |  | Data de cadastro da obra |
| `DataAlt_obr` | string (date-time) |  | Data de alteração da obra |
| `UsrCad_obr` | string |  | Usuário que cadastrou a obra |

### UAUApi.Models.Obras.MesesAbertosPorObraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresaObra` | string |  | Código da Empresa|Obra |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Obras.ObrasRequest

Danielle Bomfim Data: 23/04/2018
Projeto: 261604 - 10.06

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `obra` | string |  | Código da obra |
