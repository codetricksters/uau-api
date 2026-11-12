# InsumosGeral

## POST `/api/v{version}/InsumosGeral/AtualizarInsumosGeral`

**- Método com finalidade de realizar manutenção em massa no cadastro dos insumos gerais.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite realizar manutenção em massa no cadastro dos insumos gerais.

Utilize "" caso queira limpar os campos do cadastro sendo que, código, descrição e unidade padrão, não podem ficar vazios.

Link para Virtuau relacionado: https://ajuda.globaltec.com.br/virtuau/parametrizacao-de-insumos-gerais/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.InsumosGeral.InsumosGeralAtualizacaoRequest`](#uauapimodelsinsumosgeralinsumosgeralatualizacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Manutenção de insumos geral | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/InsumosGeral/ConsultarInsumosGeral`

**Consulta os itens de determinada revisão de um veículo ou equipamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Nenhum parâmetro é obrigatório e os dados são retornados utilizando o LIKE para encontrar as informações.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.InsumosGeral.ConsultarInsumosGeralRequest`](#uauapimodelsinsumosgeralconsultarinsumosgeralrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar insumos geral | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/InsumosGeral/ConsultarInsumosGeralPorChave`

**- Método com finalidade de consultar dados do insumo geral por chave.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.InsumosGeral.InsumosGeralRequest`](#uauapimodelsinsumosgeralinsumosgeralrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar insumos geral por chave | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/InsumosGeral/ConsultarInsumosGeralPorDescricao`

**- Método com finalidade de consultar dados de insumo geral por descrição, considerando o LIKE.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.InsumosGeral.InsumosGeralPorDescricaoRequest`](#uauapimodelsinsumosgeralinsumosgeralpordescricaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar insumos pela parte da descrição. | object |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/InsumosGeral/InserirInsumosGeral`

**- Método com finalidade de inserir dados em InsumosGeral.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.InsumosGeral.InsumosGeralRequest`](#uauapimodelsinsumosgeralinsumosgeralrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir insumos geral | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.InsumosGeral.InsumosGeralPorDescricaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Descricao` | string |  |  |

