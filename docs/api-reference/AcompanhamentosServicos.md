# AcompanhamentosServicos

## POST `/api/v{version}/AcompanhamentosServicos/AcompanharContrato`

**Grava o acompanhamento de contrato vinculado a um planejamento ou orçamento**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Grava o acompanhamento de contrato vinculado a um planejamento ou orçamento
1. Informar os parâmetros dependendo do vinculo com orçamento ou planejamento

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.AcompanharContratoRequest`](#uauapimodelsacompanhamentosservicosacompanharcontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Acompanhamento de contratos da obra. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/AcompanharServicoContrato`

**Acompanhar serviços de contrato.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método do acordo com o modelo.

Definição de Negócio:
Permite consultar e portanto acompanhar serviços referentes aos contratos.
1. Valida usuário.
2. Valida prazo de validade do contrato.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.AcompanharServicoContratoRequest`](#uauapimodelsacompanhamentosservicosacompanharservicocontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Acompanhamento de serviços de contrato. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/AcompanharServicoContratoEmLote`

**Acompanhar vários serviços do contrato.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método do acordo com o modelo.

Definição de Negócio:
Permite acompanhar vários serviços referentes ao contrato.
1. Valida usuário.
2. Valida prazo de validade do contrato.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.AcompanharServicoContratoEmLoteRequest`](#uauapimodelsacompanhamentosservicosacompanharservicocontratoemloterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Acompanhamento de serviços de contrato. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/AcompanharServicoOrcado`

**Acompanhar serviços de orçamento.**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite consultar e portanto acompanhar os serviços que foram orçados de acordo com os parâmentros passados na requisição.
1. Deve montar uma estrutura seguindo o modelo.
2. Valida se o usuário está cadastrado.
3. Valida se o serviço não possui estruturas.
4. Valida se possui distribuição no periodo acompanhado.
5. Valida o saldo do orçamento que será acompanhado.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.AcompanharServicoOrcadoRequest`](#uauapimodelsacompanhamentosservicosacompanharservicoorcadorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Acompanhamento de serviços de orçamento. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/AcompanharServicoOrcadoEmLote`

**Acompanhar vários serviços do orçamento.**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Acompanhar vários serviços do orçamento.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.AcompanharServicoOrcadoEmLoteRequest`](#uauapimodelsacompanhamentosservicosacompanharservicoorcadoemloterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Acompanhamento de serviços de orçamento. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/AcompanharServicoPL`

**Acompanhamento de Serviços do planejamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio: 
Acompanhar serviço do planejamento solicitado.
1. Valida se o usuário está cadastrado no sistema e ativo.
2. Valida se já existe acompanhamento para o código externo de integração solicitado.
3. Verifica se o fechamento do acompanhamento não foi realizado.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.AcompanharServicoPLRequest`](#uauapimodelsacompanhamentosservicosacompanharservicoplrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/AlterarAcompanhamentoServicoContrato`

**Alterar acompanhamento de serviços de contrato.**

Definição técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite consultar e portanto acompanhar os serviços que foram orçados de acordo com os parâmentros passados na requisição.
1. Deve montar uma estrutura seguindo o modelo.
2. Valida se o usuário é cadastrado e se tem permissão para realizar a alteração.
3. Valida se o serviço é controlado por tipologia de produção.
4. Valida se a quantidade a acompanhar excede o saldo a acompanhar.
5. Valida se o contrato é valido para aletrações.
6. Valida o prazo de validade do contrato.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.AcompanharServicoContratoRequest`](#uauapimodelsacompanhamentosservicosacompanharservicocontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Alterar um acompanhamento de Serviços de contrato. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorContratoEServico`

**Acompanhar contrato de serviço por empresa, contrato e serviço.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
Definição de Negócio:
Permite acompanhar contratos filtrando por:
    - Empresa
    - Contrato
    - Serviço

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.ConsultarAcompExecContratoPorContratoEServicoRequest`](#uauapimodelsacompanhamentosservicosconsultaracompexeccontratoporcontratoeservicorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Método com finalidade de retornar registros de acompanhamento de contrato de serviço por empresa, contrato e um determinado serviço. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/ConsultarAcompanhamentoContratoServicoPorServico`

