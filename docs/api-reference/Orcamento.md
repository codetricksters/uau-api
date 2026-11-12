# Orcamento

## POST `/api/v{version}/Orcamento/AlterarInsumoOrcamento`

**Alterar insumo no orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ManterInsumoOrcamentoRequest`](#uauapimodelsorcamentomanterinsumoorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Alterar insumo da composição do orçamento | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/AlterarPlanilhaCronograma`

**Alterar cronograma no orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ManterPlanilhaCronogramaPorChaveRequest`](#uauapimodelsorcamentomanterplanilhacronogramaporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Alterar cronograma no orçamento | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/AlterarServicoOrcamento`

**Alterar serviço no orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.AlterarServicoOrcamentoRequest`](#uauapimodelsorcamentoalterarservicoorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Alteração de serviço orçado | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/AtualizarEstruturaServicoDeOrcamento`

**Atualizar a quantidade e/ou preço de uma lista de estruturas de serviço no orçamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite alterar níveis ou itens de uma estrutura do serviço existente no orçamento
1. Deve preencher os parâmetros de acordo com a estrutura que deseja alterar .
   1.1 Informar se é nível ou item que esta inserindo, a sequencia e os dados do orçamento e serviço.
2. Valida se a estrutura poderá ser alterada.
3. Valida campos obrigatórios.
4. Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem inseridas.

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/776147/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Orcamento.EstruturasDeServicoDeOrcamentoRequest`](#uauapimodelsorcamentoestruturasdeservicodeorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Alteração de estrutura do orçamento | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ConsultarEstruturaOrcaPorChave`

**Consultar estrutura de serviço do orçamento de acordo com a chave do orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ConsultarEstruturaOrcaPorChaveRequest`](#uauapimodelsorcamentoconsultarestruturaorcaporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Estrutura do orçamento | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ConsultarEstruturaOrcaPorServico`

