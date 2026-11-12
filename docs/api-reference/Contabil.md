# Contabil

## POST `/api/v{version}/Contabil/ConsultarContasContabeis`

**Consulta os dados de contas contábeis do UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar os dados das contas contábeis com a URI + /api/v{version}/Contabil/ConsultarContasContabeis
3. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Consulta os dados de contas contábeis do UAU, podendo fazer filtros pela empresa,
ano, conta ou descrição da conta, com o intuito de buscar informações de uma conta contábil.
1. Deve informar obrigatoriamente o código da empresa, ano da máscara de plano de contas e o a propriedade limitarRetornoEm.
2. Pode informar opcionalmente o código da conta ou a descrição da conta.
3. Os parâmetros (DescricaoConta, Conta) podem conter o sinal de porcentagem (%), 
caso necessite fazer a consulta a partir de um caractere curinga. Exemplos: %UAU, %UAU%, UAU%.

VirtUau:
- http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Contabil/Contabil_ConsultarContasContabeis

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/777058/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Contabil.ConsultarContasContabeisRequest`](#uauapimodelscontabilconsultarcontascontabeisrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Contabil.ContasContabeis`](#uauapimodelscontabilcontascontabeis) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Contabil/ConsultarSaldoDeContas`

**Consulta o saldo de contas contábeis do UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar os saldo das contas conbaeis com a URI + /api/v{version}/Contabil/SaldoDeContas
3. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Pode-se consultar o saldo das contas contábeis do UAU, podendo fazer filtros pela empresa, 
tipo, ano e mês, com isso é possível fazer a integração da parte de saldos contábeis com o UAU
1. Deve informar obrigatoriamente todos os parâmetros da request.

VirtUau:
- http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Contabil/Contabil_ConsultarSaldoDeContas

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/777058/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Contabil.ConsultarSaldoDeContasRequest`](#uauapimodelscontabilconsultarsaldodecontasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Contabil.SaldoDeContas`](#uauapimodelscontabilsaldodecontas) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Contabil.SaldoDeContas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa |
| `Conta` | string |  | Código da conta |
| `CreditoDebito` | string |  | Tipo de Saldo de Conta (Débito ou Crédito) |
| `Valor` | number (double) |  | Valor referente ao saldo da conta |
| `Mes` | string (date-time) |  | Mês Lançamento fiscal |

### UAUApi.Models.Contabil.ConsultarSaldoDeContasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `MesAno` | string (date-time) | ✓ | Ano do Lançamento Societário e mês do Lançamento Fiscal O Mês do lançamento fiscal irá retornar somente lançamentos com mês igual ou inferior ao passado. |
| `Tipo` | string | ✓ | Tipo do Lançamento Fiscal e Societário, os valores passados serão desconsiderados na requisição.  Se For passado mais de um valor os mesmos devem ser separados por virgula. 0 - Manual 1 - Automático 2 - Inicialização de Saldo 3 - Apuração Trimestral 4 - Equivalência Patrimonial 5 - Apuração Contábil 6 - Apuração Anual |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Contabil.ContasContabeis

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa |
| `Conta` | string |  | Código da Conta |
| `DescricaoConta` | string |  | Descrição da conta |
| `ResumoFiscal` | string |  | Resumo Fiscal da conta |
| `Ano` | integer (int32) |  | Ano da máscara de plano de contas |
| `DataCadastro` | string (date-time) |  | Data de cadastro da conta |

### UAUApi.Models.Contabil.ConsultarContasContabeisRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Ano` | integer (int32) | ✓ | Ano da máscara de plano de contas |
| `Conta` | string |  | Código da Conta |
| `DescricaoConta` | string |  | Descrição da conta |
| `LimitarRetornoEm` | integer (int32) | ✓ | Limite resultados a serem retornados |
