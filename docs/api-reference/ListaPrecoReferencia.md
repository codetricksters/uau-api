# ListaPrecoReferencia

## POST `/api/v{version}/ListaPrecoReferencia/AtualizarItemFornecedor`

**Método com finalidade de atualizar um fornecedor na Lista de Preço Referência.**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
Regras Básicas:
 
 1. O usuário deve possuir permissão de alteração no programa "ALLISTAPRECOREF"
 2. Para atualizar um fornecedor, a lista já deve existir no sistema e o fornecedor já deve estar cadastro.
 3. A lista deve estar em aberto, não pode ter nenhuma confirmação de aprovação.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ListaPrecoReferencia.ListaFornecedorRequest`](#uauapimodelslistaprecoreferencialistafornecedorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir Fornecedores | array de [`UAUApi.Models.ListaPrecoReferencia.ListaDistribuida`](#uauapimodelslistaprecoreferencialistadistribuida) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ListaPrecoReferencia/ConsultarListaPrecoReferencia`

**Método com finalidade de consultar a Lista de Preco Referência, com itens da lista de preço e itens de fornecedores preenchidos ou não.**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
Regras Básicas:
 1. Pelo menos um parâmetro deve ser preenchido para consulta.
 2. Parâmetros:
-  CodigoLista: Parâmetro principal, caso seja informado irá sobrepor todos os outros.
-  FornecedorCodigo: Fará a pesquisa pelo código do fornecedor, caso não possua o CNPJ.
-  FornecedorCNPJ: Fará a pesquisa pelo CNPJ do fornecedor, caso não possua o código do fornecedor.
-  DataValidade: Data de validade da lista de preço.
-  Status:   
     - 0 - Em aberto
     - 1 - Em Análise
     - 2 - Aprovada
     - 3 - Migrada

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ListaPrecoReferencia.ConsultarListaPrecoReferenciaRequest`](#uauapimodelslistaprecoreferenciaconsultarlistaprecoreferenciarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Preço Referência | array de [`UAUApi.Models.ListaPrecoReferencia.ListaPrecoReferencia`](#uauapimodelslistaprecoreferencialistaprecoreferencia) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ListaPrecoReferencia/InserirFornecedores`

**Método com finalidade de inserir fornecedor na Lista de Preço Referência.**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
Regras Básicas:
 
 1. O usuário deve possuir permissão de inclusao no programa "ALLISTAPRECOREF"
 2. Para incluir um fornecedor, a lista já deve existir no sistema.
 3. A lista deve estar em aberto, não pode ter nenhuma confirmação de aprovação.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ListaPrecoReferencia.ListaFornecedorRequest`](#uauapimodelslistaprecoreferencialistafornecedorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir Fornecedores | array de [`UAUApi.Models.ListaPrecoReferencia.ListaDistribuida`](#uauapimodelslistaprecoreferencialistadistribuida) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.ListaPrecoReferencia.ListaPrecoReferencia

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoLista` | integer (int32) |  | Identificador único da lista de preço referência |
| `Descricao` | string |  | Descrição da lista |
| `CondicaoPagamento` | string |  | Descrição da condição de pagamento |
| `DataValidade` | string (date-time) |  | Data de vencimento da lista. |
| `Status` | integer (int32) |  | Status da lista: 0 - Em aberto; 1 - Em Análise; 2 - Aprovada;  3 - Migrada. |
| `UsuarioAlteracao` | string |  | Usuário de alteração |
| `DataAlteracao` | string (date-time) |  | Data de alteração |
| `Itens` | array de [`UAUApi.Models.ListaPrecoReferencia.ItensListaPrecoReferencia`](#uauapimodelslistaprecoreferenciaitenslistaprecoreferencia) |  | Lista de preço referência |
| `ListasDistribuidas` | array de [`UAUApi.Models.ListaPrecoReferencia.ListaDistribuida`](#uauapimodelslistaprecoreferencialistadistribuida) |  | Lista distribuida |
| `Aprovacao` | array de [`UAUApi.Models.ListaPrecoReferencia.ListaAprovacao`](#uauapimodelslistaprecoreferencialistaaprovacao) |  | Lista de aprovação |
| `ObrasExcluidas` | array de [`UAUApi.Models.ListaPrecoReferencia.ListaPrecoRefObrasExcluidas`](#uauapimodelslistaprecoreferencialistaprecorefobrasexcluidas) |  | Lista de obras excluidas |
| `Objeto` | string |  | Descrição do objeto |
| `Tipo` | integer (int32) |  | Tipo: 0 - Básica; 1 - Acordo corporativo |
| `UFEntrega` | string |  | UF de entrega |
| `CodigoServicoFrete` | string |  | Serviço de frete |
| `ControlaEstoque` | integer (int32) |  | Controla estoque: 0 - Não; 1 - Sim. |
| `AcompanharEntrega` | integer (int32) |  | Acompanhamento de entrega: 0 - Não; 1 - Sim. |
| `RegraDiasPgto` | integer (int32) |  | Dias para pagamento |

### UAUApi.Models.ListaPrecoReferencia.ListaPrecoRefObrasExcluidas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumLista` | integer (int32) |  | Identificador único da lista de preço referência |
| `Empresa` | integer (int32) |  | Código da empresa |
| `DescEmpresa` | string |  | Descrição da empresa |
| `Obra` | string |  | Código da obra |
| `DescObra` | string |  | Descrição da obra |
| `UsuarioCadastro` | string |  | Usuário que excluiu |
| `DataCadastro` | string (date-time) |  | Data de exclusão |

### UAUApi.Models.ListaPrecoReferencia.ListaAprovacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Quem` | string |  | Quem aprovou |
| `DataAprov` | string (date-time) |  | Data da aprovação |

### UAUApi.Models.ListaPrecoReferencia.ItensListaPrecoReferencia

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoItem` | string |  | Identificador único da lista de preço referência |
| `DescricaoItem` | string |  | Descrição do item |
| `Unidade` | string |  | Unidade |
| `CodigoCategoria` | string |  | Código da categoria |
| `DescCategoria` | string |  | Descrição da categoria |
| `PrecoItem` | number (double) |  | Preço |
| `Origem` | integer (int32) |  | Origem |
| `CodigoFornecedor` | integer (int32) |  | Código do fornecedor |
| `NomeFornecedor` | string |  | Nome do fornecedor |
| `Especificacao` | string |  | Especificação |
| `DataCotacao` | string (date-time) |  | Data da cotação |
| `Quantidade` | integer (int32) |  | Quantidade |
| `Observacao` | string |  | Observação |
| `UsuarioAlteracao` | string |  | Usuário que alterou a lista |

### UAUApi.Models.ListaPrecoReferencia.ConsultarListaPrecoReferenciaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroLista` | integer (int32) |  | Identificador único da lista de preço referência |
| `DataValidade` | string (date-time) |  | Data de vencimento da lista. |
| `Status` | integer (int32) |  | Status da lista: 0 - Em aberto; 1 - Em Análise; 2 - Aprovada;  3 - Migrada. |
| `FornecedorCNPJ` | string |  | Número de CNPJ do fornecedor |
| `FornecedorCodigo` | integer (int32) |  | Número do código do fornecedor |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.ListaPrecoReferencia.ListaDistribuida

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoFornecedor` | integer (int32) |  | Identificador único da lista de preço referência |
| `Nome` | string |  | Nome do fornecedor |
| `FisicaJuridica` | string |  | 0 - Física;  1 - Juridica |
| `CPFCNPJ` | string |  | CPF ou CNPJ do fornecedor |
| `Email` | string |  | Email do fornecedor |
| `Status` | integer (int32) |  | Status: 0 - Em aberto; 1 - Finalizada; |
| `UsuarioAlteracao` | string |  | Usuário de alteração |
| `DataAlteracao` | string (date-time) |  | Data de alteração |
| `ValorMinimoPedFOB` | number (double) |  | Valor mínimo de pedido FOB |
| `ValorMinimoPedCIF` | number (double) |  | Valor mínimo de pedido CIF |
| `DataInicio` | string (date-time) |  | Data de inicio |
| `DataTermino` | string (date-time) |  | Data de termino |
| `Contato` | string |  | Contato |
| `ItensPorFornecedor` | array de [`UAUApi.Models.ListaPrecoReferencia.ItensPorFornecedor`](#uauapimodelslistaprecoreferenciaitensporfornecedor) |  | Itens por fornecedor |

### UAUApi.Models.ListaPrecoReferencia.ItensPorFornecedor

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoItem` | string |  | Código do fornecedor |
| `DescricaoItem` | string |  | Descrição do fornecedor |
| `Unidade` | string |  | Código da unidade |
| `CodigoCategoria` | string |  | Código de categoria |
| `DescricaoCategoria` | string |  | Descrição da categoria |
| `PrecoItem` | number (double) |  | Preço |
| `Especificacao` | string |  | Especificação |
| `DataCotacao` | string (date-time) |  | Data da cotação |
| `QtdeMinima` | number (double) |  | Quantidade mínima para o pedido |
| `Multiplo` | number (double) |  | Múltiplo |
| `DiasEntrega` | integer (int32) |  | Dias entrega |
| `TipoFrete` | integer (int32) |  | Tipo de frete: 0 - CIF; 1 - FOB. |
| `Observacao` | string |  | Observação |
| `UsuarioAlteracao` | string |  | Usuário de alteração |
| `DataAlteracao` | string (date-time) |  | Data de alteração |

### UAUApi.Models.ListaPrecoReferencia.ListaFornecedorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroLista` | integer (int32) | ✓ | Identificador único da lista de preço referência |
| `CodigoFornecedor` | integer (int32) | ✓ | Código do fornecedor |
| `CPFCNPJ` | string |  | CPF/CNPJ do fornecedor |
| `ValorMinimoPedFOB` | number (double) |  | Valor mínimo de pedido para o tipo FOB |
| `ValorMinimoPedCIF` | number (double) |  | Valor mínimo de pedido para o tipo CIF |
| `DataInicio` | string (date-time) |  | Data início |
| `DataTermino` | string (date-time) |  | Data terminio |
| `Contato` | string |  | Contato |
| `ItensPorFornecedor` | array de [`UAUApi.Models.ListaPrecoReferencia.ItemPorFornecedorRequest`](#uauapimodelslistaprecoreferenciaitemporfornecedorrequest) |  | Itens por fornecedor |

### UAUApi.Models.ListaPrecoReferencia.ItemPorFornecedorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoItem` | string | ✓ | Código do item |
| `PrecoItem` | number (double) |  | Preço |
| `QtdeMinima` | number (double) |  | Quantidade mínima |
| `Multiplo` | number (double) |  | Múltiplo |
| `DiasEntrega` | integer (int32) |  | Dias entrega |
| `TipoFrete` | integer (int32) |  | Tipo de frete: 0 - CIF; 1 - FOB. |
| `Observacao` | string |  | Observação |
