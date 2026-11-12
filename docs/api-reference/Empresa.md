# Empresa

## POST `/api/v{version}/Empresa/ConsultarDadosBasicosEmpresasPorFiltro`

**Consultar dados básicos da empresa por filtro, com limite de registros.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Empresa/DadosBasicosEmpresa
3. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Consultar dados de empresas por meio dos seguintes filtros (empresa, cnpj e descricaoEmpresa), os resultados da busca será de acordo com o limite especificado no parâmetro (limitarRetornoEm).
2. Se apenas informar o código da empresa parâmetro (empresa) o mesmo deve estar completo.
3. Os parâmetros (DescricaoEmpresa e Cnpj) devem possuir no mínimo 3 caracteres..
4. Os parâmetros (DescricaoEmpresa e Cnpj) podem conter o sinal de porcentagem (%), caso necessite fazer a consulta a partir de um caractere curinga. Exemplos: %UAU, %UAU%, UAU%.
5. O campo LimitarRetornoEm é obrigatório.
6. Caso não informe nenhum dos parâmetros o resultado será os N primeiros registros encontrados, obedecendo o parâmetro LimitarRetornoEm.
7. O método usa o operador “Or” para montar a consulta de acordo com os parâmetros do request, consultando informações por código ou descrição ou CNPJ da empresa.


VirtUau:
- http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Empresa/Empresa_ConsultarDadosBasicosEmpresasPorFiltro

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/777099/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Empresa.ConsultarDadosBasicosEmpresasPorFiltroRequest`](#uauapimodelsempresaconsultardadosbasicosempresasporfiltrorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Empresa.DadosBasicosEmpresa`](#uauapimodelsempresadadosbasicosempresa) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Empresa/ConsultarEmpresa`

**Consultar os dados da empresa.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Empresa.ConsultarEmpresaRequest`](#uauapimodelsempresaconsultarempresarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Empresa/ObterEmpresasAtivas`

**Consulta e retorna uma lista de Empresas cadastradas e ativas na base de dados UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Empresas | array de [`UAUApi.Models.Empresa.Empresa`](#uauapimodelsempresaempresa) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Empresa.Empresa

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo_emp` | integer (int32) |  | Código da empresa |
| `Desc_emp` | string |  | Descrição da empresa |
| `CGC_emp` | string |  | CNPJ da empresa |
| `IE_emp` | string |  | Inscrição Estadual da empresa |
| `InscrMunic_emp` | string |  | Inscrição Municipal da empresa |
| `Endereco_emp` | string |  | Endereço da empresa |
| `Fone_emp` | string |  | Número do telefone da empresa |

### UAUApi.Models.Empresa.ConsultarEmpresaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Empresa.DadosBasicosEmpresa

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  | Código da empresa |
| `Cnpj` | string |  | CNPJ da empresa |
| `RazaoSocial` | string |  | descrição da empresa |
| `InscricaoMunicipal` | string |  | Inscrição Municipal da empresa |
| `InscricaoEstadual` | string |  | Inscrição Estadual da empresa |
| `Cep` | string |  | cep da empresa |
| `Endereco` | string |  | Endereço da empresa |
| `Bairro` | string |  | Bairro da empresa |
| `Cidade` | string |  | Cidade da empresa |
| `Uf` | string |  | Uf da empresa |
| `Email` | string |  | Email da empresa |
| `Natureza` | string |  | Natureza da empresa |

### UAUApi.Models.Empresa.ConsultarDadosBasicosEmpresasPorFiltroRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa |
| `DescricaoEmpresa` | string |  | Descrição da empresa |
| `Cnpj` | string |  | CNPJ da empresa (sem máscara) |
| `LimitarRetornoEm` | integer (int32) | ✓ | Limite de retorno da consulta |
