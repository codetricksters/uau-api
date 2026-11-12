# DocumentosDigitais

## GET `/api/v{version}/DocumentosDigitais/AssineOnLineConfigTemplate`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `id` | query | string | ✓ |  |
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | object |

---

## GET `/api/v{version}/DocumentosDigitais/DocuSignConsentimento`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `code` | query | string | ✓ |  |
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | object |

---

## POST `/api/v{version}/DocumentosDigitais/DocuSignEnvelopeStatus`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | object |

---
