# Estrutura

## POST `/api/v{version}/Estrutura/ExcluirEstrutura`

**Excluir estrutura.**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite excluir uma estrutura completa caso o valor do parâmetro sequência seja (0 - raiz) ou apenas um item da estrutura(Caso o tipo do item seja "0 - Nível", também serão excluídos os itens filhos).

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Estrutura.ExcluirEstruturaRequest`](#uauapimodelsestruturaexcluirestruturarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Excluir estrutura. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Estrutura/ExcluirItemDeEstrutura`

**Excluir item de estrutura.**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite excluir um item de estrutura que não está sendo utilizado no cadastro de estrutura, orçamento, contrato ou serviços do planejamento .

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Estrutura.ExcluirItemDeEstruturaRequest`](#uauapimodelsestruturaexcluiritemdeestruturarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Excluir item de estrutura. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Estrutura/InserirEstrutura`

**Inserir uma estrutura.**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite inserir uma estrutura. Após inserir, poderá vincular os itens da estrutura.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Estrutura.InserirEstruturaRequest`](#uauapimodelsestruturainserirestruturarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir estrutura. | [`UAUApi.Models.Estrutura.EstruturaInserida`](#uauapimodelsestruturaestruturainserida) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Estrutura/InserirItemDeEstrutura`

**Inserir um item de estrutura.**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite inserir um item de estrutura. Após inserir, poderá se utilizado no cadastro de estrutura e ser vinculado em orçamento, contrato e serviços do planejamento.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Estrutura.InserirItemDeEstruturaRequest`](#uauapimodelsestruturainseriritemdeestruturarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir item de estrutura. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Estrutura/InserirItemNaEstrutura`

**Inserir item em uma estrutura.**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite inserir item em uma estrutura. Após concluir o cadastro da estrutura, poderá ser vinculada em orçamento, contrato e serviços do planejamento. 

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/estruturas

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Estrutura.InserirItemNaEstruturaRequest`](#uauapimodelsestruturainseriritemnaestruturarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir item na estrutura. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Estrutura.InserirItemNaEstruturaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEstrutura` | integer (int32) | ✓ | Código da estrutura |
| `tipoEstrutura` | integer (int32) | ✓ | Tipo da estrutura  0 - Nível  1 - Item |
| `sequencia` | string | ✓ | Sequência da estrutura |
| `codigoItem` | string | ✓ | Código do item de estrutura a ser vinculado.  Deve existir no cadastrado de itens de estrutura. |

### UAUApi.Models.Estrutura.InserirItemDeEstruturaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoItem` | string | ✓ | Código do item de estrutura |
| `descricaoItem` | string | ✓ | Descrição do item de estrutura |

### UAUApi.Models.Estrutura.EstruturaInserida

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEstrutura` | integer (int32) |  | Código da estrutura |
| `descricaoEstrutura` | string |  | Descrição da estrutura |
| `tipo` | integer (int32) |  | Tipo da estrutura, onde: 0 - Nível; 1 - Item; |
| `sequencia` | string |  | Sequência da estrutura |

### UAUApi.Models.Estrutura.InserirEstruturaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `descricao` | string | ✓ | Descrição da estrutura |

### UAUApi.Models.Estrutura.ExcluirItemDeEstruturaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoItem` | string | ✓ | Código do item de estrutura |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Estrutura.ExcluirEstruturaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEstrutura` | integer (int32) | ✓ | Código da estrutura |
| `sequencia` | string | ✓ | Sequência da estrutura  Obs: Quando a sequência for (0 - Raiz) será excluído a estrutura pai e os filhos. |
