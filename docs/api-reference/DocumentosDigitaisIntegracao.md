# DocumentosDigitaisIntegracao

## POST `/api/v{version}/DocumentosDigitais/ConsultaDocumentosDigitaisAtivos`

**Rota de consulta de documentos digitais ativos e configurados no sistema**

Definição Técnica: <br />
Rota de consulta de documentos digitais ativos e configurados no sistema. <br />
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario 
Retorno do metodo é o codigo e nome dos sistemas configurados para assinatura digital

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | As informações para o envio de documentos estão inválidas. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/DocumentosDigitais/ConsultarAssinaturasEnviadas`

**Essa rota faz consulta a assinatura envidas da Docusign atraves do numero de identificação do envelope**

Definição Técnica: <br />
Rota de consulta de assinaturas enviadas da Docusign atraves do numero de identificação do envelope <br />
Passos:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
Parametros:
- Codigo identificador do envelope

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.DocumentosDigitais.NumeroEnvelopeRequest`](#uauapimodelsdocumentosdigitaisnumeroenveloperequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | As informações para o envio de documentos estão inválidas. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/DocumentosDigitais/ConsultarDocumentosEnviados`

**Essa rota faz consulta ao documentos enviados da Docusign atraves do numero de identificação do envelope**

Definição Técnica:<br />
Rota de consulta de documentos enviados da Docusign atraves do numero de identificação do envelope

1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
Parametros:
- Codigo identificador do envelope

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.DocumentosDigitais.NumeroEnvelopeRequest`](#uauapimodelsdocumentosdigitaisnumeroenveloperequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | As informações para o envio de documentos estão inválidas. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/DocumentosDigitais/ConsultarEnvelopeDocumentosCodigoExterno`

**Esta rota faz consulta de envelopes da Docusign apenas pelo codigo externo (o código externo é o código identificador do envelope na Docusign)**

Definição Técnica: <br />
Rota de consulta de envelopes da Docusign apenas pelo codigo externo do evelope. <br />
O código externo é o código identificador do envelope na Docusign <br />
Passos: 
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
Parametros:
- Codigo externo do envelope

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.DocumentosDigitais.CodigoExternoEnvelopeRequest`](#uauapimodelsdocumentosdigitaiscodigoexternoenveloperequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de string |
| 400 | As informações para o envio de documentos estão inválidas. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/DocumentosDigitais/EnviarEnvelopeDeDocumento`

**Esta rota faz o envio de documentos digitais para assinatira digital**

Definição Técnica:<br />
 Rota de envio de documentos digitais para assinatura atraves dos sistemas configurados. <br />
 Sendo possivel utilizar Docusign ou Clicksign <br />
 Passos: 
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 Parametros:
 1. ListaDePessoas
-  Nome_enva =&gt;  Nome da pessoa
-  Ordem_enva =&gt; Ordem de assinatura (Apenas para Docusign)
-  Email_enva =&gt; Email da pessoa 
 2. ListaDeDocumentos
-  DocumentoBase64_envd =&gt; Documento em base64
-  Nome_envd =&gt; nome do documento 
-  Ordem_envd =&gt; ordem de envio do documento (Apenas para Docusign)
-  Extensao_envd =&gt; Extensão do arquivo em formato: \*.extensao exemplo: *.pdf
 3. Mensagem (Apenas para ClickSign)
 4. CodigoDoSistema =&gt; Codigo do Sistema Utilizado <br />
 Obs. Consulta utilizando a rota de ConsultaDocumentosDigitaisAtivos

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.DocumentosDigitais.EnviarDocumentosDigitaisRequest`](#uauapimodelsdocumentosdigitaisenviardocumentosdigitaisrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | As informações para o envio de documentos estão inválidas. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.DocumentosDigitais.EnviarDocumentosDigitaisRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ListaDePessoas` | array de [`UAUApi.Models.DocumentosDigitais.PessoasEvelopeRequest`](#uauapimodelsdocumentosdigitaispessoaseveloperequest) | ✓ |  |
| `ListaDeDocumentos` | array de [`UAUApi.Models.DocumentosDigitais.DocumentoEnvelopeRequest`](#uauapimodelsdocumentosdigitaisdocumentoenveloperequest) | ✓ |  |
| `Mensagem` | string |  |  |
| `CodigoDoSistema` | integer (int32) | ✓ |  |

### UAUApi.Models.DocumentosDigitais.DocumentoEnvelopeRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `DocumentoBase64_envd` | string |  | Lista De Documentos em base64 |
| `Extensao_envd` | string |  | Extensao do arquivo em formato "*.enxtensao" exemplo: *.pdf |
| `Nome_envd` | string |  | Nome do arquivo |
| `Ordem_envd` | integer (int32) |  | Ordem de Envio de Documentos |

### UAUApi.Models.DocumentosDigitais.PessoasEvelopeRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Email_enva` | string |  | Email da Pessoa |
| `Nome_enva` | string |  | Nome da pessoa |
| `Ordem_enva` | integer (int32) |  | Ordem de assinatura |

### UAUApi.Models.DocumentosDigitais.CodigoExternoEnvelopeRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `EnvelopeId` | string |  | Codigo externo do envelope |

### UAUApi.Models.DocumentosDigitais.NumeroEnvelopeRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroDoEnvelope` | integer (int32) |  | Numero identificador do envelope |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |
