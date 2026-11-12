# Planejamento

## POST `/api/Planejamento/ObterAcessoUsuarioNaObra`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `login` | query | string | ✓ |  |
| `empresa` | query | string | ✓ |  |
| `obra` | query | string | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |

---

## POST `/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamento`

**Aprovar a solicitação de aprovação de planejamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Exemplo do json de request:

    {
        "NumSolicitacao" 622,
        "Usuario": "root",
        "Departamento": "FIN",
        "Cargo": "10"
    }

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Planejamento.AprovarSolicitacaoPlanejamentoRequest`](#uauapimodelsplanejamentoaprovarsolicitacaoplanejamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Aprovar solicitação de planejamento | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoEmLote`

**Aprovar várias solicitações de aprovação de planejamento em uma única requisição.**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 3. Exemplo do json de request:
 
     {
         "NumSolicitacoes" [
             625, 626
         ],
         "Usuario": "root",
         "Departamento": "FIN",
         "Cargo": "10"
}

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Planejamento.AprovarSolicitacaoPlanejamentoEmLoteRequest`](#uauapimodelsplanejamentoaprovarsolicitacaoplanejamentoemloterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Aprovar solicitação de planejamento | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoInsumosEmLote`

**Aprovar a solicitação de aprovação de planejamento de insumos em lotes de solicitações. Passando como parâmetro o número dos itens das solicitações.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Exemplo do json de request:

   {
        "IdsItensSolicitacao" [
            1615, 1616, 1617            
        ],
        "Usuario": "root",
        "Departamento": "FIN",
        "Cargo": "10"
   }

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Planejamento.AprovarSolicitacaoPlanejamentoInsumosEmLoteRequest`](#uauapimodelsplanejamentoaprovarsolicitacaoplanejamentoinsumosemloterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Aprovar solicitação de planejamento de insumos em lote. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AprovarSolicitacaoPlanejamentoServicosEmLote`

**Aprovar a solicitação de aprovação de planejamento de serviços em lotes de solicitações.**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 3. Exemplo do json de request:
 
    {
        "NumSolicitacao": 630,
        "ChavesServico": [
            {
	            "empresa": 1,
	            "obra": "00000",
	            "produto": 7,
	            "contrato": 1,
	            "item": "01.01.01.02",
	            "servico": "020201P",
	            "data": "01/09/2005"
            },
            {
	            "empresa": 1,
	            "obra": "00000",
	            "produto": 7,
	            "contrato": 1,
	            "item": "01.01.01.03",
	            "servico": "030109P",
	            "data": "01/09/2005"
            }
        ],
        "Usuario": "root",
        "Departamento": "FIN",
        "Cargo": "10"
    }

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Planejamento.SolicitacaoPlanejamentoServico`](#uauapimodelsplanejamentosolicitacaoplanejamentoservico)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Aprovar solicitação de planejamento de serviços em lote. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AtualizarEstruturaPlanejamento`

**Atualizar estrutura no planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.AtualizarEstruturaPlanejamento`](#uauapimodelsplanejamentoatualizarestruturaplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Atualizar estrutura do planejamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AtualizarInsumosPlanejamento`

**Alterar valores**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Necessário permissão de alteração no programa OBPLNOBR

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Planejamento.AtualizarInsumosPlanejamentoRequest`](#uauapimodelsplanejamentoatualizarinsumosplanejamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Insumos do planejamento | array de [`UAUApi.Models.Planejamento.PlanejamentoIntegracao.SaldoSIPlanejada`](#uauapimodelsplanejamentoplanejamentointegracaosaldosiplanejada) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AtualizarItemPlanejamento`

**Atualizar item do planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.AtualizarItemPlanejamento`](#uauapimodelsplanejamentoatualizaritemplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Atualizar item do planejamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AtualizarServicoPlanejamento`

**Atualizar serviço do planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.AtualizarServicoPlanejamento`](#uauapimodelsplanejamentoatualizarservicoplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Atualizar serviço do planejamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AtualizarServicoPlanejamentoIntegrado`