### UAUApi.Models.InsumosGeral.InsumosGeralRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo` | string | ✓ | Código do insumo |
| `descricao` | string | ✓ | Descrição do insumo |
| `unidade` | string |  | Unidade do insumo. Somente será considerado se não for informado a property unidadesInsumo. |
| `unidadesInsumo` | array de [`UAUApi.Models.InsumosGeral.UnidadeInsumo`](#uauapimodelsinsumosgeralunidadeinsumo) |  | Unidades do insumo - Lista de unidades do insumo, onde podem ser atualizados/inseridos o código da unidade, status de ativa ou inativa e determinar a unidade padrão. |
| `usuario` | string | ✓ | Usuário que está realizando o cadastro |
| `status` | integer (int32) |  | Status do insumo, onde: 0 - Ativo; 1 - Inativo |
| `confirmado` | integer (int32) |  | Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado |
| `controlarPrecoMeta` | boolean |  | Se controla ou não o preço meta, onde: 0 - Não controla; 1 - Controla |
| `diasDeCompra` | integer (int32) |  | Número de dias para realizar a compra |
| `diasUtilizacao` | integer (int32) |  | Número de dias que insumo deve estar na obra antes de sua utilização |
| `numeroDeCompras` | integer (int32) |  | Número de compras a serem feitas no mês |
| `diasEntrega` | integer (int32) |  | Número de dias para a entrega |
| `numeroPagamentos` | integer (int32) |  | Número de pagamentos a serem feitos |
| `tipoPagamento` | integer (int32) |  | Tipo de utilização do insumo, sendo: 0 -  Cotação; 1 - Medição; 2 - Solicitação de pagamento |
| `controle` | integer (int32) |  | Tipo de controle do insumo (G1G2), onde: 1 - Controle por quantidade; 2 - Controle por verba |
| `controlaEstoque` | integer (int32) |  | Indica se controla ou não o estoque, onde: 0 - Não controla; 1 - Controla |
| `pagamentoSobre` | integer (int32) |  | Pagamento sobre, onde: 1 - Entrega; 2 - Pedido |
| `preco` | string |  | Preço do insumo |
| `dataCotacao` | string (date-time) |  | Refere-se a data da última atualização do preço |
| `frequenciaCompra` | string |  | Freqüência em que as compras serão realizadas |
| `comoPagar` | string |  | Freqüência em que os pagamentos serão efetivados |
| `CAP` | string |  | O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP principal) |
| `categoriaMovFin` | string |  | Categoria de movimentação financeira. |
| `CAPAplicacaoMaterial` | string |  | O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para aplicação de material) |
| `CAPEstorno` | string |  | O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para estorno) |
| `CAPTransacaoFinanceira` | string |  | O Cap é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (para transacao financeira) |
| `CategoriaDoInsumo` | string |  | Categoria do insumo |
| `NCM` | string |  | Nomenclatura comum do MERCOSUL |
| `CEST` | string |  | Código Especificador da Substituição Tributária |
| `Aplicacao` | string |  | Código da aplicação fiscal |
| `grupo` | integer (int32) |  | Grupo do insumo, onde: 1 - Mão de obra; 2 - Equipamentos; 3 -Materiais; 4 - Serviços; 5 - Transporte |
| `calcEncargo` | integer (int32) |  | Indica se o insumo é ou não para cálculo de encargo, onde:  0 - Não; 1 - Sim |
| `controlaFVM` | boolean |  | Indica se controla ou não a FVM, onde: 0 - Não controla; 1 - Controla - Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE. |
| `patrimonio` | integer (int32) |  | Indica se o insumo é ou não de patrimônio, onde: 0 - Não patrimônio; 1 - Patrimônio |
| `depreciacao` | string |  | Código de depreciação do patrimônio, fornecido atravez de uma tabela receita federal. |
| `grupoDeInsumos` | string |  | Define se é um insumo de patrimônio, caso seja, possibilita informar o grupo de insumos e a depreciação. |
| `rateioParaMecanicos` | number (double) |  | porcentagem que será distribuido do valor total deste insumo para uma futura manutenção de patrimônio interna. |
| `indicadorUtilBem` | integer (int32) |  | Indicador de utilização do bem incorporado ao ativo imobilizado, sendo: 1 - Produção de bens destinados a venda; 2 - Prestação de serviço; 3 - Locação a terceiros; 4 - Outros |
| `capacidadeDiariaTrabalho` | string |  | Capacidade diária de trabalho. Formato: HH:MM |
| `marcaModelo` | string |  | Marca/Modelo |
| `subgrupo` | integer (int32) |  | Subgrupo |
| `itemManutencao` | boolean |  | Indica se o insumo é um item de manutenção, sendo: 0 (ou false) - Não; 1 (ou true) - Sim - Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE. |

### UAUApi.Models.InsumosGeral.UnidadeInsumo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `unidade` | string |  | Unidade do insumo |
| `unidadePadrao` | integer (int32) |  | Unidade padrão do insumo? Onde: 0 - Não; 1 - Sim. Quando o valor para esse campo não for informado, irá assumir o padrão "0 - Não". |
| `unidadeAtiva` | integer (int32) |  | Unidade ativa? Onde: 0 - Ativa; 1 - Inativa. Quando o valor para esse campo não for informado, irá assumir o padrão "0 - Ativa". |

### UAUApi.Models.InsumosGeral.ConsultarInsumosGeralRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_insumo` | string |  | Codigo do insumo |
| `descricao_insumo` | string |  | Descrição do insumo |
| `codigosub_grupo` | integer (int32) |  | Codigo do sub grupo do insumo |
| `item_manutencao` | integer (int32) — valores possíveis: 0, 1, 2 |  | Define o tipo de filtro por item da manutenção Não, Sim, Não Filtrar |
| `patrimonio` | integer (int32) — valores possíveis: 0, 1, 2 |  | Define o tipo de filtro por patrimônio Não, Sim, Não Filtrar |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.InsumosGeral.InsumosGeralAtualizacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `listaInsumosAtualizar` | array de [`UAUApi.Models.InsumosGeral.InsumosGeralAtualizacao`](#uauapimodelsinsumosgeralinsumosgeralatualizacao) |  | Lista dos insumos gerais para atualização dos dados. |

### UAUApi.Models.InsumosGeral.InsumosGeralAtualizacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo` | string | ✓ | Código do insumo |
| `descricao` | string |  | Descrição do insumo |
| `unidadesInsumo` | array de [`UAUApi.Models.InsumosGeral.UnidadeInsumo`](#uauapimodelsinsumosgeralunidadeinsumo) |  | Unidades do insumo - Lista de unidades do insumo, onde podem ser atualizados o código da unidade, status de ativa ou inativa e determinar a unidade padrão. |
| `preco` | string |  | Preço do insumo, para limpar essa informação, o parâmetro deve ser preenchido com vazio ("") |
| `inativarVincUnidPadraoSubstituida` | boolean |  | Será inativado o vínculo da unidade padrão substituída 0 - Não inativar 1 - Inativar - Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE. |
| `CategoriaDoInsumo` | string |  | Categoria do insumo |
| `grupo` | string |  | Grupo do insumo, onde: 1 - Mão de obra; 2 - Equipamentos; 3 -Materiais; 4 - Serviços; 5 - Transporte |
| `status` | integer (int32) |  | Status do insumo, onde: 0 - Ativo; 1 - Inativo |
| `codigoInsumoSubstituirNasComposicoes` | string |  | Código do insumo a ser substituído em todas as composições que utilizarem o código atual que teve o status alterado para 1 - Inativo. |
| `ComposicoesSubstituir` | array de [`UAUApi.Models.InsumosGeral.ComposicaoSubstituir`](#uauapimodelsinsumosgeralcomposicaosubstituir) |  | Lista de composições que terão o insumo atual substituído por um outro que tiver sido informado (codigoInsumoSubstituirNasComposicoes). Se a lista de composições específicas não for informada, o insumo será substituído em todas as composições em que estiver inserido. |
| `NCM` | string |  | Código do NCM - Nomenclatura comum do mercosul |
| `CEST` | string |  | Código especificador da substituição tributária |
| `aplicacao` | string |  | Código da aplicação fiscal, sendo um número positivo e maior que 0. |
| `controlarPrecoMeta` | boolean |  | Controle do preço meta do insumo False - Não controlar True - Controlar - Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE. |
| `CAP` | string |  | CAP principal - Ligação das compras e pagamentos referidos com a contabilidade |
| `CAPAplicacaoMaterial` | string |  | CAP aplicação de material - Ligação das compras e pagamentos referidos com o assistente de aplicação do material |
| `CAPEstorno` | string |  | CAP de estorno - Ligação das compras e pagamentos referidos com a contabilidade |
| `CAPTransacaoFinanceira` | string |  | CAP de transação financeira - Ligação das compras e pagamentos referidos com a contabilidade |
| `categoriaMovFin` | string |  | Código da categoria de movimentação financeira |
| `confirmado` | integer (int32) |  | Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado |
| `diasDeCompra` | string |  | Número de dias para realizar a compra, para limpar essa informação, o parâmetro deve ser preenchido com vazio ("") |
| `diasUtilizacao` | string |  | Número de dias que insumo deve estar na obra antes de sua utilização, para limpar essa informação, o parâmetro deve ser preenchido com vazio ("") |
| `numeroDeCompras` | string |  | Número de compras a serem feitas no mês, para limpar essa informação, o parâmetro deve ser preenchido com vazio ("") |
| `diasEntrega` | string |  | Número de dias para a entrega, para limpar essa informação, o parâmetro deve ser preenchido com vazio ("") |
| `numeroPagamentos` | string |  | Número de pagamentos a serem feitos, para limpar essa informação, o parâmetro deve ser preenchido com vazio ("") |
| `tipoPagamento` | string |  | Tipo de utilização do insumo, sendo: 0 - Cotação; 1 - Medição; 2 - Solicitação de pagamento, para limpar essa informação, o parâmetro deve ser preenchido com vazio ("") |
| `controle` | string |  | Tipo de controle do insumo (G1G2), onde: 1 - Controle por quantidade; 2 - Controle por verba, para limpar essa informação, o parâmetro deve ser preenchido com vazio ("") |
| `controlaEstoque` | integer (int32) |  | Indica se controla ou não o estoque, onde: 0 - Não controla; 1 - Controla |
| `pagamentoSobre` | integer (int32) |  | Pagamento sobre, onde: 1 - Entrega; 2 - Pedido |
| `dataCotacao` | string (date-time) |  | Refere-se a data da última atualização do preço |
| `frequenciaCompra` | string |  | Freqüência em que as compras serão realizadas |
| `comoPagar` | string |  | Freqüência em que os pagamentos serão efetivados |
| `calcEncargo` | integer (int32) |  | Indica se o insumo é ou não para cálculo de encargo, onde: 0 - Não; 1 - Sim |
| `controlaFVM` | boolean |  | Indica se controla ou não a FVM, onde: 0 - Não controla; 1 - Controla. Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE. |
| `patrimonio` | integer (int32) |  | Indica se o insumo é ou não de patrimônio, onde: 0 - Não patrimônio; 1 - Patrimônio |
| `depreciacao` | string |  | Código de depreciação do patrimônio, fornecido atravez de uma tabela receita federal. |
| `grupoDeInsumos` | string |  | Define se é um insumo de patrimônio, caso seja, possibilita informar o grupo de insumos e a depreciação. |
| `rateioParaMecanicos` | number (double) |  | porcentagem que será distribuido do valor total deste insumo para uma futura manutenção de patrimônio interna. |
| `indicadorUtilBem` | integer (int32) |  | Indicador de utilização do bem incorporado ao ativo imobilizado, sendo: 1 - Produção de bens destinados a venda; 2 - Prestação de serviço; 3 - Locação a terceiros; 4 - Outros |
| `capacidadeDiariaTrabalho` | string |  | Capacidade diária de trabalho. Formato: HH:MM |
| `marcaModelo` | string |  | Marca/Modelo |
| `subgrupo` | integer (int32) |  | Subgrupo |
| `itemManutencao` | boolean |  | Indica se o insumo é um item de manutenção, sendo: 0 (ou false) - Não; 1 (ou true) - Sim. Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE, portanto, ao informar um valor diferente de Zero sempre será gravado TRUE. |
| `porcQtdeExcedidaEntrega` | string |  | Percentual de tolerância para entregas com quantidade superior à que foi solicitada.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |
| `porcPrecoExcedidoEntrega` | string |  | Percentual de tolerância para entregas com preços superiores ao que foi solicitado.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |
| `porcPrecoReduzidoEntrega` | string |  | Percentual de tolerância para entregas com preços reduzidos ao que foi solicitado.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |
| `verificacaoSGQ` | integer (int32) |  | Indica qual o tipo de critério de verificação será usado, se uma descrição ou um arquivo vinculado. 0 - Texto descritivo, 1 - Anexar documento. |
| `criterioVerificacaoSGQ` | string |  | Texto descritivo dos critérios para verificação ou caminho do arquivo com os critérios para verificação. |
| `especificacaoSGQ` | string |  | Especificação do item para o SGQ. |
| `identificacaoSGQ` | string |  | Identificação e observação aplicada para o SGQ. |
| `orientacaoSGQ` | string |  | Orientação para o SGQ. |
| `observacaoSGQ` | string |  | Observação de preservação para o SGQ. |

### UAUApi.Models.InsumosGeral.ComposicaoSubstituir

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoComposicao` | string |  | Código da composição específica que terá o insumo atual substituído por um outro informado (codigoInsumoSubstituirNasComposicoes). |
