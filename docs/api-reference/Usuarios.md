# Usuarios

## POST `/api/v{version}/Usuarios/ConsultarGruposDeUsuario`

**Realiza consulta de grupos de usuário.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Grupos de usuário |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Usuarios/ConsultarUsuariosAtivos`

**Retorna a relação de usuários ativos**

Se não informar o parâmetro “login_usuario”, vai está retornando todos os usuários ativos disponíveis.
        

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.       

Parâmetros da request
1. login_usuario: Nome do login usuario.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Usuarios.ConsultarUsuariosAtivosRequest`](#uauapimodelsusuariosconsultarusuariosativosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Relação de usuários ativos |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Usuarios.ConsultarUsuariosAtivosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `login_usuario` | string |  | Nome do login usuario |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |
