# Localidade

## POST `/api/v{version}/Localidade/ConsultarLocalidadePorCEP`

**Consulta Localidades por CEP.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Consultar as informações da localidade informando apenas o CEP.
1. Valida a presença do CEP;
2. Retorna uma ou mais localidades para o CEP informado;
3. Retorna somente endereços ativos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Localidade.ConsultarSomenteCEPRequest`](#uauapimodelslocalidadeconsultarsomenteceprequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.LocalidadeResponse`](#uauapimodelslocalidaderesponse) |
| 400 |  - Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.LocalidadeResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CEP` | string |  | Número do CEP |
| `CodigoLogradouro` | integer (int32) |  | Código do Logradouro |
| `DescricaoLogradouro` | string |  | Descrição do Logradouro |
| `CodigoBairro` | integer (int32) |  | Código do Bairro |
| `Bairro` | string |  | Descrição do Bairro |
| `CodigoCidade` | integer (int32) |  | Código da Cidade |
| `Cidade` | string |  | Descrição da Cidade |
| `UF` | string |  | UF |

### UAUApi.Models.Localidade.ConsultarSomenteCEPRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Cep` | string | ✓ | Informar este parâmetro sem pontuação. |