**Acompanhar contrato de serviço por empresa e serviço.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Consulta acompanhamento de contrato de serviço filtrando por serviço.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.ConsultarAcompExecContratoPorServicoRequest`](#uauapimodelsacompanhamentosservicosconsultaracompexeccontratoporservicorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContrato`

**Excluir acompanhamento de serviço de contrato.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Exclui o acompanhamento de serviço no contrato.
1. Valida se o usuário tem permissão para excluir um acompanhamento.
2. Valida se possui estrutura e se o status do acompanhamento está como "aberto". Neste caso não será excluido.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoDeContratoRequest`](#uauapimodelsacompanhamentosservicosexcluiracompanhamentoservicodecontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de acompanhamento de serviço de contrato | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoDeContratoEmLote`

**Excluir acompanhamento de serviços do contrato.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Exclui o acompanhamento de vários serviços no contrato.
1. Valida se o usuário tem permissão para excluir um acompanhamento.
2. Valida se possui estrutura e se o status do acompanhamento está como "aberto". Neste caso não será excluido.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoDeContratoEmLoteRequest`](#uauapimodelsacompanhamentosservicosexcluiracompanhamentoservicodecontratoemloterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de acompanhamento de serviço de contrato | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcado`

**Excluir acompanhamento de serviço orçado.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite excluir acompanhamento de serviço orçado.
1. Valida se a exclusão pode ser realizada.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoOrcadoRequest`](#uauapimodelsacompanhamentosservicosexcluiracompanhamentoservicoorcadorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de acompanhamento de serviço de orçamento | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoEmLote`

**Excluir acompanhamento de serviços orçado.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite excluir acompanhamento de vários serviços orçados.
1. Valida se a exclusão pode ser realizada.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoOrcadoEmLoteRequest`](#uauapimodelsacompanhamentosservicosexcluiracompanhamentoservicoorcadoemloterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de acompanhamento de serviço de orçamento | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoOrcadoPorChave`

**Excluir acompanhamento de serviço orçado por chave.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Exclui o acompanhamento de serviço oraçado de acordo com a chave informada.
1. Valida se o acompanhamento informado existe.
2. Valida se a exclusão pode ser realizada.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoOrcadoRequest`](#uauapimodelsacompanhamentosservicosexcluiracompanhamentoservicoorcadorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de acompanhamento de serviço de orçamento por chave | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanhamentosServicos/ExcluirAcompanhamentoServicoPL`

**Excluir acompanhamento de Serviços do planejamento.**