**Atualizar serviço do planejamento integrado.**

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
Esquema: [`UAUApi.Models.Planejamento.AtualizarServicoPlanejamentoIntegrado`](#uauapimodelsplanejamentoatualizarservicoplanejamentointegrado)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Atualizar serviço do planejamento integrado. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/AtualizarServicoPlanejamentoMes`

**Atualizar serviço do planejamento de acordo com o mês.**

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
Esquema: [`UAUApi.Models.Planejamento.AtualizarServicoPlanejamentoMes`](#uauapimodelsplanejamentoatualizarservicoplanejamentomes)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Atualizar serviço do planejamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarAprovacaoPlPendentePorUsuario`

**Realiza consulta das aprovações pendentes para o usuário.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarAprovacaoPlPendentePorUsuarioRequest`](#uauapimodelsplanejamentoconsultaraprovacaoplpendenteporusuariorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Aprovação planejamento | array de [`UAUApi.Models.Planejamento.SolicitacaoAprovacaoPlanejamento`](#uauapimodelsplanejamentosolicitacaoaprovacaoplanejamento) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarDesembolsoPlanejamento`

**Consultar desembolso (Projetado, A pagar e Pago) por obra e período.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. O mês inicial e final deverão ser informados no formato MM/YYYY. Exemplo: 01/2019, 12/2019.

Definição de Negócio:
Status:
1. Projetado: Considera a data de pagamento (DtaRef) para realizar o cálculo dos valores.
2. A pagar: Considera a data de prorrogação da parcela (DtaRef) para realizar o cálculo dos valores.
3. Pago: Considera a data de pagamento da parcela (DtaRef) para realizar o cálculo dos valores.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Planejamento.ConsultarDesembolsoPlanejamento`](#uauapimodelsplanejamentoconsultardesembolsoplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.PlanejamentoRetorno`](#uauapimodelsplanejamentoretorno) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarEstruturaPlanejamento`

**Consultar estrutura do planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarEstruturaPlanejamento`](#uauapimodelsplanejamentoconsultarestruturaplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar estrutura do planejamento. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarItemPlanejamento`

**Consultar item do planejamento de acordo com a chave do planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarItemPlanejamento`](#uauapimodelsplanejamentoconsultaritemplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar item do planejamento. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarQuantidadeAprovacaoPlPendentePorUsuario`

**Realiza a busca da quantidade de solicitação pendente para o usuário.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarAprovacaoPlPendentePorUsuarioRequest`](#uauapimodelsplanejamentoconsultaraprovacaoplpendenteporusuariorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Aprovação planejamento | integer (int32) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarSaldoSIPlanejada`

**Realiza consulta de valores aprovados e saldos das SIs do planejamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Necessário permissão de consulta no programa OBPLNOBR

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Planejamento.ConsultarSaldoSIPlanejadaRequest`](#uauapimodelsplanejamentoconsultarsaldosiplanejadarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Insumos do planejamento | array de [`UAUApi.Models.Planejamento.PlanejamentoIntegracao.SaldoSIPlanejada`](#uauapimodelsplanejamentoplanejamentointegracaosaldosiplanejada) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarServicoPlanejadoDesintegrado`

**Consultar serviço planejado desintegrado.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarServicoPlanejadoDesintegrado`](#uauapimodelsplanejamentoconsultarservicoplanejadodesintegrado)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Serviço planejado desintegrado. | array de [`UAUApi.Models.Planejamento.ServicoPlanejamento`](#uauapimodelsplanejamentoservicoplanejamento) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarServicoPlanejamento`

**Consultar serviços do planejamento de acordo com a chave do planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarServicoPlanejamento`](#uauapimodelsplanejamentoconsultarservicoplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar serviço do planejamento. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarServicoPlanejamentoIntegrado`

**Consultar serviço do planejamento integrado.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarServicoPlanejamentoIntegrado`](#uauapimodelsplanejamentoconsultarservicoplanejamentointegrado)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar serviço do planejamento integrado. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarServicoPlanejamentoMes`

**Consultar serviço do planejamento de acordo com o mês.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarServicoPlanejamentoMes`](#uauapimodelsplanejamentoconsultarservicoplanejamentomes)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar serviço do planejamento. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarServicoPlanejamentoPorObra`

**Consultar serviço do planejamento por obra.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarServicoPlanejamentoPorObra`](#uauapimodelsplanejamentoconsultarservicoplanejamentoporobra)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Atualizar item do planejamento. | array de [`UAUApi.Models.Planejamento.ServicoPlanejamento`](#uauapimodelsplanejamentoservicoplanejamento) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarSolicitacaoInsumoPL`

**Consultar as solicitações de alteração de insumos do planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarSolicitacaoPLRequest`](#uauapimodelsplanejamentoconsultarsolicitacaoplrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de solicitação de aprovação de insumos do planejamento | array de [`UAUApi.Models.Planejamento.InsumoSolicitadoAprovacaoPlanejamento`](#uauapimodelsplanejamentoinsumosolicitadoaprovacaoplanejamento) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ConsultarSolicitacaoServicoPL`

**Consultar as solicitações de alteração de serviço do planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.ConsultarSolicitacaoPLRequest`](#uauapimodelsplanejamentoconsultarsolicitacaoplrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Itens de solicitação de aprovação de serviços do planejamento | array de [`UAUApi.Models.Planejamento.ServicoSolicitadoAprovacaoPlanejamento`](#uauapimodelsplanejamentoservicosolicitadoaprovacaoplanejamento) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/ExportarPlanejamentoProduto`

**Exportar planejamento de um produto**

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
Esquema: [`UAUApi.Models.Planejamento.ExportarPlanejamentoProduto`](#uauapimodelsplanejamentoexportarplanejamentoproduto)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Exportar itens de um planejamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/InserirEstruturaPlanejamento`

**Inserir estrutura no planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.InserirEstruturaPlanejamento`](#uauapimodelsplanejamentoinserirestruturaplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir estrutura no planejamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/InserirServicoPlanejamento`

**Inserir serviços no planejamento.**

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
Esquema: [`UAUApi.Models.Planejamento.InserirServicoPlanejamento`](#uauapimodelsplanejamentoinserirservicoplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir serviços no planejamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/InserirServicoPlanejamentoIntegrado`

**Inserir serviços no planejamento integrado.**

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
Esquema: [`UAUApi.Models.Planejamento.InserirServicoPlanejamentoIntegrado`](#uauapimodelsplanejamentoinserirservicoplanejamentointegrado)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir serviços no planejamento integrado. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/InserirServicoPlanejamentoMes`

**Inserir serviço do planejamento de acordo com o mês.**

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
Esquema: [`UAUApi.Models.Planejamento.AtualizarServicoPlanejamentoMes`](#uauapimodelsplanejamentoatualizarservicoplanejamentomes)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir serviço do planejamento. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/RecusarSolicitacaoPlanejamentoGeral`

**Recusar a solicitação de planejamento, como também os itens da solicitação.**

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
Esquema: [`UAUApi.Models.Planejamento.SolicitacaoPlanejamento`](#uauapimodelsplanejamentosolicitacaoplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Recusa da solicitação de planejamento | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Planejamento/RecusarSolicitacaoPlanejamentoGeralEmLote`

**Recusar a solicitação de planejamento em lote, como também os itens da solicitação.**

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
Esquema: [`UAUApi.Models.Planejamento.SolicitacaoPlanejamento`](#uauapimodelsplanejamentosolicitacaoplanejamento)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Recusa da solicitação de planejamento | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Planejamento.SolicitacaoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumSolicitacao` | integer (int32) |  | Código da solicitação de planejamento. |
| `NumSolicitacoes` | array de integer (int32) |  | Número de solicitação de planejamento. |
| `IdsItensSolicitacao` | array de integer (int32) |  | Armazena os ID's dos itens de solicitação de aprovação de planejamento. |
| `Usuario` | string |  | Código do usuário |
| `Departamento` | string |  | - Departamento do usuário, informado para a aprovação. |
| `Cargo` | string |  | - Cargo do usuário, informado para a aprovação. |

### UAUApi.Models.Planejamento.InserirServicoPlanejamentoIntegrado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | string |  |  |
| `Contrato` | string |  |  |
| `Item` | string |  |  |
| `Servico` | string |  |  |
| `TipoDeCusto` | string |  |  |
| `CodigoExterno` | string |  |  |
| `Usuario` | string |  |  |

### UAUApi.Models.Planejamento.InserirServicoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | string |  |  |
| `Contrato` | string |  |  |
| `Item` | string |  |  |
| `Servico` | string |  |  |
| `TipoDeCusto` | string |  |  |
| `Usuario` | string |  |  |

### UAUApi.Models.Planejamento.InserirEstruturaPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | string |  |  |
| `Contrato` | string |  |  |
| `Item` | string |  |  |
| `Servico` | string |  |  |
| `Sequencia` | string |  |  |
| `CodigoItem` | string |  |  |
| `Tipo` | integer (int32) |  |  |
| `Qtde` | number (double) |  |  |
| `Usuario` | string |  |  |

### UAUApi.Models.Planejamento.ExportarPlanejamentoProduto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa. |
| `Obra` | string |  | Código da obra. |
| `Contrato` | integer (int32) |  | Código do contrato. |
| `Produto` | integer (int32) |  | Código do produto |

### UAUApi.Models.Planejamento.ServicoSolicitadoAprovacaoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `EmpObra` | string |  | Código da empresa e código da obra do serviço solicitado do planejamento. Formato: Emp|Obra. |
| `Produto` | string |  | Código do produto do serviço solicitado do planejamento. Formato: 'Cód - Descrição' |
| `Contrato` | string |  | Código do contrato do serviço solicitado do planejamento. Formato: 'Cód - Descrição' |
| `ItemPl` | string |  | Item PL do serviço solicitado do planejamento |
| `Composicao` | string |  | Código do serviço solicitado do planejamento. |
| `DescComposicao` | string |  | Descricao do serviço solicitado do planejamento |
| `MesPL` | string (date-time) |  | Mês PL do item do serviço solicitado do planejamento |
| `TotalPlanejadoMes` | number (double) |  | Total PLANEJADO do serviço solicitado no MÊS |
| `TotalPlanejadoObra` | number (double) |  | Total PLANEJADO do serviço solicitado na OBRA |
| `TotalSolicitado` | number (double) |  | Total solicitado do serviço do planejamento |
| `Num_sap` | integer (int32) |  | Número da solicitação do planejamento |
| `Num_isap` | integer (int32) |  | ID do item da solicitação de planejamento. |

### UAUApi.Models.Planejamento.InsumoSolicitadoAprovacaoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `EmpObra` | string |  | Código da empresa e código da obra do insumo solicitado do planejamento. Formato: Emp|Obra. |
| `Produto` | string |  | Código do produto do insumo solicitado do planejamento. Formato: 'Cód - Descrição' |
| `Contrato` | string |  | Código do contrato do insumo solicitado do planejamento. Formato: 'Cód - Descrição' |
| `ItemPl` | string |  | Item PL do insumo solicitado do planejamento |
| `Composicao` | string |  | Código do seriço do insumo solicitado do planejamento. |
| `DescComposicao` | string |  | Descricao do serviço do insumo solicitado do planejamento |
| `Insumo` | string |  | Código do insumo solicitado do planejamento. |
| `DescInsumo` | string |  | Descricao do insumo solicitado do planejamento |
| `MesPL` | string (date-time) |  | Mês PL do item do insumo solicitado do planejamento |
| `TotalPlanejadoMes` | number (double) |  | Total PLANEJADO do insumo solicitado no MÊS |
| `TotalPlanejadoObra` | number (double) |  | Total PLANEJADO do insumo solicitado na OBRA |
| `TotalSolicitado` | number (double) |  | Total solicitado do insumo do planejamento |
| `Num_sap` | integer (int32) |  | Número da solicitação do planejamento |
| `Num_isap` | integer (int32) |  | ID do item da solicitação de planejamento. |

### UAUApi.Models.Planejamento.ConsultarSolicitacaoPLRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numSolicitacao` | integer (int32) |  | Código da solicitação de planejamento. |

### UAUApi.Models.Planejamento.ConsultarServicoPlanejamentoPorObra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa. |
| `Obra` | string |  | Código da obra. |

### UAUApi.Models.Planejamento.ConsultarServicoPlanejamentoMes

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | string |  |  |
| `Contrato` | string |  |  |
| `Item` | string |  |  |
| `Servico` | string |  |  |
| `Mes` | string |  |  |

### UAUApi.Models.Planejamento.ConsultarServicoPlanejamentoIntegrado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoExterno` | string |  |  |

### UAUApi.Models.Planejamento.ConsultarServicoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa do planejamento |
| `Obra` | string |  | Código da obra do planejamento |
| `Produto` | string |  | Código do produto vinculado ao planejamento |
| `Contrato` | string |  | Código do contrato vinculado ao planejamento |
| `Item` | string |  | Código do item do planejamento (considerar o código referente ao ITEM e não o código do SERVIÇO) |
| `Servico` | string |  | Código do serviço do planejamento (considerar o código referente ao SERVIÇO e não o código do ITEM) |

### UAUApi.Models.Planejamento.ServicoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa_plt` | integer (int32) |  | Código da empresa. |
| `Obra_plt` | string |  | Código da obra. |
| `Item_plt` | string |  | Item do planejamento. |
| `Serv_plt` | string |  | Serviço do planejamento. |
| `Prod_plt` | integer (int32) |  | Código do produto do planejamento. |
| `Contrato_plt` | integer (int32) |  | Código do contrato do planejamento. |
| `Id_plt` | integer (int32) |  | Id de planTotal. |
| `Descr_plt` | string |  | Descrição do serviço. |
| `CodGrupo_plt` | string |  | Código do grupo de serviço. |
| `G1g2_plt` | integer (int32) |  | Tipo - Quantidade/Verba. |
| `DataIni_plt` | string (date-time) |  | Data início do serviço. |
| `DataFim_plt` | string (date-time) |  | Data fim do serviço. |
| `ProdEq_plt` | number (double) |  | Produção equipe. |
| `Custo_plt` | string |  | Custo serviço. |
| `Anexos_plt` | integer (int32) |  | Anexo. |
| `Qtde_plt` | number (double) |  | Quantidade do serviço. |
| `Unid_plt` | string |  | Unidade do serviço. |
| `RateioCRD_plt` | boolean |  | Rateio. |
| `ValidarCusto_plt` | boolean |  | Validar custo. |
| `TipoControle_plt` | integer (int32) |  | Tipo controle de aprovação de solicitação de planejamento. |
| `Integrado_plt` | boolean |  | Tipo de integração do serviço. |
| `CodExternoInteg_plt` | string |  | Código de integração do serviço. |

### UAUApi.Models.Planejamento.ConsultarServicoPlanejadoDesintegrado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa. |
| `Obra` | string |  | Código da obra. |

### UAUApi.Models.Planejamento.ConsultarSaldoSIPlanejadaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa do planejamento |
| `Obra` | string | ✓ | Código da obra do planejamento |
| `Produto` | integer (int32) | ✓ | Código do produto do planejamento |
| `Contrato` | integer (int32) | ✓ | Código do contrato do planejamento |
| `Item` | string |  | Código do item do planejamento |
| `Servico` | string |  | Código do serviço do planejamento |
| `MesPl` | string |  | Mês do planejamento |
| `Insumo` | string |  | Insumo do planejamento |

### UAUApi.Models.Planejamento.ConsultarItemPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa do planejamento |
| `Obra` | string |  | Código da obra do planejamento |
| `Produto` | string |  | Código do produto vinculado ao planejamento |
| `Contrato` | string |  | Código do contrato vinculado ao planejamento |
| `Item` | string |  | Código do item do planejamento (considerar o código referente ao ITEM e não o código do SERVIÇO) |

### UAUApi.Models.Planejamento.ConsultarEstruturaPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | string |  |  |
| `Contrato` | string |  |  |
| `Item` | string |  |  |
| `Servico` | string |  |  |
| `Sequencia` | string |  |  |

### UAUApi.Models.PlanejamentoRetorno

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Status` | string |  | Status o planejamento: - Projetado - A pagar - Pago |
| `Empresa` | integer (int32) |  | Código da empresa. |
| `Obra` | string |  | Código da obra. |
| `Contrato` | integer (int32) |  | Código do contrato. |
| `Produto` | integer (int32) |  | Código do produto. |
| `Composicao` | string |  | Código do serviço. |
| `Item` | string |  | Código do item. |
| `Insumo` | string |  | Código do insumo. |
| `DtaRef` | string (date-time) |  | Data de projeção/prorrogação/pagamento |
| `DtaRefMes` | integer (int32) |  | Mês de projeção/prorrogação/pagamento |
| `DtaRefAno` | integer (int32) |  | Ano de projeção/prorrogação/pagamento |
| `Total` | number (double) |  | Preço do insumo. |
| `Acrescimo` | number (double) |  | Valor do acréscimo. |
| `Desconto` | number (double) |  | Valor do desconto. |
| `TotalLiq` | number (double) |  | Valor total líquido. |
| `TotalBruto` | number (double) |  | Valor total bruto. |

### UAUApi.Models.Planejamento.ConsultarDesembolsoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa. |
| `Obra` | string | ✓ | Código da obra. |
| `MesInicial` | string | ✓ | Mês PL inicial. |
| `MesFinal` | string | ✓ | Mês PL final. |

### UAUApi.Models.Planejamento.SolicitacaoAprovacaoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Num_Sap` | integer (int32) |  | Código da solicitação de aprovação de planejamento. |
| `Empresa_sap` | integer (int32) |  | Código da empresa da solicitação de aprovação de planejamento. |
| `Obra_sap` | string |  | Código da obra da solicitação de aprovação de planejamento. |
| `Desc_emp` | string |  | Descrição da empresa da solicitação de aprovação de planejamento. |
| `DescObra_sap` | string |  | Descrição da obra da solicitação de aprovação de planejamento. |
| `Origem_sap` | string |  | Descrição da Origem da solicitação de aprovação de planejamento. |
| `UsrCad_sap` | string |  | Código do usuário de cadastro da solicitação de aprovação de planejamento. |
| `DataCad_sap` | string |  | Data de cadastro da solicitação de aprovação de planejamento. |
| `ValorImpactoCustoObra_sap` | number (double) |  | Valor de impacto da solicitação de aprovação de planejamento. |
| `Descricao_sap` | string |  | Descrição da solicitação de aprovação de planejamento. |
| `StatusAprovacao_sap` | integer (int32) |  | Status da solicitação de aprovação de planejamento. |
| `Justificativa_sap` | string |  | Justificativa da solicitação de aprovação de planejamento. |

### UAUApi.Models.Planejamento.ConsultarAprovacaoPlPendentePorUsuarioRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  | Código do usuário. |
| `departamento` | string |  | Departamento do usuário. |
| `cargo` | string |  | Cargo do usuário. |
| `empresasObras` | string |  | Lista de empresas e obras |
| `tipoConsultaAprovacao` | string |  | Tipo da consulta da aprovacao |
| `numero_dias` | integer (int32) |  | Numero de dias |

### UAUApi.Models.Planejamento.AtualizarServicoPlanejamentoMes

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa do planejamento |
| `Obra` | string | ✓ | Código da obra do planejamento |
| `Produto` | string | ✓ | Código do produto vinculado ao planejamento |
| `Contrato` | string | ✓ | Código do contrato vinculado ao planejamento |
| `Item` | string | ✓ | Código do item do planejamento (considerar o código referente ao ITEM e não o código do SERVIÇO) |
| `Servico` | string | ✓ | Código do serviço do planejamento (considerar o código referente ao SERVIÇO e não o código do ITEM) |
| `Mes` | string | ✓ | Mês do planejamento |
| `Qtde` | number (double) | ✓ | Quantidade do serviço do planejamento. |
| `Usuario` | string | ✓ | Login usuário. |

### UAUApi.Models.Planejamento.AtualizarServicoPlanejamentoIntegrado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoExterno` | string |  |  |
| `Qtde` | number (double) |  |  |
| `DataInicio` | string |  |  |
| `DataTermino` | string |  |  |
| `Usuario` | string |  |  |

### UAUApi.Models.Planejamento.AtualizarServicoPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | string |  |  |
| `Contrato` | string |  |  |
| `Item` | string |  |  |
| `Servico` | string |  |  |
| `Qtde` | number (double) |  |  |
| `DataInicio` | string |  |  |
| `DataTermino` | string |  |  |
| `Usuario` | string |  |  |

### UAUApi.Models.Planejamento.AtualizarItemPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | string |  |  |
| `Contrato` | string |  |  |
| `Item` | string |  |  |
| `DescricaoItem` | string |  |  |
| `Usuario` | string |  |  |

### UAUApi.Models.Planejamento.PlanejamentoIntegracao.SaldoSIPlanejada

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Codigo da empresa do planejamento |
| `DescEmpresa` | string |  | Descrição da empresa do planejamento |
| `Obra` | string |  | Código da obra do planejamento |
| `DescObra` | string |  | Descrição da obra do planejamento |
| `Produto` | integer (int32) |  | Código do produto do planejamento |
| `DescProduto` | string |  | Descrição do produto do planejamento |
| `Contrato` | integer (int32) |  | Código do contrato do planejamento |
| `DescContrato` | string |  | Descrição do contrato do planejamento |
| `Item` | string |  | Código do item do planejamento |
| `Servico` | string |  | Código do serviço do planejamento |
| `DescServico` | string |  | Descrição do serviço do planejamento |
| `Insumo` | string |  | Código do insumo do planejamento |
| `DescInsumo` | string |  | Descrição do insumo do planejamento |
| `MesPl` | string |  | Mês de planejamento do insumo |
| `TipoControle` | string |  | Tipo de controle do insumo no planejamento    1 - Quantidade    2 - Verba |
| `ValorProjetado` | number (double) |  | Valor projetado do insumo no planejamento |
| `ValorAprovado` | number (double) |  | Valor aprovado do insumo no planejamento |
| `TotalDisponivelMes` | number (double) |  | Verba ou Quantidade disponível no mês |
| `SaldoObra` | number (double) |  | Saldo disponível na obra |

### UAUApi.Models.Planejamento.AtualizarInsumosPlanejamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Insumos` | array de [`UAUApi.Models.Planejamento.InsumoAlterarPlanejamento`](#uauapimodelsplanejamentoinsumoalterarplanejamento) | ✓ | Insumos para alteração de custo de planejamento |
| `justificativaAprovacaoPl` | string |  | Justificativa de solicitação de aprovação de planejamento |

### UAUApi.Models.Planejamento.InsumoAlterarPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa do planejamento |
| `Obra` | string | ✓ | Código da obra do planejamento |
| `Produto` | integer (int32) | ✓ | Código do produto do planejamento |
| `Contrato` | integer (int32) | ✓ | Código do contrato do planejamento |
| `Item` | string | ✓ | Código do item do planejamento |
| `Servico` | string | ✓ | Código do serviço do planejamento |
| `MesPl` | string | ✓ | Mês do planejamento |
| `Insumo` | string | ✓ | Insumo do planejamento |
| `quantidade` | number (double) |  | Quantidade do insumo do planejamento. Não informar o parâmetro caso queira atualizar somente o preço. |
| `preco` | number (double) |  | Preço do insumo do planejamento. Não informar o parâmetro caso queira atualizar somente a quantidade. |

### UAUApi.Models.Planejamento.AtualizarEstruturaPlanejamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | string |  |  |
| `Contrato` | string |  |  |
| `Item` | string |  |  |
| `Servico` | string |  |  |
| `Sequencia` | string |  |  |
| `Qtde` | number (double) |  |  |
| `Usuario` | string |  |  |

### UAUApi.Models.Planejamento.SolicitacaoPlanejamentoServico

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumSolicitacao` | integer (int32) |  | Código da solicitação de aprovação de planejamento. |
| `ChavesServico` | array de [`UAUApi.Models.Planejamento.ChaveServicoPlRequest`](#uauapimodelsplanejamentochaveservicoplrequest) |  | Armazena uma cadeia de chaves de serviço PL. (Sequência: Empresa, Obra, Produto, Contrato, Item, Servico, Mes do planejamento (MesPL) no formato (dd/mm/yyyy)) |
| `Usuario` | string |  | Login do usuário logado |
| `Departamento` | string |  | Código do departamento que o usuário está alocado |
| `Cargo` | string |  | Código do cargo que o usuário está alocado |

### UAUApi.Models.Planejamento.ChaveServicoPlRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa. |
| `obra` | string |  | Código da obra. |
| `produto` | integer (int32) |  | Código do produto Pl. |
| `contrato` | integer (int32) |  | Código do contrato Pl. |
| `item` | string |  | Código do item Pl. |
| `servico` | string |  | Código do servico ou composicao Pl. |
| `data` | string |  | Data no formato (dd/mm/yyyy)) |

### UAUApi.Models.Planejamento.AprovarSolicitacaoPlanejamentoInsumosEmLoteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `IdsItensSolicitacao` | array de integer (int32) |  | Número dos ITENS de solicitação de planejamento que deseja aprovar. No formato "IdsItensSolicitacao": [0001, 0002, 0003]. Não confunda com o Número da solicitação. |
| `Usuario` | string |  | Login do usuário logado |
| `Departamento` | string |  | Código do departamento do usuário |
| `Cargo` | string |  | Código do cargo do usuário |

### UAUApi.Models.Planejamento.AprovarSolicitacaoPlanejamentoEmLoteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumSolicitacoes` | array de integer (int32) |  | Número das solicitação de planejamento que deseja aprovar. No formato "NumSolicitacoes": [0001, 0002, 0003] |
| `Usuario` | string |  | Login do usuário logado |
| `Departamento` | string |  | Código do departamento do usuário |
| `Cargo` | string |  | Código do cargo do usuário |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Planejamento.AprovarSolicitacaoPlanejamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumSolicitacao` | integer (int32) |  | Código da solicitação de planejamento. |
| `Usuario` | string |  | Login do usuário logado |
| `Departamento` | string |  | Código do departamento do usuário |
| `Cargo` | string |  | Código do cargo do usuário |

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |
