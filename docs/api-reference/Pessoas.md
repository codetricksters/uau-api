# Pessoas

## POST `/api/v{version}/Pessoas/AlterarContaPadrao`

**Altera a conta corrente padrão de uma pessoa.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Parâmetros da request
1. codigoPessoa: Código da Pessoa.
2. codigoBanco: Código do Banco.
3. agencia: Número da Agência.
4. conta: Conta.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoa.RequestAlterarContaPadrao`](#uauapimodelspessoarequestalterarcontapadrao)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Arquivo |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/AlterarPessoaAcessoPortal`

**Atualiza os dados de acesso ao UAU Web de uma determinada pessoa.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Autenticador/ConsultarDadosUsrLogado
3. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite alterar os dados de acesso ao Uau Web login, senha e e-mail.
1. Deve informar o código do próprio cliente logado no Uau Web no qual serão atualizados os dados.
2. A senha deve conter exatamente 6 caracteres e não poderá estar criptografada.
3. Realiza validação se o login informado está sendo utilizado por outro cliente.

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Alteracao_dos_Dados_de_Acesso_do_Cliente

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/775432/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.AlterarPessoaAcessoPortalRequest`](#uauapimodelspessoasalterarpessoaacessoportalrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/AlterarSenhaCliente`

**Alterar a Senha da Pessoa/Cliente que permite acesso a área de Clientes no Uau Web**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar os dados do usuário logado para obter o código do cliente URI + /api/v{version}/Autenticador/ConsultarDadosUsrLogado
3. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite alterar a senha do cliente.
1. Deve informar o código do próprio cliente logado no Uau Web no qual será alterada a senha.
2. A senha deve conter exatamente 6 caracteres e não poderá estar criptografada.
3. Realiza validação se o login informado está sendo utilizado por outro cliente.

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Alteracao_de_Senha_do_Usuario_Cliente

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/774830/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.AlterarSenhaClienteRequest`](#uauapimodelspessoasalterarsenhaclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Senha alterada com sucesso! | string |
| 400 | O código do cliente e a senha são parâmetros obrigatórios. - A senha deve ter 6 caracteres. - O código do cliente informado está diferente do cliente logado na aplicação. - Existe mais de um cliente com o mesmo login. - Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarContasBancarias`

**Consultar contas bancárias por código de determinada pessoa**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
3. Informar o código da pessoa para uso do método.

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarContasBancariasRequest`](#uauapimodelspessoasconsultarcontasbancariasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Pessoas.GravarContaBancariaRequest`](#uauapimodelspessoasgravarcontabancariarequest) |
| 400 | Verifique se a condição para realizar a consulta está correta. - Os campos string devem conter as aspas simples. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarDadosAdicionaisPessoaPorChave`

**Consulta dados adicionais de uma pessoa por chave**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Busca por dados adicionais de pessoa filtrando pela chave.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarDadosAdicionaisPessoaPorChaveRequest`](#uauapimodelspessoasconsultardadosadicionaispessoaporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarDadosPessoaFisicaPorCodigo`

**Consultar dados de pessoa física**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta dados de pessoa física filtrando pelo código da pessoa.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarDadosPessoaFisicaPorCodigoRequest`](#uauapimodelspessoasconsultardadospessoafisicaporcodigorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus`

**Consulta pessoa por CPF/CNPJ e Status**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Informar o CPF/CNPJ e status da pessoa para uso do método.

Regras de Negócio:
1. CPF/CNPJ aceita apenas números.
2. Valida se encontrou a pessoa.

Informação:
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarPessoasPorCPFCNPJRequest`](#uauapimodelspessoasconsultarpessoasporcpfcnpjrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Pessoa.Pessoa`](#uauapimodelspessoapessoa) |
| 400 | Verifique se a condição para realizar a consulta está correta. - Os campos string devem conter as aspas simples. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarEnderecoPessoasPorChave`

**Consultar endereços de pessoa por código da pessoa e tipo de endereço**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarEnderecoPessoasPorChaveRequest`](#uauapimodelspessoasconsultarenderecopessoasporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarPessoaPorChave`

**Consulta dados primários de uma pessoa**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Cosulta os dados de uma pessoa filtrando pelo código.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarPessoaPorChaveRequest`](#uauapimodelspessoasconsultarpessoaporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarPessoasComVenda`

**Consulta clientes que são titulares de vendas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Retorna código de nome da pessoa.

Definição de Negócio:
1. As vendas podem ser quitadas ou não.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarPessoasFuncionariosAtivos`

**Consultar funcionários ativos**

Informação:
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarPessoasFuncionariosAtivosRequest`](#uauapimodelspessoasconsultarpessoasfuncionariosativosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarPessoasPorCPFCNPJ`

**Consulta os dados da pessoa por CPF/CNPJ e Status**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Deve informar o CPF/CNPJ sem formatações e o status.
4. O status pode ser:
    - 0 = Ativo 
    - 1 = Inativo
    - 2 = Ambos

Definição de Negócio:
Permite obter os dados de determinada pessoa física ou jurídica.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).


VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes/#Servico_para_Consultar_dados_da_pessoa_por_CPFCNPJ

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/774849/
- Exemplo Retorno: https://ajuda.globaltec.com.br/download/774846/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarPessoasPorCPFCNPJRequest`](#uauapimodelspessoasconsultarpessoasporcpfcnpjrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarPessoasPorCondicao`

**Consulta os dados da pessoa de acordo com a condição informanda na busca**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. A condição informada é uma clausula SQL pós WHERE, segue exemplo:
    - cpf_pes = '12345678910' AND nome_pes LIKE 'GLOBALTEC%'
4. Devem ser passado as aspas simples para campos string.