Definição Técnica:
Permite excluir acompanhamento de Serviços do planejamento.
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio: 
Acompanhar serviço do planejamento solicitado.
1. Valida se existe acompanhamento para o código informado.
2. Valida se existe acompanhamento para o registro informado.
3. Valida se o acompanhamento se encontra aberto.
4. Valida a quantidade informada para exclusão.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoPLRequest`](#uauapimodelsacompanhamentosservicosexcluiracompanhamentoservicoplrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exclusão de acompanhamento de Serviços do planejamento da obra. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoPLRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | string | ✓ | Codigo da empresa do serviço |
| `obra` | string | ✓ | Codigo da obra do serviço |
| `produto` | integer (int32) |  | Codigo do produto do serviço |
| `contrato` | integer (int32) | ✓ | Codigo do contrato do serviço |
| `item` | string |  | Codigo do item do serviço |
| `servico` | string |  | Codigo do serviço |
| `mes` | string |  | Mês pl do serviço |
| `usuario` | string | ✓ | login do usuário do serviço |
| `qtde` | number (double) |  | Quantidade do serviço |
| `sequencia` | string |  | Sequencia do serviço |
| `codExternoIntegracao` | string |  | Código externo de integração do acompanhamento de serviço PL |

### UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoOrcadoEmLoteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do serviço. |
| `obra` | string | ✓ | Codigo da obra do serviço |
| `orcamento` | integer (int32) |  | Codigo do orçamento do serviço |
| `avancos` | array de [`UAUApi.Models.AcompanhamentosServicos.ServicosOrcadoParaExcluir`](#uauapimodelsacompanhamentosservicosservicosorcadoparaexcluir) | ✓ | Codigo do serviço |

### UAUApi.Models.AcompanhamentosServicos.ServicosOrcadoParaExcluir

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `servico` | string | ✓ |  |
| `item` | string |  | Codigo do item do serviço |
| `periodo` | string |  | Período do serviço |
| `quantidade` | number (double) |  | Quantidade do serviço |
| `sequencia` | string |  | Sequencia do serviço. |
| `numAcomp` | integer (int32) |  | Numero do acompanhamento do serviço. |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao acompanhamento do serviço do orçamento |

### UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoOrcadoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do serviço. |
| `obra` | string | ✓ | Codigo da obra do serviço |
| `servico` | string | ✓ | Codigo do serviço |
| `item` | string |  | Codigo do item do serviço |
| `orcamento` | integer (int32) |  | Codigo do orçamento do serviço |
| `periodo` | string |  | Período do serviço |
| `quantidade` | number (double) |  | Quantidade do serviço |
| `sequencia` | string |  | Sequencia do serviço. |
| `numAcomp` | integer (int32) |  | Numero do acompanhamento do serviço. |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao acompanhamento do serviço do orçamento |

### UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoDeContratoEmLoteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do serviço |
| `contrato_servico` | integer (int32) | ✓ | Codigo do contrato do serviço |
| `usuario_logado` | string | ✓ | Login do usuário logado |
| `avancos` | array de [`UAUApi.Models.AcompanhamentosServicos.Avanco`](#uauapimodelsacompanhamentosservicosavanco) | ✓ |  |

### UAUApi.Models.AcompanhamentosServicos.Avanco

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `item_contrato` | integer (int32) | ✓ | Codigo do item do serviço |
| `servico` | string | ✓ | Codigo do serviço |
| `quantidade` | number (double) |  | Quantidade do serviço |
| `sequencia` | string |  | Sequencia do serviço |
| `codigo_estrutura` | string |  | Codigo da estrutura do serviço |
| `codAec` | integer (int32) |  | Codigo do acompanhamento de execução de contrato |

### UAUApi.Models.AcompanhamentosServicos.ExcluirAcompanhamentoServicoDeContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do serviço |
| `contrato_servico` | integer (int32) | ✓ | Codigo do contrato do serviço |
| `item_contrato` | integer (int32) | ✓ | Codigo do item do serviço |
| `servico` | string | ✓ | Codigo do serviço |
| `quantidade` | number (double) |  | Quantidade do serviço |
| `sequencia` | string |  | Sequencia do serviço |
| `codigo_estrutura` | string |  | Codigo da estrutura do serviço |
| `usuario_logado` | string | ✓ | Login do usuário logado |
| `codAec` | integer (int32) |  | Codigo do acompanhamento de execução de contrato |

### UAUApi.Models.AcompanhamentosServicos.ConsultarAcompExecContratoPorServicoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Servico` | string | ✓ | Código do serviço |

### UAUApi.Models.AcompanhamentosServicos.ConsultarAcompExecContratoPorContratoEServicoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Contrato` | integer (int32) | ✓ | Código do contrato |
| `Servico` | string | ✓ | Código do serviço |

### UAUApi.Models.AcompanhamentosServicos.AcompanharServicoPLRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | string | ✓ | Codigo da empresa do serviço |
| `obra` | string | ✓ | Codigo da obra do serviço |
| `produto` | integer (int32) |  | Codigo do produto do serviço |
| `contrato` | integer (int32) |  | Codigo do contrato do serviço |
| `item` | string |  | Codigo do item do serviço |
| `servico` | string |  | Codigo do serviço |
| `mes` | string |  | Mês pl do serviço |
| `usuario` | string | ✓ | Login do usuário logado |
| `qtde` | number (double) |  | Quantidade do serviço |
| `sequencia` | string |  | Sequencia do serviço |
| `codExternoIntegracao` | string |  | Código externo de integração do acompanhamento de serviço PL |
| `aprovaContrato` | boolean |  | indica se deve aprovar o contrato vinculado |
| `contratoVinculado` | integer (int32) |  | contrato |
| `descricaoServico` | string |  |  |
| `ordem` | integer (int32) |  |  |
| `etapa` | string |  |  |
| `observacao` | string |  |  |

