# CessaoRecebiveis

## POST `/api/v{version}/CessaoRecebiveis/AprovarContrato`

**Aprovar o contrato de cessão de recebível, conforme o identificador passado como parâmetro**

<b>Definição Técnica:</b>
<br>Dados básicos para o funcionamento da API.</br>
<list type="bullet">
  <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
  <item>2. Preencher os parâmetros de request para uso do método.</item>
</list>
<b>Definição de Negócio:</b>
<br>Aprovar um contrato de cessão de recebíveis.</br>
<list type="bullet">
  <item>1. É obrigatório informar os dados básicos do contrasto de cessão de recebíveis.</item>
  <item>2. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.</item>
</list>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.CessaoRecebiveis.PostAprovarContratoRequest`](#uauapimodelscessaorecebiveispostaprovarcontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Aprovação de cessão de recebíveis. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## GET `/api/v{version}/CessaoRecebiveis/ConsultarContrato`

**Consultar os dados dos contratos de cessão de recebíveis, conforme os parâmetros informado**

<b>Definição Técnica:</b>
<br>Dados básicos para o funcionamento da API.</br>
<list type="bullet">
  <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
</list>
<b>Definição de Negócio:</b>
<br>Consultar um contrato de cessão de recebíveis.</br>
<list type="bullet">
  <item>1. É obrigatório informar ao menos um dos parâmetros da rota para realizar a busca.</item>
  <item>2. A data pode ser informada no padrão Dia/Mês/Ano.</item>
  <item>3. O comprador, deve ser informado o código do usuário no UAU.</item>
  <item>4. O nome contrato, deve ser informado igual ao número do contrato de cessão de recebíveis</item>
  <item>5. A chave da venda, dever ser informada no padrão Empresa|Obra|Venda.</item>
</list>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `dataContrato` | query | string |  | Data do contrato |
| `nomeContrato` | query | string |  | Nome do contrato |
| `comprador` | query | integer (int32) |  | ID do comprador |
| `chaveVenda` | query | string |  | Chave da venda composta por Empresa|Obra|NumeroVenda. Ex.: 101|OBR01|1 |
| `mostraHistorico` | query | boolean |  | Controla de deverá exibir o historico de registros. O padrão é False |
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consulta de cessão de recebíveis. | [`UAUApi.Models.CessaoRecebiveis.GetContratoModel`](#uauapimodelscessaorecebiveisgetcontratomodel) |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/CessaoRecebiveis/GerarVendaDoContrato`

**Gerar uma venda de um contrato de cessão de recebíveis, conforme o identificador passado como parâmetro**

<b>Definição Técnica:</b>
<br>Dados básicos para o funcionamento da API.</br>
<list type="bullet">
  <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
  <item>2. Preencher os parâmetros de request para uso do método.</item>
</list>
<b>Definição de Negócio:</b>
<br>Gerar a venda um contrato de cessão de recebíveis.</br>
<list type="bullet">
  <item>1. É obrigatório informar os dados básicos do contrasto de cessão de recebíveis.</item>
  <item>2. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.</item>
</list>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.CessaoRecebiveis.PostGerarVendaDoContratoRequest`](#uauapimodelscessaorecebiveispostgerarvendadocontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Geração de venda do contrato de cessão de recebíveis. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/CessaoRecebiveis/InserirContrato`

**Cadastra um novo contrato de cessão de recebíveis com os dados informados, que ficará pendente de aprovação caso não gere uma venda, pois aí precisará ficar aprovado**

<b>Definição Técnica:</b>
<br>Dados básicos para o funcionamento da API.</br>
<list type="bullet">
  <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
  <item>2. Preencher os parâmetros de request para uso do método.</item>
</list>
<b>Definição de Negócio:</b>
<br>Inserir um contrato de cessão de recebíveis.</br>
<list type="bullet">
  <item>1. É obrigatório informar os dados básicos do contrasto de cessão de recebíveis.</item>
  <item>2. O usuário autenticado precisa ter acesso à empresa e obra que está fazendo a requisição.</item>
  <item>3. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.</item>
