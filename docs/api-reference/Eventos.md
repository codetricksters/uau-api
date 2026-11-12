# Eventos

## POST `/api/v{version}/Eventos/ConsultarChavesLogDeEventos`

**Consulta a lista com as chaves dos eventos que podem ser consultados**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Regras de Negócio:
1. A chave de acesso consultada informa quais chaves poderão ser utilizadas no seguinte endpoint:
    1. URI + /api/v{version}/Eventos/ConsultarLogEventos
    
Anexos:
1. Postman: https://ajuda.globaltec.com.br/download/777172/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Eventos.ConsultarChavesLogDeEventosResponse`](#uauapimodelseventosconsultarchaveslogdeeventosresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Eventos/ConsultarLogEventos`

**Consultar os logs de eventos do sistema**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
3. Preencher os parâmetros de request para uso do método.
4. Os campos do tipo data devem obedecer o formato especificado pelo JSON.
    1. yyyy-MM-dd HH:mm:ss &gt; 2019-01-22 00:00:00
    2. yyyy-MM-dd &gt; 2018-12-25

Definição de Negócio:
Permite consultar logs de eventos.
1. Verifique as chaves de consultas disponíveis no endpoint:
    - URI + /api/v{version}/Eventos/ConsultarChavesLogDeEventos
2. Deve informar uma data inicial e outra final.

Anexos:
1. Postman: https://ajuda.globaltec.com.br/download/777172/
2. Retorno: https://ajuda.globaltec.com.br/download/777175/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Eventos.ConsultarLogEventosRequest`](#uauapimodelseventosconsultarlogeventosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Eventos.ConsultarLogEventosResponse`](#uauapimodelseventosconsultarlogeventosresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Eventos.ConsultarLogEventosResponse

Classe modelos com colunas especificadas da tabela eventos.

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Objeto` | string |  | Tipo do evento |
| `DataHora` | string (date-time) |  | Data da ocorrência |
| `TipoEvento` | string |  | Tipo do Evento |
| `Usuario` | string |  | Usuário causador |
| `Origem` | string |  | Origem do evento |
| `Descricao` | string |  | Descrição do evento |

### UAUApi.Models.Eventos.ConsultarLogEventosRequest

Classe para mapeamento do request. Endpoint: /api/v{version}/Eventos/ConsultarChavesLogDeEventos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Chave` | string | ✓ | Chave para consulta |
| `DataInicial` | string (date-time) | ✓ | Data inicial |
| `DataFinal` | string (date-time) | ✓ | Data final |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Eventos.ConsultarChavesLogDeEventosResponse

Classe utililzada na montagem do response do endpoint: URI + /api/v{version}/Eventos/ConsultarChavesLogDeEventos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Chave` | string |  | Chave para consulta dos logs de eventos |