### UAUApi.Models.AcompanhamentosServicos.AcompanharServicoOrcadoEmLoteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do serviço |
| `obra` | string | ✓ | Codigo da obra do serviço |
| `orcamento` | integer (int32) |  | Codigo do orçamento do serviço |
| `usuario_logado` | string | ✓ | Login do usuário logado |
| `servicos` | array de [`UAUApi.Models.AcompanhamentosServicos.ListaServicosOrcados`](#uauapimodelsacompanhamentosservicoslistaservicosorcados) | ✓ |  |

### UAUApi.Models.AcompanhamentosServicos.ListaServicosOrcados

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `servico` | string | ✓ | Codigo do serviço |
| `item` | string | ✓ | Codigo do item do serviço |
| `periodo` | string |  | Período do serviço |
| `quantidade` | number (double) |  | Quantidade do serviço |
| `sequencia` | string |  | Sequencia do serviço |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao acompanhamento do serviço do orçamento |
| `aprovaContrato` | boolean |  | indica se deve aprovar o contrato vinculado |
| `contratoVinculado` | integer (int32) |  | contrato |
| `descricaoServico` | string |  |  |
| `etapa` | string |  |  |
| `mes` | string |  |  |
| `produto` | integer (int32) |  |  |
| `contrato` | integer (int32) |  |  |
| `observacao` | string |  |  |

### UAUApi.Models.AcompanhamentosServicos.AcompanharServicoOrcadoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do serviço |
| `obra` | string | ✓ | Codigo da obra do serviço |
| `servico` | string | ✓ | Codigo do serviço |
| `item` | string | ✓ | Codigo do item do serviço |
| `orcamento` | integer (int32) |  | Codigo do orçamento do serviço |
| `periodo` | string |  | Período do serviço |
| `quantidade` | number (double) |  | Quantidade do serviço |
| `usuario_logado` | string | ✓ | Login do usuário logado |
| `sequencia` | string |  | Sequencia do serviço |
| `codExternoIntegracao` | string |  | Código externo de integração vinculado ao acompanhamento do serviço do orçamento |
| `aprovaContrato` | boolean |  | indica se deve aprovar o contrato vinculado |
| `contratoVinculado` | integer (int32) |  | contrato |
| `descricaoServico` | string |  |  |
| `ordem` | integer (int32) |  |  |
| `etapa` | string |  |  |
| `mes` | string |  |  |
| `produto` | integer (int32) |  |  |
| `contrato` | integer (int32) |  |  |
| `observacao` | string |  |  |

### UAUApi.Models.AcompanhamentosServicos.AcompanharServicoContratoEmLoteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do serivço |
| `obra` | string | ✓ | Codigo da obra do serviço |
| `contrato_servico` | integer (int32) | ✓ | Codigo do contrato do serviço |
| `usuario_logado` | string | ✓ | Login do usuário logado |
| `servicos` | array de [`UAUApi.Models.AcompanhamentosServicos.ListaServicos`](#uauapimodelsacompanhamentosservicoslistaservicos) | ✓ |  |

### UAUApi.Models.AcompanhamentosServicos.ListaServicos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `item_contrato` | integer (int32) | ✓ | Codigo do item do contrato do serviço |
| `servico` | string |  | Codigo do serviço |
| `data_inicio` | string |  | Data início do serviço. |
| `data_fim` | string |  | Data fim do serviço |
| `mes_pl` | string |  | Mes pl do serviço |
| `quantidade` | number (double) |  | Quantidade do serivço |
| `porcentagem_acomp` | number (double) |  | Porcentagem do serviço |
| `observacoes` | string |  | Observações do serviço |
| `etapa` | string |  | Etapa do serviço |
| `cod_estrutura` | string |  | Codigo da estrutura do serviço. Deve ser passado como "" em caso de item sem estrutura. (CodItem_aec) |
| `sequencia` | string |  | Sequencia do serviço. Deve ser passado como "" em caso de item sem estrutura. |
| `cod_acomp` | number (double) |  | Código do acompanhamento |
| `orcamento` | integer (int32) |  | Código do orçamento para realizar o acompanhamento de execução em paralelo. |
| `itemOrcamento` | string |  | Item do orçamento para realizar o acompanhamento de execução em paralelo. |
| `aplicacaoMaterial` | array de [`UAUApi.Models.AcompanhamentosServicos.QtdAplicadaPorMaterial`](#uauapimodelsacompanhamentosservicosqtdaplicadapormaterial) |  | Lista para informar a quantidade que será aplicada por item de material. (Usada quando há vínculos entre itens do contrato) |

### UAUApi.Models.AcompanhamentosServicos.QtdAplicadaPorMaterial

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `itemMaterial` | integer (int32) |  | Identificador do item de material em que será aplicadado a quantidade |
| `QtdeAplicada` | number (double) |  | Quantidade que será aplicada no material |

### UAUApi.Models.AcompanhamentosServicos.AcompanharServicoContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Codigo da empresa do serivço |
| `obra` | string | ✓ | Codigo da obra do serviço |
| `contrato_servico` | integer (int32) | ✓ | Codigo do contrato do serviço |
| `item_contrato` | integer (int32) | ✓ | Codigo do item do contrato do serviço |
| `servico` | string |  | Codigo do serviço |
| `data_inicio` | string |  | Data início do serviço. |
| `data_fim` | string |  | Data fim do serviço |
| `mes_pl` | string |  | Mes pl do serviço |
| `quantidade` | number (double) |  | Quantidade do serivço |
| `porcentagem_acomp` | number (double) |  | Porcentagem do serviço |
| `observacoes` | string |  | Observações do serviço |
| `etapa` | string |  | Etapa do serviço |
| `cod_estrutura` | string |  | Codigo da estrutura do serviço. Deve ser passado como "" em caso de item sem estrutura. |
| `sequencia` | string |  | Sequencia do serviço. Deve ser passado como "" em caso de item sem estrutura. |
| `usuario_logado` | string |  | Login do usuário logado |
| `cod_acomp` | number (double) |  | Código do acompanhamento |
| `orcamento` | integer (int32) |  | Código do orçamento para realizar o acompanhamento de execução em paralelo. |
| `itemOrcamento` | string |  | Item do orçamento para realizar o acompanhamento de execução em paralelo. |
| `aplicacaoMaterial` | array de [`UAUApi.Models.AcompanhamentosServicos.QtdAplicadaPorMaterial`](#uauapimodelsacompanhamentosservicosqtdaplicadapormaterial) |  | Lista para informar a quantidade que será aplicada por item de material. (Usada quando há vínculos entre itens do contrato) |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.AcompanhamentosServicos.AcompanharContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | string |  | Codigo da empresa |
| `obra` | string |  | Codigo da obra |
| `produto` | integer (int32) |  | Codigo do produto (apenas para planejamento) |
| `contrato` | integer (int32) |  | Codigo do contrato (apenas para planejamento) |
| `item` | string |  | Codigo do item do serviço (planejamento ou orçamento) |
| `servico` | string |  | Codigo do serviço |
| `descricaoServico` | string |  | Descrição do serviço |
| `mes` | string (date-time) |  | Mês pl para planejamento ou Período Mensal, para orçamento. Obs informar data no formato Mês/Dia/Ano |
| `dataInicio` | string (date-time) |  | Data inicio do acompanhamento do contrato. Obs informar data no formato Mês/Dia/Ano |
| `dataFim` | string (date-time) |  | Data final do acompanhamento do contrato. Obs informar data no formato Mês/Dia/Ano |
| `usuario` | string |  | Usuário logado |
| `qtde` | number (double) |  | Quantidade a ser acompanhada |
| `sequencia` | string |  | Sequencia da estrutura (para quando for acompanhamento de estrutura) |
| `codigoEstrutura` | string |  | Código da estrutura (para quando for acompanhamento de estrutura) |
| `orcamento` | integer (int32) |  | Código do orçamento (apenas para orçamento) |
| `contratoVinculado` | integer (int32) |  | Código do contrato vinculado ao planejamento/orçamento |
| `ordem` | integer (int32) |  | É o Item do Serv. no acompanhamento de execução de contrato |
| `etapa` | string |  | A descrição da etapa que está sendo acompanhada |
| `observacao` | string |  | Campo livre |
| `aplicacaoMaterial` | array de [`UAUApi.Models.AcompanhamentosServicos.QtdAplicadaPorMaterial`](#uauapimodelsacompanhamentosservicosqtdaplicadapormaterial) |  | Lista para informar a quantidade que será aplicada por item de material. (Usada quando há vínculos entre itens do contrato) |
