# Funcionario

## POST `/api/v{version}/Funcionario/ConsultarFuncionario`

**Objetivo: Consultar os dados de funcionários do UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar os dados dos funcionários URI + api/v{version:apiVersion}/Funcionario/ConsultarFuncionario
3. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Consulta os dados de funcionários do UAU, podendo fazer filtros pela empresa, obra, pessoa, funcionário, matrícula e situação.
1. Deve informar obrigatoriamente o código da empresa.
2. Pode informar opcionalmente o código da obra, pessoa, funcionário, matrícula e situação.

VirtUau:
-  Link para Virtuau relacionado:https://ajuda.globaltec.com.br/virtuau/cadastro-de-funcionarios/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Funcionario.ConsultarFuncionarioRequest`](#uauapimodelsfuncionarioconsultarfuncionariorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Funcionario.FuncionarioDTO`](#uauapimodelsfuncionariofuncionariodto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Funcionario.FuncionarioDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoEmpresa` | integer (int32) | ✓ | Código da empresa de lotação do funcionário. |
| `NomeEmpresa` | string | ✓ | Nome da empresa de lotação do funcionário. |
| `CnpjEmpresa` | string | ✓ | CNPJ da empresa de lotação do funcionário. |
| `CodigoObra` | string | ✓ | Código da obra de lotação do funcionário. |
| `NomeObra` | string | ✓ | Nome da Obra de lotação do funcionário. |
| `CNOObra` | string |  | CNO da Obra de lotação do funcionário (No caso de Obras com o CNO próprio). |
| `CodigoPessoa` | integer (int32) | ✓ | Código do cadastro de pessoas. |
| `CodigoFuncionario` | integer (int32) | ✓ | Controle interno (NumCap). |
| `NomeFuncionario` | string | ✓ | Nome do funcionário. |
| `Matricula` | string | ✓ | Matrícula do funcionário. |
| `DtNascimento` | string (date-time) | ✓ | Data de nascimento |
| `Sexo` | integer (int32) | ✓ | Sexo do funcionário    [0 - Masculino, 1 - Feminino] |
| `EstadoCivil` | integer (int32) | ✓ | Estado civil |
| `CPF` | string | ✓ | CPF do funcionário |
| `NIS` | string |  | Número de Identificação Social - NIS ou PIS |
| `RG` | string |  | RG do funcionário |
| `UfRG` | string |  | UF do RG |
| `RGOrgaoEmissor` | string |  | Órgão emissor do Funcionário |
| `CTPS` | string |  | Número da CTPS |
| `SerieCTPS` | string |  | Número de série da CTPS. |
| `UFCTPS` | string |  | UF da expedição da CTPS. |
| `Endereco` | string |  | Endereço do funcionário |
| `Bairro` | string |  | Bairro do funcionário |
| `Municipio` | string |  | Código do município do endereço do funcionário |
| `Estado` | string |  | Estado do funcionário |
| `CEP` | string |  | CEP do funcionário |
| `Telefone` | string |  | Telefone do funcionário |
| `Nacionalidade` | string | ✓ | Nacionalidade do funcionário |
| `Naturalidade` | string | ✓ | Naturalidade do funcionário (Código do município) |
| `RacaCor` | string | ✓ | Raça e cor do funcionário |
| `Email` | string |  | E-mail do funcionário |
| `NomeDaMae` | string |  | Nome da mãe do Funcionário |
| `DataEmissaoCtps` | string (date-time) |  | Data de emissão da CTPS |
| `GrauInstrucao` | string |  | Grau de instrução do Funcionário |
| `DtAdmissao` | string (date-time) | ✓ | Data de admissão |
| `CBO` | string | ✓ | CBO do funcionário |
| `CodigoDepartamento` | string |  | Código do departamento |
| `NomeDepartamento` | string |  | Nome do departamento |
| `CodigoCargo` | string | ✓ | Código do cargo |
| `NomeCargo` | string | ✓ | Nome do cargo |
| `CodigoFuncao` | integer (int32) |  | Função do funcionário |
| `NomeFuncao` | string |  | Nome da função do funcionário |
| `CodigoSindicato` | string |  | Nome do sindicato do funcionário |
| `NomeSindicato` | string |  | Nome do sindicato do funcionário |
| `ContribuiINSS` | integer (int32) |  | Funcionário contribui com INSS |
| `Situacao` | string | ✓ | Código da situação do funcionário.   [0 - Ativo, 1 - Demitido, 2 - Doente, 3 - Licenciado, 4 - Outros, 5 - Em demissão, 6 - Em férias, 7 - Resc.Complementar, 8 - Término de Vínculo] |
| `DtDemissao` | string (date-time) |  | Retornará valor se o funcionário estiver demitido |
| `Categoria` | string | ✓ | Categorias de Trabalhadores conforme códigos do eSocial cadastrados. |
| `TipoContrato` | integer (int32) |  | Tipo do contrato |
| `TerminoContrato` | string (date-time) |  | Data de término do contrato |
| `ClausulaAssecuratoria` | integer (int32) |  | Possui cláusula assecuratória no contrato |
| `ObjetoDeterminante` | string |  | Objeto determinante do contrato |
| `RegTrabalhista` | integer (int32) |  | Tipo de regime trabalhista |
| `RegPrevidencia` | integer (int32) |  | Tipo de regime previdenciário |
| `TipoAdmissao` | integer (int32) |  | Tipo de admissão do funcionário |
| `IndicativoAdmissao` | integer (int32) |  | Indicativo do tipo de admissão do funcionário |
| `NaturezaAtividade` | integer (int32) |  | Natureza da atividade |
| `InstituicaoEnsino` | integer (int32) |  | Instituição de ensino |
| `CNPJInstituicaoEnsino` | string |  | CNPJ da instituição de ensino |
| `NaturezaEstagio` | integer (int32) |  | Natureza do Estágio |
| `TerminoEstagio` | string (date-time) |  | Data do término do estágio |
| `NivelEstagio` | integer (int32) |  | Nível do estágio |
| `MotivoContratacao` | integer (int32) |  | Motivo da contratação (Hipótese legal) |
| `TipoInclusao` | integer (int32) |  | Tipo de inclusão de contrato |
| `CPFSubstituido` | string |  | CPF do trabalhador substituído |
| `JustificativaContratacao` | string |  | Descrição da justificativa da contratação (Hipótese legal) |
| `JustificativaProrrogacao` | string |  | Descrição da justificativa da prorrogação (Hipótese legal) |
| `HorasMensais` | string | ✓ | Quantidade de horas trabalhadas no mês |
| `HorasSemanais` | integer (int32) | ✓ | Quantidade de horas trabalhadas na semana |
| `TipoDeSalario` | integer (int32) | ✓ | Tipo de salário do funcionário |
| `SalarioFuncionario` | number (double) | ✓ | Salário  do funcionário |
| `CodigoEmpresaPagto` | integer (int32) | ✓ | Código da empresa de pagamento do funcionário |
| `CodigoObraPagto` | string | ✓ | Código da Obra de pagamento do funcionário |

### UAUApi.Models.Funcionario.ConsultarFuncionarioRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoEmpresa` | integer (int32) | ✓ | Código da empresa de lotação do funcionário. |
| `CodigoObra` | string |  | Código da obra de lotação do funcionário. |
| `CodigoPessoa` | integer (int32) |  | Código do cadastro de pessoas. |
| `CodigoFuncionario` | integer (int32) |  | Controle interno (NumCap). |
| `Matricula` | string |  | Matrícula do funcionário. |
| `Situacao` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5, 6, 7, 8 |  | Código da situação do funcionário.   [0 - Ativo, 1 - Demitido, 2 - Doente, 3 - Licenciado, 4 - Outros, 5 - Em demissão, 6 - Em férias, 7 - Resc.Complementar, 8 - Término de Vínculo] |
