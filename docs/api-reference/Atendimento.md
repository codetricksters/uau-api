# Atendimento

## POST `/api/v{version}/Atendimento/ConsultarAtendimento`

**Método que consulta atendimento.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarAtendimentoRequest`](#uauapimodelsatendimentoconsultaratendimentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarAtendimentoDetalhadoPorChave`

**Consulta atendimento detalhado por código do atendimento.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarAtendimentoDetalhadoPorChaveRequest`](#uauapimodelsatendimentoconsultaratendimentodetalhadoporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarAtendimentoPorCategoriasUauWeb`

**Realiza consulta de atendimentos do cliente por categorias de comentários configuradas para o Uau Web.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarAtendimentoPorCategoriasUauWebRequest`](#uauapimodelsatendimentoconsultaratendimentoporcategoriasuauwebrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarAtendimentoPorPessoa`

**Realiza consulta de atendimentos do cliente independente de categorias configuradas para o Uau Web.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarAtendimentoPorPessoaRequest`](#uauapimodelsatendimentoconsultaratendimentoporpessoarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Atendimento |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarAtendimentoPorPessoaComentario`

**Consulta atendimento pelo pessoa e código da categoria de comentário**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarAtendimentoPorPessoaComentarioRequest`](#uauapimodelsatendimentoconsultaratendimentoporpessoacomentariorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarCategDeComentAtivas`

**Consulta as categorias de comentários ativas.**

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
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarCategoriaAtendimentoWeb`

**Consulta as categorias de atendimento web.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarCategoriaAtendimentoWebRequest`](#uauapimodelsatendimentoconsultarcategoriaatendimentowebrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarConfiguracaoAtendimentoUAUWEB`

**Método que consulta as configurações do uauweb.**

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
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Repositorio.ConfigAtendimentoUAUWEBInfo`](#globaltecuaurepositorioconfigatendimentouauwebinfo) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarDataPrevistaDeTerminoAtendimento`

**Método que consulta a data prevista para término do atendimento.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarDataPrevistaDeTerminoAtendimentoRequest`](#uauapimodelsatendimentoconsultardataprevistadeterminoatendimentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string (date-time) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarEmpreendimentosCliente`

**Consultar todos os empreendimentos do cliente do qual ele é titular da venda.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarEmpreendimentosClienteRequest`](#uauapimodelsatendimentoconsultarempreendimentosclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarNumeroVinculoCategoriaDeComentarioComWorkFlow`

**Método que consulta o número do vinculo da categoria de comentário com o workflow.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarNumeroVinculoCategoriaDeComentarioComWorkFlowRequest`](#uauapimodelsatendimentoconsultarnumerovinculocategoriadecomentariocomworkflowrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | integer (int32) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarNumeroWorkFlowVinculado`

**Consulta o número do workflow vinculado.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarNumeroWorkFlowVinculadoRequest`](#uauapimodelsatendimentoconsultarnumeroworkflowvinculadorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | integer (int32) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarPendencia`

**Consulta as pendências**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarPendenciaRequest`](#uauapimodelsatendimentoconsultarpendenciarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Atendimento.Pendencia`](#uauapimodelsatendimentopendencia) |
| 400 | O número da pendência é obrigatório! - O responsável pela resolução da pendência é obrigatório. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarPendenciaObservacao`

**Consulta as etapas (pendências).**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarPendenciaObservacaoRequest`](#uauapimodelsatendimentoconsultarpendenciaobservacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarPendenciasPorNumeroVinculo`

**Consulta as etapas(pendências) de um atendimento.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarPendenciasPorNumeroVinculoRequest`](#uauapimodelsatendimentoconsultarpendenciaspornumerovinculorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/ConsultarUnidadesDoEmpreendimentoCliente`

**Método que consulta a data prevista para término do atendimento.**

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
Esquema: [`UAUApi.Models.Atendimento.ConsultarUnidadesDoEmpreendimentoClienteRequest`](#uauapimodelsatendimentoconsultarunidadesdoempreendimentoclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/GerarAtendimentoPorChatOnlineCliente`

**Gerar o atendimento para um cliente do atendimento online do cliente.**

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
Esquema: [`UAUApi.Models.Atendimento.GerarAtendimentoPorChatOnlineClienteRequest`](#uauapimodelsatendimentogeraratendimentoporchatonlineclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.Prospects.ImportacaoProspect.RetornoLote`](#globaltecuaucompprospectsimportacaoprospectretornolote) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/GerarPendencia`

**Criar uma pendência do UAU com as informações informada**

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
Esquema: [`UAUApi.Models.Atendimento.GerarPendenciaRequest`](#uauapimodelsatendimentogerarpendenciarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar a ação. Verifique os parâmetros da requisição/acesso à internet. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar a ação. Entre em contato com o administrador do sistema | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/GravarAtendimento`

**Gravar atendimento no Uau.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Atendimento/GravarAtendimento
3. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite Gravar o Atendimento.
1. Deve montar uma estrutura com as informações do Atendimento verificando os parâmetros obrigatórios.
2. Será apenas registrado Atendimentos com o status [0 - Em Aberto].
3. Caso não seja informado: usrrespon_atd, numccm_atd e usrcad_atd, será obrigatório ter configurado o serviço atendimento uauweb no CRM. CRM - Utilitários - Configurações de serviço
4. Para informar a unidade do atendimento é obrigatório informar a empresa, obra e produto. Caso não informe a empresa, vamos desconsiderar essa informação e gravar o atendimento.

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/configuracao-de-atendimento-do-uau-web/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Atendimento.GravarAtendimentoRequest`](#uauapimodelsatendimentogravaratendimentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Atendimento/VincularArquivoAoAtendimento`

**Vincular arquivo ao atendimento.**

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
Esquema: [`UAUApi.Models.Atendimento.VincularArquivoAoAtendimentoRequest`](#uauapimodelsatendimentovinculararquivoaoatendimentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Anexo vinculado com sucesso! |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Atendimento.VincularArquivoAoAtendimentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `arquivo` | string (byte) |  | Arquivo em bytes |
| `nome_arquivo` | string |  |  |
| `num_atendimento` | integer (int32) |  | Número do atendimento |
| `usuario` | string |  | Usuário (UAU) que vai anexar o arquivo. |

### UAUApi.Models.Atendimento.GravarAtendimentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `atendimento` | [`UAUApi.Models.Atendimento.Atendimento`](#uauapimodelsatendimentoatendimento) |  |  |

### UAUApi.Models.Atendimento.Atendimento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codcateg_atd` | string | ✓ | Código da Categoria do Atendimento. |
| `descr_atd` | string | ✓ | Descrição do Atendimento. |
| `usrrespon_atd` | string |  | Usúario responsável pelo Atendimento. |
| `usrcad_atd` | string |  | Usuário que cadastrou o atendimento. |
| `numccm_atd` | integer (int32) |  | Número do canal de comunicação utilizado. |
| `codpes_atd` | integer (int32) | ✓ | Código da pessoa que foi atendida/vai ser atendida pelo workflow. |
| `retoraten_atd` | integer (int32) | ✓ | Identifica se deve ou não gerar um passo no workflow referente ao retorno ao cliente. 0 - Não 1 - Sim. |
| `empresa_atd` | integer (int32) |  | Código da empresa |
| `obra_atd` | string |  | Código da obra (Empreendimento) |
| `produnid_atd` | integer (int32) |  | Número do produto. |
| `numper_atd` | integer (int32) |  | Número da personalização |
| `datacad_atd` | string (date-time) | ✓ | Data de cadastro. |
| `reincidente_atd` | boolean |  | Reincidência de  Atendimento. |
| `vlrmaoobra_atd` | number (double) |  | Valor da mão de obra do Atendimento. |
| `tipo_atd` | integer (int32) |  | Tipo de  Atendimento. 0 - Solicitação 1 - Informação 2 - Reclamação 3 - Elogio 4 - Sugestão |

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |

### UAUApi.Models.Atendimento.GerarPendenciaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuariouau_destino` | string | ✓ |  |
| `data_prevista` | string (date-time) |  |  |
| `data_aviso` | string (date-time) |  |  |
| `hora_aviso` | string (date-time) |  |  |
| `mensagem` | string |  |  |
| `geraremail_interno` | boolean |  |  |
| `gerar_email_externo` | boolean |  |  |
| `gerar_aviso` | boolean |  |  |
| `categoria` | string |  |  |

### Globaltec.UAU.Comp.Prospects.ImportacaoProspect.RetornoLote

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `_Sucesso` | boolean |  |  |
| `_ListaErros` | array de string |  |  |

### UAUApi.Models.Atendimento.GerarAtendimentoPorChatOnlineClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dados_atendimento` | [`UAUApi.Models.Atendimento.DadosAtendimentoChat`](#uauapimodelsatendimentodadosatendimentochat) |  | Objeto com os dados. |

### UAUApi.Models.Atendimento.DadosAtendimentoChat

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string |  |  |
| `NomeCliente` | string |  |  |
| `CodCategoria` | string |  |  |
| `DescAtendimento` | string |  |  |
| `DescChat` | string |  |  |
| `UsrAtendente` | string |  |  |
| `CanalComunicacao` | string |  |  |
| `Email` | string |  |  |
| `CodAtd` | string |  |  |

### UAUApi.Models.Atendimento.ConsultarUnidadesDoEmpreendimentoClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `obra` | string |  |  |
| `empresa` | integer (int32) |  |  |
| `cod_pessoa` | integer (int32) |  |  |

### UAUApi.Models.Atendimento.ConsultarPendenciasPorNumeroVinculoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_vinculo` | integer (int32) |  | Número do vinculo do atendimento. |

### UAUApi.Models.Atendimento.ConsultarPendenciaObservacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_pendencia` | integer (int32) |  | Número da pendência. |
| `dataquando_lancou` | string (date-time) |  | Data do lançamento. |
| `usuario_resolve` | string |  | Usuário definido para resolução. |

### UAUApi.Models.Atendimento.Pendencia

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `quemr_pen` | string |  |  |
| `qdol_pen` | string (date-time) |  |  |
| `num_pen` | integer (int32) |  |  |
| `desc_pen` | string |  |  |
| `queml_pen` | string |  |  |
| `qdor_pen` | string (date-time) |  |  |
| `dtprev_pen` | string (date-time) |  |  |
| `status_pen` | integer (int32) |  |  |
| `comemail_pen` | integer (int32) |  |  |
| `numdoc_pen` | string |  |  |
| `empresa_pen` | integer (int32) |  |  |
| `dtaviso_pen` | string (date-time) |  |  |
| `hraviso_pen` | string (date-time) |  |  |
| `codcateg_pen` | string |  |  |
| `obs_pen` | string |  |  |
| `dataativacao_pen` | string (date-time) |  |  |
| `numvtwf_pen` | integer (int32) |  |  |
| `numpasso_pen` | integer (int32) |  |  |
| `numresp_pen` | integer (int32) |  |  |
| `tiporesp_pen` | integer (int32) |  |  |

### UAUApi.Models.Atendimento.ConsultarPendenciaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero` | integer (int32) |  |  |
| `data_lancamento` | string (date-time) |  |  |
| `responsavel_resolucao` | string |  |  |

### UAUApi.Models.Atendimento.ConsultarNumeroWorkFlowVinculadoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numerovinculo_workflow` | integer (int32) |  | Número do vínculo do workflow. |
| `empresa` | integer (int32) |  | Código da empresa. |
| `obra` | string |  | Código da obra. |

### UAUApi.Models.Atendimento.ConsultarNumeroVinculoCategoriaDeComentarioComWorkFlowRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_categoria` | string |  | Código da categoria. |

### UAUApi.Models.Atendimento.ConsultarEmpreendimentosClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_pessoa` | integer (int32) |  | Código da pessoa do cliente |

### UAUApi.Models.Atendimento.ConsultarDataPrevistaDeTerminoAtendimentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numerovinculo_workflow` | integer (int32) |  | Número do vínculo do workflow. |
| `numero_workflow` | integer (int32) |  | número do workflow. |

### Globaltec.UAU.Repositorio.ConfigAtendimentoUAUWEBInfo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Num_CfgAtdWeb` | integer (int32) |  |  |
| `AtInat_CfgAtdWeb` | integer (int32) |  |  |
| `UsrResp_CfgAtdWeb` | string |  |  |
| `NumCanalComunicacao_CfgAtdWeb` | integer (int32) |  |  |
| `PermiteAcompanhamento_CfgAtdWeb` | boolean |  |  |
| `RetorAten_CfgAtdWeb` | boolean |  |  |
| `VisualizaAtendCategUauWeb_CfgAtdWeb` | boolean |  |  |

### UAUApi.Models.Atendimento.ConsultarCategoriaAtendimentoWebRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipo_atend` | string |  |  |

### UAUApi.Models.Atendimento.ConsultarAtendimentoPorPessoaComentarioRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_pessoa` | integer (int32) |  | código da pessoa |
| `lista_categoria` | array de string |  | código de comentário |
| `periodo_incio` | string (date-time) |  | Período que incia a consulta da data de cadastro |
| `periodo_fim` | string (date-time) |  | Período que finaliza a consulta da data de cadastro |

### UAUApi.Models.Atendimento.ConsultarAtendimentoPorPessoaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_pessoa` | integer (int32) |  |  |

### UAUApi.Models.Atendimento.ConsultarAtendimentoPorCategoriasUauWebRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_pessoa` | integer (int32) |  | Codigo da pessoa |

### UAUApi.Models.Atendimento.ConsultarAtendimentoDetalhadoPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_atendimento` | integer (int32) |  | Código do atendimento a ser consultado. |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Atendimento.ConsultarAtendimentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_atendimento` | integer (int32) |  | Código do atendimento a ser consultado. |
