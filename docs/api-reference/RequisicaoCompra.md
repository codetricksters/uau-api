# RequisicaoCompra

## POST `/api/v{version}/RequisicaoCompra/AprovarRequisicoesCompra`

**Método com finalidade de aprovar requisições de compra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Regras básicas:
1. É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.RequisicaoDeCompra.AprovarRequisicoesCompraRequest`](#uauapimodelsrequisicaodecompraaprovarrequisicoescomprarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RequisicaoCompra/DesaprovarRequisicoesCompra`

**Método com finalidade de desaprovar requisições de compra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Regras básicas:
1. É necessário permissão de aprovação para o programa ALREQUISICAOCOMPRA
2. Será permitido desaprovar apenas requisições de compra com estágio 0 - Criada

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.RequisicaoDeCompra.DesaprovarRequisicoesCompraRequest`](#uauapimodelsrequisicaodecompradesaprovarrequisicoescomprarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.RequisicaoDeCompra.DesaprovarRequisicoesCompraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Requisicoes` | array de [`UAUApi.Models.RequisicaoDeCompra.DesaprovarRequisicaoCompraRequest`](#uauapimodelsrequisicaodecompradesaprovarrequisicaocomprarequest) | ✓ | Requisições de compra a serem aprovadas |
| `CodJustificativaDesaprovacao` | integer (int32) |  | Código da justificativa para desaprovação da requisição de compra.  É necessário quando o sistema está configurado para obrigar informar o motivo da desaprovação. |
| `ObsJustificativaDesaprovacao` | string |  | Observação da justificativa para desaprovação da requisição de compra |

### UAUApi.Models.RequisicaoDeCompra.DesaprovarRequisicaoCompraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `NumRequisicao` | integer (int32) | ✓ | Número da requisição de compra |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.RequisicaoDeCompra.AprovarRequisicoesCompraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Requisicoes` | array de [`UAUApi.Models.RequisicaoDeCompra.AprovarRequisicaoCompraRequest`](#uauapimodelsrequisicaodecompraaprovarrequisicaocomprarequest) | ✓ | Requisições de compra a serem aprovadas |
| `Departamento` | string |  | Código do departamento do usuário para aprovação |
| `Cargo` | string |  | Código do cargo do usuário para aprovação |
| `CodJustificativa` | integer (int32) |  | Código da justificativa para aprovação fora da sequência do usuário |
| `ObsJustificativa` | string |  | Observação da justificativa para aprovação fora da sequência do usuário |

### UAUApi.Models.RequisicaoDeCompra.AprovarRequisicaoCompraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `NumRequisicao` | integer (int32) | ✓ | Número da requisição de compra |
