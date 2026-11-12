# Folha

## POST `/api/v{version}/Folha/GravarAlocacaoMaoObra`

**Objetivo: Incluir/Alterar alocação de mão de obra para funcionários do UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método GravarAlocacaoMaoObra.

Definição de Negócio:
1. Efetua a inclusão ou alteração(caso o registro já exista) na alocação de mão de obra para funcionários do UAU.
2. Deve informar obrigatoriamente os campos:
  - Código da empresa de lotação do funcionário
  - Matrícula do funcionário
  - Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY
  - Código da empresa que o funcionário será alocado
  - Código da obra que o funcionário será alocado
  - Quantidade de dias que o funcionário está sendo alocado

VirtUau:
1. Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-a-importacao-de-alocação-de-mão-de-obra
2. Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/alocacao-de-mao-de-obra-de-funcionarios/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AlocacaoMaoObra.AlocacaoMaoObraRequest`](#uauapimodelsalocacaomaoobraalocacaomaoobrarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | A importação ocorrerá de forma parcial. Caso o retorno esteja vazio toda importação foi realizada com sucesso. Se encontrado inconsistência que impede a importação de algum registro será retornado o seu motivo. | array de [`UAUApi.Models.AlocacaoMaoObra.AlocacaoMaoObraResponse`](#uauapimodelsalocacaomaoobraalocacaomaoobraresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Folha/GravarMovimentacaoMensalObra`

**Objetivo: Incluir/Alterar movimentação mensal por obra dos funcionários do UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método GravarMovimentacaoMensalObra.

Definição de Negócio:
1. Efetua a inclusão ou alteração(caso o registro já exista) na movimentação mensal por obra dos funcionários do UAU.
2. Deve informar obrigatoriamente os campos:
  - Código da empresa de lotação do funcionário
  - Matrícula do funcionário
  - Código da rubrica a ser rateada na empresa/obra
  - Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY
  - Código da empresa de rateio dos cálculos do funcionário
  - Código da obra de rateio dos cálculos do funcionário
  - Quantidade ou valor da proporção definida para a empresa/obra de rateio

VirtUau:
1. Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-a-importacao-de-movimentacao-mensal-e-movimentacao-por-obra/
2. Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/como-realizar-calculo-da-folha-de-pagamento-com-rateio

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.MovimentacaoObra.MovimentacaoObraRequest`](#uauapimodelsmovimentacaoobramovimentacaoobrarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | A importação ocorrerá de forma parcial. Caso o retorno esteja vazio toda importação foi realizada com sucesso. Se encontrado inconsistência que impede a importação de algum registro será retornado o seu motivo. | array de [`UAUApi.Models.MovimentacaoObra.MovimentacaoObraResponse`](#uauapimodelsmovimentacaoobramovimentacaoobraresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.MovimentacaoObra.MovimentacaoObraResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodEmpresaLotacao` | integer (int32) | ✓ | Código da empresa de lotação do funcionário informado na API |
| `Matricula` | string | ✓ | Matrícula do funcionário informado na API |
| `CodigoRubrica` | integer (int32) | ✓ | Código da rubrica a ser rateada na empresa/obra informado na API |
| `MesFolha` | string (date-time) | ✓ | Mês de referência do cálculo da folha do funcionário informado na API |
| `CodEmpresaRateio` | integer (int32) | ✓ | Código da empresa de rateio dos cálculos do funcionário informado na API |
| `CodObraRateio` | string | ✓ | Código da obra de rateio dos cálculos do funcionário informado na API |
| `Proporcao` | number (double) | ✓ | Quantidade ou valor da proporção definida para a empresa/obra de rateio informado na API |
| `Motivo` | array de string | ✓ | Inconsistências encontradas que impediram a importação |

### UAUApi.Models.MovimentacaoObra.MovimentacaoObraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ListaMovimentacaoObra` | array de [`UAUApi.Models.MovimentacaoObra.EntidadeMovimentacaoObra`](#uauapimodelsmovimentacaoobraentidademovimentacaoobra) | ✓ |  |

### UAUApi.Models.MovimentacaoObra.EntidadeMovimentacaoObra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodEmpresaLotacao` | integer (int32) | ✓ | Código da empresa de lotação do funcionário, conforme cadastro de empresa no sistema Uau |
| `Matricula` | string | ✓ | Matrícula do funcionário, conforme cadastro no sistema Uau |
| `CodigoRubrica` | integer (int32) | ✓ | Código da rubrica a ser rateada na empresa/obra, rubrica precisa está cadastrada e configurada por funcionário ou empresa no sistema UAU |
| `MesFolha` | string (date-time) | ✓ | Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY |
| `CodEmpresaRateio` | integer (int32) | ✓ | Código da empresa de rateio dos cálculos do funcionário, conforme cadastro de empresa no sistema Uau |
| `CodObraRateio` | string | ✓ | Código da obra de rateio dos cálculos do funcionário, conforme cadastro de obras no sistema Uau |
| `Proporcao` | number (double) | ✓ | Quantidade ou valor da proporção definida para a empresa/obra de rateio Deve ser uma quantidade para definir um proporcional para divisão do valor da rubrica por empresa/obra. Para da rubrica igual a 103 (Horista) também será a quantidade de horas pagas ao funcionário no mês. |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.AlocacaoMaoObra.AlocacaoMaoObraResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodEmpresaLotacao` | integer (int32) | ✓ | Código da empresa de lotação do funcionário informado na API |
| `Matricula` | string | ✓ | Matrícula do funcionário informado na API |
| `MesFolha` | string (date-time) | ✓ | Mês de referência do cálculo da folha do funcionário informado na API |
| `CodEmpresaAlocacao` | integer (int32) | ✓ | Código da empresa onde o funcionário está sendo alocado informado na API |
| `CodObraAlocacao` | string | ✓ | Código da obra onde o funcionário está sendo alocado informado na API |
| `QtdeAlocada` | number (double) | ✓ | Quantidade de dias que o funcionário está sendo alocado dentro do mês de referência informado na API |
| `Motivo` | array de string | ✓ | Inconsistências encontradas que impediram a importação |

### UAUApi.Models.AlocacaoMaoObra.AlocacaoMaoObraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ListaAlocacao` | array de [`UAUApi.Models.AlocacaoMaoObra.EntidadeAlocacaoMaoObra`](#uauapimodelsalocacaomaoobraentidadealocacaomaoobra) | ✓ |  |

### UAUApi.Models.AlocacaoMaoObra.EntidadeAlocacaoMaoObra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodEmpresaLotacao` | integer (int32) | ✓ | Código da empresa de lotação do funcionário, conforme cadastro de empresa no sistema Uau |
| `Matricula` | string | ✓ | Matrícula do funcionário, conforme cadastro no sistema Uau |
| `MesFolha` | string (date-time) | ✓ | Mês de referência do cálculo da folha do funcionário. Data no formato MM/DD/YYYY |
| `CodEmpresaAlocacao` | integer (int32) | ✓ | Código da empresa de alocação, conforme cadastro de empresa no sistema Uau |
| `CodObraAlocacao` | string | ✓ | Código da obra de alocação, conforme cadastro de obras no sistema Uau |
| `QtdeAlocada` | number (double) | ✓ | Quantidade alocada no mês de referência |