Definição de Negócio:
1. Consulta pessoa por condição informada. 
2. Valida a condição da consulta, evitando SQL Injection.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarPessoasPorCondicaoRequest`](#uauapimodelspessoasconsultarpessoasporcondicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Pessoas.PessoasCondicao`](#uauapimodelspessoaspessoascondicao) |
| 400 | Verifique se a condição para realizar a consulta está correta. - Os campos string devem contar as aspas simples. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarTelefonePesPorChave`

**Consulta telefones da pessoa**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
3. Preencher os parâmetros de request para uso do método.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarTelefonePesPorChaveRequest`](#uauapimodelspessoasconsultartelefonepesporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Verifique se a condição para realizar a consulta está correta. - Os campos string devem conter as aspas simples. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarTelefones`

**Consultar telefones em relação ao usuário**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Número de usuário é obrigatório.
4. Nível de permissão, GETELPES Consulta

Definição de Negócio:
1. Listagem dos telefones relacionadas ao usuário.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoa.RequestConsultaTelefone`](#uauapimodelspessoarequestconsultatelefone)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Pessoa.ManterTelefone`](#uauapimodelspessoamantertelefone) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarTipoEndereco`

**Consultar tipo de endereço da pessoa**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarTipoEnderecoRequest`](#uauapimodelspessoasconsultartipoenderecorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ConsultarUnidades`

**Consultar unidades do cliente**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Informar o código da pessoa ou CPF/CNPJ da pessoa para uso do método.

Regras de Negócio:
1. CPF/CNPJ aceita apenas números.
2. Valida se encontrou a pessoa.
VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ConsultarUnidadesRequest`](#uauapimodelspessoasconsultarunidadesrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Pessoas.UnidadesClientes`](#uauapimodelspessoasunidadesclientes) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/CriarCredenciaisUAUWeb`

**Cria um novo usuário e senha para a pessoa no UAUWeb.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request com os dados do usuário para uso do método.

Regras de Negócio:
1. É necessário que o usuario forneça o UsuarioUAUSite ao obter o token de autenticação.
2. O usuário não pode estar duplicado no banco de dados.
3. O Email não pode estar sendo utilizado por outra pessoa.
4. O usuário não pode já ter um Login UAUWeb.
5. O novo login não pode estar sendo utilizado por outra pessoa.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.CriarCredenciaisUAUWebRequest`](#uauapimodelspessoascriarcredenciaisuauwebrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ExcluirBancoEContaPorChave`

**Exclui banco e conta por pessoa**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
3. Consultar os dados bancarios da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarContasBancarias.
4. Preencher os parâmetros de request com os dados bancários e o código da pessoa para uso do método.

Regras de Negócio:
1. Valida usuário e permissões.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ExcluirBancoContaPessoaRequest`](#uauapimodelspessoasexcluirbancocontapessoarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Verifique se a condição para realizar a consulta está correta. - Os campos string devem conter as aspas simples. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ExcluirTelefone`

**Excluir telefones em relação ao usuário**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Número de usuário é obrigatório.
4. Nível de permissão, GETELPES Exclusão

Definição de Negócio:
1. A exclusão do telefone é feita somente para o usuário informado.

Informação:
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoa.RequestExcluirTelefone`](#uauapimodelspessoarequestexcluirtelefone)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/GravarContaBancaria`

**Grava banco e conta por pessoa**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar o codigo da pessoa na rota URI +/api/v{version}/Pessoas/ConsultarDadosPessoaPorCpfCnpjEStatus.
3. Preencher os parâmetros de request com os dados bancários e o código da pessoa para uso do método.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/integracao-uauweb-com-sites-de-clientes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.GravarContaBancariaRequest`](#uauapimodelspessoasgravarcontabancariarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Pessoas.GravarContaBancariaRequest`](#uauapimodelspessoasgravarcontabancariarequest) |
| 400 | Verifique se a condição para realizar a consulta está correta. - Os campos string devem conter as aspas simples. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/GravarPessoa`

**Insere ou altera Pessoa Física ou Jurídica e seus dados**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite inserir ou alterar pessoa física ou jurídica e seus respectivos dados. Se for uma nova pessoa, informar "0" no parâmetro cod_pes.
Se for alterar uma pessoa já existente, informar o código no parâmetro cod_pes.
1. Deve montar uma estrutura com as informações de determinada pessoa.
- https://ajuda.globaltec.com.br/download/801043/
2. Valida a estrutura do e-mail
3. Valida se o nome de usuário informado para acesso ao uau web existe para outra pessoa
4. Valida campos obrigatórios
5. O campo *dspes_tel_json* espera uma String json no formato abaixo.
 "dspes_tel_json": [ { \"PesTel\": 
  [ { \"ddd_tel\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
      \"fone_tel\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
      \"ram_tel\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
      \"tipo_tel\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
      \"TipoTel_tel\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\", 
      \"ExisteTel_tel\": \"System.Boolean, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
      \"Principal_tel\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"},
{ \"ddd_tel\": \"62\", \"fone_tel\": \"39529100\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ,
{ \"ddd_tel\": \"62\", \"fone_tel\": \"81129773\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ,
{ \"ddd_tel\": \"62\", \"fone_tel\": \"3952-9149\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ,
{ \"ddd_tel\": \"62\", \"fone_tel\": \"984689664\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ,
{ \"ddd_tel\": \"62\", \"fone_tel\": \"39529136\", \"ram_tel\": \"\", \"tipo_tel\": 4, \"TipoTel_tel\": \"\", \"ExisteTel_tel\": false, \"Principal_tel\":0 } ] }]"

    - Sempre a primeira linha do json é a estrutura do mesmo, então ela sempre irá se repetir, apartir dela, as proximas serão os telefones. No exemplo tempo 5 telefones.
    - Isto ocorre por ser um método antigo do UAU, que foi migrado para API. Futuramente esse endpoint vai ser descontinuado.
6. Valida Nação e UF referente aos campos 'codnacao_pf' e 'ufnasc_pf' respectivamente, Ex: Nação: 'BRA' UF: 'GO',ou seja se for informado Nação será obrigado UF ou vice-versa.
    - https://ajuda.globaltec.com.br/virtuau/cadastro-de-unidade-federativa/
    
7. Valida código e descrição do município referente aos campos 'cidadenat_pf' e 'naturalid_pf' respectivamente, Ex: Código: '1' Descrição: 'Goiânia'. 
    - Se caso for informado cidadenat_pf também será obrigado informar o campo naturalid_pf ou vice-versa. 
    - https://ajuda.globaltec.com.br/virtuau/virtuau/cadastro-de-municipios/
     
8. Validação tamanho do endereço: Essa validação pode ser ativada no cadastro de Pessoas em “Config.” ou seja em configuração de endereço, quando se marca a opção:
     “Limitar o cadastro de endereço de cobrança de pessoas e prospects para o máximo permitido nos boletos”, se essa opção estiver marcada no momento da requisição 
     se tiver utilizando o endereço maior  que o permitido poderá receber a seguinte mensagem” O campo 'Bairro - Endereço de cobrança' está com o tamanho acima do permitido: 15 | atual: 27.", como exemplo.
    
9.  Verificação para Gravação das informações do documento da Pessoa: Verifica se o campo "info_pesfis" (informações da Pessoa física) foi informado, pois se não foi, o infopes_doc (informações dos documentos da Pessoa) não será considerado. 

10. Informação: 
Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).
    
VirtUau:
- https://ajuda.globaltec.com.br/virtuau/uau-pessoas/#GravarPessoa

Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/774876/
- Exemplo Retorno: https://ajuda.globaltec.com.br/download/774882/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.GravarPessoaRequest`](#uauapimodelspessoasgravarpessoarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Pessoas.PessoasController.Resultado`](#uauapipessoaspessoascontrollerresultado) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ImportarDadosPessoasParaUau`

**Importa os dados de pessoas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Deve seguir arquivo XSD com o formato aceito.

Definição de Negócio:
1. Realiza a importação dos dados de pessoas para o UAU atravéz de arquivo XML.
2. Será validado o xml deserializado que preenche a classe de importação validando os dados.

Informação: 
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/uau-pessoas-2/

Anexos:
1. Arquivo XSD do XML: https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2016/06/Pessoasxsd-1.rar
2. Exemplo XML: https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2016/06/Pessoas-3.rar

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.ImportarDadosPessoasParaUauRequest`](#uauapimodelspessoasimportardadospessoasparauaurequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/ManterTelefone`

**Alterar ou inserir telefones ao usuário**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Número de usuário é obrigatório.
4. Nível de permissão, GETELPES Alteração ou Inclusão

Definição de Negócio:
1. Quando o telefone não existe, ele é adicionado em relacionamento ao usuário proposto.
2. Quando o telefone já existe, ele faz a alteração dos dados.
3. Não se pode ter telefones iguais para a mesma pessoa. Caso tente colocar um telefone que já existe para determinada pessoa, irá retornar uma mensagem de erro.
4. O mesmo telefone pode ter usuários diferentes, e a alteração é feita somente naquele diretamente relacionado.
4.Só pode possuir um telefone como principal por pessoa

4. Informação:
Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoa.RequestManterTelefone`](#uauapimodelspessoarequestmantertelefone)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Pessoa.RequestManterTelefone`](#uauapimodelspessoarequestmantertelefone) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Pessoas/RecuperarCredenciaisUAUWeb`

**Envia por e-mail a senha de uma pessoa do UAUWeb.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request com o login ou o email do usuário da pessoa para uso do método.

Regras de Negócio:

1. É necessário que o usuário forneça o UsuarioUAUSite ao obter o token de autenticação.
2. O usuário logado (informado na rota de autenticação) deverá possuir configuração de email cadastrada. Para verificar, acesse a Tela de Configurações do Usuário - Configurações - Configuração Email.
3. Deverá estar parametrizado a configuração "Enviar os avisos de pendências também por email externo", na aba Geral da tela de Configurações do Sistema.
4. O usuário não pode estar duplicado no banco de dados.
5. O usuário deve já ter um Login UAUWeb.
6. O usuário deve ter um email cadastrado.
7. Caso login e email seja enviado, é verificado se o usuário com esse login possui esse email cadastrado.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Pessoas.RecuperarCredenciaisUAUWebRequest`](#uauapimodelspessoasrecuperarcredenciaisuauwebrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Pessoas.RecuperarCredenciaisUAUWebRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Login` | string |  | Contém o login da pessoa |
| `Email` | string |  | Contém o email da pessoa |

### UAUApi.Models.Pessoa.RequestManterTelefone

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) | ✓ | Código da pessoa |
| `Telefones` | array de [`UAUApi.Models.Pessoa.ManterTelefone`](#uauapimodelspessoamantertelefone) | ✓ | Lista de telefones |

### UAUApi.Models.Pessoas.ImportarDadosPessoasParaUauRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `xml` | string | ✓ | Xml montado conforme o arquivo XSD de Pessoas |

### UAUApi.Pessoas.PessoasController.Resultado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoPessoa` | integer (int32) |  |  |
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |

### UAUApi.Models.Pessoas.GravarPessoaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nao_validar_campos_obrigatorios` | boolean |  | Indica se está utilizando campos obrigatórios |
| `info_pes` | [`UAUApi.Models.Pessoas.Pessoas`](#uauapimodelspessoaspessoas) | ✓ | Contém informações da Pessoa(física ou jurídica) |
| `info_pesfis` | [`UAUApi.Models.Pessoas.PesFis`](#uauapimodelspessoaspesfis) |  | Contém informações da Pessoa física |
| `infopes_jur` | [`UAUApi.Models.Pessoas.PesJur`](#uauapimodelspessoaspesjur) |  | Contém informações da Pessoa jurídica |
| `dspes_tel_json` | string |  | Contém os telefones da Pessoa(física ou jurídica) |
| `infopes_doc` | [`UAUApi.Models.Pessoas.PessoasDoc`](#uauapimodelspessoaspessoasdoc) |  | Contém as informações dos documentos da Pessoa |
| `info_pesendereco_principal` | [`UAUApi.Models.Pessoas.PesEndereco`](#uauapimodelspessoaspesendereco) |  | Contém os endereço principal da pessoa |
| `infopesendereco_cobranca` | [`UAUApi.Models.Pessoas.PesEndereco`](#uauapimodelspessoaspesendereco) |  | Contém o endereço de cobrança da pessoa |
| `infopesendereco_comercial` | [`UAUApi.Models.Pessoas.PesEndereco`](#uauapimodelspessoaspesendereco) |  | Contém o endereço comercial da pessoa |

### UAUApi.Models.Pessoas.PesEndereco

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodPes_pend` | integer (int32) | ✓ | Código da Pessoa |
| `Tipo_pend` | integer (int32) | ✓ | Tipo de endereço: 0 - Endereço Principal 1 - Endereço Cobrança 2 - Endereço Comercial |
| `Endereco_pend` | string |  | Logradouro |
| `Bairro_pend` | string |  | Bairro |
| `Cidade_pend` | string |  | Cidade |
| `UF_pend` | string |  | Sigla da UF |
| `CEP_pend` | string |  | CEP |
| `NumEnd_pend` | string |  | Número endereço |
| `ComplEndereco_pend` | string |  | Complemento do endereço |
| `ReferEnd_pend` | string |  | Referência do endereço |
| `Proprio_pend` | integer (int32) |  | Identifica se o endereço da pessoa é próprio. 0 - sim 1 - não |
| `NumCid_pend` | integer (int32) |  | Código da cidade |
| `NumBrr_pend` | integer (int32) |  | Código do bairro |
| `NumLogr_pend` | integer (int32) |  | Código do logradouro |
| `CodEmp_pend` | integer (int32) |  | Código da empresa |
| `NomeEmp_pend` | string |  | Nome da empresa |
| `TipoEndEmp_pend` | integer (int32) |  | Tipo do endereço comercial.  0 - selecionado 1 - gravado |

### UAUApi.Models.Pessoas.PessoasDoc

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codpes_doc` | integer (int32) | ✓ | Código da pessoa |
| `tipo_doc` | integer (int32) | ✓ | Tipo do documento |
| `registro_doc` | string | ✓ | Código de registro |
| `orgaoemissor_doc` | string |  | Órgão emissor |
| `codnacao_doc` | string |  | Código da nação |
| `uf_doc` | string |  | UF do Documento |
| `dataemissao_doc` | string (date-time) |  | Data da emissão do documento |
| `datavalidade_doc` | string (date-time) |  | Data de validade do documento |
| `categoria_doc` | string |  | Categoria do documento |
| `zonaeleit_doc` | string |  | Zona Eleitoral |
| `secao_doc` | string |  | Seção eleitoral |
| `tipoentclasse_doc` | integer (int32) |  | Tipo entidade: 0 - Administração 1 - Advocacia 2 - Biblioteconomia 3 - Biologia 4 - Biomedicina 5 - Contabilidade 6 - Economia 7 - Educação física 8 - Enfermagem 9 - Engenharia 10 - Farmácia 11 - Fisioterapia 12 - Fonoaudiologia 13 - Medicina 14 - Medicina veterinária 15 - Nutrição 17 - Psicologia 18 - Química 19 - Serviço Social |
| `seqconselho_doc` | string |  | Número sequencial do conselho |
| `dataalt_doc` | string (date-time) |  | Data alteração |
| `usralt_doc` | string |  | Usuário alterou |

### UAUApi.Models.Pessoas.PesJur

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_pj` | integer (int32) | ✓ | Informar o mesmo valor do campo Cod_Pes |
| `contato_pj` | string |  | Nome da pessoa de contato na empresa |
| `contato2_pj` | string |  | Nome da segunda pessoa de contato da empresa |
| `inssuframa_pj` | string |  | Armazenar o código de inscrição no SUFRAMA da pessoa jurídica |
| `natureza_pj` | integer (int32) |  | Indicador da natureza da pessoa: 1 - Órgão, Autarquia ou Fundação Federal 2 - Entidade da Administração Pública Federal 3 - Pessoa Jurídica de Direito Privado 4 - Sociedade Cooperativa 5 - Fabricante de Máquinas e Veículos |
| `optantesimples_pj` | boolean |  | Verificar se é Optante do Simples:  0 - Não 1 - Sim. |
| `ans_pj` | string |  | Código ANS |

### UAUApi.Models.Pessoas.PesFis

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_pf` | integer (int32) | ✓ | Contém o código da pessoa Física, se for um novo informar 0. |
| `lotacao_pf` | string |  | Lotação da pessoa Física |
| `cargo_pf` | string |  | Cargo da pessoa |
| `dtadm_pf` | string (date-time) |  | Contém a data de admissão |
| `corresp_pf` | integer (int32) |  | Endereço de correspondência: 0 - nenhum 1 - comercial 2 - residencial |
| `estciv_pf` | integer (int32) |  | Estado civil: 0 - separado 1 - solteiro 2 - casado 3 - desquitado 4 - viúvo 5 - divorciado 6 - outros |
| `doc_pf` | string |  | Número do documento |
| `tdoc_pf` | string |  | Tipo do documento |
| `dtdoc_pf` | string (date-time) |  | Data do documento |
| `sexo_pf` | integer (int32) |  | Sexo: 0 - masculino 1 - feminino |
| `nacion_pf` | string |  | Contém a nacionalidade da pessoa |
| `numdep_pf` | integer (int32) |  | Número de dependentes |
| `pai_pf` | string |  | Nome do pai |
| `dtpai_pf` | string (date-time) |  | Data de nascimento do pai |
| `mae_pf` | string |  | Nome da Mãe |
| `dtmae_pf` | string (date-time) |  | Data de nascimento da mãe |
| `naturalid_pf` | string |  | Naturalidade da pessoa. |
| `codnacao_pf` | string |  | Contém o código da nascionalidade |
| `codgrau_pf` | string |  | Contém o grau de escolaridade |
| `codraca_pf` | string |  | Contém a raça da pessoa |
| `codsmil_pf` | string |  | Código da Situação Militar |
| `ufnasc_pf` | string |  | Contém o UF de nascimento da pessoa |
| `cidadenat_pf` | integer (int32) |  | Código da cidade de nascimento |
| `fatorrh_pf` | string |  | Fator do RH |
| `regcasamento_pf` | integer (int32) |  | Regime de casamento     0 - Comunhão parcial de bens     1 - Comunhão total de bens     2 - Separação total de bens     3 - Participação final nos aquestos |
| `cdi_pf` | string |  | Numero CDI |
| `numpro_pf` | integer (int32) |  | Código da profissão |
| `uniaoestavel_pf` | boolean |  | União estável:  0 - não 1 - sim |
| `detalhanacao_pf` | integer (int32) |  | Código do detalhamento da nacionalidade |
| `codnacaoorigem_pf` | string |  | Código da nação de origem |
| `codmunicnasc_pf` | integer (int32) |  | Código município de nascimento |
| `indicativofiscal_pf` | integer (int32) |  | Indicativo fiscal |
| `formatributacao_pf` | string |  | Forma de tributação |
| `renda_pf` | [`UAUApi.Models.Pessoas.PesFis.Renda`](#uauapimodelspessoaspesfisrenda) |  | Renda pessoa física (moeda + valor) |

### UAUApi.Models.Pessoas.PesFis.Renda

Classe interna para agrupar moeda e valor da renda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `moeda_renda_pf` | string |  | Moeda da renda |
| `valor_renda_pf` | number (double) |  | Valor da renda |

### UAUApi.Models.Pessoas.Pessoas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_pes` | integer (int32) | ✓ | Código da pessoa |
| `nome_pes` | string | ✓ | Descrição da pessoa |
| `tipo_pes` | integer (int32) | ✓ | Define o tipo da pessoa 0 - Pessoa Física; 1 - Pessoa Jurídica; |
| `cpf_pes` | string |  | Codigo do cpf ou CNPJ da pessoa |
| `dtcad_pes` | string (date-time) |  | Data de cadastro da pessoa no sistema |
| `dtnasc_pes` | string (date-time) |  | Data de nascimento da pessoa |
| `intext_pes` | integer (int32) |  | Define se a pessoa é interno ou externo 1 - Interno; 2 - Externo; |
| `usrcad_pes` | string | ✓ | Usuário que cadastrou a pessoa no sistema |
| `usralt_pes` | string |  | Usuário que alterou os dados da pessoa no sistema, obrigatório apenas no caso de alteração de usuário |
| `status_pes` | integer (int32) | ✓ | Status da pessoa no sistema 1 - Temporário; 2 - Confirmado; |
| `tratamento_pes` | string |  | Define como será o tratamento com a pessoa Ex: Sr(ª), Dr(ª) |
| `siglaobr_pes` | string |  | Define a sigla da obra para a pessoa do tipo Interno |
| `email_pes` | string |  | Email da pessoa |
| `endwww_pes` | string |  | Endereço URL cadastrado para a pessoa |
| `matricula_pes` | string |  | Matricula da pessoa caso seja funcionário |
| `atinat_pes` | integer (int32) | ✓ | Define se a pessoa esta ativo ou inativo 0 - Ativo; 1 - Inativo; |
| `dataalt_pes` | string (date-time) |  | Data que os dados da pessoa foi alterada |
| `nomefant_pes` | string |  | Nome fantasia da pessoa |
| `anexos_pes` | integer (int32) |  | Exibe os anexos vinculados a pessoa |
| `inscrmunic_pes` | string |  | Codigo da inscrição municipal da pessoa |
| `inscrest_pes` | string |  | Codigo da inscrição estadual da pessoa |
| `siglaemp_pes` | integer (int32) |  | Define a sigla da empresa para pessoa do tipo interno. |
| `login_pes` | string |  | Login usado para a pessoa acessar o UauWeb como fornecedor. |
| `senha_pes` | string |  | Senha que será usada para acessa o UauWeb como fornecedor |
| `cnae_pes` | string |  | É o codigo que define a atividade econômica da empresa |
| `datacadportal_pes` | string (date-time) |  | Registra a data de primeiro cadastrado no portal |
| `cadastradoprefeituragyn_pes` | boolean | ✓ | Define se a pessoa está cadastrada na prefeitura de Goiânia |
| `habilitadoriscosacado_pes` | boolean | ✓ | Define se será possível realizar a antecipação de títulos enviados ao banco através da geração de arquivo de remessa |
| `cei_pes` | string |  | Numero CEI da pessoa |

### UAUApi.Models.Pessoa.RequestExcluirTelefone

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) | ✓ | Código da pessoa |
| `Telefones` | array de [`UAUApi.Models.Pessoa.ExcluirTelefone`](#uauapimodelspessoaexcluirtelefone) | ✓ | Lista de telefones |

### UAUApi.Models.Pessoa.ExcluirTelefone

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Telefone` | string | ✓ | Número do telefone da pessoa |
| `DDD` | string | ✓ | DDD do telefone da pessoa |

### UAUApi.Models.Pessoas.ExcluirBancoContaPessoaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoPessoa` | integer (int32) | ✓ | Código da pessoa |
| `banco` | integer (int32) | ✓ | Banco |
| `conta` | string | ✓ | Conta (Ex. 10200-3) |
| `agencia` | string | ✓ | Agência |

### UAUApi.Models.Pessoas.CriarCredenciaisUAUWebRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CPF` | string | ✓ | Contém o CPF ou o CNPJ da pessoa. Deve ser informado sem pontuação |
| `DataNascimento` | string (date-time) | ✓ | Contém a data de nascimento da pessoa caso seja um CPF na propriedade CPF_CNPJ ou contém a data de fundação caso seja um CNPJ |
| `Login` | string | ✓ | Contém o Login do UAUWeb |
| `Senha` | string | ✓ | Contém a nova senha no UAUWeb |
| `Email` | string | ✓ | Contém o email da pessoa |

### UAUApi.Models.Pessoas.UnidadesClientes

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int64) |  | Código da empresa |
| `DescricaoEmpresa` | string |  | Descrição da empresa |
| `Obra` | string |  | Código da obra |
| `DescricaoObra` | string |  | Descrição da obra; |
| `Venda` | integer (int32) |  | Número da venda |
| `Produto` | integer (int32) |  | Código do produto |
| `DescricaoProduto` | string |  | Descrição do produto |
| `Identificador` | string |  | Identificadores das unidades vinculadas a venda separados por " | " |

### UAUApi.Models.Pessoas.ConsultarUnidadesRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoPessoa` | integer (int32) |  | Código da pessoa |
| `CpfCnpj` | string |  | CPF ou CNPJ da pessoa |

### UAUApi.Models.Pessoas.ConsultarTipoEnderecoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoPessoa` | integer (int32) | ✓ | Número do código da pessoa |

### UAUApi.Models.Pessoa.ManterTelefone

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Telefone` | string | ✓ | Número do Telefone da pessoa |
| `DDD` | string | ✓ | DDD do Telefone da pessoa |
| `Complemento` | string |  | Complemento do telefone da pessoa |
| `Tipo` | integer (int32) | ✓ | Tipo de contato. 0 - Residencial, 1 - Comercial, 2 - Celular, 3 - Recado, 4 - Fax, 5 - Bip, 6 - Telex, 7 - Outros, 8 - Fone/Fax |
| `Principal` | integer (int32) |  |  |

### UAUApi.Models.Pessoa.RequestConsultaTelefone

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) | ✓ | Código da pessoa |

### UAUApi.Models.Pessoas.ConsultarTelefonePesPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoPessoa` | integer (int32) |  | Código da pessoa |

### UAUApi.Models.Pessoas.PessoasCondicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoPessoa` | integer (int32) |  | Codigo da pessoa |
| `NomePessoa` | string |  | Descrição da pessoa |
| `TipoPessoa` | integer (int32) |  | Define o tipo da pessoa 0 - Pessoa Física; 1 - Pessoa Jurídica; |
| `CpfPessoa` | string |  | Codigo do cpf da pessoa |
| `DataCadastroPessoa` | string (date-time) |  | Data de cadastro da pessoa no sistema |
| `DataNascimentoPessoa` | string (date-time) |  | Data de nascimento da pessoa |
| `InternoExterno` | integer (int32) |  | Define se a pessoa é interno ou externo 1 - Interno; 2 - Externo; |
| `UsuarioCadastro` | string |  | Usuário que cadastrou a pessoa no sistema |
| `UsuarioAlteracao` | string |  | Usuário que alterou os dados da pessoa no sistema |
| `StatusPessoa` | integer (int32) |  | Status da pessoa no sistema 1 - Temporário; 2 - Confirmado; |
| `TratamentoPessoa` | string |  | Define como será o tratamento com a pessoa Ex: Sr(ª), Dr(ª) |
| `SiglaObraPessoa` | string |  | Define a sigla da obra para a pessoa do tipo Interno |
| `EmailPessoa` | string |  | Email da pessoa |
| `EnderecoEletronicoPessoa` | string |  | Endereço URL cadastrado para a pessoa |
| `MatriculaPessoa` | string |  | Matricula da pessoa caso seja funcionário |
| `AtivoInativo` | integer (int32) |  | Define se a pessoa esta ativo ou inativo 0 - Ativo; 1 - Inativo; |
| `DataAlteracaoPessoa` | string (date-time) |  | Data que os dados da pessoa foi alterada |
| `NomeFantasia` | string |  | Nome fantasia da pessoa |
| `AnexosPessoa` | integer (int32) |  | Exibe os anéxos vinculados a pessoa |
| `InscricaoMunicipal` | string |  | Codigo da inscrição municipal da pessoa |
| `InscricaoEstadual` | string |  | Codigo da inscrição estadual da pessoa |
| `SiglaEmpresaPessoa` | integer (int32) |  | Define a sigla da empresa para pessoa do tipo interno. |
| `LoginPessoa` | string |  | Login usado para a pessoa acessar o UauWeb como fornecedor. |
| `SenhaLoginPessoa` | string |  | Senha que será usada para acessa o UauWeb como fornecedor |
| `CnaePessoa` | string |  | É o codigo que define a atividade econômica da empresa |
| `DataCadastroPortal` | string (date-time) |  | Registra a data de primeiro cadastrado no portal |
| `PessoaCadastradoPrefeituraGyn` | boolean |  | Define se a pessoa está cadastrada na prefeitura de Goiânia |
| `HabilitarRiscoSacado` | boolean |  | Define se será possível realizar a antecipação de títulos enviados ao banco através da geração de aquivo de remessa |
| `CeiPessoa` | string |  | Numero CEI da pessoa |
| `ListaDadosPessoaJuridica` | array de [`UAUApi.Models.Pessoas.PessoaJuridicaCondicao`](#uauapimodelspessoaspessoajuridicacondicao) |  | Lista com os dados da pessoa jurídica |
| `ListaDadosPessoFisica` | array de [`UAUApi.Models.Pessoas.PessoaFisicaCondicao`](#uauapimodelspessoaspessoafisicacondicao) |  | Lista com os dados da pessoa Física |
| `ListaDadosPessoaEndereco` | array de [`UAUApi.Models.Pessoas.PessoaEnderecoCondicao`](#uauapimodelspessoaspessoaenderecocondicao) |  | Lista com os dados de endereço da pessoa |

### UAUApi.Models.Pessoas.PessoaEnderecoCondicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoPessoa` | integer (int32) |  | Codigo da pessoa |
| `TipoEndereco` | integer (int32) |  | Define o tipo do endereço da pessoa 0 - Principal, 1 - Cobrança, 2 - Comercial |
| `EnderecoPessoa` | string |  | Endereço da pessoa |
| `BairroPessoa` | string |  | Bairro da pessoa |
| `CidadePessoa` | string |  | Cidade da pessoa |
| `UfPessoa` | string |  | Unidade federativa da pessoa |
| `CepPessoa` | string |  | Cep da pessoa |
| `NumeroEnderecoPessoa` | string |  | Numero do endereço da pessoa |
| `ComplementoEndereco` | string |  | Complemento do endereço da pessoa |
| `ReferenciaEndereco` | string |  | Referencia do endereço da pessoa |
| `EnderecoProprio` | integer (int32) |  | Define se o endereço da pessoa é um endereço próprio 0 - Não, 1 - Sim |
| `NumeroCidadeEndereco` | integer (int32) |  | Numero do cadastro da cidade do endereço |
| `NumeroBairroEndereco` | integer (int32) |  | Numero do cadastro do bairro do endereço |
| `NumeroLogadouroEndereco` | integer (int32) |  | Numero do cadastro do logradouro do endereço |
| `CodigoEmpresaPessoa` | integer (int32) |  | Codigo da empresa do endereço |
| `NomeEmpresaPessoa` | string |  | Nome da empresa do endereço |
| `TipoEnderecoEmpresa` | integer (int32) |  | Define o tipo do endereço da empresa para a pessoa 0 - Empresa não cadastrada, 1 - Empresa cadastrada |

### UAUApi.Models.Pessoas.PessoaFisicaCondicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoPessoa` | integer (int32) |  | Codigo da pessoa |
| `LotacaoPessoa` | string |  | Lotação da pessoa |
| `CargoPessoa` | string |  | Cargo da pessoa |
| `DataAdmissao` | string (date-time) |  | Data admissão da pessoa |
| `EnderecoCorrespondencia` | integer (int32) |  | Define o tipo de endereço para a correspondência 0 - Nenhum, 1 - Comercial, 2 - Residêncial |
| `EstadoCivil` | integer (int32) |  | Estado civil da pessoa |
| `DocumentoPessoa` | string |  | Documento apresentado da pessoa |
| `TipoDocumento` | string |  | Tido do documento da pessoa 1 - Registro Geral(RG), 2 - Registro Único de Identificação(RIC), 3 - Registro em Orgão de Classe(OC), 4 - Carteira Nacional de Habilitação(CNH), 5 - Título de Eleitor, 6 - Certidão Militar,  7 - Numero Identificação Fiscal(NIF) |
| `DataDocumento` | string (date-time) |  | Data do documento |
| `SexoPessoa` | integer (int32) |  | Sexo da pessoa |
| `NacionalidadePessoa` | string |  | Nacionalidade da pessoa |
| `NumeroDependentes` | integer (int32) |  | Numero de dependentes da pessoa |
| `NomePai` | string |  | Nome do pai da pessoa |
| `DataNascimentoPai` | string (date-time) |  | Data de nascimento do pai da pessoa |
| `NomeMae` | string |  | Nome da Mãe da pessoa |
| `DataNascimentoMae` | string (date-time) |  | Data nascimento da mãe da pessoa |
| `NaturalidadePessoa` | string |  | Naturalidade da pessoa |
| `CodigoNacao` | string |  | Codigo da nação cadastrada |
| `CodigoGrauInstrucao` | string |  | Codigo do grau de instrução da pessoa |
| `CodigoRaca` | string |  | Codigo da raça da pessoa |
| `CodigoSituacaoMilitar` | string |  | Codigo da situação militar |
| `UfNascimento` | string |  | Unudade federativa de nascimento da pessoa |
| `CidadeNatal` | integer (int32) |  | Cidade natal da pessoa |
| `FatorRH` | string |  | Fator RH da pessoa |
| `RegistroCasamento` | integer (int32) |  | Registro de casamento da pessoa |
| `NumeroCdi` | string |  | Numero do certificado de despença da incorporação |
| `NumeroProfissao` | integer (int32) |  | Numero da profissão da pessoa |
| `UniaoEstavel` | boolean |  | Define se a pessa tem união estável |
| `DetalhaNacao` | integer (int32) |  | Define a nação da pessoa 0 - Estrangeiro, 1 - Brasileiro Nato, 2 - Brasileiro Naturalizado, 3 - Brasileiro Nascido no Exterior |
| `CodigoNacaoOrigem` | string |  | Codigo da nação de origem da pessoa |
| `CodigoMunicipalNascimento` | integer (int32) |  | Codigo munícipal de nascimento da pessoa |
| `NumeroIndicativoFiscal` | integer (int32) |  | 1 - Beneficiário com NIF, 2 - Beneficiário dispensado do NIF, 3 - País não Exige NIF |
| `CodigoFormaTributacao` | string |  | Código da forma de tributação   10 Retenção do IRRF - alíquota padrão.   11 Retenção do IRRF - alíquota da tabela progressiva.   12 Retenção do IRRF - alíquota diferenciada (países com tributação favorecida ou regime fiscal privilegiado).   13 Retenção do IRRF - alíquota limitada conforme cláusula em ADT.   30 Retenção do IRRF - outras hipóteses.   40 Não retenção do IRRF - isenção estabelecida em ADT.   41 Não retenção do IRRF - isenção prevista em lei interna   42 Não retenção do IRRF - alíquota de 0% (zero por cento) prevista em lei interna   43 Não retenção do IRRF - pagamento antecipado do imposto   44 Não retenção do IRRF - medida Judicial   50 Não retenção do IRRF - outras hipóteses |
| `Moeda` | string |  |  |
| `Renda` | number (double) |  |  |

### UAUApi.Models.Pessoas.PessoaJuridicaCondicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoPessoa` | integer (int32) |  | Codigo da pessoa |
| `ContatoPessoa` | string |  | Contato da pessoa |
| `ContatoPessoa2` | string |  | Segundo contato da pessoa |
| `InscricaoSuframa` | string |  | Inscrição da pessoa no SUFRAMA |
| `NaturezaPessoa` | integer (int32) |  | Natureza da pessoa |
| `OptanteSimples` | boolean |  | Define se a pessoa é optante simples |
| `CodigoANS` | string |  | Codigo Agencia Ncional de Saude da pessoa |

### UAUApi.Models.Pessoas.ConsultarPessoasPorCondicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `condicaoConsultarPessoa` | string |  | Condição WHERE que será usada para consultar pessoas  Ex: cod_pes = 1855     cpf_pes = '13113131313331' AND nome_pes LIKE 'GLOBALTEC%' obs.: Devem ser passado as aspas simples para campos string. |

### UAUApi.Models.Pessoas.ConsultarPessoasFuncionariosAtivosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Page` | integer (int32) |  |  |
| `PageSize` | integer (int32) |  |  |
| `SearchText` | string |  |  |

### UAUApi.Models.Pessoas.ConsultarPessoaPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_pessoa` | integer (int32) |  | Código da pessoa |

### UAUApi.Models.Pessoas.ConsultarEnderecoPessoasPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoPessoa` | integer (int32) | ✓ | Número do código da pessoa |
| `tipoEndereco` | integer (int32) | ✓ | Tipo de endereço: 0 - Endereço Principal, 1 - Endereço Cobrança, 2 - Endereço Comercial |

### UAUApi.Models.Pessoa.Pessoa

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoPessoa` | integer (int32) |  | Código da pessoa |
| `nomePessoa` | string |  | Descrição da pessoa |
| `tipo` | integer (int32) |  | Define o tipo da pessoa 0 - Pessoa Física; 1 - Pessoa Jurídica; |
| `cpfCnpj` | string |  | cpf ou cnpj da pessoa |
| `dataDeCadastro` | string (date-time) |  | Data de cadastro da pessoa no sistema |
| `dataDeNascimento` | string (date-time) |  | Data de nascimento da pessoa |
| `pessoaInterna` | integer (int32) |  | Define se a pessoa é interna ou externo 1 - Interno; 2 - Externo; |
| `usuarioCadastro` | string |  | Usuário que cadastrou a pessoa no sistema |
| `usuarioAlteracao` | string |  | Usuário que alterou os dados da pessoa no sistema |
| `status` | integer (int32) |  | Status da pessoa no sistema 1 - Temporário; 2 - Confirmado; |
| `tratamentoPessoa` | string |  | Define como será o tratamento com a pessoa Ex: Sr(ª), Dr(ª) |
| `email` | string |  | E-mail da pessoa |
| `enderecoURL` | string |  | Endereço URL cadastrado para a pessoa |
| `matricula` | string |  | Matricula da pessoa caso seja funcionário |
| `pessoaAtiva` | integer (int32) |  | Define se a pessoa está ativo ou inativo. 0 - Ativo; 1 - Inativo; |
| `dataDeAlteracao` | string (date-time) |  | Data que os dados da pessoa foram alterados |
| `nomeFantasia` | string |  | Nome fantasia da pessoa |
| `anexos` | integer (int32) |  | Exibe os anexos vinculados a pessoa |
| `inscricaoMunicipal` | string |  | Código da inscrição municipal da pessoa |
| `inscricaoEstadual` | string |  | Código da inscrição estadual da pessoa |
| `loguinUauWeb` | string |  | Login usado para a pessoa acessar o UauWeb como fornecedor. |
| `senhaUauWeb` | string |  | Senha que será usada para acessa o UauWeb como fornecedor |
| `codigoAtividade` | string |  | É o código que define a atividade econômica da empresa |
| `dataCadastroPortal` | string (date-time) |  | Registra a data de primeiro cadastrado no portal |
| `cadastradoPrefeituraGoiania` | boolean |  | Define se a pessoa está cadastrada na prefeitura de Goiânia |
| `habilitadoRiscoSacado` | boolean |  | Habilitado para risco sacado |
| `cei` | string |  | Número CEI da pessoa |
| `dadosBancarios` | array de [`UAUApi.Models.Pessoa.PessoaBanco`](#uauapimodelspessoapessoabanco) |  | Dados bancários da pessoa |
| `enderecos` | array de [`UAUApi.Models.Pessoa.pessoaEndereco`](#uauapimodelspessoapessoaendereco) |  | Endereços da pessoa |
| `dadosPessoaFisica` | array de [`UAUApi.Models.Pessoa.PessoaFisica`](#uauapimodelspessoapessoafisica) |  | Dados da Pessoa Física |
| `dadosPessoaJuridica` | array de [`UAUApi.Models.Pessoa.PessoaJuridica`](#uauapimodelspessoapessoajuridica) |  | Dados da Pessoa Jurídica |
| `documentos` | array de [`UAUApi.Models.Pessoa.PessoasDocumento`](#uauapimodelspessoapessoasdocumento) |  | Documentos da pessoa |
| `telefones` | array de [`UAUApi.Models.Pessoa.PessoaTelefone`](#uauapimodelspessoapessoatelefone) |  | Telefones da pessoa |

### UAUApi.Models.Pessoa.PessoaTelefone

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero` | string |  | Número da pessoa |
| `ddd` | string |  | DDD do número da pessoa |
| `Complemento` | string |  | Complemento do telefone da pessoa |
| `tipo` | integer (int32) |  | Tipo de contato. 0 - Residencial, 1 - Comercial, 2 - Celular, 3 - Recado, 4 - Fax, 5 - Bip, 6 - Telex, 7 - Outros, 8 - Fone/Fax |

### UAUApi.Models.Pessoa.PessoasDocumento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoDocumento` | integer (int32) |  | Tipo do documento apresentado. 1 - Registro Geral (RG), 2 - Registro Único de Identificação, 3 - Registro em Órgãos de Classe, 4 -  Carteira Nacional de Habilitação, 5 - Título de Eleitor, 6 - Certidão Militar, 7 - Número de Identificação Fiscal, 8 - Registro do Auditor Independente |
| `numeroRegistroDocumento` | string |  | Número de registro do documento apresentado |
| `orgaoEmissor` | string |  | Órgão de emissão do documento |
| `codigoNacao` | string |  | Código da nação. EX: BRA |
| `ufDocumento` | string |  | Unidade Federativa do documento |
| `dataEmissaoDocumento` | string (date-time) |  | Data de emissão do documento |
| `dataValidade` | string (date-time) |  | Data de validade do documento |
| `categoria` | string |  | Categoria da CNH da pessoa |
| `zonaEleitoral` | string |  | Zona eleitoral da pessoa |
| `secaoEleitoral` | string |  | Número da seção eleitoral da pessoa |
| `entidadeDeClasse` | integer (int32) |  | Tipo de entidade de classe. 1 - Administração, 2 - Advocacia, 3 - Biologia, 4 -  Biomedicina, 5 - Contabilidade, 6 - Economia, 7 - Educação física, 8 - enfermagem, 9 - Engenharia, 10 - Farmácia, 11 - Fisioterapia, 12 - Medicina, 13 - Medicina Veterinária, 15 - Nutrição, 16 - Odontologia, 17 - Psicologia, 18 - Química, 19 - Serviço Social |
| `sequencialConselho` | string |  | Número sequencial do conselho |
| `dataAlteracao` | string (date-time) |  | Data de alteração do cadastro do documento |
| `usuarioAlteracao` | string |  | Usuário da alteração do cadastro do documento |

### UAUApi.Models.Pessoa.PessoaJuridica

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `contato` | string |  | Contato 1 da pessoa jurídica |
| `contato2` | string |  | Contato 2 da pessoa jurídica |
| `inscricaoSuframa` | string |  | Código de inscrição da Superintendência da Zona Franca de Manaus |
| `naturezaJuridica` | integer (int32) |  | 1 - Órgão, Autarquia ou Fundação Federal, 2 - Entidade da Administração Pública Federal, 3 - Pessoa Jurídica de Direito Privado, 4 - Sociedade Cooperativa, 5 - Fabricante de Máquinas de Veículos |
| `optanteSimples` | boolean |  | Optante do simples |
| `registroAns` | string |  | Número de Registro da Agência Nacional de Saúde Suplementar |

### UAUApi.Models.Pessoa.PessoaFisica

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `lotacao` | string |  | Órgão, Despertamento ou seção da lotação |
| `cargo` | string |  | Cargo da pessoa |
| `dataAdmissão` | string (date-time) |  | Data de admissão da pessoa |
| `correspondencia` | integer (int32) |  | Tipo de correspondência, 0 - Residencial, 1 - Comercial, 2 - Nenhum |
| `estadoCivil` | integer (int32) |  | Estado Civil da pessoa. 0 - Solteiro, 1 - Casado, 2 - Divorciado, 3 - Desquitado, 4 - Separado, 5 - Viúvo, 6 - Outros |
| `numeroDocumento` | string |  | Número do documento da pessoa |
| `tipoDocumento` | string |  | Tipo de documento da pessoa |
| `dataDocumento` | string (date-time) |  | Data do documento da pessoa |
| `sexo` | integer (int32) |  | Sexo da pessoa. M - Masculino, F - Feminino |
| `nacionalidade` | string |  | Nacionalidade da pessoa |
| `numeroDependentes` | integer (int32) |  | Quantidade de dependentes da pessoa |
| `nomePai` | string |  | Nome do pai |
| `dataNascimentoPai` | string (date-time) |  | Data de nascimento do pai |
| `nomeMae` | string |  | Nome da mãe |
| `dataNascimentoMae` | string (date-time) |  | Data de nascimento da mãe |
| `naturalidade` | string |  | Naturalidade da pessoa |
| `codigoNacao` | string |  | Código da nação. Ex: BRA, ARG. |
| `grauInstrucao` | string |  | Grau de instrução da pessoa. Ex: Doutorado Completo, Ensino médio completo |
| `codigoRaça` | string |  | Raça da pessoa. EX: Branco, indígena. |
| `codigoSituacaoMilitar` | string |  | Código da situação militar |
| `ufNascimento` | string |  | UF de Nascimento da pessoa |
| `cidadeNatal` | integer (int32) |  | Cidade natal |
| `fatorRh` | string |  | Fator RH |
| `regimeCasamento` | integer (int32) |  | Regime de casamento da pessoa. |
| `numeroCDI` | string |  | Número do Certificado de Dispensa da Incorporação |
| `numeroProfissao` | integer (int32) |  | Número da profissão |
| `uniaoEstavel` | boolean |  | União estável. 0 - Não, 1 - Sim |
| `detalheNacionalidade` | integer (int32) |  | Detalhe da nacionalidade da pessoa. 0 - Estrangeiro, 1 - Brasileiro Nato, 2 - Brasileiro Naturalizado, 3 - Brasileiro nascido no exterior |
| `codigoNacaoOrigem` | string |  | Código da origem da nação |
| `codigoMunicipioNascimento` | integer (int32) |  | Código do município de nascimento da pessoa |
| `indicativoFiscal` | integer (int32) |  | 1 - Beneficiário com NIF, 2 - Beneficiário Dispensado do NIF, 3 - País não exige NIF |
| `codigoFormaTributacao` | string |  | Código da forma de tributação   10 Retenção do IRRF - alíquota padrão.   11 Retenção do IRRF - alíquota da tabela progressiva.   12 Retenção do IRRF - alíquota diferenciada (países com tributação favorecida ou regime fiscal privilegiado).   13 Retenção do IRRF - alíquota limitada conforme cláusula em ADT.   30 Retenção do IRRF - outras hipóteses.   40 Não retenção do IRRF - isenção estabelecida em ADT.   41 Não retenção do IRRF - isenção prevista em lei interna   42 Não retenção do IRRF - alíquota de 0% (zero por cento) prevista em lei interna   43 Não retenção do IRRF - pagamento antecipado do imposto   44 Não retenção do IRRF - medida Judicial   50 Não retenção do IRRF - outras hipóteses |
| `renda` | number (double) |  | Renda da Pessoa |
| `moeda` | string |  | Moeda da Renda |

### UAUApi.Models.Pessoa.pessoaEndereco

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoEndereco` | integer (int32) |  | Tipo do endereço.  0 - Principal, 1 - Cobrança, 2 - Comercial |
| `endereco` | string |  | Endereço da pessoa |
| `bairro` | string |  | Bairro da pessoa |
| `cidade` | string |  | Cidade da pessoa |
| `uf` | string |  | Unidade Federativa da pessoa |
| `cep` | string |  | CEP da pessoa |
| `numeroEndereco` | string |  | Número do endereço da pessoa |
| `complementoEndereco` | string |  | Complemento do endereço da pessoa |
| `referencia` | string |  | Referência do endereço da pessoa |
| `imovelProprio` | integer (int32) |  | Imóvel próprio. 0 - Não, 1 - Sim |
| `numeroCidade` | integer (int32) |  | Número da cidade |
| `numeroBairro` | integer (int32) |  | Número da cidade |
| `numeroLogradouro` | integer (int32) |  | Número do logradouro |
| `codigoEmpresa` | integer (int32) |  | Código da empresa da pessoa |
| `nomeEmpresa` | string |  | Nome da empresa da pessoa |
| `tipoEnderecoEmpresa` | integer (int32) |  | Tipo do endereço da empresa da pessoa. 0 - Empresa não cadastrada, 1 - Empresa cadastrada |

### UAUApi.Models.Pessoa.PessoaBanco

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `banco` | integer (int32) |  | Banco |
| `conta` | string |  | Conta (Ex. 10200-3) |
| `padrao` | boolean |  | Conta padrão (true para sim e False para não) |
| `tipo` | integer (int32) |  | Tipo da conta (0 - Conta Corrente, 1 - Conta Poupança, 2 - Conta FGTS, 3 - Conta Salário) |
| `agencia` | string |  | Agência |
| `debitoAutomatico` | boolean |  | Débito automático (true para sim e false para não) |
| `nomeAgencia` | string |  | Nome da agência |

### UAUApi.Models.Pessoas.ConsultarPessoasPorCPFCNPJRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cpf_cnpj` | string | ✓ | Número do CPF/CNPJ - SOMENTE NÚMEROS |
| `status` | integer (int32) — valores possíveis: 0, 1, 2 | ✓ | Status 0-Ativos 1-Inativos 2-Ambos |

### UAUApi.Models.Pessoas.ConsultarDadosPessoaFisicaPorCodigoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigopessoa_fis` | integer (int32) |  | Código da pessoa física |

### UAUApi.Models.Pessoas.ConsultarDadosAdicionaisPessoaPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_pessoa` | integer (int32) | ✓ | Código da pessoa |

### UAUApi.Models.Pessoas.GravarContaBancariaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoPessoa` | integer (int32) | ✓ | Código da pessoa |
| `banco` | integer (int32) | ✓ | Banco |
| `conta` | string | ✓ | Conta (Ex. 10200-3) |
| `padrao` | boolean |  | Conta padrão (true para sim e false para não) |
| `tipo` | integer (int32) | ✓ | Tipo da conta (0 - Conta Corrente, 1 - Conta Poupança, 2 - Conta FGTS ou 3 - Conta Salário) |
| `agencia` | string | ✓ | Agência |
| `nomeAgencia` | string |  | Nome da agência |
| `debitoAutomatico` | boolean |  | Débito automático (true para sim e false para não) |

### UAUApi.Models.Pessoas.ConsultarContasBancariasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo` | string | ✓ | Código da pessoa |

### UAUApi.Models.Pessoas.AlterarSenhaClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_cliente` | integer (int32) | ✓ | Código do cliente |
| `senha` | string | ✓ | Senha do cliente |

### UAUApi.Models.Pessoas.AlterarPessoaAcessoPortalRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_pessoa` | integer (int32) | ✓ | Código da pessoa |
| `login` | string |  | Login de acesso ao Uau Web |
| `senha` | string |  | Senha de acesso |
| `email` | string |  | Endereço de email |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Pessoa.RequestAlterarContaPadrao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoPessoa` | integer (int32) | ✓ | Código da pessoa |
| `CodigoBanco` | integer (int32) | ✓ | Código do banco |
| `Agencia` | string | ✓ | Numero da agência |
| `Conta` | string | ✓ | Conta |