</list>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.CessaoRecebiveis.PostContratoRequest`](#uauapimodelscessaorecebiveispostcontratorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Cadastro de cessão de recebíveis. | string |
| 400 | Não foi possível realizar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua ação. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.CessaoRecebiveis.PostContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Contrato` | string | ✓ | Código do contrato |
| `Descricao` | string | ✓ | Drescrição do contrato |
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `DataContrato` | string (date-time) | ✓ | Data do contrato |
| `Comprador` | string | ✓ | Informar o código ou o nome do comprador que está cadastrado no sistema |
| `PeriodoParcelas` | [`UAUApi.Models.CessaoRecebiveis.PeriodoParcelas`](#uauapimodelscessaorecebiveisperiodoparcelas) | ✓ | Periodo de vencimento das parcelas |
| `Obras` | array de [`UAUApi.Models.CessaoRecebiveis.Obras`](#uauapimodelscessaorecebiveisobras) |  | Lista de obras para serem usadas como filtro na busca de parcelas. <list type="bullet"><item>1. Ao informar as parcelas que faram parte do contrarto, a lista    de obras será montada conforme as empresas e obras contidas na parcela, considerando somente essas emrpesas e obras.</item></list> |
| `ObraVenda` | string | ✓ | Obra da venda |
| `DataVenda` | string (date-time) | ✓ | Data da venda |
| `ModeloVendas` | integer (int32) | ✓ | Modelo de vendas |
| `ProdutoVenda` | integer (int32) | ✓ | O produto definido para gerar a venda do contrato |
| `ValorTotalVenda` | number (double) | ✓ | Valor total da venda |
| `RiscoContrato` | boolean | ✓ | Contrato sem risco |
| `PermitirRenegociacao` | boolean | ✓ | Permitir renegociação |
| `GerarVendaDoContrato` | boolean | ✓ | Define se ao gerar o novo contrato de cessão de recebíveis, o sistema irá gerar a venda desse contrato automaticamente <list type="bullet"><item>Serão validados as informações necessárias para gerar a venda, e também ao criar o contrato de cessebíbeis,     o mesmo já será criado aprovado, e o usuário de aprovação será o usuário que está fazendo a requisição.    A venda é gerada sobre o valor total do contrato informado, usando o modelo de venda e a obra da venda, mesmo    que não tenha parcela vincualda ao contrato, a venda será gerada.</item></list> |
| `Parcelas` | array de [`UAUApi.Models.CessaoRecebiveis.Parcelas`](#uauapimodelscessaorecebiveisparcelas) |  | Parcelas da venda de carteira |
| `GrupoCobranca` | integer (int32) |  |  |

### UAUApi.Models.CessaoRecebiveis.Parcelas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Empresa da parcela |
| `Obra` | string |  | Obra da parcela |
| `Venda` | string |  | Venda da parcela |
| `Tipo` | string |  | Tipo da parcela |
| `Num` | integer (int32) |  | Número da parcela |
| `NumGer` | integer (int32) |  | NumGer da parcela |

### UAUApi.Models.CessaoRecebiveis.Obras

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Empresa da parcela |
| `Obra` | string |  | Obra da parcela |

### UAUApi.Models.CessaoRecebiveis.PeriodoParcelas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Inicio` | string (date-time) |  | Data inicial de vencimento das parcelas |
| `Fim` | string (date-time) |  | Data final de vencimento das parcelas |

### UAUApi.Models.CessaoRecebiveis.PostGerarVendaDoContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `idContrato` | integer (int32) | ✓ | Código do contrato |

### UAUApi.Models.CessaoRecebiveis.GetContratoModel

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoRegistro` | integer (int32) |  | Tipo do registro. Se é um registro histórico ou não (0 - Histórico / 1 - contrato Atual) |
| `empresaContrato` | integer (int32) |  | Empresa do contrato |
| `descricaoEmpresaContrato` | string |  | Descrição da empresa do contrato |
| `contrato` | string |  | Número do contrato |
| `IdContrato` | integer (int32) |  | Identificador do contrato |
| `descricaoContrato` | string |  | Descrição do contrato |
| `valorContrato` | number (double) |  | Valor do contrato atual |
| `valorPrincipalContrato` | number (double) |  | Valor principal do contrato, soma do valor reajustado das parcelas <list type="bullet"><item>1. Soma das parcelas vinculadas ao contrato, desconsiderando as parcelas excluídas com o tipo de manutenção de 1 - Distrado. As manutenções de 0 - Cessão de direito e 2 - Rengociação, excluem as parcelas alteradas, e já adiciona as novas vinculadas. Apenas o distrato que só remover as parcelas, por isso subtrai o valor das parcelas excluídas do tipo distrato.</item></list> |
| `dataContrato` | string (date-time) |  | Data do contrato |
| `dataAprovacaoContrato` | string (date-time) |  | Data da aprovação do contrato |
| `usuarioAprovacaoContrato` | string |  | Usuário da aprovação do contrato |
| `dataCadastroContrato` | string (date-time) |  | Data de cadastro do contrato |
| `usuarioCadastroContrato` | string |  | Usuário que cadastrou o contrato |
| `IdGrupoCobranca` | integer (int32) |  |  |
| `DescricaoGrupoCobranca` | string |  |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.CessaoRecebiveis.PostAprovarContratoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `idContrato` | integer (int32) | ✓ | Código do contrato |
