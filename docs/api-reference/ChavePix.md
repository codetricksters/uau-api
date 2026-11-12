# ChavePix

## POST `/api/v{version}/ChavePix/Pessoas/Atualizar`

**Atualiza a chave pix de uma pessoa.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:
1. É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
2. O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
3. A chave pix deve ter no máximo 77 caracteres.
4. A chave padrão deve ser: 0 - NÃO, 1 - SIM.
5. O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ChavePix.ChavePixRequest`](#uauapimodelschavepixchavepixrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ChavePix/Pessoas/Cadastrar`

**Cadastra uma nova chave pix para a pessoa.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:
1. É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
2. O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
3. A chave pix deve ter no máximo 77 caracteres.
4. A chave padrão deve ser: 0 - NÃO, 1 - SIM.
5. O campo ativo inativo deve ser: 0 - ATIVO, 1 - INATIVO.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ChavePix.ChavePixRequest`](#uauapimodelschavepixchavepixrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## GET `/api/v{version}/ChavePix/Pessoas/Consultar/{cpfCnpj}`

**Retorna as chaves pix cadastradas ao CPF/CNPJ informado.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:
1. É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `cpfCnpj` | path | string | ✓ |  |
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.ChavePix.ChavePixResponse`](#uauapimodelschavepixchavepixresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ChavePix/Pessoas/Deletar`

**Remove uma chave pix de pessoa.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:
1. É necessário que exista uma pessoa cadastrada no sistema com o CPF/CNPJ informado.
2. O tipo de chave pix deve ser: 1 - Celular, 2 - E-mail, 3 - CPF/CNPJ, 4 - Chave aleatória.
3. A chave pix deve ter no máximo 77 caracteres.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ChavePix.ChavePixDeletarRequest`](#uauapimodelschavepixchavepixdeletarrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.ChavePix.ChavePixDeletarRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpfCnpj` | string | ✓ | CPF do cliente |
| `chavePix` | string | ✓ | Chave Pix |
| `tipoChavePix` | integer (int32) | ✓ | 0 - CPF/CNPJ, 1 - Celular, 2 - E-mail, 3 - Chave aleatória |

### UAUApi.Models.ChavePix.ChavePixResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `chavePix` | string |  |  |
| `tipoChavePix` | integer (int32) |  |  |
| `chavePixPadrao` | integer (int32) |  |  |
| `ativoInativo` | integer (int32) |  |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.ChavePix.ChavePixRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpfCnpj` | string | ✓ | CPF do cliente |
| `chavePix` | string | ✓ | Chave Pix |
| `tipoChavePix` | integer (int32) | ✓ | 0 - CPF/CNPJ, 1 - Celular, 2 - E-mail, 3 - Chave aleatória |
| `chavePixPadrao` | integer (int32) | ✓ | 0 - SIM, 1 - NÃO |
| `ativoInativo` | integer (int32) | ✓ | 0 - ATIVO, 1 - INATIVO |
