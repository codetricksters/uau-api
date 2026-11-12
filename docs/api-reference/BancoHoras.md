# BancoHoras

## POST `/api/v{version}/BancoHoras/LancarBancoHorasFuncionario`

**Gravar lançamentos de banco de horas para o funcionário**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Gravar lançamento de horas no banco de horas para o funcionário.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.BancoHoras.BancoHorasRequest`](#uauapimodelsbancohorasbancohorasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Lançamento de banco de horas. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
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

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |

### UAUApi.Models.BancoHoras.BancoHorasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ListaBancoHoras` | array de [`UAUApi.Models.BancoHoras.EntidadeBancoHoras`](#uauapimodelsbancohorasentidadebancohoras) |  | Lista de banco de horas. |

### UAUApi.Models.BancoHoras.EntidadeBancoHoras

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa. |
| `Obra` | string |  | Código da obra. |
| `MesFolha` | string |  | Mês folha de pagamento. Formato "dd/mm/yyyy" |
| `Tipo` | integer (int32) |  | Tipo de lançamento. (0 - Crédito, 1 - Débito) |
| `HorasMinutosLanc` | string |  | Horas para lançamento. Formato HH:mm |
| `DataLancamento` | string (date-time) |  | Data do lançamento de banco de horas para o funcionário. Formato "dd/mm/yyyy HH:mm" |
| `Matricula` | integer (int32) |  | Código da matrícula do funcionário. |
