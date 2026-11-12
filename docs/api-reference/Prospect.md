# Prospect

## POST `/api/v{version}/Prospect/AlterarResponsavelProspect`

**Alterar responsável do prospect**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Alterar responsável do prospect.
2. Os dados informados passam por validações.
3. O campo codEmpresa não é obrigatório, porém, se informado será validado se na configuração da empresa está marcado para 
"Realizar venda somente se o vendedor estiver em uma estrutura de comissão", e caso o novo responsável não esteja em nenhuma
estrutura de comissão, não será possível incluir. Caso não esteja marcado a configuração ou o codEmpresa não for informado,
será possível alterar para qualquer novo responsável, desde que esteja ativo.

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
Esquema: [`UAUApi.Models.Prospect.AlterarResponsavelProspect`](#uauapimodelsprospectalterarresponsavelprospect)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Prospect/BuscarGrauParentescoPorCodigo`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.GrauParentesco.ConsultarGrauParentescoPorChave`](#uauapimodelsgrauparentescoconsultargrauparentescoporchave)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Prospect/ConsultarProspectComFiltro`

**Consulta prospect de acordo com as informações do request**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta prospect filtrando os parâmentros inseridos da request.

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
Esquema: [`UAUApi.Models.Prospect.ConsultarProspectComFiltroRequest`](#uauapimodelsprospectconsultarprospectcomfiltrorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Prospect/ConsultarProspectPorChave`

**Consultar prospect por código**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta determinado prospect filtrando pelo número deste prospect.

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
Esquema: [`UAUApi.Models.Prospect.ConsultarProspectPorChaveRequest`](#uauapimodelsprospectconsultarprospectporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Prospect.ConsultarDadosProspect`](#uauapimodelsprospectconsultardadosprospect) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Prospect/ConsultarTodosProspects`

**Consultar todos os prospects**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta os prospects de acordo com os parâmetros definidos na request.

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
Esquema: [`UAUApi.Models.Prospect.ConsultarTodosProspectsRequest`](#uauapimodelsprospectconsultartodosprospectsrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Prospect.ProspectResponsavel`](#uauapimodelsprospectprospectresponsavel) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Prospect/GravarProspect`

**Grava as informações do prospect**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Grava as informações do prospect.
2. Os dados informados passam por validações.

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
Esquema: [`UAUApi.Models.Prospect.GravarProspectRequest`](#uauapimodelsprospectgravarprospectrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Prospect/ImportarProspect`

**Realiza a importação de prospects para o UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Importa prospects para dentro do UAU.
2. Valida usuário e permissões.
3. Valida arquivo XML.

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
Esquema: [`UAUApi.Models.Prospect.ImportarProspectRequest`](#uauapimodelsprospectimportarprospectrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Prospect/ListarGrauParentesco`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Prospect/MigrarProspectPessoa`

**Realiza a migração dos dados do prospect para pessoa**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Migra um prospect para pessoa.

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
Esquema: [`UAUApi.Models.Prospect.MigrarProspectPessoaRequest`](#uauapimodelsprospectmigrarprospectpessoarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Prospect.ProspectMigrarPessoa`](#uauapimodelsprospectprospectmigrarpessoa) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Prospect.ProspectMigrarPessoa

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroPessoa` | integer (int32) |  | Número da pessoa que o prospect originou. |
| `mensagemRetorno` | string |  | Validação que impediu a migração do prospect |
| `validouDependentes` | boolean |  | Indica se validou dependente ou não. |

### UAUApi.Models.Prospect.MigrarProspectPessoaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroProspect` | integer (int32) | ✓ | Número do prospect. |

### UAUApi.Models.Prospect.ImportarProspectRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `xml` | string | ✓ | Arquivo XML com os dados a serem importados. |

### UAUApi.Models.Prospect.GravarProspectRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `permitirResponsavelSemEstrutura` | boolean |  | Indica se deve permitir o responsável não estar em uma estrutura de comissão |
| `login` | string |  | Login do usuário logado |
| `prospect` | [`UAUApi.Models.Prospect.Prospect`](#uauapimodelsprospectprospect) |  | Dados do prospect |
| `prospectFis` | [`UAUApi.Models.Prospect.ProspectFis`](#uauapimodelsprospectprospectfis) |  | Dados adicionais do prospect |
| `prospectInteresse` | [`UAUApi.Models.Prospect.ProspectInteresse`](#uauapimodelsprospectprospectinteresse) |  | Dados dos interesses (pretensões) do prospect |
| `prospectInteresseProdutos` | array de [`UAUApi.Models.Prospect.ProspectInteresseProduto`](#uauapimodelsprospectprospectinteresseproduto) |  | Dados dos produtos dos interesses (pretensões) do prospect |
| `prospectInteresseBairros` | array de [`UAUApi.Models.Prospect.ProspectInteresseBairro`](#uauapimodelsprospectprospectinteressebairro) |  | Dados dos bairros dos interesses (pretensões) do prospect |
| `prospectTelefones` | array de [`UAUApi.Models.Prospect.ProspectTelefone`](#uauapimodelsprospectprospecttelefone) |  | Dados dos telefones do prospect |
| `prospectEnderecoPrincipal` | [`UAUApi.Models.Prospect.ProspectEndereco`](#uauapimodelsprospectprospectendereco) |  | Dados do endereço principal do prospect |
| `prospectEnderecoCobranca` | [`UAUApi.Models.Prospect.ProspectEndereco`](#uauapimodelsprospectprospectendereco) |  | Dados do endereço de cobrança do prospect |
| `prospectEnderecoComercial` | [`UAUApi.Models.Prospect.ProspectEndereco`](#uauapimodelsprospectprospectendereco) |  | Dados do endereço comercial do prospect |
| `prospectDependente` | array de [`UAUApi.Models.Prospect.ProspectDependente`](#uauapimodelsprospectprospectdependente) |  | Lista de dependentes do prospect |
| `responsavel` | string |  | Nome do Responsável pelo prospect |
| `buscouDePessoas` | boolean |  | Indica se buscou os dados de pessoas |
| `atualizarPessoas` | boolean |  | Indica se irá atualizar os dados de pessoas |
| `mensagemRetorno` | string |  | Mensagem de retorno |
| `prospectDoc` | array de [`UAUApi.Models.Prospect.ProspectDoc`](#uauapimodelsprospectprospectdoc) |  | Lista de documentos do prospect |

### UAUApi.Models.Prospect.ProspectDoc

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoProspect` | integer (int32) | ✓ | tipo de documento: 1 - Identidade, 2 - RIC - Registro Único de Identificação, 3 - OC - Órgão de Classe, 4 - CNH - Carteira Nacional de Habilitação |
| `registro` | string | ✓ | nº de registro do documento |
| `orgaoEmissor` | string |  | órgão emissor: RG, RIC, OC, CNH |
| `codigoNacao` | string |  | código da nação que a UF pertence |
| `UF` | string |  | UF do documento |
| `dataCadastro` | string (date-time) |  | data da emissão do RG data da expedição (RIC, OC, CNH) |
| `dataValidade` | string (date-time) |  | data da validade do documento |
| `usuarioAlterou` | string | ✓ | usuário que cadastrou/alterou o registro. |

### UAUApi.Models.Prospect.ProspectDependente

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numProspect` | integer (int32) |  | número do prospect |
| `numDependente` | integer (int32) |  | número do dependente |
| `dataCasamento` | string (date-time) |  | data do casamento, se o dependente for um cônjugue |
| `cartorio` | string |  | nome do cartório onde foi feito o registro |
| `usuarioCadastrou` | string |  | usuário que cadastrou o dependente |
| `codGrauParentesco` | integer (int32) |  | código do grau de parentesco. 1 - Cônjuge |
| `dataCadastro` | string (date-time) |  | data de cadastro do dependente |

### UAUApi.Models.Prospect.ProspectEndereco

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroProspect` | integer (int32) |  | Número do prospect |
| `tipoEndereco` | integer (int32) |  | Tipo do endereço:     0 - Principal     1 - Cobrança     2 - Comercial |
| `logradouro` | string |  | Logradouro |
| `bairro` | string |  | Bairro |
| `cidade` | string |  | Cidade |
| `uf` | string |  | Código da UF |
| `cep` | string |  | Número do CEP |
| `numero` | string |  | Número do endereço |
| `complemento` | string |  | Complemento |
| `referencia` | string |  | Referência |
| `enderecoProprio` | integer (int32) |  | Prospect possui endereço próprio:     0 - Não     1 - Sim |
| `numeroCidade` | integer (int32) |  | Número da cidade |
| `numeroBairro` | integer (int32) |  | Número do bairro |
| `numeroLogradouro` | integer (int32) |  | Número do logradouro |
| `codigoEmpresa` | integer (int32) |  | Código da empresa |
| `nomeEmpresa` | string |  | Nome da empresa |
| `empresaEstaCadastrada` | integer (int32) |  | Indica se irá usar o endereço comercial de uma empresa cadastrada:     0 - Não     1 - Sim |

### UAUApi.Models.Prospect.ProspectTelefone

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ddd` | string |  | Número do DDD do telefone |
| `telefone` | string |  | Número do telefone |
| `complemento` | string |  | Complemento do telefone |
| `tipoTelefone` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5, 6, 7, 8 |  | Tipo do telefone:     0 - Residencial     1 - Comercial     2 - Celular     3 - Recado     4 - Fax     5 - Bip     6 - Telex     7 - Outros     8 - Fone/Fax |
| `principal` | boolean |  | Telefone principal:     False - Não     True - Sim |

### UAUApi.Models.Prospect.ProspectInteresseBairro

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroProspect` | integer (int32) |  | Número do prospect |
| `numeroInteresse` | integer (int32) |  | Número do interesse(pretensão) |
| `numeroInteresseBairro` | integer (int32) |  | Número do interesse(pretensão) do bairro (controle) |
| `numeroCidade` | integer (int32) |  | Número da cidade do interesse(pretensão) |
| `numeroBairro` | integer (int32) |  | Número do bairro do interesse(pretensão) |

### UAUApi.Models.Prospect.ProspectInteresseProduto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroProduto` | integer (int32) |  | Número do produto do interesse(pretensão) |
| `numeroProspect` | integer (int32) |  | Número do prospect |
| `numeroInteresse` | integer (int32) |  | Número do interesse(pretensão) |

### UAUApi.Models.Prospect.ProspectInteresse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroInteresse` | integer (int32) |  | Número do interesse(pretensão) do prospect |
| `numeroProspect` | integer (int32) |  | Número do prospect |
| `faixaPrecoInicial` | number (double) |  | Faixa de preço inicial do interesse(pretensão) |
| `faixaPrecoFinal` | number (double) |  | Faixa de preço final interesse(pretensão) |
| `interessadoEm` | integer (int32) |  | Interesse(pretensão) do prospect:     0 - Lançamento/Venda     1 - Aluguel     2 - Revenda |
| `usuarioCadastro` | string |  | Usuário que cadastrou o interesse(pretensão) do prospect |
| `dataCadastro` | string (date-time) |  | Usuário que cadastrou o interesse(pretensão) do prospect |
| `anexos` | integer (int32) |  | Tipos do anexo (Caso possua mais de um anexo, o valor deverá ser a combinação dos tipos):     1 - Cometário     2 - Pendência     4 - Arquivos     8 - Questionário     16 - Ocorrência |
| `observacao` | string |  | Observação |
| `usuarioQueAlterouStatus` | string |  | Usuário que alterou o status |
| `dataQueAlterouStatus` | string (date-time) |  | Data que alterou o status |
| `status` | integer (int32) |  | Status do interesse(pretensão):      0 - Aberto     1 - Atendido     2 - Cancelado     3 - Não atendido     4 - Desistência |
| `qtdeDeQuartos` | integer (int32) |  | Quantidade de quartos do interesse(pretensão) |
| `qtdeDeSuites` | integer (int32) |  | Quantidade de suítes do interesse(pretensão) |
| `qtdeDeGaragens` | integer (int32) |  | Quantidade de garagens do interesse(pretensão) |

### UAUApi.Models.Prospect.ProspectFis

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroProspect` | integer (int32) |  | Número do prospect |
| `sexo` | integer (int32) |  | Sexo do prospect:     0 - Masculino     1 - Feminino |
| `estadoCivil` | integer (int32) |  | Estado civil do prospect:     0 - Separado     1 - Solteiro     2 - Casado     3 - Desquitado     4 - Viúvo     5 - Divorciado     6 - Outros |
| `regimeDeBens` | integer (int32) |  | Regime de bens do prospect:     0 - Comunhão parcial de bens     1 - Comunhão total de bens     2 - Separação total de bens     3 - Participação final nos aquestos |
| `nomeMae` | string |  | Nome da mãe do prospect |
| `nomePai` | string |  | Nome do pai do prospect |
| `numeroProfissao` | integer (int32) |  | Número da profissão do prospect |
| `valorRenda` | number (double) |  | Valor da renda do prospect |
| `moedaRenda` | string |  | Código da moeda da renda do prospect |
| `cargo` | string |  | Cargo do prospect |
| `codigoNacionalidade` | string |  | Código da nacionalidade do prospect |
| `referenciaPessoal1` | string |  | Referência pessoal 1 do prospect |
| `referenciaPessoal1DDD` | string |  | DDD da referência pessoal 1 do prospect |
| `referenciaPessoal1Telefone` | string |  | Telefone da referência pessoal 1 do prospect |
| `referenciaPessoal2` | string |  | Referência pessoal 2 do prospect |
| `referenciaPessoal2DDD` | string |  | DDD da referência pessoal 2 do prospect |
| `referenciaPessoal2Telefone` | string |  | Telefone da referência pessoal 2 do prospect |
| `numeroNaturalidade` | integer (int32) |  | Número da naturalidade do prospect |
| `uniaoEstavel` | boolean |  | União estável do prospect:     false - Não     true - Sim |

### UAUApi.Models.Prospect.Prospect

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroProspect` | integer (int32) |  | Número do prospect |
| `nomeProspect` | string |  | Nome do prospect |
| `naturezaJuridica` | integer (int32) |  | Natureza jurídica do prospect:      0 - Física     1 - Jurídica |
| `cpfCnpj` | string |  | CPF ou CPNJ do prospect |
| `dataCadastro` | string (date-time) |  | Data de cadastro do prospect |
| `usuarioCadastro` | string |  | Usuário que cadastrou o prospect |
| `dataNascimento` | string (date-time) |  | Data de nascimento do prospect |
| `email` | string |  | Email do prospect |
| `canalComunicacao` | integer (int32) |  | Código do canal de comunicação com o prospect |
| `numeroResponsavel` | integer (int32) |  | Número do responsável pelo prospect |
| `numeroCliente` | integer (int32) |  | Número da pessoa vinculada ao prospect |
| `contato` | string |  | Contato |
| `anexo` | integer (int32) |  | Tipos do anexo (Caso possua mais de um anexo, o valor deverá ser a combinação dos tipos):     1 - Comentário     2 - Pendência     4 - Arquivos     8 - Questionário     16 - Ocorrência |
| `veiculoDivulgacao` | integer (int32) |  | Código do veículo de divulgação |
| `localAtendimento` | integer (int32) |  | Código do local de atendimento |

### UAUApi.Models.Prospect.ProspectResponsavel

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nomeResponsavel` | string |  | Nome do responsável |
| `numeroProspect` | integer (int32) |  | Número do prospect |
| `nomeProspect` | string |  | Nome do prospect |
| `naturezaJuridica` | integer (int32) |  | Natureza jurídica do prospect:      0 - Física     1 - Jurídica |
| `cpfCnpj` | string |  | CPF ou CPNJ do prospect |
| `dataCadastro` | string (date-time) |  | Data de cadastro do prospect |
| `usuarioCadastro` | string |  | Usuário que cadastrou o prospect |
| `dataNascimento` | string (date-time) |  | Data de nascimento do prospect |
| `email` | string |  | Email do prospect |
| `canalComunicacao` | integer (int32) |  | Código do canal de comunicação com o prospect |
| `numeroResponsavel` | integer (int32) |  | Número do responsável pelo prospect |
| `numeroCliente` | integer (int32) |  | Número da pessoa vinculada ao prospect |
| `contato` | string |  | Contato |
| `anexo` | integer (int32) |  | Tipos do anexo (Caso possua mais de um anexo, o valor deverá ser a combinação dos tipos):     1 - Comentário     2 - Pendência     4 - Arquivos     8 - Questionário     16 - Ocorrência |
| `veiculoDivulgacao` | integer (int32) |  | Código do veículo de divulgação |
| `localAtendimento` | integer (int32) |  | Código do local de atendimento |

### UAUApi.Models.Prospect.ConsultarTodosProspectsRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `enumOpcaoTodos` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4 |  | Tipo de prospects 0 - Todos os prospects, 1 - Todos os prospects, exceto os prospects informados, 2 - Somente os prospects informados, 3 - Todos os prospects sem responsável e do responsável informado, 4 - Todos os prospects sem responsável e do responsável informado, exceto os prospects informados. |
| `codigoProspect` | string |  | Filtra pelo código do prospect |
| `codigoVendedor` | integer (int32) |  | Filtra pelo código do vendedor |

### UAUApi.Models.Prospect.ConsultarDadosProspect

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `prospect` | [`UAUApi.Models.Prospect.Prospect`](#uauapimodelsprospectprospect) |  |  |
| `prospectFis` | [`UAUApi.Models.Prospect.ProspectFis`](#uauapimodelsprospectprospectfis) |  |  |
| `prospectInteresses` | array de [`UAUApi.Models.Prospect.ProspectInteresse`](#uauapimodelsprospectprospectinteresse) |  |  |
| `prospectTelefones` | array de [`UAUApi.Models.Prospect.ProspectTelefone`](#uauapimodelsprospectprospecttelefone) |  |  |
| `prospectInteressesProdutos` | array de [`UAUApi.Models.Prospect.ProspectInteresseProduto`](#uauapimodelsprospectprospectinteresseproduto) |  |  |
| `prospectEnderecoPrincipal` | [`UAUApi.Models.Prospect.ProspectEndereco`](#uauapimodelsprospectprospectendereco) |  |  |
| `prospectEnderecoCobranca` | [`UAUApi.Models.Prospect.ProspectEndereco`](#uauapimodelsprospectprospectendereco) |  |  |
| `prospectEnderecoComercial` | [`UAUApi.Models.Prospect.ProspectEndereco`](#uauapimodelsprospectprospectendereco) |  |  |
| `prospectInteressesBairros` | array de [`UAUApi.Models.Prospect.ProspectInteresseBairro`](#uauapimodelsprospectprospectinteressebairro) |  |  |
| `prospectDependente` | array de [`UAUApi.Models.Prospect.ProspectDependente`](#uauapimodelsprospectprospectdependente) |  |  |
| `prospectDocumento` | array de [`UAUApi.Models.Prospect.ProspectDoc`](#uauapimodelsprospectprospectdoc) |  |  |

### UAUApi.Models.Prospect.ConsultarProspectPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoProspect` | integer (int32) | ✓ | Número do prospect |

### UAUApi.Models.Prospect.ConsultarProspectComFiltroRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroOpcao` | integer (int32) — valores possíveis: 0, 1, 2, 3 |  | Numero da operação do prospect (0= Hierarquia, 1= CodProspect, 2= NomeProspect, 3= CPFProspect) |
| `numeroVisao` | integer (int32) — valores possíveis: 0, 1, 2 |  | Status do do prospect (0= EmAndamento, 1= Encerrado, 2= Todos) |
| `prospectSemResponsavel` | boolean |  | Prospect com responsável = true. Prospect sem responsável = false |
| `codigoResponsavel` | string |  | Código do responsável |
| `nomePessoa` | string |  | Nome da pessoa |
| `telefone` | string |  | Telefone do prospect |
| `cpfCnpj` | string |  | CPF ou CNPJ do prospect |
| `trataSemResponsavel` | boolean |  | tratar com responsável = true. tratar sem responsável = false |
| `ufProsp` | string |  | UF (unidade da Federação) do prospect |

### UAUApi.Models.GrauParentesco.ConsultarGrauParentescoPorChave

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) | ✓ |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Prospect.AlterarResponsavelProspect

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `novoResponsavel` | integer (int32) | ✓ | Código do novo responsável do prospect. |
| `codEmpresa` | integer (int32) |  | código da empresa. |
| `numProspect` | integer (int32) | ✓ | Número do prospect. |
