# AcompanhamentoContratoVenda

## POST `/api/v{version}/AcompanhamentoContratoVenda/GravarAcompanhamento`

**Método responsável por gravar o acompanhamento de contrato de vendas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Retorna json com as informações de empresa, obra, número do contrato e número do acompanhamento.

Definição de Negócio:
1. Permite inserir ou alterar um acompanhamento de contrato de venda. 
2. O usuário autenticado deve ter permissão de inclusão ou alteração em OBACOMPVENDA, a depender do objetivo (inserir ou editar acompanhamento).
3. O sistema identifica que é uma edição no acompanhamento quando a propriedade [NumAcompanhamento] está preenchida. Em caso de não informação deste campo, será gravado um novo acompanhamento.
4. O usuário autenticado deve ter permissão de inclusão em OBMEDICAOVENDA.
5. Em caso de manutenção de um acompanhamento, as informações serão sobrescritas e as quantidades "Qtde medida" e "Qtde falta medir" calculadas a partir da propriedade [QtdeAMedir] informada.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.AcompanhamentoContratoVenda.AcompanhamentoContratoVendaRequest`](#uauapimodelsacompanhamentocontratovendaacompanhamentocontratovendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.AcompanhamentoContratoVenda.AcompanhamentoContratoVendaResponse`](#uauapimodelsacompanhamentocontratovendaacompanhamentocontratovendaresponse) |
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

### UAUApi.Models.AcompanhamentoContratoVenda.AcompanhamentoContratoVendaResponse

Classe usada para a resposta do método GravarAcompanhamento da API de AcompanhamentoContratoVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Empresa |
| `Obra` | string |  | Obra |
| `NumContrato` | string |  | Número do contrato |
| `NumAcompanhamento` | integer (int32) |  | Número do acompanhamento para o caso de manutenção |

### UAUApi.Models.AcompanhamentoContratoVenda.AcompanhamentoContratoVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumAcompanhamento` | integer (int32) |  | Número do acompanhamento para o caso de manutenção. Para criação de um novo acompanhamento, este campo não deve ser informado. |
| `Empresa` | integer (int32) | ✓ | Código da Empresa |
| `Obra` | string | ✓ | Código da Obra |
| `NumContrato` | string | ✓ | Número do contrato |
| `PeriodoInicio` | string (date-time) | ✓ | Período de acompanhamento - Início |
| `PeriodoFim` | string (date-time) |  | Período de acompanhamento - Fim |
| `ListaDeProdutos` | array de [`UAUApi.Models.AcompanhamentoContratoVenda.ProdutoAcompanhamentoRequest`](#uauapimodelsacompanhamentocontratovendaprodutoacompanhamentorequest) | ✓ | Produtos que serão inseridos/alterados no acompanhamento |
| `Responsavel` | integer (int32) |  | Código do responsável pelo acompanhamento |
| `Status` | integer (int32) | ✓ | Status (0 - Não aprovado | 1 - Aprovado) |
| `ObservacaoParaEntrega` | string |  | Observação para entrega |
| `Motorista` | integer (int32) |  | Código do motorista |
| `CaminhaoPlaca` | string |  | Placa do caminhão |
| `UFPlaca` | string |  | Estado da placa do caminhão |
| `LocalPrestacaoServico` | integer (int32) |  | Local da prestação de serviço - município |

### UAUApi.Models.AcompanhamentoContratoVenda.ProdutoAcompanhamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroProduto` | string | ✓ | Produto contendo número do produto, quantidade a medir do produto e plano reajuste |
| `QtdAMedir` | number (double) | ✓ |  |
