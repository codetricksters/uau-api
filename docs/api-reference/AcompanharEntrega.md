# AcompanharEntrega

## POST `/api/v{version}/AcompanharEntrega/AcompanharPreEntrega`

**Método com finalidade de acompanhar pre entrega**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
Regras Básicas:
 
 1. O usuário deve possuir acesso na empresa e obra informada.
 2. O usuário deve possuir permissão de alteração no programa FIANALISE.
 3. O número do processo deve ser um processo existente.
 4. A NF e NF de frete devem ser númericos e válidos.
 5. O código de barras deve ser númerico e possuir no mínimo 36 caracteres.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanharEntrega.PreEntregaRequest`](#uauapimodelsacompanharentregapreentregarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Acompanhar Pre Entrega | array de [`UAUApi.Models.AcompanharEntrega.ProcessoDePagamentoResponse`](#uauapimodelsacompanharentregaprocessodepagamentoresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/AcompanharEntrega/ConsultarProcessos`

**Método com finalidade de consultar processos do acompanhamento de entrega.**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
Regras Básicas:
 
 1. Retorna os processos e itens que estão com o acompanhamento de entrega pendente para uma dada empresa e obra informada.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanharEntrega.ConsultarProcessosRequest`](#uauapimodelsacompanharentregaconsultarprocessosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar Processos | array de [`UAUApi.Models.AcompanharEntrega.ProcessoDePagamentoResponse`](#uauapimodelsacompanharentregaprocessodepagamentoresponse) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.AcompanharEntrega.ConsultarProcessosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ |  |
| `obra` | string | ✓ |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.AcompanharEntrega.ProcessoDePagamentoResponse

Classe usada na resposta do método RetornarProcessos da API de AcompanharEntrega

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Cotacao` | integer (int32) |  | Número da cotação |
| `OrdemDeCompra` | integer (int32) |  | Número de ordem de compra |
| `Processo` | integer (int32) |  | Número do processo |
| `CodigoFornecedor` | integer (int32) |  | Código |
| `NomeFornecedor` | string |  | Descrição do fornecedor |
| `Subtotal` | number (double) |  | Subtotal do processo de pagamento |
| `Desconto` | number (double) |  | Desconto no processo de pagamento |
| `Total` | number (double) |  | Valor total do processo de pagamento |
| `Tipo` | integer (int32) |  | Tipos: 0 - Cotação 2 - Solicitação de pagamento 10 - Acompanhamento de entrega sem estoque 11 - Controle de patrimônio 26 - Acompanhamento de ordem de serviço |
| `DataPrevista` | string (date-time) |  | Data Prevista |
| `Antecipado` | string |  | Antecipado: 0 - Não 1 - Sim |
| `Itens` | array de [`UAUApi.Models.AcompanharEntrega.EstoqueProcessoResponse`](#uauapimodelsacompanharentregaestoqueprocessoresponse) |  |  |

### UAUApi.Models.AcompanharEntrega.EstoqueProcessoResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Insumo` | string |  | Código do insumo |
| `DescricaoInsumo` | string |  | Insumo |
| `Unidade` | string |  | Unidade |
| `Quantidade` | number (double) |  | Quantidade |
| `PrecoUnitario` | number (double) |  | Preço unitário do insumo |
| `SubTotal` | number (double) |  | Subtotal |
| `Total` | number (double) |  | Total |
| `NumeroProcesso` | integer (int32) |  | Número do processo |

### UAUApi.Models.AcompanharEntrega.PreEntregaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa no UAU |
| `Obra` | string | ✓ | Código da obra no UAU |
| `Processo` | integer (int32) | ✓ | Número do processo de pagamento no UAU |
| `ChaveNotaFiscal` | string |  | Chave da nota fiscal para inclusão no UAU |
| `ChaveNotaFiscalFrete` | string |  | Chave da nota fiscal do frete para inclusão no UAU |
| `CodigoDoBoleto` | string |  | Linha digitável do boleto |
| `CodigoDoBoletoFrete` | string |  | Linha digitável do boleto do frete |
| `Itens` | array de [`UAUApi.Models.AcompanharEntrega.ItemPreEntregaRequest`](#uauapimodelsacompanharentregaitempreentregarequest) | ✓ | Itens a serem acompanhados |

### UAUApi.Models.AcompanharEntrega.ItemPreEntregaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoItem` | string | ✓ | Código do item a acompanhar |
| `Quantidade` | number (double) | ✓ | Quantidade do item a acompanhar |
| `Preco` | number (double) | ✓ | Preço do item a acompanhar |
