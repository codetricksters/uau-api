# Autenticador

## POST `/api/v{version}/Autenticador/AutenticarUsuario`

**Autenticação padrão do Uau via usuário e senha cadastrados no banco de dados.**

Definição técnica:
1. Preencher os parâmetros de request para uso do método.

Definição de negócio:
1. Verifica o método de Login configurado no Sistema Uau https://ajuda.globaltec.com.br/virtuau/configuracao-de-seguranca/ 
2. Empresa configurada com Autenticação AD e utilizar este serviço a autenticação será como Cliente/Pessoa.
3. Empresa configurada com Autenticação Uau
   - Login do usuário maior que 8 caracteres a autenticação será como Cliente/Pessoa.
   - Login do usuário menor que 8 caracteres a autenticação será Uau.
4. Para utilizar o recurso de GerarBoleto deve-se informar a propriedade UsuarioUAUSite.
   
VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_Uau
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_via_Active_Directory

Anexos: 
- Exemplo Postman: https://ajuda.globaltec.com.br/download/774812/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Autenticador.AutenticarUsuarioRequest`](#uauapimodelsautenticadorautenticarusuariorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | token | string |
| 400 | Login do usuário ou a senha estão incorretos. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao realizar a autenticação, não foi possível verificar os dados de login. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Autenticador/AutenticarUsuarioApp`

**Realiza a autenticação do usuário e senha verificando o método de login sendo AD será autenticado o usuário corporativo,
caso contrário será validado como usuário UAU ou Cliente.
Atualmente utilizado pela API do Mobile.**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Autenticador.AutenticarUsuarioRequest`](#uauapimodelsautenticadorautenticarusuariorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Usuario | object |
| 400 | Usuário não encontrado. Autenticação de usuário via AD é necessário que o usuário Uau tenha o usuário AD vinculado. Acessar o módulo Segurança e configurar o usuário AD. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao realizar a autenticação, não foi possível verificar os dados de login. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Autenticador/AutenticarUsuarioCorporativo`

**Realiza a autenticação do usuário através do Active Directory**

Definição técnica:
1. Preencher os parâmetros de request para uso do método.

Definição de negócio:
1. Verifica o método de Login configurado no Sistema Uau https://ajuda.globaltec.com.br/virtuau/configuracao-de-seguranca/ 
2. Empresa configurada para método de Login Uau via banco de dados
   - Será realizada a verificação se existe o usuário com a senha informada.
3. Empresa configurada para método de Login via AD
   - Será realizada a autenticação validando no Active Directory
4. No parâmetro login_uau do corpo da requisição, deve ser informado o login que é utilizado no uau quando o Active Directory não está habilitado. 
   - A informação do login do usuário está no módulo segurança.  
   
VirtUau: 
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Autenticacao_de_Usuario_via_Active_Directory

Anexos: 
- Exemplo Postman: https://ajuda.globaltec.com.br/download/774812/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Autenticador.AutenticarUsuarioCorporativoRequest`](#uauapimodelsautenticadorautenticarusuariocorporativorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | token | string |
| 400 | Login do usuário ou a senha estão incorretos. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao realizar a autenticação, não foi possível verificar os dados de login. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Autenticador/AutentificarUsuarioTitanium`

**Faz a autenticação de um usuário titanium**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Autenticador.AutentificarUsuarioTitaniumRequest`](#uauapimodelsautenticadorautentificarusuariotitaniumrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | token | string |
| 400 | Login do usuário ou a senha estão incorretos. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao realizar a autenticação, não foi possível verificar os dados de login. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Autenticador/ConsultarDadosUsrLogado`

**Consulta os dados pessoais, endereço e telefone do usuário logado. Só consulta os dados caso o
usuário logado seja do tipo pessoa. Caso contrário uma exceção é lançada informando que
o usuário logado precisa ser do tipo pessoa para este método.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
Permite consultar os dados do usuário do tipo cliente do Cadastro de Pessoas do Uau.
1. O usuário cliente deve estar autenticado.
2. Retorna as informações do cliente logado, conforme a estrutura abaixo.

- Estrutura do Retorno: https://ajuda.globaltec.com.br/download/774818/
3. Dados Pessoais: 
    - codigo = Código do cliente
    - nome = Nome completo
    - cpf = CPF
    - dtnasc = Data de nascimento
    - email = E-mail
    - login = Login do Cliente no UAU Web
    - senha = Senha do cliente
4. Dados do Telefone:
    - codigo = Código do cliente
    - numero = Número do telefone do cliente
    - ddd = DDD do telefone
    - ramal = Ramal do telefone do cliente
    - tipo = Tipo do telefone (0-residencial;1-comercial;2-celular;3-recado;4-fax;5-bip;6-telex;7-outros;8-fone/fax)
5. Dados do Endereço:
    - codPes = Código do cliente
    - tipoEndereco = 0-Principal 1-Cobrança 2-Comercial
    - endereco = Endereço do cliente
    - complemento = Complemento do endereço
    - numero = Número do endereço do cliente
    - referencia = Referência do endereço
    - bairro = Bairro
    - cep = CEP
    - cidade = Cidade
    - uf = UF

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Consultar_dados_do_Usuario_Logado

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/774809/
- Exemplo Retorno: https://ajuda.globaltec.com.br/download/774818/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | dadospessoais https://ajuda.globaltec.com.br/download/774818/ | object |
| 400 | Implementado apenas para usuários do tipo pessoa! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Autenticador/LogoutUsuario`

**Realiza o logout de um usuário destruíndo a sessão do usuário logado**

Criação: Diogo Rodrigues Gonçalves      Data: 22/01/2018

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Autenticador/VerificaUsuarioLogado`

**Verifica se um usuário está logado**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string |  | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK |  |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Autenticador.AutentificarUsuarioTitaniumRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  |  |
| `senha` | string |  |  |

### UAUApi.Models.Autenticador.AutenticarUsuarioCorporativoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `login_ad` | string | ✓ | Login de rede AD |
| `senha` | string | ✓ | Senha de rede AD |
| `login_uau` | string | ✓ | Login do usuário Uau |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Autenticador.AutenticarUsuarioRequest

Essa classe está como exemplo das validações usando o DataAnnotation e o FluentValidation 
sendo que o mesmo pode ser usado dentro do projeto simultaneamente

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Login` | string | ✓ | Login do usuário |
| `Senha` | string | ✓ | Senha do usuário |
| `UsuarioUAUSite` | string |  | Login de usuário do UAU que tem permissão de gerar boletos. |
