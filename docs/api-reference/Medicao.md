# Medicao

## POST `/api/Medicao/ValidarCNPJAoGravarMedicao`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `CNPJ` | query | string | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`System.Int32&`](#systemint32)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |

---

## POST `/api/v{version}/Medicao/AprovarMedicaoContrato`

**Método com finalidade de aprovar medições de contrato de material e serviço**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Regras básicas:
1. O contrato precisa estar com status aprovado.
2. É necessário permissão de aprovação para o programa OBMEDCONT

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Medicao.AprovarMedicaoContratoRequest`](#uauapimodelsmedicaoaprovarmedicaocontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Medição de contrato | [`Globaltec.UAU.Comp.ResultadoExecucaoResponse`](#globaltecuaucompresultadoexecucaoresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarBoletimMedicao`

**Consultar boletim de medição.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta boletim de medição dentro do sistema UAU.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Medicao.ConsultarBoletimMedicaoRequest`](#uauapimodelsmedicaoconsultarboletimmedicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Boletim de medições | [`UAUApi.Models.BoletimMedicao.ObjetoBoletimMedicao`](#uauapimodelsboletimmedicaoobjetoboletimmedicao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarItensMedicao`

**Consultar itens de medição por empresa, contrato e medição.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Retorna uma lista de itens da medição por empresa, contrato e medição.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Medicao.ConsultarItensMedicaoPorMedicaoRequest`](#uauapimodelsmedicaoconsultaritensmedicaopormedicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de medição de contrato | array de [`UAUApi.Models.Medicao.ItensMedicaoDTO`](#uauapimodelsmedicaoitensmedicaodto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarItensMedicaoPorContrato`

**Consultar itens de medição por contrato.**

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
Esquema: [`UAUApi.Models.Medicao.ConsultarItensMedicaoPorContratoRequest`](#uauapimodelsmedicaoconsultaritensmedicaoporcontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de medição de contrato | array de [`UAUApi.Models.Medicao.ItensMedicao`](#uauapimodelsmedicaoitensmedicao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarItensMedicaoPorItemContrato`

**Consultar itens de medição por item de contrato.**

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
Esquema: [`UAUApi.Models.Medicao.ConsultarItensMedicaoPorItemContratoRequest`](#uauapimodelsmedicaoconsultaritensmedicaoporitemcontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de medição de contrato | array de [`UAUApi.Models.Medicao.ItensMedicao`](#uauapimodelsmedicaoitensmedicao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarItensMedicaoPorMedicao`

**Consultar itens de medição por medição.**

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
Esquema: [`UAUApi.Models.Medicao.ConsultarItensMedicaoPorMedicaoRequest`](#uauapimodelsmedicaoconsultaritensmedicaopormedicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de medição de contrato | array de [`UAUApi.Models.Medicao.ItensMedicao`](#uauapimodelsmedicaoitensmedicao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarItensMedicaoPorServMat`

**Consultar itens de medição por empresa e serviço/material.**

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
Esquema: [`UAUApi.Models.Medicao.ConsultarItensMedicaoPorServMatRequest`](#uauapimodelsmedicaoconsultaritensmedicaoporservmatrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de medição de contrato | array de [`UAUApi.Models.Medicao.ItensMedicao`](#uauapimodelsmedicaoitensmedicao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarMedicao`

**Consultar medição por empresa, contrato e código da medição.**

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
Esquema: [`UAUApi.Models.Medicao.ConsultarMedicaoRequest`](#uauapimodelsmedicaoconsultarmedicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Medição de contrato | array de [`UAUApi.Models.Medicao.Medicao`](#uauapimodelsmedicaomedicao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarMedicaoCompleta`

**Método com finalidade de consultar as medições de contrato de material e serviço**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Para retornar as medições, podem ser feitas as seguintes combinações:
    1. Código da empresa e código do contrato
    2. Código da empresa, código do contrato e código da medição
    3. Código da empresa e CNPJ do contrato ou CNPJ do fornecedor (informado na medição)
    4. Código da empresa e período de geração da medição (data inicial e data final)

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Medicao.ConsultarMedicaoCompletaRequest`](#uauapimodelsmedicaoconsultarmedicaocompletarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Medição de contrato | array de [`UAUApi.Models.Medicao.MedicaoCompleta`](#uauapimodelsmedicaomedicaocompleta) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarMedicaoPorContrato`

**Consultar medição por contrato.**

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
Esquema: [`UAUApi.Models.Medicao.ConsultarMedicaoPorContratoRequest`](#uauapimodelsmedicaoconsultarmedicaoporcontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Medição de contrato | array de [`UAUApi.Models.Medicao.Medicao`](#uauapimodelsmedicaomedicao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarMedicaoPorServMat`

**Consultar medição por empresa, contrato e código da medição.**

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
Esquema: [`UAUApi.Models.Medicao.ConsultarItensMedicaoPorServMatRequest`](#uauapimodelsmedicaoconsultaritensmedicaoporservmatrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Medição de contrato | array de [`UAUApi.Models.Medicao.Medicao`](#uauapimodelsmedicaomedicao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ConsultarMedicoesPorStatus`

**Consultar medições por status e usuário.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Retorna uma lista de medições por status e usuário.
2. Os possíveis status de uma medição são: 
   0 - Aberta;
   1 - Aprovada;
   2 - Medida;
   3 - Proc. Serviço Gerado.
3. O usuário é para indicar quais são as obras que ele possui permissão para retornar as medições pertinentes.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Medicao.ConsultarMedicoesGeradasPorStatusRequest`](#uauapimodelsmedicaoconsultarmedicoesgeradasporstatusrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Medições por status | array de [`UAUApi.Models.Medicao.MedicaoPorStatus`](#uauapimodelsmedicaomedicaoporstatus) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ExcluirMedicao`

**Método com finalidade de excluir uma determinada medição de contrato de material e serviço**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Regras básicas:
1. Somente medições que estiverem abertas e sem nenhuma aprovação poderão ser excluídas.
2. Nenhum processo de pagamento poderá estar vinculado à medição.
3. Nâo pode haver vínculos dependentes entre os itens da medição (vínculo de item do tipo material com item de serviço).
4. Não pode excluir medição que contenha itens que tenham gerado valores excedentes para itens de outras medições.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Medicao.ExcluirMedicaoRequest`](#uauapimodelsmedicaoexcluirmedicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Medição de contrato | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Medicao/ManterMedicao`

**Método com finalidade de inserir ou atualizar uma determinada medição de contrato de material e serviço**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Regras básicas:
1. É possível inserir ou atualizar uma medição de contrato de material e/ou serviço.
1.2. Se o número da medição for informado e essa medição existir, então ela será atualzada, caso contrário será inserida.
2. Só poderão ser atualizadas as medições que estiverem em aberto, ou seja, sem nenhuma confirmação de aprovação.
3. Os adiantamentos de contratos podem ser informados de duas formas, dependendo do tipo de vínculo de planejamento do contrato, se for vinculado por item, pode ser informado diretamente no item específico, 
   ou de forma geral, onde nesse caso será feito o cálculo proporcional, se o vínculo do planejamento for somente por contrato ou não possuir vínculo algum, só pode ser informado o adiantamento geral.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Medicao.ManterMedicaoRequest`](#uauapimodelsmedicaomantermedicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Medição de contrato | array de [`UAUApi.Models.Medicao.MedicaoCompleta`](#uauapimodelsmedicaomedicaocompleta) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Medicao.ManterMedicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `NumeroContrato` | integer (int32) | ✓ | Código do contrato |
| `NumeroMedicao` | integer (int32) |  | Codigo identificador da medição |
| `CodigoFornecedor` | integer (int32) |  | 1. Código do fornecedor - este fornecedor pode ser escolhido na medição em caso de contrato com múltiplos contratados, do contrário é o mesmo fornecedor do contrato. 2. Deve ser informado o código do fornecedor, conforme cadastro ou o CNJP deste, se os dois forem informados, o código será considerado para a atualização da medição. |
| `CNPJFornecedor` | string |  | 1. CNPJ do fornecedor - este fornecedor pode ser escolhido na medição em caso de contrato com múltiplos contratados, do contrário é o mesmo fornecedor do contrato. 2. Deve ser informado o código do fornecedor, conforme cadastro ou o CNJP deste, se os dois forem informados, o código será considerado para a atualização da medição. |
| `NumCidadePrestacaoServ` | integer (int32) |  | Número da cidade do prestador de serviço |
| `Observacao` | string |  | Observação referente à medição |
| `UltimaMedicao` | integer (int32) |  | Indicativo de que se trata da última medição do contrato de material e serviço |
| `DataBase` | string (date-time) |  | Data base para cálculo dos acréscimos, conforme plano de reajuste |
| `UsrCadastro` | string |  | Nome do usuário que está realizando o cadastro da medição |
| `DescontosMedicao` | array de [`UAUApi.Models.Medicao.DescontoMedicaoRequest`](#uauapimodelsmedicaodescontomedicaorequest) |  | Lista dos descontos simples da medição |
| `Itens` | array de [`UAUApi.Models.Medicao.ItemMedicaoRequest`](#uauapimodelsmedicaoitemmedicaorequest) |  | Lista com os itens da medição |
| `Adiantamentos` | array de [`UAUApi.Models.Medicao.AdiantamentoRequest`](#uauapimodelsmedicaoadiantamentorequest) |  | Lista com os adiantamentos da medição |

### UAUApi.Models.Medicao.AdiantamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroProcesso` | integer (int32) | ✓ | Número do processo que deu origem ao adiantamento |
| `Valor` | number (double) | ✓ | Valor do adiantamento |
| `Tipo` | integer (int32) | ✓ | Tipo do adiantamento, onde: 0 - Calc. Desc.; 1 - Não Calc. Desc. -  Se o tipo for 0 o desconto impactará no cálculo dos descontos vinculados |

### UAUApi.Models.Medicao.ItemMedicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Item` | integer (int32) | ✓ | Identificador do item da medição |
| `CodigoAcompanhamento` | integer (int32) |  | Código do serviço ou do material do item da medição |
| `DescontosAdiantamentos` | array de [`UAUApi.Models.Medicao.DescontoAdiantamentoRequest`](#uauapimodelsmedicaodescontoadiantamentorequest) |  |  |

### UAUApi.Models.Medicao.DescontoAdiantamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroProcesso` | integer (int32) | ✓ | Número do processo que deu origem ao adiantamento |
| `Valor` | number (double) | ✓ | Valor do adiantamento |
| `Tipo` | integer (int32) | ✓ | Tipo do adiantamento, onde: 0 - Calc. Desc.; 1 - Não Calc. Desc. -  Se o tipo for 0 o desconto impactará no cálculo dos descontos vinculados |

### UAUApi.Models.Medicao.DescontoMedicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Valor` | number (double) |  | Valor do desconto |
| `Tipo` | integer (int32) |  | Tipo do desconto, onde: 0 - Calc. Desc.; 1 - Não Calc. Desc. -  Se o tipo for 0 o desconto terá impacto no cálculo dos descontos vinculados |
| `Observacao` | string |  | Observação para o desconto |

### UAUApi.Models.Medicao.ExcluirMedicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Codigo da empresa da medição |
| `Contrato` | integer (int32) | ✓ | Codigo do contrato de material ou serviço referente à medição |
| `NumeroMedicao` | integer (int32) | ✓ | Codigo identificador da medição (sempre sequencial) |

### UAUApi.Models.Medicao.MedicaoPorStatus

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoEmpresa` | integer (int32) |  | Código da empresa da medição |
| `DescricaoEmpresa` | string |  | Descrição da empresa da medição |
| `CodigoObra` | string |  | Código da obra da medição |
| `DescricaoObra` | string |  | Descrição da obra da medição |
| `CodigoContrato` | integer (int32) |  | Código do contrato |
| `ObjetoContrato` | string |  | Descrição do contrato |
| `ObservacaoMedicao` | string |  | Observação da medição |
| `TipoControle` | integer (int32) |  | Tipo do controle do contrato: 0 - Serviço; 1 - Material; 2 - Misto; |
| `StatusMedicao` | integer (int32) |  | Status da medição: 0 - Aberta; 1 - Aprovada; 2 - Medida; |
| `UltimaMedicao` | integer (int32) |  | Indicador de última medição do contrato: 0 - Não; 1 - Sim |
| `DataReajuste` | string (date-time) |  | Data de reajuste da medição |
| `CodigoCidade` | integer (int32) |  | Código da cidade da medição |
| `NomeCidade` | string |  | Nome da cidade da medição |
| `ValorExcedenteMedicao` | number (double) |  | Valor excedente da medição (resíduos de medições anteriores) |
| `CodigoFornecedor` | integer (int32) |  | Código do fornecedor da medição |
| `NomeFornecedor` | string |  | Nome do fornecedor da medição |
| `CodigoMedicao` | integer (int32) |  | Código da medição |
| `UF` | string |  | Descrição da UF da cidade da medição |

### UAUApi.Models.Medicao.ConsultarMedicoesGeradasPorStatusRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `status_med` | integer (int32) | ✓ | Status da medição |
| `login_usu` | string | ✓ | Usuário da operação |

### UAUApi.Models.Medicao.ConsultarMedicaoPorContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa da medição. |
| `contrato` | integer (int32) |  | Código do contrato da medição. |

### UAUApi.Models.Medicao.MedicaoCompleta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa da medição |
| `DescrEmpresa` | string |  | Descrição da empresa da medição |
| `CodigoContratado` | integer (int32) |  | Código do fornecedor contratado (informado no contrato de material e serviço) |
| `DescrContratado` | string |  | Nome do fornecedor contratado (informado no contrato de material e serviço) |
| `CNPJContratado` | string |  | CNPJ do contratado (informado no contrato de material e serviço) |
| `NumeroContrato` | integer (int32) |  | Número/Código do contrato de material e serviço |
| `DescrContrato` | string |  | Descrição/Objeto do contrato de material e serviço |
| `NumeroMedicao` | integer (int32) |  | Número/Código da medição do contrato de material e serviço |
| `Status` | integer (int32) |  | Status da medição, onde: 0 - Aberta; 1 - Aprovada, 2 - Medida, 3 - Processo de serviço gerado |
| `DescrStatus` | string |  | Descrição do status de aprovação da medição |
| `CodigoFornecedor` | integer (int32) |  | Código do fornecedor - este fornecedor pode ser escolhido na medição em caso de contrato com múltiplos contratados |
| `DescrFornecedor` | string |  | Nome do fornecedor - este fornecedor pode ser escolhido na medição em caso de contrato com múltiplos contratados |
| `CNPJFornecedor` | string |  | CNPJ do fornecedor - este fornecedor pode ser escolhido na medição em caso de contrato com múltiplos contratados |
| `NumCidadePrestacaoServ` | integer (int32) |  | Número da cidade do prestador de serviço |
| `DescrCidade` | string |  | Descrição da cidade do fornecedor de serviço |
| `UFCidade` | string |  | Unidade Federativa do fornecedor de serviço |
| `Observacao` | string |  | Observação referente a medição |
| `UltimaMedicao` | boolean |  | Indicativo de que se trata da última medição do contrato de material e serviço |
| `DataBase` | string (date-time) |  | Data base para cálculo dos acréscimos, conforme plano de reajuste |
| `SubTotal` | number (double) |  | Total bruto da medição, sem considerar os descontos, acréscimos e valores excedentes |
| `Acrescimos` | number (double) |  | Total de acréscimos da medição, conforme plano de reajuste vigente |
| `Descontos` | number (double) |  | Total de descontos da medição, considera os descontos normais e os descontos vinculados |
| `DescontoVinculado` | number (double) |  | Total de descontos do tipo vinculado (retenções) |
| `Excedente` | number (double) |  | Valores excedentes da medição - existente em situação em que a medição anterior extrapolou  o previsto |
| `Total` | number (double) |  | Total da medição já considerando todos os descontos, acréscimos e valores excedentes |
| `DataIniMedicao` | string (date-time) |  | Data de início da medição - considera a data de início da primeira execução de acompanhamento de contrato |
| `DataFimMedicao` | string (date-time) |  | Data de término da medição - considera a data de início da primeira execução de acompanhamento de contrato |
| `DataCadastro` | string (date-time) |  | Data da geração da medição |
| `UsrCadastro` | string |  | Nome do usuário que realizou o cadastro da medição |
| `DataAprovacao` | string (date-time) |  | Data da aprovação da medição |
| `QuemAprovou` | string |  | Nome do usuário que aprovou a medição |
| `DescontosMedicao` | array de [`UAUApi.Models.Medicao.DescontoMedicao`](#uauapimodelsmedicaodescontomedicao) |  | Lista dos descontos simples da medição |
| `AcrescimosDescontos` | array de [`UAUApi.Models.Medicao.AcrescimoDesconto`](#uauapimodelsmedicaoacrescimodesconto) |  | Lista dos acréscimos existentes na medição |
| `Itens` | array de [`UAUApi.Models.Medicao.Item`](#uauapimodelsmedicaoitem) |  | Lista com os itens da medição |
| `Adiantamentos` | array de [`UAUApi.Models.Medicao.Adiantamento`](#uauapimodelsmedicaoadiantamento) |  | Lista com os adiantamentos da medição |
| `Aprovacoes` | array de [`UAUApi.Models.Medicao.Aprovacao`](#uauapimodelsmedicaoaprovacao) |  | Lista com as aprovações existentes para a medição |

### UAUApi.Models.Medicao.Aprovacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Seq` | integer (int32) |  | Código sequencial da aprovação da medição |
| `Quem` | string |  | Usuário que aprovou a medição |
| `CodigoDepartamento` | string |  | Código do departamento do usuário que aprovou a medição |
| `DescrDepartamento` | string |  | Descrição do departamento do usuário que aprovou a medição |
| `CodigoCargo` | string |  | Código do cargo do usuário que aprovou a medição |
| `DescrCargo` | string |  | Descrição do cargo do usuário que aprovou a medição |
| `Data` | string (date-time) |  | Data da aprovação |
| `Justificativa` | string |  | Justificativa da aprovação |

### UAUApi.Models.Medicao.Adiantamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  | Código do adiantamento |
| `NumeroProcesso` | integer (int32) |  | Número do processo que deu origem ao adiantamento |
| `Valor` | number (double) |  | Valor do adiantamento |
| `Tipo` | integer (int32) |  | Tipo do adiantamento, onde: 0 - Calc. Desc.; 1 - Não Calc. Desc. -  Se o tipo for 0 o desconto impactará no cálculo dos descontos vinculados |
| `DescrTipo` | string |  | Descrição do tipo do adiantamento |
| `CodigoFornecedor` | integer (int32) |  | Código do fornecedor do processo de adiantamento |
| `DescrFornecedor` | string |  | Descrição do fornecedor do processo de adiantamento |
| `CnpjFornecedor` | string |  | CNPJ do fornecedor do processo de adiantamento |
| `Nominal` | string |  | Nominal do processo |

### UAUApi.Models.Medicao.Item

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Item` | integer (int32) |  | Identificador do item da medição |
| `Codigo` | string |  | Código do serviço ou do material do item da medição |
| `Descricao` | string |  | Descrição do item da medição |
| `Unid` | string |  | Unidade do item, ex: KG, UN, CX |
| `Quantidade` | number (double) |  | Quantidade do item a ser medido |
| `Preco` | number (double) |  | Preço do item da medição |
| `Total` | number (double) |  | Total bruto do item na medição |
| `Saldo` | number (double) |  | Saldo de SI referente aos vínculos do item da medição |
| `CodigoServicoFiscal` | string |  | Código de serviço fiscal (CSF) - válido somente para serviço/composição |
| `DescrServicoFiscal` | string |  | Descrição do serviço fiscal |
| `NumServico` | string |  | Número do serviço |
| `DescontosAdiantamentos` | array de [`UAUApi.Models.Medicao.DescontoAdiantamento`](#uauapimodelsmedicaodescontoadiantamento) |  | Lista com os descontos de adiantamentos para o item da medição |

### UAUApi.Models.Medicao.DescontoAdiantamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  | Código do adiantamento |
| `NumeroProcesso` | integer (int32) |  | Número do processo que deu origem ao adiantamento |
| `Valor` | number (double) |  | Valor do adiantamento |
| `Tipo` | integer (int32) |  | Tipo do adiantamento, onde: 0 - Calc. Desc.; 1 - Não Calc. Desc. -  Se o tipo for 0 o desconto impactará no cálculo dos descontos vinculados |
| `DescrTipo` | string |  | Descrição do tipo de adiantamento |

### UAUApi.Models.Medicao.AcrescimoDesconto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Tipo` | integer (int32) |  | Tipo do acréscimo, onde: 0 - Acréscimo; 1 - Desconto; |
| `DescrTipo` | string |  | Descrição do tipo, se acréscimo ou desconto. |
| `Modo` | integer (int32) |  | Modo do acréscimo ou desconto, onde: 0 - Normal; 1 - Vinculado; 2 - Adiantamento; |
| `DescrModo` | string |  | Descrição do modo do acréscimo ou desconto |
| `Valor` | number (double) |  | Valor do acréscimo ou desconto. |

### UAUApi.Models.Medicao.DescontoMedicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  | Código sequencial do desconto |
| `Valor` | number (double) |  | Valor do desconto |
| `Tipo` | integer (int32) |  | Tipo do desconto, onde: 0 - Calc. Desc.; 1 - Não Calc. Desc. -  Se o tipo for 0 o desconto terá impacto no cálculo dos descontos vinculados |
| `DescrTipo` | string |  | Descrição do tipo de desconto |
| `Observacao` | string |  | Observação para o desconto |

### UAUApi.Models.Medicao.ConsultarMedicaoCompletaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Contrato` | integer (int32) |  | Código do contrato |
| `Medicao` | integer (int32) |  | Código da medição |
| `CNPJContratado` | string |  | CNPJ do contratado |
| `CNPJFornecedor` | string |  | CNPJ do fornecedor |
| `DataInicial` | string (date-time) |  | Data de início do primeiro acompanhamento da medição |
| `DataFinal` | string (date-time) |  | Data de término do último acompanhamento da medição |

### UAUApi.Models.Medicao.Medicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa_med` | integer (int32) |  |  |
| `Contrato_med` | integer (int32) |  |  |
| `Cod_med` | integer (int32) |  |  |
| `Acres_med` | number (double) |  |  |
| `Desc_med` | number (double) |  |  |
| `Valor_med` | number (double) |  |  |
| `DtCriacao_med` | string (date-time) |  |  |
| `Quem_med` | string |  |  |
| `Obs_med` | string |  |  |
| `Status_med` | integer (int32) |  |  |
| `UsrAprov_med` | string |  |  |
| `DataAprov_med` | string (date-time) |  |  |
| `Ultima_med` | integer (int32) |  |  |
| `ValorExcedente_med` | number (double) |  |  |
| `DescVinc_med` | number (double) |  |  |
| `DataReajuste_med` | string (date-time) |  |  |
| `CalcAprov_med` | boolean |  |  |
| `CodPes_med` | integer (int32) |  |  |
| `NumCid_med` | integer (int32) |  |  |
| `DescrContrato_med` | string |  |  |
| `DescrPes_med` | string |  |  |

### UAUApi.Models.Medicao.ConsultarMedicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `contrato` | integer (int32) |  | Código do contrato |
| `medicao` | integer (int32) |  | Código da medição |

### UAUApi.Models.Medicao.ConsultarItensMedicaoPorServMatRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa da medição. |
| `servMat` | string |  | Código do serviço ou material da medição. |

### UAUApi.Models.Medicao.ConsultarItensMedicaoPorItemContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `contrato` | integer (int32) |  | Código do contrato |
| `medicao` | integer (int32) |  | Código da medição |
| `itemContrato` | integer (int32) |  | Código do item do contrato |

### UAUApi.Models.Medicao.ItensMedicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa_Item` | integer (int32) |  |  |
| `Contrato_Item` | integer (int32) |  |  |
| `CodMed_Item` | integer (int32) |  |  |
| `Ins_Item` | string |  |  |
| `Qtde_Item` | number (double) |  |  |
| `PrecoUnit_Item` | number (double) |  |  |
| `Unid_Item` | string |  |  |
| `Reaj_item` | number (double) |  |  |
| `Desc_Item` | number (double) |  |  |
| `ValDiferenca_Item` | number (double) |  |  |
| `Total_Item` | number (double) |  |  |
| `ItensCont_Item` | integer (int32) |  |  |
| `DescrCont_item` | string |  |  |
| `DescrIns_Item` | string |  |  |

### UAUApi.Models.Medicao.ConsultarItensMedicaoPorContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa da medição. |
| `contrato` | integer (int32) |  | Código do contrato da medição. |

### UAUApi.Models.Medicao.ItensMedicaoDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Serv_itens` | string |  | Código do serviço ou material |
| `Descr_itens` | string |  | Descrição do serviço ou material |
| `TipoServMat_Itens` | string |  | Tipo do item do contrato, se serviço/composição ou material |
| `Qtde_Item` | string |  | Quantidade do item na medição |
| `PrecoUnit_Item` | string |  | Preço unitário do item |
| `Valor_Total` | string |  | Subtotal do item da medição: (Quantidade * Preço ) + ValorDiferenca (resíduos de medições anteriores) |

### UAUApi.Models.Medicao.ConsultarItensMedicaoPorMedicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `contrato` | integer (int32) | ✓ | Código do contrato |
| `medicao` | integer (int32) | ✓ | Código da medição |

### UAUApi.Models.BoletimMedicao.ObjetoBoletimMedicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa |
| `DescrEmpresa` | string |  | Descrição da empresa |
| `Obra` | string |  | Código da obra |
| `DescrObra` | string |  | Descrição da obra |
| `Objeto` | string |  | Objeto da medição |
| `Contrato` | integer (int32) |  | Código do contrato |
| `Medicao` | integer (int32) |  | Código da medição principal do contrato, neste caso sendo considerada como sendo a última para o contrato. |
| `Contratado` | integer (int32) |  | Código do contratado |
| `DescrContratado` | string |  | Descrição do contratado |
| `ContratadoMedicao` | integer (int32) |  | Código do contratado da medição principal. |
| `DescrContratadoMedicao` | string |  | Descrição do contratado da medição principal. |
| `Telefone` | string |  | Telefone da medição |
| `Contato` | string |  | Contato da medição |
| `MedicaoFisicaAcumulada` | number (double) |  | Medição fisica acumulada |
| `ValoresADescontar` | number (double) |  | Valores a descontar |
| `SaldoContratualLiquido` | number (double) |  | Saldo contra atual liquido |
| `Medicoes` | array de [`UAUApi.Models.BoletimMedicao.DadosMedicoes`](#uauapimodelsboletimmedicaodadosmedicoes) |  | Lista de medições |
| `VlrContratual` | number (double) |  | Valor contra atual |
| `VlrContratualLiquido` | number (double) |  | Valor contratual liquido: Total do contrato - Valor burto físico medido - saldo Adiantado. |
| `Observacao` | string |  | Observação da medição |
| `Nota` | string |  | Nota da medição |
| `NotaQuitacao` | string |  | Nota quitação |
| `AvancoFisico` | array de [`UAUApi.Models.BoletimMedicao.DadosAvancoFisico`](#uauapimodelsboletimmedicaodadosavancofisico) |  | Lista avanço fisico |
| `AdiantamentoVinculado` | array de [`UAUApi.Models.BoletimMedicao.AdiantamentoVinculado`](#uauapimodelsboletimmedicaoadiantamentovinculado) |  |  |

### UAUApi.Models.BoletimMedicao.AdiantamentoVinculado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  | Código do adiantamento |
| `NumeroProcesso` | integer (int32) |  | Número do processo do adiantamento de contrato |
| `Fornecedor` | string |  | Nome do fornecedor |
| `CodigoFornecedor` | integer (int32) |  | Código do fornecedor |
| `CnpjFornecedor` | string |  | CNPJ do fornecedor |
| `Valor` | number (double) |  | Valor do processo |
| `ValorExcedido` | number (double) |  | Valor vinculado excedido |
| `Tipo` | integer (int32) |  | Código do tipo do processo |
| `DescrTipo` | string |  | Descrição do tipo do processo |
| `Nominal` | string |  | Nominal do processo |
| `NotaFiscal` | string |  | Número da nota fiscal |
| `ValorNF` | number (double) |  | Valor da nota fiscal |
| `DataPagamento` | string (date-time) |  | Data de pagamento do processo |

### UAUApi.Models.BoletimMedicao.DadosAvancoFisico

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Item` | integer (int32) |  | Código do item |
| `Descricao` | string |  | Descrição do avanço fisico |
| `Unidade` | string |  | Unidade |
| `Qtde` | number (double) |  | Quantidade do avanço fisico |
| `Preco` | number (double) |  | Preço do avanço fisico |
| `Total` | number (double) |  | Total do avanço fisico |
| `AvancoQuantitativo` | [`UAUApi.Models.BoletimMedicao.DadosAvancoQuantFinan`](#uauapimodelsboletimmedicaodadosavancoquantfinan) |  | Avanço quantitativo |
| `AvancoFinanceiro` | [`UAUApi.Models.BoletimMedicao.DadosAvancoQuantFinan`](#uauapimodelsboletimmedicaodadosavancoquantfinan) |  | Avanço financeiro |

### UAUApi.Models.BoletimMedicao.DadosAvancoQuantFinan

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `AcumAnterior` | number (double) |  | Acumulativa anterior |
| `TotalAtual` | number (double) |  | Total atual |
| `TotalAcum` | number (double) |  | Total acumulativa |
| `SaldoContrato` | number (double) |  | Saldo do contrato |

### UAUApi.Models.BoletimMedicao.DadosMedicoes

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Medicao` | integer (int32) |  | Código da medição |
| `Periodo` | string |  | Periodo da medição |
| `Data` | string (date-time) |  | Data da medição |
| `NotaFiscal` | string |  | Nota fiscal |
| `BrutoFisico` | number (double) |  | Valor bruto físico medido: Só os valores medidos vinculados a serviços. (A) |
| `FatDiretoOutrosDebitos` | number (double) |  | Faturamento direto e outros débitos: São os descontos vinculados a medição (adiantamento de valores). (B) |
| `MedicaoAdiantada` | number (double) |  | Medição adianta: São medições de material sem estarem com serviços vinculados (sem ter medido serviço). (C) |
| `Retencao` | number (double) |  | Retenção: é o valor de retenção vinculada ao contrato aplicada ao valor da medição que vai ser paga. (D) |
| `Desconto` | number (double) |  | Desconto: São os descontos aplicados referente ao saldo adiantado da medição ao fornecedor,  quantidade de serviços executada, de materiais já entregues. (E) |
| `SaldoAdiantado` | number (double) |  | Saldo adiantado.: é o resultado de Faturamento direto/Outros débitos + Medição Adiantado - Desconto. (F=Fant+(B+C-E)) |
| `ValorLiquido` | number (double) |  | Valor liquido (G=(H-D)) |
| `ValorNF` | number (double) |  | Valor NF (H=(A+C-E)) |

### UAUApi.Models.Medicao.ConsultarBoletimMedicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa. |
| `contrato` | integer (int32) | ✓ | Código do contrato. |
| `avancoFisico` | boolean | ✓ | Exibir o avanço físico no relatório. |
| `medicao` | integer (int32) |  | Código da medição -&gt; (0 – Para retorna todas as medições ou o número específico da medição.) |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### Globaltec.UAU.Comp.ResultadoExecucaoResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sucesso` | boolean |  |  |
| `mensagem` | string |  |  |

### UAUApi.Models.Medicao.AprovarMedicaoContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa da Medição |
| `contrato` | integer (int32) |  | Código do contrato da medição |
| `medicao` | integer (int32) |  | Codigo da medição a ser aprovada |
| `Codigojustificativa` | integer (int32) |  | Código da justificativa de aprovacao fora de sequência |
| `Observacaojustificativa` | string |  | Observação da justificativa de aprovação fora de sequência |
| `departamento` | string |  | Código do departamento do usuário da aprovação |
| `cargo` | string |  | Código do cargo do usuário da aprovação |

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |

### System.Int32&

Tipo: object