**Consultar as estruturas do orçamento para um determinado serviço.**

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
Esquema: [`UAUApi.Models.Orcamento.ConsultarServicoOrcamentoPorChaveRequest`](#uauapimodelsorcamentoconsultarservicoorcamentoporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Estrutura do orçamento | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ConsultarInsumosPorChave`

**Consultar a tabela PlanilhaCronograma pela sua chave**

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
Esquema: [`UAUApi.Models.Orcamento.ConsultarInsumosPorChaveRequest`](#uauapimodelsorcamentoconsultarinsumosporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Insumos Orçamento | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ConsultarPlanilhaCronogramaPorChave`

**Consultar a tabela PlanilhaCronograma pela sua chave**

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
Esquema: [`UAUApi.Models.Orcamento.ConsultarPlanilhaCronogramaPorChaveRequest`](#uauapimodelsorcamentoconsultarplanilhacronogramaporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | PlanilhaCronograma | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ConsultarServicoOrcadoDesintegrado`

**Consultar serviço orçado desintegrado.**

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
Esquema: [`UAUApi.Models.Orcamento.ConsultarServicoOrcadoDesintegrado`](#uauapimodelsorcamentoconsultarservicoorcadodesintegrado)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Serviço orçado desintegrado | array de [`UAUApi.Models.Orcamento.Planilha`](#uauapimodelsorcamentoplanilha) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ConsultarServicoOrcamentoPorChave`

**Buscar os serviços do orçamento de acordo com a chave do orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ConsultarServicoOrcamentoPorChaveRequest`](#uauapimodelsorcamentoconsultarservicoorcamentoporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Serviço orçado | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ConsultarServicoOrcamentoPorOrcamento`

**Buscar os serviços do orçamento de acordo com o código do orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ConsultarServicoOrcamentoPorOrcamentoRequest`](#uauapimodelsorcamentoconsultarservicoorcamentopororcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Serviço orçado | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ExcluirEstruturaServicoDeOrcamento`

**Excluir uma determinada estrutura de serviço no orçamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite excluir níveis ou itens de estruturas do serviço do orçamento.
1. Deve preencher os parâmetros de acordo com a estrutura que deseja excluir.
   1.1 Informar se é nível ou item que esta excluindo, a sequencia e os dados do orçamento e serviço.
2. Valida se a estrutura poderá ser excluída.
3. Valida campos obrigatórios.
4. Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem excluídas.

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/776140/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Orcamento.ExcluirEstruturasDeServicoDeOrcamentoRequest`](#uauapimodelsorcamentoexcluirestruturasdeservicodeorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de estrutura do orçamento | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ExcluirInsumoOrcamento`

**Excluir insumo no orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ManterInsumoOrcamentoRequest`](#uauapimodelsorcamentomanterinsumoorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de insumo do orçamento | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ExcluirPlanilhaCronograma`

**Excluir cronograma no orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ManterPlanilhaCronogramaPorChaveRequest`](#uauapimodelsorcamentomanterplanilhacronogramaporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de cronograma no orçamento | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ExcluirServicoOrcamento`

**Exclui serviço ou item do orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ExcluirServicoOrcamentoRequest`](#uauapimodelsorcamentoexcluirservicoorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de serviço orçado | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ExportarOrcamentoEstrutura`

**Exportar orçamento com suas estruturas**

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
Esquema: [`UAUApi.Models.Orcamento.ExportarOrcamentoEstruturaRequest`](#uauapimodelsorcamentoexportarorcamentoestruturarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exportar itens de um orçamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/ExportarOrcamentoEstruturaPaginada`

**Exporta os itens de um orçamento com suporte à paginação.**

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
Esquema: [`UAUApi.Models.Orcamento.ExportarOrcamentoEstruturaRequestPaginada`](#uauapimodelsorcamentoexportarorcamentoestruturarequestpaginada)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exportar itens de um orçamento com paginação. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/InserirEstruturaServicoDeOrcamento`

**Inserir estrutura para um determinado serviço no orçamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite inserir níveis ou itens de estruturas no serviço existente no orçamento.
1. Deve preencher os parâmetros de acordo com a estrutura que deseja inserir.
   1.1 Informar se é nível ou item que esta inserindo, a sequencia e os dados do orçamento e serviço.
2. Valida se a estrutura poderá ser inserida.
3. Valida campos obrigatórios.
4. Permite que as estruturas sejam informadas em lote, em um formato de lista de estruturas para serem inseridas.

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/776144/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Orcamento.EstruturasDeServicoDeOrcamentoRequest`](#uauapimodelsorcamentoestruturasdeservicodeorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserção de estrutura do orçamento | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/InserirInsumoOrcamento`

**Inserir insumos no orçamento. Podem ser informados diversos insumos para que sejam inseridos em lote.**

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
Esquema: [`UAUApi.Models.Orcamento.InsumosOrcamentoRequest`](#uauapimodelsorcamentoinsumosorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserção de insumo na composição do orçamento | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/InserirPlanilhaCronograma`

**Inserir cronograma no orçamento.**

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
Esquema: [`UAUApi.Models.Orcamento.ManterPlanilhaCronogramaPorChaveRequest`](#uauapimodelsorcamentomanterplanilhacronogramaporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserção de cronograma no orçamento | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Orcamento/InserirServicoOrcamento`

**Inserir serviços no orçamento. Podem ser informados diversos serviços para que sejam inseridos em lote.**

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
Esquema: [`UAUApi.Models.Orcamento.ServicosOrcamentoRequest`](#uauapimodelsorcamentoservicosorcamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserção de serviço orçado | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Orcamento.ServicosOrcamentoRequest

Leonrique Oliveira 
Projeto: 367085 - Sprint 77

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ServicosOrcamento` | array de [`UAUApi.Models.Orcamento.InserirServicoOrcamentoRequest`](#uauapimodelsorcamentoinserirservicoorcamentorequest) |  |  |

### UAUApi.Models.Orcamento.InserirServicoOrcamentoRequest

Ulisses Cardoso de Souza Data: 21/06/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  | Usuário logado |
| `quantidade` | number (double) |  | Quantidade do item/serviço |
| `dataInicio` | string (date-time) |  | Data de início do serviço |
| `dataFim` | string (date-time) |  | Data final do serviço |
| `descricaoServico` | string |  | Descrição que será inserida no item ou serviço do orçamento.  Para inserção de item a informação da descrição é obrigatória. Para inserção de serviço, segue as regras: 1. Se a descrição não for informada, considera a descrição no cadastro de composições. 2. Se a descrição for informada, mas já existe o serviço no orçamento, considera a descrição desse serviço. 3. A descrição informada só será considerada quando for a primeira inserção do serviço. |
| `empresa` | integer (int32) | ✓ | Codigo da empresa do orçamento |
| `obra` | string | ✓ | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) | ✓ | Número do orçamento |
| `item` | string | ✓ | Código do item do orçamento |
| `servico` | string | ✓ | Código do serviço do orçamento |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao serviço |

### UAUApi.Models.Orcamento.InsumosOrcamentoRequest

Leonrique Oliveira 
Projeto: 367085 - Sprint 77

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `InsumosOrcamento` | array de [`UAUApi.Models.Orcamento.ManterInsumoOrcamentoRequest`](#uauapimodelsorcamentomanterinsumoorcamentorequest) |  |  |

### UAUApi.Models.Orcamento.ExportarOrcamentoEstruturaRequestPaginada

Classe de requisição para exportação paginada dos itens de estrutura de um orçamento.

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa responsável pelo orçamento. |
| `obra` | string | ✓ | Identificador da obra vinculada ao orçamento. |
| `orcamento` | integer (int32) | ✓ | Número do orçamento a ser exportado. |
| `Page` | integer (int32) | ✓ | Número da página a ser consultada (inicia em 1). |
| `PageSize` | integer (int32) | ✓ | Quantidade de registros por página. |

### UAUApi.Models.Orcamento.ExportarOrcamentoEstruturaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa. |
| `obra` | string | ✓ | Código da obra. |
| `orcamento` | integer (int32) | ✓ | Numero do orçamento. |

### UAUApi.Models.Orcamento.ExcluirServicoOrcamentoRequest

Ulisses Cardoso de Souza Data: 21/06/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  | Usuário logado |
| `empresa` | integer (int32) | ✓ | Codigo da empresa do orçamento |
| `obra` | string | ✓ | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) | ✓ | Número do orçamento |
| `item` | string | ✓ | Código do item do orçamento |
| `servico` | string | ✓ | Código do serviço do orçamento |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao serviço |

### UAUApi.Models.Orcamento.ExcluirEstruturasDeServicoDeOrcamentoRequest

- Lista de estruturas de serviço de orçamento, para permitir a exclusão em massa.

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `EstruturasDeServicoDeOrcamento` | array de [`UAUApi.Models.Orcamento.ExcluirEstruturaServicoDeOrcamentoRequest`](#uauapimodelsorcamentoexcluirestruturaservicodeorcamentorequest) |  |  |

### UAUApi.Models.Orcamento.ExcluirEstruturaServicoDeOrcamentoRequest

Ulisses Cardoso de Souza Data: 21/06/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sequencia` | string | ✓ | Código da sequência da estrutura do serviço |
| `empresa` | integer (int32) | ✓ | Codigo da empresa do orçamento |
| `obra` | string | ✓ | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) | ✓ | Número do orçamento |
| `item` | string | ✓ | Código do item do orçamento |
| `servico` | string | ✓ | Código do serviço do orçamento |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao serviço |

### UAUApi.Models.Orcamento.ConsultarServicoOrcamentoPorOrcamentoRequest

Ulisses Cardoso de Souza Data: 21/06/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Codigo da empresa do orçamento |
| `obra` | string |  | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) |  | Número do orçamento |
| `tipoItem` | integer (int32) |  | Tipo do item 0 - Atividade (Item) 1 - Servico  2 - Ambos |

### UAUApi.Models.Orcamento.Planilha

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa_pla` | integer (int32) |  |  |
| `Obra_pla` | string |  |  |
| `NumOrca_pla` | integer (int32) |  |  |
| `Serv_pla` | string |  |  |
| `Item_pla` | string |  |  |
| `Unid_pla` | string |  |  |
| `Descr_pla` | string |  |  |
| `Prodeq_pla` | number (double) |  |  |
| `Custo_pla` | string |  |  |
| `Qdade_pla` | number (double) |  |  |
| `Dini_pla` | string |  |  |
| `Dfim_pla` | string |  |  |
| `BDI_pla` | number (double) |  |  |
| `CustoPorcent_pla` | number (double) |  |  |
| `CustoUnitMao_pla` | number (double) |  |  |
| `CustoUnitEquip_pla` | number (double) |  |  |
| `CustoUnitMat_pla` | number (double) |  |  |
| `CustoUnitServ_pla` | number (double) |  |  |
| `CustoUnit_pla` | number (double) |  |  |
| `CustoTot_pla` | number (double) |  |  |
| `CustoUnitTrans_pla` | number (double) |  |  |
| `CivilPes_pla` | integer (int32) |  |  |
| `DescrDetalhe_Pla` | string |  |  |
| `CodCateg_Pla` | string |  |  |
| `ItemQtdeUnid_pla` | boolean |  |  |
| `ItemPai_pla` | string |  |  |
| `Agrupador_pla` | boolean |  |  |
| `Totalizador_pla` | number (double) |  |  |
| `Integrado_pla` | boolean |  |  |
| `CodExternoInteg_pla` | string |  |  |

### UAUApi.Models.Orcamento.ConsultarServicoOrcadoDesintegrado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa. |
| `obra` | string |  | Código da obra. |
| `numOrcamento` | integer (int32) |  | Numero do orçamento. |

### UAUApi.Models.Orcamento.ConsultarPlanilhaCronogramaPorChaveRequest

Paulo Roberto de Almeida Júnior Data: 16/11/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  | Usuário logado no sistema |
| `empresa` | integer (int32) |  | Codigo da empresa do orçamento |
| `obra` | string |  | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) |  | Número do orçamento |
| `item` | string |  | Código do item do orçamento |
| `servico` | string |  | Código do serviço do orçamento |
| `periodo` | string |  | Código externo de integração vinculado ao serviço |

### UAUApi.Models.Orcamento.ConsultarInsumosPorChaveRequest

Paulo Roberto de Almeida Júnior Data: 20/11/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa. |
| `obra` | string |  | Código da obra. |
| `orcamento` | integer (int32) |  | Numero do orçamento. |
| `composicao` | string |  | Código da composição |

### UAUApi.Models.Orcamento.ConsultarServicoOrcamentoPorChaveRequest

Ulisses Cardoso de Souza Data: 21/06/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do orçamento |
| `obra` | string | ✓ | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) | ✓ | Número do orçamento |
| `item` | string | ✓ | Código do item do orçamento |
| `servico` | string | ✓ | Código do serviço do orçamento |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao serviço |

### UAUApi.Models.Orcamento.ConsultarEstruturaOrcaPorChaveRequest

Ulisses Cardoso de Souza Data: 21/06/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sequencia` | string | ✓ | Código da sequência da estrutura do serviço |
| `empresa` | integer (int32) | ✓ | Codigo da empresa do orçamento |
| `obra` | string | ✓ | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) | ✓ | Número do orçamento |
| `item` | string | ✓ | Código do item do orçamento |
| `servico` | string | ✓ | Código do serviço do orçamento |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao serviço |

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |

### UAUApi.Models.Orcamento.EstruturasDeServicoDeOrcamentoRequest

- Lista de estruturas de serviço de orçamento, para permitir a inserção em massa.

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `EstruturasDeServicoDeOrcamento` | array de [`UAUApi.Models.Orcamento.InserirEstruturaServicoDeOrcamentoRequest`](#uauapimodelsorcamentoinserirestruturaservicodeorcamentorequest) |  |  |

### UAUApi.Models.Orcamento.InserirEstruturaServicoDeOrcamentoRequest

Ulisses Cardoso de Souza Data: 21/06/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoEstrutura` | integer (int32) |  | Tipo da estrutura 0 - Nível 1 - Item |
| `codigo` | string | ✓ | Código da estrutura |
| `qtde` | number (double) |  | Quantidade da estrutura |
| `valor` | number (double) |  | Valor da estrutura |
| `usuario` | string |  | Usuário logado |
| `sequencia` | string | ✓ | Código da sequência da estrutura do serviço |
| `empresa` | integer (int32) | ✓ | Codigo da empresa do orçamento |
| `obra` | string | ✓ | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) | ✓ | Número do orçamento |
| `item` | string | ✓ | Código do item do orçamento |
| `servico` | string | ✓ | Código do serviço do orçamento |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao serviço |

### UAUApi.Models.Orcamento.AlterarServicoOrcamentoRequest

Ulisses Cardoso de Souza Data: 21/06/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  | Usuário logado |
| `quantidade` | number (double) |  | Quantidade do item/serviço |
| `dataInicio` | string (date-time) |  | Data de início do serviço |
| `dataFim` | string (date-time) |  | Data final do serviço |
| `empresa` | integer (int32) | ✓ | Codigo da empresa do orçamento |
| `obra` | string | ✓ | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) | ✓ | Número do orçamento |
| `item` | string | ✓ | Código do item do orçamento |
| `servico` | string | ✓ | Código do serviço do orçamento |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao serviço |

### UAUApi.Models.Orcamento.ManterPlanilhaCronogramaPorChaveRequest

Paulo Roberto de Almeida Júnior Data: 16/11/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  | Usuário logado no sistema |
| `empresa` | integer (int32) |  | Codigo da empresa do orçamento |
| `obra` | string |  | Codigo da obra do orçamento |
| `numOrcamento` | integer (int32) |  | Número do orçamento |
| `item` | string |  | Código do item do orçamento |
| `servico` | string |  | Código do serviço do orçamento |
| `periodo` | string |  | Código externo de integração vinculado ao serviço |
| `quantidade` | number (double) |  | Quantidade do serviço no cronograma do orçamento, poderá ser 0 ou maior que zero. |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Orcamento.ManterInsumoOrcamentoRequest

Paulo Roberto de Almeida Júnior Data: 20/11/2018

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa. |
| `obra` | string |  | Código da obra. |
| `orcamento` | integer (int32) |  | Numero do orçamento. |
| `composicao` | string |  | Código da composição |
| `insumo` | string |  | Código do insumo |
| `usuario` | string |  | Usuário logado |
| `quantidade` | number (double) |  | Quantidade do insumo do serviço, poderá ser 0 ou maior que zero. |
| `preco` | number (double) |  | preco do insumo do serviço, poderá ser 0 ou maior que zero. |
| `tipoInsumo` | integer (int32) |  | Tipo do insumo em CInsOrca |
| `encargo` | integer (int32) |  | Insumos de mão de obra podem ser de encargo |
