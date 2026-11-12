# Venda

## POST `/api/Venda/ConsultarStatusCobrancaAtiva`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `codigo` | query | string | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | [`Globaltec.UAU.Repositorio.StatusCobranca`](#globaltecuaurepositoriostatuscobranca) |

---

## POST `/api/v{version}/Venda/AlterarDataProrrogacao`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.AlterarDataProrrogacaoRequest`](#uauapimodelsvendaalterardataprorrogacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível alterar a data de prorrogação! - Nova data de prorrogação é inválida! - Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/AprovDesaprovReneg`

**Aprovar ou desaprovar renegociações**

Definição técnica:
- Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de negócio
- A rota aprova ou desaprova uma renegociação de venda.
- É realizada uma validação da Alçada.
- Os anexos são atualizados conforme a operação solicitada.

Pré requisito:
- É necessário ter permissão de aprovação em FIMNTVENRENCON

- Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
    - URL + /api/v{version}/Venda/AprovDesaprovReneg

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.AprovDesaprovReneg`](#uauapimodelsvendaaprovdesaprovreneg)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/AtualizarPedidoDeRecebimento`

**Atualizar o(s) pedido(s) de recebimento junto a NTK**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Serão atualizadas as parcelas do pedido que ainda estão com status: 0 - Em aberto 
2. Valida usuário e permissões
3. Valida outras informações passadas no request

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.PedidoRequest`](#uauapimodelsvendapedidorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoPedido`](#globaltecuauvendasdtoscartaointencaopedido) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscaParcRenegWeb`

**Buscar parcelas calculadas na data atual**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Possibilita buscar parcelas calculadas para a data atual (dia da requisição).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.BuscaParcRenegWebRequest`](#uauapimodelsvendabuscaparcrenegwebrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarCampanhaDescontoVenda`

**Busca a campanha de desconto de antecipação disponível para uma venda.**

Definição Técnica:
1. Autenticar o usuário através da rota:
   URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros da requisição.

Definição de Negócio:
Permite consultar a campanha de desconto de antecipação vinculada a uma venda,
retornando suas configurações para utilização em consultas e cálculos de desconto.

Regras:
1. O usuário deve estar autenticado.
2. Informar os dados da venda para a qual deseja consultar a campanha.
3. Caso exista uma campanha de desconto de antecipação vigente e aplicável à venda,
   suas configurações serão retornadas.

Retorno:
- Serão retornadas as informações da campanha de desconto de antecipação
  associada à venda informada.
- Caso não exista campanha vigente ou aplicável à venda, nenhum registro será retornado.

Observação:
As informações retornadas por esta rota podem ser utilizadas para preencher os
dados da campanha na requisição da rota
/api/v{version}/Venda/CalcularDescontoCampanhaAntecipacao.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.CalcularDesconto.CampanhaVendaRequest`](#uauapimodelscalculardescontocampanhavendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.CalcularDesconto.CampanhaVenda`](#uauapimodelscalculardescontocampanhavenda) |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarParametroCobranca`

**Retornar a lista com parâmetros de cobranças**

Definição Técnica:
1. Busca a lista de parâmetros de cobrança ativos do sistema:
 - URI + /api/v{version}/Venda/BuscarParametroCobranca

2. Formato dos dados retornados:
 - Banco     (String) : Número do banco
 - NomeBanco (String) : Nome do banco
 - Conta     (String) : Número da conta
 - Agencia   (String) : Código da agência do banco
 - Carteira  (String) : Código da carteira do convênio com banco
 - Codigo    (String) : Código do parâmetro de cobrança no sistema
 - Descricao (String) : Descrição do parâmetro de cobrança no sistema
 - Empresa   (String) : Código da empresa
 - Cedente   (String) : Código do cedente da remessa de cobrança
 
Definição de negócio:
1. Para buscar todos os padrões de cobrança ativos, usar null nos parâmetros da requisição ou não enviar os campos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ParametroCobrancaRequest`](#uauapimodelsvendaparametrocobrancarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Vendas.ParametroCobrancaDTO`](#globaltecuauvendasparametrocobrancadto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarParcelasAReceber`

**Buscar parcelas a receber calculadas para a data atual**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Possibilita a busca de parcelas a receber na data atual.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.BuscarParcelasAReceberRequest`](#uauapimodelsvendabuscarparcelasareceberrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarParcelasRecebidas`

**Buscar parcelas recebidas da venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Possibilita buscar parcelas que foram recebidas.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.BuscarParcelasRecebidasRequest`](#uauapimodelsvendabuscarparcelasrecebidasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarRecebimentosDaVenda`

**Consulta os recebimentos de uma venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Permite consultar os reecebimentos de uma venda, ou seja, o que já foi recebido.
2. Caso o campo "parcelasnao_conciliadas" esteja marcado como "true" as parcelas não conciliadas também serão retornadas.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.BuscarRecebimentosDaVendaRequest`](#uauapimodelsvendabuscarrecebimentosdavendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarStatusCobranca`

**Retornar a lista de status de cobrança ativos.**

Definição Técnica:
1. Busca a lista de status de cobrança ativos do sistema:
 - URI + /api/v{version}/Venda/BuscarStatusCobranca

1. Formato dos dados retornados:
 - Codigo(Integer):Código do status de cobrança
 - Descricao(String):Descrição do status de cobrança

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Vendas.StatusCobrancaDTO`](#globaltecuauvendasstatuscobrancadto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarStatusDeEscritura`

**Retornar a lista de Status de escritura ativos.**

Definição Técnica:
1. Busca a lista de Status de escritura ativos do sistema:
 - URI + /api/v{version}/Venda/BuscarStatusDeEscritura

1. Formato dos dados retornados:
 - Codigo(Integer):Código de Status de escritura
 - Descricao(String):Descrição do Status de escritura

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Vendas.StatusDeEscrituraDTO`](#globaltecuauvendasstatusdeescrituradto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarTiposDeCustas`

**Retornar a lista de tipos de custas ativos.**

Definição Técnica:
1. Busca a lista de status de cobrança ativos do sistema:
 - URI + /api/v{version}/Venda/BuscarTiposDeCustas

1. Formato dos dados retornados:
 - Codigo(String):Código do tipo de custa
 - Descricao(String):Descrição do status de cobrança

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Vendas.CustasTipoDTO`](#globaltecuauvendascustastipodto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/BuscarTiposDeParcelas`

**Retornar a lista de tipos de parcelas ativos**

Definição Técnica:
1. Busca a lista de status de cobrança ativos do sistema:
 - URI + /api/v{version}/Venda/BuscarTiposDeParcelas

1. Formato dos dados retornados:
 - Tipo(String):Código do tipo de parcela
 - Descricao(String):Descrição do tipo de parcela

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Vendas.ParcelasDTO`](#globaltecuauvendasparcelasdto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/CalcularDescontoCampanhaAntecipacao`

**Calcula o desconto de campanha de antecipação para as parcelas de uma venda.**

Definição Técnica:
1. Autenticar o usuário através da rota:
   URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros da requisição.

Definição de Negócio:
Permite calcular o desconto de campanha de antecipação para uma ou mais parcelas de uma venda.

Regras:
1. O usuário deve estar autenticado.
2. A venda deve possuir uma campanha de desconto de antecipação vigente.
3. Os dados da campanha devem ser informados na requisição. Para obtê-los, utilize previamente a rota
   /api/v{version}/Venda/BuscarCampanhaDescontoVenda.
4. Informar as parcelas para as quais o desconto será calculado.

Retorno:
- A resposta conterá as mesmas parcelas enviadas na requisição, com o campo
  ValorDescontoCalculado preenchido conforme as regras da campanha.
- Caso não exista campanha vigente para a venda ou a parcela não atenda às regras da campanha,
  o campo ValorDescontoCalculado será retornado com o valor 0.

Observação:
O valor calculado por esta rota deve ser o mesmo apresentado na tela de Recebimento Avulso
ao antecipar parcelas que estejam contempladas por uma campanha de desconto.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.CalcularDesconto.ParcelasCalculadasCampanhaRequest`](#uauapimodelscalculardescontoparcelascalculadascampanharequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.CalcularDesconto.ParcelaCalculadaCampanha`](#uauapimodelscalculardescontoparcelacalculadacampanha) |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/CancelarPedidoDeRecebimento`

**Cancelar o pedido de recebimento junto a NTK**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Pedidos que já tiveram um recebimento parcial junto a NTK, não são cancelados. (trava na NTK).
2. É necessário ter permissão de alteração no programa VEPEDIDORECEBIMENTO

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.PedidoRequest`](#uauapimodelsvendapedidorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoPedido`](#globaltecuauvendasdtoscartaointencaopedido) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarCampanhaDescontoDisponivel`

**Consultar campanha de desconto disponível para a venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Consulta a campanha de desconto disponível para utilização.
1. Valida usuário logado e permissões

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.CampanhaDescontoDisponivelRequest`](#uauapimodelsvendacampanhadescontodisponivelrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Venda.VendaIntegracao.CampanhaDescontoDisponivel`](#uauapimodelsvendavendaintegracaocampanhadescontodisponivel) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarContasReceberCalc`

**Consulta de parcelas de contas a receber já calculadas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Possibilita Consultar as parcelas de contas a receber já calculadas com retorno a lista de parcelas.
2. Nenhuma propriedade é obrigatória, porém é obrigatório ser enviado pelo menos um tipo de filtro para consultar os dados.
3. Na propriedade vendas, é obrigatório apenas o parâmetro empresa.
4. É indispensável que o PROUAU esteja rodando diariamente o cálculo de parcelas para que os resultados estejam sempre corretos.
5. O Filtro de período filtrará pela data de vencimento da parcela.
6. O filtro por tipo de parcelas pode aceitar mais de um tipo, é obrigatório colocar entre aspas simples cada código de parcela e separadas por virgula. Ex.: 'P', 'M'

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultarContasReceberCalcRequest`](#uauapimodelsvendaconsultarcontasrecebercalcrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Venda.VendaIntegracao.ContasReceberCalc`](#uauapimodelsvendavendaintegracaocontasrecebercalc) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarDemonstrativoCorrecao`

**Consultar demonstrativo de correção da parcela da venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite consultar demonstrativo de correção da parcela da venda.
1. Valida usuário e suas permissões.
2. Valida existência da venda.
3. Valida existência das parcelas.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.DemonstrativoCorrecaoRequest`](#uauapimodelsvendademonstrativocorrecaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Venda.VendaIntegracao.DemonstrativoCorrecao`](#uauapimodelsvendavendaintegracaodemonstrativocorrecao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarDescontoAntecipacaoParcela`

**Calcular desconto por antecipação da parcela**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Consulta o valor do desconto caso a parcela seja paga antecipadamente.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultarDescontoAntecipacaoParcelaRequest`](#uauapimodelsvendaconsultardescontoantecipacaoparcelarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarEmpreendimentosCliente`

**Consulta os empreendimentos que o cliente possui contrato em aberto**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Consulta os empreendimento que o cliente possui e está com situação em aberto.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultarEmpreendimentosClienteRequest`](#uauapimodelsvendaconsultarempreendimentosclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarHistoricos`

**Consultar os históricos de uma ou mais vendas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. O preenchimento da lista de vendas, devem ser preenchidos de forma padronizada, ou preenche todas as vendas com o número da venda, ou todas com apenas empresa e obra.
4. Para o preenchimento dos tipos de manutenção, o valor de tipo de manutenção deve ser numérico e caso tenha mais de um, devem ser separados por vírgula. Exemplo: 1,2,4.
5. Recomendável buscar períodos curtos ou uma venda específica para evitar timeout.

Definição de Negócio:
Consultar os históricos de uma ou mais vendas selecionadas.
Para buscar os históricos das vendas um dos parâmetros devem estar preenchidos, ou a lista de vendas ou o período da manutenção.
1. As classes abaixo não serão preenchidas no objeto de retorno porque essas informações não possuem histórico:
    - Comissoes
    - Comentarios
    - AluguelShopping
    - VendaVinculada
    - DescontosDeCusta
    - Recebimentos
    - Prorrogacoes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultarHistoricosRequest`](#uauapimodelsvendaconsultarhistoricosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Venda.HistoricoVenda`](#uauapimodelsvendahistoricovenda) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarParcelasDaVenda`

**Consultar parcelas da venda calculadas para a data informada**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite consultar as parcelas de uma venda.
1. Ao enviar somenteParcelasAptasBoleto como TRUE, irá validar se a venda possui bloqueio ou manutenção pendente e se a empresa está configurada
para "Não permitir enviar para banco parcelas com status [em banco]"
    - Caso a venda possua bloqueio ou esteja em manutenção, não irá retornar nenhuma parcela da venda.
    - Caso esteja configurado para não enviar parcelas com status em banco, não irá retornar as parcelas que já tenham boletos gerados.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultarParcelasDaVendaRequest`](#uauapimodelsvendaconsultarparcelasdavendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarPedidoDeRecebimento`

**Consultar o pedido de recebimento junto a NTK**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Possibilita consultar pedido de recebimento junto a NTK
2. As informações retornadas serão informações do pedido na NTK.
3. É necessário ter permissão de consulta em VEPEDIDORECEBIMENTO

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.PedidoRequest`](#uauapimodelsvendapedidorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoPedido`](#globaltecuauvendasdtoscartaointencaopedido) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarPedidoDeRecebimentoUAU`

**Consultar o pedido de recebimento no UAU**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
1. Possibilita consultar pedido de recebimento registrado no UAU por número do pedido junto a NTK ou pelo número do pedido no UAU.
2. As informações retornadas são referentes a como o UAU registrou o pedido internamente.
3. É necessário ter permissão de consulta em VEPEDIDORECEBIMENTO

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.PedidoRequestUAU`](#uauapimodelsvendapedidorequestuau)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Vendas.DTOPedidoRecebimento`](#globaltecuauvendasdtopedidorecebimento) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarPlanoIndexadoresVenda`

**Consulta o plano indexador da venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Retorna informações pertinentes ao plano indexador da venda.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultarPlanoIndexadoresVendaRequest`](#uauapimodelsvendaconsultarplanoindexadoresvendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarResumoVenda`

**Consultar resumo da venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Obtêm informações referentes a venda consultada.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ResumoVendaRequest`](#uauapimodelsvendaresumovendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Venda.VendaIntegracao.ResumoVenda`](#uauapimodelsvendavendaintegracaoresumovenda) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarUnidadesCompradasPorCPF`

**Consulta unidades compradas pelo número de CPF**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
Possibilita consultar unidades que foram compradas por determinado CPF/CNPJ
1. Valida se o usuário está autenticado (logado) no sitema.
2. Verifica se o Cpf/Cnpj informado existe cadastrado no sistema.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultarUnidadesCompradasPorCPFRequest`](#uauapimodelsvendaconsultarunidadescompradasporcpfrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarUnidadesCompradasPorCPFCNPJ`

**Consulta unidades compradas pelo número de CPF ou CNPJ**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
Possibilita consultar unidades que foram compradas por determinado CPF/CNPJ
1. Valida se o usuário está autenticado (logado) no sitema.
2. Verifica se o Cpf/Cnpj informado existe cadastrado no sistema.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ConsultarUnidadesCompradasPorCPFRequest`](#uauapimodelsvendaconsultarunidadescompradasporcpfrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Venda.VendaIntegracao.UnidadeVendida`](#uauapimodelsvendavendaintegracaounidadevendida) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ConsultarUnidadesCompradasUsrLogado`

**Consulta unidades compradas pelo usuário que está logado**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
Possibilita consultar unidades que foram compradas por determinado usuário.
1. Valida se o usuário está autenticado (logado) no sitema.
2. Usuário só pode ser do tipo pessoa.
3. Valida se o usuário está cadastrado para acesso no UAUWeb.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | - Implementado apenas para usuários do tipo pessoa! - Não existe pessoa cadastrada para acesso ao UAU Web com o login: xxx - Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ExcluirParcelaCusta`

**Reliza a exclusão de Parcela de Custa.**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ExcluirPracelaCusta`](#uauapimodelsvendaexcluirpracelacusta)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ExclusaoDeBoletos`

**Faz a exclusão dos boletos informados**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Possibilita excluir boletos que estão com o status de normal.
2. Será permitido a exclusão de no máximo 20 boletos por requisição.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ListaBoletosExclusaoRequest`](#uauapimodelsvendalistaboletosexclusaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Venda.ListaBoletosExclusaoRequest`](#uauapimodelsvendalistaboletosexclusaorequest) |
| 400 | Não foi possível realizar sua requisição. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ExportarPessoasDaVendaXml`

**Busca as pessoas vinculadas às vendas informadas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Possibilita acesso às pessoas que estão relacionadas com a venda informada.
1. Valida a existência da venda.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ExportarPessoasDaVendaXmlRequest`](#uauapimodelsvendaexportarpessoasdavendaxmlrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de object |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ExportarVendasXml`

**Busca as vendas informadas ou as vendas inseridas/alteradas no periodo informado.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Consultar os dados das contas contábeis com a URI + /api/v{version}/Venda/ExportarVendasXml
3. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite exportar os registros de uma ou mais vendas do UAU para um arquivo XML no formato esperado para realização de importação de vendas.
1. Deve informar a venda ou o período para que seja realizada a consulta.
2. Pode informar as chaves de Venda que são [Empresa, Obra, Venda].
3. Valida as datas e campos inseridos.
4. O perído informado buscará vendas considerando a data de cadastro, a data de manutenção e a data de quitação.
5. O item "listaVendas" permite informar empresa, obra e venda que serão adicionados ao retorno da consulta. 
Não será filtrado exclusivamente por esta lista de vendas, mas serão acrescidas ao resultado do período informado.

VirtUau:
- http://snetapi.globaltec.com.br:90/UAUApi_Integracao/swagger/ui/index#!/Venda/Venda_ExportarVendasXml

 Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/777060/ 
- Arquivo de Retorno: https://ajuda.globaltec.com.br/download/777060/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ExportarVendasXmlRequest`](#uauapimodelsvendaexportarvendasxmlrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de object |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/FinalizarRenegociacao`

**Finalizar uma negociação**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Possibilita finalizar determinada negociação.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.FinalizarRenegociacaoRequest`](#uauapimodelsvendafinalizarrenegociacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/GerarBoletoBancario`

**Gravar o arquivo de remessa para geração do boleto bancario ou carne**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Permite gerar o boleto bancário ou carnê.
2. O usuário autenticado deve ter permissão de inclusão no programa de permissão VEBOLETOAVULSO.
3. Para gerar boleto parcial é necessário informar a propriedade ValorBoleto.
    - Não pode ser um valor negativo nem inferior a 0,01 centavo.
    - Se informar um valor igual ao valor total das parcelas enviadas, será gerado um boleto normal.
    - Se informar um valor menor que o valor total das parcelas enviadas, será gerado um boleto parcial.
        - Apenas uma parcela das enviadas deverá ser parcial
        - Não será gerado boleto caso informe um valor que não cubra todas as parcelas enviadas
        - A ordem de envio das parcelas deve ser a mesma ordem de seleção das parcelas ao gerar o boleto pela tela de recebimento avulso.
        Exemplo: Na tela de recebimento avulso, selecionei as parcelas 360, 359 e 358. Ao gerar pela API, as parcelas devem ser enviadas
        na mesma sequência selecionada.
        - Irá validar se as parcelas enviadas podem gerar o boleto parcial de acordo com a regra de dias para vencimento.
    - Será possível gerar boleto parcial somente para parcelas de uma única empresa, obra e venda.
    - Só é possível gerar boleto parcial para mais de uma parcela quando for antecipação.
    - É obrigatório reajustar ao gerar o boleto parcial.
4. Padrão de cobrança    
    - Não é obrigatório informá-lo.
    - Caso informado, o sistema irá desconsiderar a configuração do parâmetro usarpadraoboleto_avulso e irá gerar o boleto pelo padrão informado.
    - Caso informado, será desconsiderado o padrão de cobrança de todas as parcelas, incluindo custas administrativas, e boleto será gerado com o padrão de cobrança informado.
    - Apenas os padrões de cobrança ativos serão aceitos.
    - Será possivel gerar boleto com o padrão de cobrança informado, somente para parcelas de uma única empresa.
    - Obs.: Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão AVULSO informado no grupo, o sistema irá desconsiderar o padrão informado no JSON e manter o padrão de cobrança da configuração de grupo de cobrança.
5. Excluir Boletos Existentes
    - Não é obrigatório informar o parâmetro ExcluirBoletosExistentes.
    - Caso não seja informado será mantido a opção padrão de não excluir.
    - Caso informado, irá executar as mesmas ações que a configuração 'Excluir boletos já emitidos ao gerar um novo boleto para a parcela' no cadastro de empresas &gt; config. vendas.
6. Reaproveitar boleto
    - Não é obrigatório informar o parâmetro ReaproveitarBoleto
    - Caso não seja informado será mantida a opção padrão de não reaproveitar o boleto,
    - Caso informado, irá tentar reaproveitar algum boleto que já exista para uma das parcelas enviadas.
        - Somente válido para bancos e/ou tipos de cobrança que permitem a manutenção do boleto.
        - Somente para parcelas de uma única empresa, obra e venda. Caso envie parcelas de vendas diferentes, a opção de reaproveitar boleto será desconsiderada e irá gerar um novo boleto.
        - Será gerado arquivo de alteração de vencimento ou valor do boleto.
        - Não será possivel reaproveitar caso não exista boleto gerado ou o agrupamento das parcelas gere mais de um boleto.
    - Sempre homologue junto ao banco antes de usar!
7. Valor taxa boleto
    - Não é obrigatório informar o parâmetro ValorTaxaBoleto
    - Essa taxa será utilizada independente do parâmetro de reaproveitar boleto for true e a venda cobrar taxa de boleto.
    - Caso informado, irá desconsiderar o valor da taxa cadastrado na empresa e aplicar o valor informado.
    - Caso não seja informado ou seja informado zero, irá aplicar o valor da taxa cadastrado na empresa do boleto reaproveitado.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.GerarBoletoBancarioRequest`](#uauapimodelsvendagerarboletobancariorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAU.VendasProxy.ParcelasBoletoRetorno`](#uauvendasproxyparcelasboletoretorno) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/GerarPDFEvolucaoContrato`

**Gerar PDF do relatório da evolução do contrato**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.

Definição de Negócio:
Gera PDF da evolução do contrato em string do tipo Base64.
1. Validações a nível de usuário.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.EvolucaoContratoVendaRequest`](#uauapimodelsvendaevolucaocontratovendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/GerarPDFEvolucaoSaldoDevedorFinanciamento`

**Gerar PDF do relatório de evolução do saldo devedor do financiamento imobiliário**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.

Definição de Negócio:
Gerar PDF do relatório de evolução do saldo devedor do financiamento imobiliário da venda em formato Base64.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.EvolucaoSaldoDevedorRequest`](#uauapimodelsvendaevolucaosaldodevedorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/GerarPDFResumoVenda`

**Gerar PDF do relatório do resumo da venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Para transformar a string de retorno em PDF utilize algo como: Base64 to PDF.

Definição de Negócio:
Gera boleto PDF do resumo da venda em formato Base64.
1. Validações a nível de usuário.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ResumoVendaRequest`](#uauapimodelsvendaresumovendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/GerarVendaDeProposta`

**Efetua a venda da proposta informada e retorna o Objeto Venda da mesma**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Realiza venda de acordo com a proposta informada.
1. Validações serão realizadas para efetuar a operação.
2. Todas alterações informadas no request apenas afetarão a venda gerada.
3. A opção de desconsiderar não titulares avalistas, serve para o caso onde queriam gravar uma venda sem titular avalista, que possa está configurado na proposta.
4. Se informar o lista de não titulares, o sistema vai desconsiderar os da proposta e utilizar os informados no request.
5. A lista de não titulares deve conter o código das pessoas no UAU.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.GerarVendaDePropostaRequest`](#uauapimodelsvendagerarvendadepropostarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Venda.RetornoImportacaoVenda`](#uauapimodelsvendaretornoimportacaovenda) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/GravarNumContratoFinanciamento`

**Altera numero de contrato da venda**

Definição técnica:
- Altera número de contrato para uma venda.

Pré requisito:
- Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
    - URL + /api/v{version}/Venda/GravarNumContratoFinanciamento 
Anexos:
- Exemplo Postman: [ALTERAR EXEMPLO]

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.VendasGravarNumContratoFinanciamentoRequest`](#uauapimodelsvendavendasgravarnumcontratofinanciamentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Número de contrato atualizado com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/GravarOcorrenciaAnexo`

**Anexar uma ocorrência**

Definição técnica:
- Adiciona uma ou várias ocorrências vinculada de anexo de acordo com os parâmetros passados na requisição.

Parâmetros da request
1. Chave: Chave para consulta.
2. Campos: 
    - Campos obrigatórios para a chave="Venda" (empresa, obra, venda, codigo ocorrencia, usuario). 
    - Campos obrigatórios para a chave="Parcela" (empresa, obra, venda, número parcela, número geral da parcela, tipo da parcela, codigo ocorrência, usuario)

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.AnexarOcorrenciaRequest`](#uauapimodelsvendaanexarocorrenciarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso | [`UAUApi.Models.Venda.ResultadoOperacao`](#uauapimodelsvendaresultadooperacao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/GravarPedidoDeRecebimento`

**Gravar pedido de recebimento junto a NTK**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. É obrigatório ter o ambiente de integração com a PAYGO configurado, só após o registro junto a eles que o registro será gerado no UAU.
2. É necessário ter permissão de inclusão no programa VEPEDIDORECEBIMENTO

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.PedidoRecebimentoRequest`](#uauapimodelsvendapedidorecebimentorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoPedido`](#globaltecuauvendasdtoscartaointencaopedido) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ImportacaoDeVenda`

**Importar vendas para o UAU via XML**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Número máximo de importações por vez: 50.
4. Para obter retorno de sucesso ou falha na importação consulte o endpoint:
    - URI + /api/v1.0/Venda/ImportacaoVendaComRetorno

Validação:
1. Arquivo XSD: https://ajuda.globaltec.com.br/wp-content/uploads/2021/01/Manual-de-integracao-de-Vendas_versao1006_2.zip

2. Dicionário de dados: https://ajuda.globaltec.com.br/wp-content/uploads/2021/01/Venda.zip

Definição de Negócio:

Permite importar vendas para o UAU via XML.
1. Valida quantidade de importações por requisição.
2. Caso ocorra erro em uma venda, todas as outras importações são canceladas.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ImportacaoDeVendaRequest`](#uauapimodelsvendaimportacaodevendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de object |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ImportacaoParcelasDeCustas`

**Importar parcelas do tipo Custa**

Definição Técnica:
1. Importação de parcelas do tipo Custas:
 - URI + /api/v{version}/Venda/ImportacaoParcelasDeCustas

Definição de Negócio:
1. Permite importar parcelas do tipo Custas com as seguintes regras:
 - Os campos: Observacao, CobrarJurosAtraso, CobrarMulta, CobrarCorrecao, CobrarImposto, CobrarTxAdm, CobrarRepasseLocador, Competencia, NUMEROPARCELA e MeioPreferencialDeRecebimento são opcionais.

1. Referente a propriedade de CAPs:
  - Caso não sejam informados os CAPs para uma ou mais parcelas de custas, para essas parcelas, será utilizada a configuração padrão de CAPs da empresa;
  - Será possível utilizar em uma mesma requisição parcelas com CAPs definidos no JSON e parcelas com CAPs padrão da empresa (não informado no JSON);
  - Será validada a existência dos CAPs informado e só será possível utilizar CAPs ativos;
  - Caso seja informado um CAP para uma determinada parcela, todos os demais CAPs daquela parcela, serão obrigatórios;
  
Anexos:
1. Link para download de exemplos:
- Exemplo de parcela tipo Custa: https://ajuda.globaltec.com.br/wp-content/uploads/2019/05/UAUApi-Importacao-Parcelas-de-Custas.postman_collection.zip

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ParcelasDeCustaRequest`](#uauapimodelsvendaparcelasdecustarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Bad Request | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ImportacaoVendaComRetorno`

**Importar vendas para o UAU via XML com retorno de venda importada**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Número máximo de importações por vez: 50.

Definição de Negócio:
Possibilita importa vendas via XML para o UAU e receber como retorno as vendas importadas.
1. Valida quantidade de importações por requisição.
2. Caso ocorra erro em uma venda, todas as outras importações são canceladas e terá um retorno com informações da venda que falhou.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ImportacaoDeVendaRequest`](#uauapimodelsvendaimportacaodevendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Venda.RetornoImportacaoVenda`](#uauapimodelsvendaretornoimportacaovenda) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ManterStatusCobrancaVenda`

**Alterar status de cobrança da venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Possibilita alterar o status de cobrança referentes a determinada venda.
Validações serão realizadas para efetuar a operação:
1. Se os parâmetros forem da parcela, o ocorrência será gravada na parcela correspondente.
2. Se os parâmetros forem da venda, o ocorrência será gravada na venda correspondente.
3. Caso seja informado o parâmetro numeroParcela, numeroParcelaGeral ou tipoParcela, os três serão obrigatórios.
4. O parâmetro 'código' deverá ser do tipo numérico.
5. Os status de cobrança da venda ou parcela, serão substituídos pelos status informados.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ManterStatusCobrancaVendaRequest`](#uauapimodelsvendamanterstatuscobrancavendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ManterStatusEscrituracaoVenda`

**Alterar status da escrituração da venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Valida usuário e suas permissões

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ManterStatusEscrituracaoVendaRequest`](#uauapimodelsvendamanterstatusescrituracaovendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/ProcessarRecebimentoParcelas`

**Processa o recebimento de parcelas realizados por outros sistemas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Responsável por processar recebimentos de parcelas com os dados de recebimento e forma de pagamento.
1. A origem do recebimento das parcelas DEVE sempre ser 0.
2. Serão realizadas várias validações para realização da requisição.
3. O valor do desconto aplicado ao recebimento será sempre do objeto de recebimento, o valor do desconto da parcela será aplicado somente pela tela de recebimento avulso.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.ProcessarRecebimentoParcelasRequest`](#uauapimodelsvendaprocessarrecebimentoparcelasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de object |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/RenegociarVenda`

**Realiza a renegociação de parcelas de uma venda realizando as validações necessárias.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método

Definição de Negócio:
Permite renegociar parcelas de uma venda
1. O usuário deverá estar autenticado e validado
2. Informar os dados da venda
3. Informar as parcelas a serem geradas
4. Informar as parcelas escolhidas para renegociação
5. Informar o plano de indexação
6. Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
   retorna mensagem informando a inconsistência encontrada para que seja analisada
7. Após as validações realiza a renegociação das parcelas
8. Será registrado comentário na venda sobre a renegociação realizada
9. Lista de planos indexadores
    - Caso não informe a lista de planos indexadores, serão considerados os planos que já existem na venda. 
    - Caso informe a lista de planos indexadores, a lista informada será considerada.
        - Caso um grupo informado de plano indexador já exista na venda, ele não será inserido novamente.
        - Para verificar se os planos já existem, serão considerados os grupos. Se para um grupo informado, já existir os mesmos indíces e datas na venda, ele não será adicionado.
10. Padrão de Cobrança
    - Padrão de Cobrança Informado no JSON. (Se o tipo de parcela tiver um padrão de cobrança vinculado, esse padrão será priorizado.)
        Exemplo:
        Padrão de cobrança informado: 4
        Parcela: P, Padrão de cobrança: 2
        Parcela: J, Não possui padrão de cobrança
        Parcelas geradas:
        Parcela: P, Padrão de cobrança: 2
        Parcela: J, Padrão de cobrança: 4

    -Padrão de Cobrança Não Informado no JSON:
        - Se o padrão de cobrança não for informado no JSON, ele será consultado pela obra.
        
        - Se o número do padrão de cobrança não for informado no JSON e na obra não estiver cadastrado, será utilizado o padrão de cobrança da primeira parcela
        que foi selecionada para renegociação. Esse padrão de cobrança será então preenchido em todas as parcelas.

VirtUau:
- https://ajuda.globaltec.com.br/virtuau/assistente-de-renegociacao/

 Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/777777/
- Arquivo de Retorno: Retorno será as mensagens de validações ou True indicando que a Renegociação foi realizada com sucesso

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.RenegociarVenda.RenegociarVendaRequest`](#uauapimodelsvendarenegociarvendarenegociarvendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/RetornaChavesVendasPorPeriodo`

**Consulta as chaves das vendas e comentários de status de escrituração de acordo com o período informado**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.   
3. Formatação das chaves de resposta:
        "Empresa-Obra/Venda, Empresa-Obra/Venda, Empresa-Obra/Venda"
        "01705-B1705/00159,01705-B1705/00160,01705-B1705/00161"

Definição de Negócio:
1. Permite consultar as chaves das vendas que foram inseridas, tiveram manutenção ou foram quitadas no período informado.
2. Se o campo "status_escrituracao" do request for marcado como "true" serão retonadas as chaves que tiveram alterações no status de escrituração.
3. Parâmetro opcional para request: statusVenda.  0 - Normal, 1 - Cancelada, 3 - Quitado, 4 - Em acerto, 5 Aluguel antecipado.
4. Parâmetros opcionais para request: codigoEmpresa e codigoObra.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.RetornaChavesVendasPorPeriodoRequest`](#uauapimodelsvendaretornachavesvendasporperiodorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Venda/VendaValidaParaManutencao`

**Valida se a venda pode ser renegociada pela tela de renegociação na Web.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Valida a possibilidade de realizar a renegociação da venda, para tal tarefa a venda não pode ter restrições.
1. Os campos inseridos na request serão utilizado para buscar e verificar disponibilidade de renegociação.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Venda.VendaValidaParaManutencaoRequest`](#uauapimodelsvendavendavalidaparamanutencaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Venda.VendaValidaParaManutencaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |
| `venda` | integer (int32) | ✓ | Código da venda |
| `usr_logado` | string | ✓ | Usuário logado |
| `mensagem_securitizacao` | string |  |  |

### UAUApi.Models.Venda.RetornaChavesVendasPorPeriodoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `data_inicio` | string (date-time) |  | Data inicial |
| `data_fim` | string (date-time) |  | Data final |
| `status_escrituracao` | boolean |  | Status escrituração com alterações ("true": aceita, "false": rejeita) |
| `statusVenda` | string |  | Status da venda  0 - Normal, 1 - Cancelada, 3 - Quitado, 4 - Em acerto, 5 Aluguel antecipado. |
| `listaEmpresaObra` | array de [`UAUApi.Models.Venda.EmpresaObra`](#uauapimodelsvendaempresaobra) |  |  |

### UAUApi.Models.Venda.EmpresaObra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa |
| `codigoObra` | string |  | Código a obra |

### UAUApi.Models.Venda.RenegociarVenda.RenegociarVendaRequest

Dados da venda renegociados pela API

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `Venda` | integer (int32) | ✓ | Número do contrato a ser renegociado (Venda, aluguel, aluguel shopping, etc) |
| `Parc_Geradas` | array de [`UAUApi.Models.Venda.RenegociarVenda.ParcelaRenegociacaoRequest`](#uauapimodelsvendarenegociarvendaparcelarenegociacaorequest) | ✓ | Novas parcelas geradas após realizar a renegociação |
| `ParcSel_Reneg` | array de [`UAUApi.Models.Venda.RenegociarVenda.ParcelaSelRenegociacaoRequest`](#uauapimodelsvendarenegociarvendaparcelaselrenegociacaorequest) | ✓ | Tabela com as parcelas originais, selecionadas para ser renegociada (somente chave) |
| `ValDesc_reneg` | number (double) |  | Valor de desconto utilizado na renegociação |
| `ValAcresc_reneg` | number (double) |  | Valor de acréscimo utilizado na renegociação |
| `Valor_Reajustado` | integer (int32) |  | Renegociação será feita com  [1]-valores reajustado ou [0]-valores dos principais |
| `NumeroPadraoCobranca` | integer (int32) |  | Número do padrão de cobrança as ser usado nas novas parcelas geradas após renegociação |
| `Tabelaplano_idx` | array de [`UAUApi.Models.Venda.RenegociarVenda.PlanoIndexadorRenegociacaoRequest`](#uauapimodelsvendarenegociarvendaplanoindexadorrenegociacaorequest) |  | Plano indexador novo a ser utilizado pela venda renegociada |
| `DataCalculo` | string |  | Data de cálculo das parcelas a serem renegociada |

### UAUApi.Models.Venda.RenegociarVenda.PlanoIndexadorRenegociacaoRequest

Dados dos planos indexadores renegociados pela API

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumPlano_pip` | integer (int32) |  | Número do grupo |
| `CodigoIdx_pip` | string |  | Código do índice utilizado no grupo |
| `Data_pidx` | string (date-time) |  | Data que inicia o cálculo de correção do grupo |

### UAUApi.Models.Venda.RenegociarVenda.ParcelaSelRenegociacaoRequest

Dados das parcelas selecionadas para renegociação pela API

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumParc_pg` | integer (int32) | ✓ | Número da parcela |
| `NumParcGer_pg` | integer (int32) | ✓ | Número geral da parcela (identificador) |
| `Tipo_pg` | string | ✓ | Tipo da parcela |

### UAUApi.Models.Venda.RenegociarVenda.ParcelaRenegociacaoRequest

Dados das parcelas renegociados pela API

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumParc_pg` | integer (int32) | ✓ | Número da parcela |
| `NumParcGer_pg` | integer (int32) | ✓ | Número geral da parcela (identificador) |
| `Tipo_pg` | string | ✓ | Tipo da parcela |
| `Valor_pg` | number (double) | ✓ | Valor principal |
| `Data_pg` | string (date-time) | ✓ | Data de vencimento |
| `DtParc_pg` | string (date-time) | ✓ | Data da primeira parcela do grupo Preencher com a data de vencimento da primeira parcela |
| `AmortParc_pg` | integer (int32) | ✓ | Tipo de amortização 0-Gradiente 1-Price 2-SAC 3-Simples |
| `BeginEndParc_pg` | integer (int32) | ✓ | 0-Begin ou 1-End (quando for amortização PRICE) |
| `GrupoParc_pg` | integer (int32) | ✓ | Número do grupo que a parcela pertence |
| `TotParcGrupo_pg` | integer (int32) | ✓ | Total de parcelas do grupo |
| `ComoParc_pg` | string | ✓ | Frequência de vencimento (mensal, semestral, anual etc...) |
| `DtJurParc_pg` | string (date-time) | ✓ | Data de início de cobrança da 1ª taxa de juros contratuais |
| `JurosParc_pg` | number (double) | ✓ | 1ª Taxa de juros contratual |
| `DataSegJuros_pg` | string (date-time) |  | Data de início de cobrança da 2ª taxa de juros contratuais |
| `PorcSegJuros_pg` | number (double) |  | 2ª Taxa de juros contratual |
| `DtIdxParc_pg` | string (date-time) | ✓ | Data do início da correção indexada |
| `IdxReaj_pg` | string | ✓ | Código do índice de reajuste |
| `GrupoIdx_pg` | integer (int32) | ✓ | Número do plano indexador utilizado no cálculo |
| `DtJurosComJuros_pg` | integer (int32) | ✓ | Cobrar juros no mês/dia da data de juros |
| `CobrarJurosProRata_pg` | integer (int32) | ✓ | Cobrar juros pró-rata |
| `CobrarJurosProRataPrimeiroMes_pg` | integer (int32) | ✓ | Cobrar juros pró-rata 1º mês |
| `CarenciaAtraso_pg` | integer (int32) | ✓ | Dias de carência para multa e juros por atraso |
| `CarenciaAtrasoCorrecao_pg` | integer (int32) | ✓ | Dias de carência para cobrar correção atraso |
| `DataCompetencia_pg` | string (date-time) |  | Data do início do período de aluguel |
| `CobrarMulta_pg` | integer (int32) | ✓ | Cobrar multa (parcela de custas) 0-Não 1-Sim |
| `CobrarJurosAtr_pg` | integer (int32) | ✓ | Cobrar juros por atraso (parcela de custas) 0-Não 1-Sim |
| `CobrarCorrecao_pg` | integer (int32) | ✓ | Cobrar correçao (parcela de custas) 0-Não 1-Sim |
| `CobrarTxAdm_pg` | integer (int32) | ✓ | Cobrar taxa de administração (parcela de custas) 0-Não 1-Sim |
| `CobrarImposto_pg` | integer (int32) | ✓ | Cobrar imposto (parcela de custas) 0-Não 1-Sim |
| `CobrarCPMF_pg` | integer (int32) | ✓ | Cobrar CPMF (parcela de custas) 0-Não 1-Sim |
| `OrigemCusta_pg` | integer (int32) | ✓ | Origem da custa [0 - Obra / 1 - Administração] (parcela de custas) |
| `RepassarLocador_pg` | integer (int32) | ✓ | Repassar locador (parcela de custas) 0-Não 1-Sim |
| `NumCtp_pg` | integer (int32) |  | Tipo da custa [Honorários, IPTU, etc.. cadastro sistema] (parcela de custas) |
| `TipoSeguro_pg` | integer (int32) |  | Tipo de seguro [0 - MIP / 1 - DFI] (parcelas de seguro) |
| `TotParc_pg` | integer (int32) | ✓ | Total de parcelas |
| `Cap_pg` | string | ✓ | Cap principal |
| `CapAcrescimo_pg` | string | ✓ | Cap de acréscimo |
| `CapDesconto_pg` | string | ✓ | Cap de desconto |
| `CapDescontoCusta_pg` | string | ✓ | Cap de desconto de custas |
| `CapDescontoAntec_pg` | string | ✓ | Cap de desconto de antecipação |
| `CapCorrecao_pg` | string | ✓ | Cap de correção |
| `CapCorrecaoAtr_pg` | string | ✓ | Cap de correção por atraso |
| `CapDescontoCondicional_pg` | string | ✓ | Cap de desconto condicional |
| `CapJuros_pg` | string | ✓ | Cap de juros contratual |
| `CapJurosAtr_pg` | string | ✓ | Cap de juros por atraso |
| `CapMulta_pg` | string | ✓ | Cap de multa |
| `CapRepasse_pg` | string | ✓ | Cap de repasse |
| `CapTaxaBol_pg` | string | ✓ | Cap de taxa de boleto |

### UAUApi.Models.Venda.ProcessarRecebimentoParcelasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `recebimento` | [`UAUApi.Models.Venda.DTORecebimentoSimplificado`](#uauapimodelsvendadtorecebimentosimplificado) | ✓ | Dados do recebimento |
| `formaPagamento` | [`UAUApi.Models.Venda.DTOFormaPagamento`](#uauapimodelsvendadtoformapagamento) | ✓ | Dados do pagamento |

### UAUApi.Models.Venda.DTOFormaPagamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Cheques` | array de [`UAUApi.Models.Venda.DTOCheque`](#uauapimodelsvendadtocheque) |  | Lista de cheques |
| `Bens` | array de [`UAUApi.Models.Venda.DTOBens`](#uauapimodelsvendadtobens) |  | Lista de bens |
| `Dinheiro` | array de [`UAUApi.Models.Venda.DTODinheiro`](#uauapimodelsvendadtodinheiro) |  | Lista de pagamentos em dinheiro |
| `CredEletro` | array de [`UAUApi.Models.Venda.DTOCreditoEletronico`](#uauapimodelsvendadtocreditoeletronico) |  | Lista de créditos eletrônicos |
| `Cartao` | array de [`UAUApi.Models.Venda.DTOCartao`](#uauapimodelsvendadtocartao) |  | Lista de cartão |

### UAUApi.Models.Venda.DTOCartao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumControle` | integer (int32) |  | Num. controle |
| `Valor` | number (double) |  | Valor |
| `QuemRecebeu` | string |  | Login |
| `DataRecebimento` | string (date-time) |  | Data do recebimento |
| `NumTerminal` | integer (int32) |  | Número do terminal |
| `NSU` | string |  | Número sequencial unico |
| `NumReferencia` | string |  | Número de referencia |
| `CodAutorizacao` | string |  | Código da autorizacao |
| `Modalidade` | integer (int32) |  | Modalidade |
| `TotalParcelas` | integer (int32) |  | Se foi pago em crédito, informar em quantas parcelas. Para crédito avista e débito enviar 1. |
| `Comprovante` | string |  | Comprovante do pagamento |

### UAUApi.Models.Venda.DTOCreditoEletronico

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumControle` | integer (int32) |  | Num. controle |
| `Valor` | number (double) |  | Valor |
| `QuemRecebeu` | string |  | Login do usuário que recebeu. |
| `DataRecebimento` | string (date-time) |  | Data do recebimento |
| `DataDeposito` | string (date-time) |  | Data de depósito |
| `DataConciliacao` | string (date-time) |  | Data de conciliação. (Se houver uma lista de pagamentos com crédito eletrônico, a data de conciliação será determinada pela data mais recente registrada entre os pagamentos.) |

### UAUApi.Models.Venda.DTODinheiro

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumControle` | integer (int32) |  | Número do controle |
| `Valor` | number (double) |  | Valor |
| `QuemRecebeu` | string |  | Login do usuário que recebeu. |
| `DataRecebeu` | string (date-time) |  | Data recebeu |

### UAUApi.Models.Venda.DTOBens

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumBem` | integer (int32) |  | Nº do Bem |
| `Descricao` | string |  | Descrição |
| `Valor` | number (double) |  | Valor |
| `QuemRecebeu` | string |  | Quem Recebeu |
| `QuemRespons` | string |  | Quem Respons. |
| `DataRecebeu` | string (date-time) |  | Quem Respons. |

### UAUApi.Models.Venda.DTOCheque

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Banco` | integer (int32) |  | Banco |
| `Agencia` | string |  | Agencia |
| `Conta` | string |  | Conta |
| `NumCheque` | string |  | Nº do Cheque |
| `DataCadastro` | string (date-time) |  | Dt de Cadas. do Chq |
| `Valor` | number (double) |  | Valor |
| `Titular` | string |  | Titular |
| `QuemRecebeu` | string |  | Quem Recebeu o cheque |
| `Predatado` | string (date-time) |  | Data pré-datada para recebimento do cheque |
| `ValorDescontoCedido` | number (double) |  | Vlr do desconto cedido [CALCULADO] |
| `ValorAcrescimoCedido` | number (double) |  | Vlr do Acréscimo cedido [CALCULADO] |
| `NumeroControle` | integer (int32) |  | Nº de controle |
| `TipoValorJurosPredatado` | integer (int32) |  | Informa a forma da distribuição dos juros gerados pelos cheques pré-datados |

### UAUApi.Models.Venda.DTORecebimentoSimplificado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa do recebimento. |
| `Banco` | string |  | Número do banco de deposito. |
| `Conta` | string |  | Número da conta de deposito. |
| `HistContabil` | string |  | Histórico contábil |
| `UsuarioLogado` | string |  | Usuário logado |
| `TipoRecebimento` | integer (int32) — valores possíveis: 0, 1, 2, 3 |  | Tipo de recebimento: todas as parc, parte das parc, todas as parc e parte residuo, recebimento total resíduo 0 - Realizar o recebimento total das parcelas 1 - Realizar o recebimento de parte das parcelas 2 - Realizar o recebimento total das parcelas e parte do resíduo 3 - Realizar o recebimento total do resíduo |
| `DataRecebimento` | string (date-time) |  | Data de recebimento |
| `ValorJurosPreDatado` | number (double) |  | Armazena o valor do juros pré-datado, para saber se gera uma nova parcela com o mesmo ou não. |
| `DataParcelaPreDatada` | string (date-time) |  | Data para vencimento da parcela referente ao juros que faltaram para cheques pré-datados. |
| `ValorLiquidoRecebido` | number (double) |  | Liquido Recebido |
| `ValorDesconto` | number (double) |  | Valor de Desconto concedido no recebimento. |
| `ValorAcrescimo` | number (double) |  | Valor de Acrescimo concedido no recebimento. |
| `DataCalculo` | string (date-time) |  | Data de cálculo para utilizar no recebimento das parcelas. |
| `Antecipacao` | boolean |  | Identifica se é para calcular as parcelas antecipadas ou não. |
| `NovaDataVenc` | string (date-time) |  | Nova data de vencimento para a parcela que será gerada (recebimento parcial) |
| `ReceberResiduo` | boolean |  | Verificar se é para receber o residuo. |
| `OrigemRecebimento` | integer (int32) — valores possíveis: 0, 1 |  | Origem do recebimento das parcelas 0 - Venda 1 - Proposta |
| `Parcelas` | array de [`UAUApi.Models.Venda.DTORecebimentoParcelaSimplificada`](#uauapimodelsvendadtorecebimentoparcelasimplificada) |  | Parcelas a serem recebidas. |

### UAUApi.Models.Venda.DTORecebimentoParcelaSimplificada

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumParc` | integer (int32) |  | Nº da parcela |
| `NumParcGer` | integer (int32) |  | Nº de Parcela geral |
| `NumeroContrato` | integer (int32) |  | Numero do contrato (Venda ou Proposta) |
| `Obra` | string |  | Número da obra do recebimento. |
| `TipoParc` | string |  | Tipo da parcela: Balão,Parcela,entrada,Cache |
| `ValorDesconto` | number (double) |  | Valor do desconto da parcela. ***Só é aplicado por recebimento Avulso.*** |

### UAUApi.Models.Venda.ManterStatusEscrituracaoVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa. |
| `obra` | string | ✓ | Código da obra. |
| `venda` | integer (int32) | ✓ | Número da venda. |
| `statusEscrituracao` | array de [`UAUApi.Models.Venda.CodigoStatus`](#uauapimodelsvendacodigostatus) |  | Código de status de escrituração da venda. (Lista de objeto de códigos) |

### UAUApi.Models.Venda.CodigoStatus

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo` | integer (int32) |  |  |

### UAUApi.Models.Venda.ManterStatusCobrancaVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa. |
| `obra` | string | ✓ | Código da obra. |
| `venda` | integer (int32) | ✓ | Número da venda. |
| `numeroParcela` | integer (int32) |  | Número da parcela da venda. |
| `numeroParcelaGeral` | integer (int32) |  | Número da parcela geral. |
| `tipoParcela` | string |  | Tipo da parcela. |
| `statusCobranca` | array de [`UAUApi.Models.Venda.CodigoStatus`](#uauapimodelsvendacodigostatus) |  | Código de status de cobrança da venda. (Lista de objeto de códigos) |

### UAUApi.Models.Venda.ParcelasDeCustaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `custas` | array de [`UAUApi.Models.Venda.CustaRequest`](#uauapimodelsvendacustarequest) | ✓ | Lista de custas. |

### UAUApi.Models.Venda.CustaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa. |
| `Obra` | string | ✓ | Código da obra. |
| `Venda` | integer (int32) | ✓ | Número da venda. |
| `Valor` | number (double) | ✓ | Valor principal da parcela. |
| `Origem` | integer (int32) | ✓ | Origem da parcela. |
| `PlanoIdx` | integer (int32) | ✓ | Plano indexador da parcela. |
| `Tipo` | integer (int32) | ✓ | Tipo da custa. |
| `Frequencia` | string | ✓ | Frequência de vencimento utilizada na parcela. |
| `Reajuste` | string | ✓ | Código do índice de reajuste da parcela |
| `DtVencimento` | string (date-time) | ✓ | Data de vencimento da parcela. |
| `DtReajuste` | string (date-time) | ✓ | Data de cálculo utilizada para calcular o valor de reajuste de uma parcela recebida. |
| `PadraoCobranca` | integer (int32) | ✓ | Código do padrão de cobrança utilizado na parcela. |
| `Observacao` | string |  | Observação da parcela do tipo custa específica. |
| `CobrarJurosAtraso` | integer (int32) |  | Indica se irá haver cobrança de juros por atraso na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarMulta` | integer (int32) |  | Indica se irá haver cobrança de multa por atraso na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarCorrecao` | integer (int32) |  | Indica se irá haver cobrança de correção na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarImposto` | integer (int32) |  | Indica se irá haver cobrança de imposto na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarTxAdm` | integer (int32) |  | Indica se irá haver cobrança de taxa de administração na parcela Do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarRepasseLocador` | integer (int32) |  | Indica se irá haver repasse ao locador para a parcela do tipo custa específica. 0 - Não 1 - Sim |
| `DataDeCompetencia` | string (date-time) |  | Competência/Início do período de aluguel(Aluguel, Aluguel Garantido e Aluguel Shopping) |
| `NUMEROPARCELA` | integer (int32) |  | Número da parcela da venda. |
| `MeioPreferencialDeRecebimento` | integer (int32) |  | Meio preferencial de recebimento da custa |
| `Cap` | [`UAUApi.Models.Venda.CapImportacaoCustasRequest`](#uauapimodelsvendacapimportacaocustasrequest) |  | Caps para a parcela de custas |

### UAUApi.Models.Venda.CapImportacaoCustasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CapPrincipal` | string |  | Cap principal |
| `CapAcrescimo` | string |  | Cap de acréscimo |
| `CapCorrecao` | string |  | Cap de Correção |
| `CapCorrecaoAtraso` | string |  | Cap de correção atraso |
| `CapDesconto` | string |  | Cap de desconto |
| `CapDescontoAntecipacao` | string |  | Cap de desconto de antecipação |
| `CapDescontoCondicional` | string |  | Cap de desconto condicional |
| `CapDescontoCusta` | string |  | Cap de desconto custa |
| `CapJuros` | string |  | Cap de juros |
| `CapJurosAtraso` | string |  | Cap de juros por atraso |
| `CapMulta` | string |  | Cap de multa |
| `CapRepasse` | string |  | Cap de repasse |
| `CapTaxaBoleto` | string |  | Cap de taxa de boleto |

### UAUApi.Models.Venda.ImportacaoDeVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `xml_vendas` | string | ✓ | XML de importação das vendas |
| `alterarnumerodas_vendas` | boolean | ✓ | Gerar novo número para as vendas importadas. True False |

### UAUApi.Models.Venda.PedidoRecebimentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empesa |
| `Obra` | string | ✓ | Código da obra |
| `NumContrato` | integer (int32) | ✓ | Número da venda ou da proposta de venda |
| `Estabelecimento` | string | ✓ | Número do estabelecimento |
| `FormaPgto` | integer (int32) | ✓ | Forma de pagamento (0 - Débito, 1 - Crédito a vista, 2 - Crédito sem juros) |
| `QtdeParcelas` | integer (int32) | ✓ | Quantidade de parcelas que será realizado o recebimento. Para forma de pagamento Débito e Crédito a vista, a quantidade de parcelas dever ser = 1. |
| `DataCalculo` | string (date-time) | ✓ | Data de cálculo para reajuste das parcelas |
| `ValorLiquido` | number (double) |  | Valor total do pedido. Deverá ser informado somente quando o tipo de recebimento for 1 - Parte das parcelas |
| `TipoRecebimento` | integer (int32) | ✓ | Tipo de recebimento: todas as parcelas, parte das parcelas, 0 - Realizar o pedido de recebimento total das parcelas 1 - Realizar o pedido de recebimento de parte das parcelas |
| `Antecipacao` | boolean | ✓ | Indica se está antecipando as parcelas True - Está antecipando False - Não está antecipando |
| `Parcelas` | array de [`UAUApi.Models.Venda.ParcelasPedido`](#uauapimodelsvendaparcelaspedido) | ✓ | Lista de objeto (Parcelas) com as parcelas que será realizada o inserção do pedido de recebimento junto a NTK. |

### UAUApi.Models.Venda.ParcelasPedido

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroParcela` | integer (int32) | ✓ | Número da parcela |
| `NumeroParcelaGeral` | integer (int32) | ✓ | Número geral da parcela |
| `TipoParcela` | string | ✓ | Tipo da parcela |
| `ValorDesconto` | number (double) |  | Valor do desconto da parcela |
| `ValorDescontoAntecipado` | number (double) |  | Valor do desconto de antecipação aplicado na parcela |

### UAUApi.Models.Venda.ResultadoOperacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Mensagem` | string |  |  |

### UAUApi.Models.Venda.AnexarOcorrenciaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Ocorrencias` | array de [`UAUApi.Models.Venda.DadosAnexarOcorrencia`](#uauapimodelsvendadadosanexarocorrencia) | ✓ |  |

### UAUApi.Models.Venda.DadosAnexarOcorrencia

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Chave` | string |  |  |
| `Campos` | array de [`UAUApi.Models.Venda.DadosCamposOcorrencia`](#uauapimodelsvendadadoscamposocorrencia) | ✓ |  |

### UAUApi.Models.Venda.DadosCamposOcorrencia

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  |  |
| `obra` | string |  |  |
| `numeroVenda` | integer (int32) |  |  |
| `numeroParcela` | integer (int32) |  |  |
| `numeroGeralParcela` | integer (int32) |  |  |
| `tipoParcela` | string |  |  |
| `codigoOcorrencia` | integer (int32) |  |  |
| `usuario` | string |  |  |
| `observacao` | string |  |  |

### UAUApi.Models.Venda.VendasGravarNumContratoFinanciamentoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codgEmpresa` | integer (int32) | ✓ | Código da empresa |
| `codgObra` | string | ✓ | Código da obra |
| `numVenda` | number (double) | ✓ | Código da venda |
| `codgUsuario` | string | ✓ | Usuário do sistema |
| `numContrato` | string | ✓ | Número do contrato |

### UAUApi.Models.Venda.RetornoImportacaoVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `retornoImportacaoVendaXml` | [`UAUApi.Models.Venda.RetornoImportacaoVendaXml`](#uauapimodelsvendaretornoimportacaovendaxml) |  |  |
| `listaVenda` | array de [`UAUApi.Models.Venda.Venda`](#uauapimodelsvendavenda) |  |  |

### UAUApi.Models.Venda.Venda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa. |
| `Obra` | string |  | Código da obra. |
| `Numero` | integer (int32) |  | Número da venda. |
| `ContratoDeMedicao` | integer (int32) |  | Número do contrato de medição. |
| `CodigoVendedor` | integer (int32) |  | Código do vendedor. |
| `CpfCnpjVendedor` | string |  | CPf ou Cnpj do vendedor. |
| `ValorTotal` | number (double) |  | Valor total da venda. |
| `PercentualJurosAtraso` | number (double) |  | Percentual dos juros de atraso. |
| `Multa` | number (double) |  | Valor da multa. |
| `Desconto` | number (double) |  | Valor do desconto. |
| `Usuario` | string |  | Código do usuário de cadastro da venda. |
| `DataDaVenda` | string (date-time) |  | Data da venda. |
| `StatusVenda` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4 |  | Status da venda. 0 - Normal 1 - Cancelada 2 - Alterada 3 - Quitada 4 - Em acerto |
| `Acrescimo` | number (double) |  | Valor de acréscimo. |
| `ContinuarCobrandoJurosContratualAoAtrasarParcela` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá continuar cobrando juros contratual ao atrasar as parcelas da venda. 0 - Não 1 - Sim |
| `StatusEscritura` | array de integer (int32) |  | Lista de status de escritura vinculados à venda. |
| `StatusCobranca` | array de integer (int32) |  | Lista de status de cobrança vinculados à venda. |
| `PossuiReajusteAnual` | integer (int32) |  | Indica se o cálculo do reajuste não será mensal. 0 - Não (significa que o cálculo de reajuste será mensal) 1 - Sim (significa que o cálculo de reajuste não será mensal, ou seja, será semestral ou anual |
| `GerarResiduo` | integer (int32) |  | Indica se irá gerar resíduo no caso de calcular reajuste não mensal. 0 - Não  1 - Sim |
| `CarenciaAtraso` | integer (int32) |  | Número de dias de carência para cobrança de juros e multa por atraso. |
| `QuantidadeMesesRetroagirCorrecao` | integer (int32) |  | Número de meses que irá retroagir a data de reajuste. |
| `DataBaseResiduo` | string (date-time) |  | Data base para geração das parcelas de resíduo. |
| `PossuiCorrecaoPorAtraso` | integer (int32) |  | Indica se irá cobrar correção por atraso. 0 - Não 1 - Sim |
| `PossuiCorrecaoProRata` | integer (int32) |  | Indica se o cálculo da correção será pró-rata. 0 - Não 1 - Sim |
| `DataCessaoDeDireito` | string (date-time) |  | Data de cessão de direitos. |
| `DataCancelamento` | string (date-time) |  | Data de cancelamento da venda. |
| `CodigoDeDivulgacao` | integer (int32) |  | Código do meio de divulgação que originou a venda. |
| `CodigoFinalidade` | integer (int32) |  | Código da finalidade da compra que originou a venda. |
| `CobrarTaxaDeBoleto` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá cobrar taxa de boleto para os boletos emitidos para a venda. 0 - Não 1 - Sim |
| `DataDeCadastro` | string (date-time) |  | Data de cadastro da venda. |
| `ObraFiscal` | string |  | Código da obra fiscal. |
| `TipoDeVenda` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5 |  | Código do tipo da venda. 0 - Venda 1 - Aluguel 2 - Aluguel Garantido 3 - Transação financeira 4 - Revenda 5 - Aluguel shopping |
| `AluguelShopping` | [`UAUApi.Models.Venda.AluguelDeShopping`](#uauapimodelsvendaalugueldeshopping) |  | Parâmetros de um aluguel shopping. |
| `DiaDoRepasse` | integer (int32) |  | Define o dia do mês que será repassado o valor de aluguel para o(s) proprietário(s). |
| `ValorProvisaoCurto` | number (double) |  | Valor de provisionamento de curto prazo. |
| `ValorProvisaoLongo` | number (double) |  | Valor de provisionamento de longo prazo. |
| `CapProvisaoCurto` | string |  | CAP do valor de provisionamento de curto prazo. |
| `CapProvisaoLongo` | string |  | CAP do valor de provisionamento de longo prazo. |
| `DiasCarenciaCorrecaoPorAtraso` | integer (int32) |  | Número de dias de carência para cobrança de correção por atraso. |
| `AnteciparCorrecao` | integer (int32) |  | Indica se será cobrado correção diária ao realizar antecipação das parcelas da venda. 0 - Não 1 - Sim |
| `CobrarJurosPosChave` | integer (int32) — valores possíveis: 0, 1 |  | Indica se uma parcela, cujo vencimento seja anterior ao início de juros, caso seja recebido após a data de início de juros, irá cobrar juros. 0 - Não 1 - Sim |
| `DataInicioContrato` | string (date-time) |  | Data do início do contrato de venda ou aluguel. |
| `DataFimContrato` | string (date-time) |  | Data do fim do contrato de venda ou aluguel. |
| `TipoDeFianca` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5, 6, 7 |  | Código que define o tipo da fiança da venda.  0 - Sem fiança 1 - Fiadores 2 - Fiança bancária 3 - Caução 4 - Seguro fiança locaticia 5 - Carta fiança 6 - Título de capitalização 7 - Imóvel em garantia |
| `DadosDaFianca1` | string |  | Informação do tipo de fiança da venda. |
| `DadosDaFianca2` | string |  | Informação do tipo de fiança da venda. |
| `DadosDaFianca3` | string |  | Informação do tipo de fiança da venda. |
| `DataDaFianca` | string (date-time) |  | Data da fiança. Seu contexto varia de acordo com o tipo da fiança . |
| `ValorDaFianca` | number (double) |  | Valor da fiança. Seu contexto varia de acordo com o tipo da fiança. |
| `NomeSeguroIncendio` | string |  | Nome da seguradora responsável pelo seguro contra incêndio. |
| `ApoliceSeguroIncendio` | string |  | Número da apólice do seguro contra incêndio. |
| `ValorSeguroIncendio` | number (double) |  | Valor da apólice do seguro contra incêndio. |
| `DataVencimentoSeguroIncendio` | string (date-time) |  | Data do vencimento do seguro contra incêndio. |
| `CobrarMultaFracionada` | integer (int32) — valores possíveis: 0, 1 |  | Indica se a multa cobrada em caso de atraso da parcela será cobrada fracionada por dia. 0 - Não 1 - sim |
| `AnteciparJurosLinear` | integer (int32) |  | Indica se a antecipação das parcelas com juros simples será realizada de forma linear. 0 - Não 1 - sim |
| `ValorDescontoImposto` | number (double) |  | Valor total de imposto lançado na venda. |
| `PeriodoDeReajuste` | integer (int32) |  | Indica a periodicidade de reajuste nos casos de correção não mensal. |
| `HistoricoLancamentoContabilVenda` | string |  | Histórico de lançamento contábil da venda. |
| `HistoricoLancamentoContabilParcela` | string |  | Histórico de lançamento contábil das parcelas da venda. |
| `HistoricoLancamentoContabilJurosCorrecao` | string |  | Histórico de lançamento contábil dos juros e correções da venda. |
| `ZerarCorrecaoNegativa` | integer (int32) |  | Indica se irá zerar o valor de correção da parcela nos casos que o valor líquido da mesma seja inferior ao valor principal. 0 - Não 1 - Sim |
| `CobrarJurosPorAtrasoMensal` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o cálculo de juros por atraso será realizado de forma mensal ou pró-rata. 0 - Não 1 - Sim |
| `CorrecaoCrescente` | integer (int32) |  | Indica se irá congelar o valor de correção da parcela caso o índice de correção da mesma possua deflação entre o mês anterior e o atual. 0 - Não 1 - Sim |
| `EnviarSpedPisCofins` | integer (int32) — valores possíveis: 0, 1 |  | Indica se a venda ou aluguel será enviado para o SPED PIS/CONFINS. 0 - Não 1 - Sim |
| `ContratoCaixaEconomicaFederal` | string |  | Número do contrato de financiamento associativo da venda na Caixa Econômica Federal. |
| `Atividade` | integer (int32) — valores possíveis: 0, 1, 2, 3 |  | Código do tipo de atividade da venda. 0 - Atividade imobiliária 1 - Prestação de serviço |
| `ValorProvisaoCurtoBaixa` | number (double) |  | Valor de provisionamento de curto prazo no momento da quitação/cancelamento da venda. |
| `ValorProvisaoLongoBaixa` | number (double) |  | Valor de provisionamento de longo prazo no momento da quitação/cancelamento da venda. |
| `ValorProvisaoCurtoCessao` | number (double) |  | Valor de provisionamento de curto prazo no momento da realização de cessão de direito da venda. |
| `ValorProvisaoLongoCessao` | number (double) |  | Valor de provisionamento de longo prazo no momento da realização de cessão de direito da venda. |
| `CapProvisaoCurtoBaixa` | string |  | CAP do valor de provisionamento de curto prazo no momento da quitação/cancelamento da venda. |
| `CapProvisaoLongoBaixa` | string |  | CAP do valor de provisionamento de longo prazo no momento da quitação/cancelamento da venda. |
| `HistoricoLancamentoBaixaProvisao` | string |  | Histórico de lançamento contábil do provisionamento no momento da quitação/cancelamento da venda. |
| `CobrarCorrecaoMaisProrataMesRecebimento` | integer (int32) — valores possíveis: 0, 1 |  | Indica se deverá cobrar correção mais prórata no mês de recebimento da parcela da venda. |
| `CobrarJurosAnual` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o cálculo de juros contratual da venda será mensal. 0 - Não 1 - Sim |
| `PeriodoCobrancaDeJuros` | integer (int32) |  | Indica a periodicidade de reajuste nos casos de correção não mensal. |
| `ValorPrestacaoDeServicos` | number (double) |  | Valor de prestação de serviço da venda. |
| `AnteciparCorrecaoProximoPeriodo` | integer (int32) |  | Indica se o cálculo de correção ao antecipar as parcelas da venda será realizado apenas no próximo período da venda de acordo com a data de cálculo. 0 - Não 1 - Sim |
| `VendaVinculada` | [`UAUApi.Models.Venda.VendaVinculada`](#uauapimodelsvendavendavinculada) |  | Venda a qual a venda está vinculada. |
| `CodigoUltimaManutencao` | integer (int32) |  | Código da última manutenção. |
| `TributadoPeloRet` | integer (int32) — valores possíveis: 0, 1 |  | Tributado pelo retorno. 0 - Não 1 - Sim |
| `TributacaoRET` | string |  | Tributado do retorno. |
| `CodigoServico` | integer (int32) |  | Código do serviço. |
| `ValorTotalImposto` | number (double) |  | Valor total do imposto. |
| `ValorTotalComissao` | number (double) |  | Valor total da comissão. |
| `Parametros` | array de [`UAUApi.Models.Venda.ParametrosDaVenda`](#uauapimodelsvendaparametrosdavenda) |  | Parâmetros da venda. |
| `Clientes` | array de [`UAUApi.Models.Venda.ClienteDaVenda`](#uauapimodelsvendaclientedavenda) |  | Lista de clientes da venda. |
| `Itens` | array de [`UAUApi.Models.Venda.ItemDaVenda`](#uauapimodelsvendaitemdavenda) |  | Lista dos itens vendidos na venda. |
| `Parcelas` | array de [`UAUApi.Models.Venda.Parcela`](#uauapimodelsvendaparcela) |  | Lista de parcelas a receber e recebidas da venda. |
| `Impostos` | array de [`UAUApi.Models.Venda.ImpostoDaVenda`](#uauapimodelsvendaimpostodavenda) |  | Lista de impostos vinculados à venda. |
| `Comissoes` | array de [`UAUApi.Models.Venda.ControleDeComissaoDaVenda`](#uauapimodelsvendacontroledecomissaodavenda) |  | Lista de comissões geradas a partir da venda. |
| `Seguros` | array de [`UAUApi.Models.Venda.Seguro`](#uauapimodelsvendaseguro) |  | Lista de seguros vinculados à venda. |
| `PlanosIndexadores` | array de [`UAUApi.Models.Venda.PlanoIndexadorDaVenda`](#uauapimodelsvendaplanoindexadordavenda) |  | Lista de planos indexadores configurados na venda. |
| `Comentarios` | array de [`UAUApi.Models.Venda.ComentarioDaVenda`](#uauapimodelsvendacomentariodavenda) |  | Lista de comentários da venda. |
| `FinanciamentoImobiliario` | [`UAUApi.Models.Venda.VendasFinancImob`](#uauapimodelsvendavendasfinancimob) |  | Informação do financiamento imobiliário |

### UAUApi.Models.Venda.VendasFinancImob

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `DataAssinatura` | string (date-time) |  | Data de assinatura do contrato de financiamento |

### UAUApi.Models.Venda.ComentarioDaVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Usuario` | string |  | Usuário que vinculou o comentário na venda. |
| `Data` | string (date-time) |  | Data do vínculo do comentário na venda. |
| `Comentario` | string |  | Comentário vinculado na venda. |

### UAUApi.Models.Venda.PlanoIndexadorDaVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Grupo` | integer (int32) |  | Número do grupo do plano indexador vinculado à venda. |
| `IndiceReajuste` | string |  | Código do índice de reajuste contido no grupo do plano indexado vinculado à venda . |
| `Data` | string (date-time) |  | Data de início de correção do índice dentro do grupo do plano indexador vinculado à venda . |

### UAUApi.Models.Venda.Seguro

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `TipoDeSeguro` | integer (int32) — valores possíveis: 0, 1 |  | Tipo do seguro vinculado à venda. 0 - MIP 1 - DFI |
| `TipoDoValorDoSeguro` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o valor do seguro será calculado por uma taxa percentual sobre o valor da venda ou por um valor fixo. 0 - Por taxa percentual 1 - Por valor fixo |
| `ValorSeguro` | number (double) |  | Valor do seguro a ser cobrado (percentual ou valor fixo). |
| `UsuarioDeCadastro` | string |  | Usuário que cadastrou o seguro na venda. |
| `DataDeCadastro` | string (date-time) |  | Data de cadastro do vínculo com a venda vinculada. |
| `Cap` | string |  | CAP de seguro vinculado à venda. |

### UAUApi.Models.Venda.ControleDeComissaoDaVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroComissao` | integer (int32) |  | Número do controle de comissão para o corretor dentro da venda. |
| `CodigoPessoa` | integer (int32) |  | Código do corretor do controle de comissão vinculado à venda. |
| `CodigoDoCargo` | string |  | Código do cargo do corretor na estrutura de comissão utilizado no cadastro da venda. |
| `CpfCnpjDaPessoa` | string |  | CNPJ ou CPF do corretor do controle de comissão vinculado à venda. |
| `ValorDaComissao` | number (double) |  | Valor do controle de comissão. |
| `DataPagamento` | string (date-time) |  | Data de pagamento do controle de comissão. |
| `PorcentagemVenda` | number (double) |  | Percentual de recebimento da venda necessário para liberação Do controle de comissão. |
| `StatusComissao` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4 |  | Código do status do controle de comissão. 0 - Não liberado 1 - Liberado 2 - Pago  3 - Cancelado |
| `GerarProcessoDePagamento` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o pagamento do controle de comissão poderá ser realizado através de um processo de pagamento. 0 - Não  1 - Sim |
| `TipoDePagamento` | integer (int32) — valores possíveis: 0, 1 |  | Código do tipo de pagamento. 0 - Direto (comissões pagas diretamente pelo comprador aos integrantes da estrutura de comissão no momento da venda) 1 - Indireto (comissões pagas pela empresa da venda aos integrantes da estrutura de comissão após a realização da venda) |
| `DataLiberacaoDaComissao` | string (date-time) |  | Data de liberação do controle de comissão. |
| `UsuarioRealizouPagamento` | string |  | Usuário que realizou o pagamento do controle de comissão. |
| `UsuarioCancelouComissao` | string |  | Usuário que realizou o pagamento do controle de comissão. |
| `DataCancelamentoDaComissao` | string (date-time) |  | Data que foi realizado o cancelamento do controle de comissão. |
| `ObservacoesCancelamento` | string |  | Observação informada referente ao cancelamento do controle de comissão. |
| `DataAcrescimoDaComissao` | string (date-time) |  | Data que foi realizado acréscimo no valor do controle de comissão. |
| `UsuarioAcrescimo` | string |  | Usuário que realizou o acréscimo no valor do controle de comissão. |
| `ValorAcrescimo` | number (double) |  | Valor do acréscimo do controle de comissão. |
| `DataDescontoDoComissao` | string (date-time) |  | Data que foi realizado desconto no valor do controle de comissão. |
| `UsuarioDesconto` | string |  | Usuário que realizou o desconto no valor do controle de comissão. |
| `ValorDesconto` | number (double) |  | Valor do desconto do controle de comissão. |
| `TipoDeLancamento` | integer (int32) — valores possíveis: 0, 1 |  | Código do tipo de lançamento do controle de comissão. 0 - Comissão 1 - Bonificação |
| `NumeroRecibo` | integer (int32) |  | Número do recibo para o corretor do controle de comissão. |
| `UsuarioLiberacao` | string |  | Usuário que realizou a liberação do controle de comissão. |
| `EmpresaPagamento` | integer (int32) |  | Empresa que realizou o pagamento da comissão. |
| `BancoPagamento` | integer (int32) |  | Banco onde o pagamento da comissão foi debitado. |
| `ContaPagamento` | string |  | Conta onde o pagamento da comissão foi debitado. |
| `DataPrevistaPagamento` | string (date-time) |  | Data prevista para o pagamento da comissão. |
| `NumeroParcela` | integer (int32) |  | Número da parcela  na comissão |
| `NumeroParcelaGeral` | integer (int32) |  | Número Geral da parcela na comissão |
| `TipoParcela` | string |  | Tipo da parcela  na comissão |
| `StatusEscritura` | integer (int32) |  | Codigo do status de escritura |

### UAUApi.Models.Venda.ImpostoDaVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | string |  | Código do imposto vinculado à parcela. |
| `CAP` | string |  | CAP de desconto de imposto vinculado à parcela. |
| `ValorBase` | number (double) |  | Valor base de incidência da alíquota do imposto. |
| `Aliquota` | number (double) |  | Percentual da alíquota do imposto. |
| `HistoricoLancamentoContabil` | string |  | Histórico de lançamento contábil para o imposto da parcela da venda. |

### UAUApi.Models.Venda.Parcela

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Utilizado apenas para importação de parcelas |
| `Obra` | string |  | Utilizado apenas para importação de parcelas |
| `Numero` | integer (int32) |  | Utilizado apenas para importação de parcelas |
| `NumeroParcela` | integer (int32) |  | Número do grupo do plano indexador vinculado à venda. |
| `NumeroParcelaGeral` | integer (int32) |  | Numeração única da parcela dentro da vinda. |
| `ParcelaRecebida` | integer (int32) — valores possíveis: 0, 1 |  | Indica se a parcela está a receber ou recebida. 0 - A receber 1 - Recebida |
| `OrigemParcela` | integer (int32) |  | Número da parcela de origem. |
| `NumeroDoGrupoDaParcela` | integer (int32) |  | Número do grupo da parcela. |
| `TotalParcelasDoGrupo` | integer (int32) |  | Quantidade de parcelas do grupo da parcela. |
| `TotalParcelasDoGrupoInformado` | integer (int32) |  | Quantidade de parcelas do grupo da parcela informado pelo usuário. |
| `TipoParcela` | string |  | Código do tipo da parcela. |
| `TipoRecebimento` | string |  | Tipo da parcela. |
| `NumeroDoRecebimento` | string |  | Número do recebimento. |
| `DataRecebimento` | string (date-time) |  | Data de recebimento da parcela. |
| `DataCalculoReajuste` | string (date-time) |  | Data de cálculo utilizada para calcular o valor de reajuste de uma parcela recebida. |
| `ValorPrincipal` | number (double) |  | Valor principal da parcela. |
| `ValorResiduo` | number (double) |  | Valor de resíduo gerado para a parcela. |
| `ValorTaxaBoleto` | number (double) |  | Valor da taxa de boleto. |
| `DataVencimento` | string (date-time) |  | Data de vencimento da parcela. |
| `DataPrimeiraParcelaGrupo` | string (date-time) |  | Data de vencimento da primeira parcela do grupo da parcela. |
| `DataProrrogacao` | string (date-time) |  | Data de prorrogação da parcela. |
| `Amortizacao` | integer (int32) — valores possíveis: 0, 1, 2, 3 |  | Código do tipo de amortização de juros utilizado na parcela. 0 - Gradiente 1 - Price 2 - SAC 3 - Simples |
| `BeginEndPrice` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá utilizar referência Begin ou End quando utilizar o tipo de amortização Price. 0 - Begin 1 - End Caso o campo Amortização possua valor diferente de 1 (Price), utilizar sempre o valor 1 (End). |
| `FrequenciaVencimento` | string |  | Frequência de vencimento utilizada na parcela. |
| `DataInicioPrimeiroJuros` | string (date-time) |  | Data de início da cobrança do primeiro juros da parcela. |
| `TaxaPrimeiroJuros` | number (double) |  | Taxa do primeiro juros da parcela. |
| `DataInicioSegundoJuros` | string (date-time) |  | Data de início da cobrança do segundo juros da parcela. |
| `TaxaSegundoJuros` | number (double) |  | Taxa do segundo juros da parcela. |
| `DataInicioReajuste` | string (date-time) |  | Data de inicio de reajuste da parcela. |
| `IndiceReajuste` | string |  | Código do índice de reajuste da parcela |
| `GrupoPlanoIndexador` | integer (int32) |  | Código do grupo de plano indexador utilizado na parcela. |
| `CobrarJurosPrimeiroPeriodo` | integer (int32) — valores possíveis: 0, 1 |  | Indica se as parcelas que possuem amortização Price ou SAC terão juros calculo nos casos que a data de vencimento esteja no mesmo mês(frequências mensais ou anuais) ou dia(frequência diária) da data de início de juros. 0 - Não 1 - Sim |
| `DiasCarenciaMultaJurosAtraso` | integer (int32) |  | Quantidade de dias de carência na cobrança de multa e juros por atraso da parcela. |
| `DiasCarenciaCorrecaoAtraso` | integer (int32) |  | Quantidade de dias de carência na cobrança de correção por atraso da parcela. |
| `CobrarJurosProRata` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o cálculo do reajuste da parcela será realizado de forma pró-rata.  0 - Não   1 - Sim |
| `CobrarJurosProRataPrimeiroMes` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o cálculo do reajuste do primeiro mês da parcela será realizado de forma pró-rata.  0 - Não   1 - Sim |
| `ValorDescontoImposto` | number (double) |  | Valor total de imposto lançado na venda. |
| `CapPrincipal` | string |  | CAP do valor do principal da parcela. |
| `CapAcrescimo` | string |  | CAP do valor de acréscimo da parcela. |
| `CapCorrecao` | string |  | CAP do valor de correção da parcela. |
| `CapCorrecaoAtraso` | string |  | CAP do valor de correção por atraso da parcela. |
| `CapDesconto` | string |  | CAP do valor de desconto da parcela. |
| `CapDescontoAntecipacao` | string |  | CAP do valor de desconto de antecipação da parcela. |
| `CapDescontoCondicional` | string |  | CAP do valor de desconto condicional da parcela. |
| `CapDescontoCusta` | string |  | CAP do valor de desconto de custa da parcela. |
| `CapJuros` | string |  | CAP do valor de juros da parcela. |
| `CapJurosAtraso` | string |  | CAP do valor de juros por atraso da parcela. |
| `CapMulta` | string |  | CAP do valor de multa da parcela. |
| `CapRepasse` | string |  | CAP do valor de repasse da parcela. |
| `CapTaxaBoleto` | string |  | CAP do valor de taxa de boleto da parcela. |
| `TipoDaCusta` | integer (int32) |  | Código do tipo de custa para parcelas do tipo Custas. |
| `OrigemCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se a origem da custa e pela obra ou administrativa. 0 - Obra 1 - Administração |
| `CobrarMultaCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá haver cobrança de multa por atraso na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarJurosAtrasoCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá haver cobrança de juros por atraso na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarTaxaAdministracaoCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá haver cobrança de taxa de administração na parcela Do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarImpostoCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá haver cobrança de imposto na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `CobrarCorrecaoCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá haver cobrança de correção na parcela do tipo custa específica. 0 - Não 1 - Sim |
| `RepassarValorLocadorCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá haver repasse ao locador para a parcela do tipo custa específica. 0 - Não 1 - Sim |
| `ValorDescontoCusta` | number (double) |  | Valor total de desconto de custas. |
| `ObservacaoCusta` | string |  | Observação da parcela do tipo custa específica. |
| `PadraoCobranca` | integer (int32) |  | Código do padrão de cobrança utilizado na parcela. |
| `TipoSeguro` | integer (int32) — valores possíveis: 0, 1 |  | Indica o tipo de seguro para parcelas do tipo seguro. 0 - MIP 1 - DFI |
| `DescontosDeCusta` | array de [`UAUApi.Models.Venda.DescontoDeCustas`](#uauapimodelsvendadescontodecustas) |  | Lista de descontos de custa da parcela. |
| `DescontosDeImposto` | array de [`UAUApi.Models.Venda.DescontoDeImposto`](#uauapimodelsvendadescontodeimposto) |  | Lista de descontos de imposto da parcela. |
| `DadosDescontoCondicional` | [`UAUApi.Models.Venda.DescontoCondicional`](#uauapimodelsvendadescontocondicional) |  | Dados do desconto condicional da parcela. |
| `ValorDescontoCondicional` | number (double) |  | Valor não confirmado de desconto condicional da parcela recebida. |
| `ValorDescontoCondicionalConfirmado` | number (double) |  | Valor confirmado de desconto condicional da parcela recebida. |
| `ValorDescontoCustaConfirmado` | number (double) |  |  |
| `ValorDescontoImpostoConfirmado` | number (double) |  |  |
| `ValorPrincipalConfirmado` | number (double) |  | Valor confirmado de principal da parcela recebida. |
| `ValorAcrescimo` | number (double) |  | Valor não confirmado de acréscimo da parcela recebida. |
| `ValorAcrescimoConfirmado` | number (double) |  | Valor confirmado de acréscimo da parcela recebida. |
| `ValorDesconto` | number (double) |  | Valor não confirmado de desconto da parcela recebida. |
| `ValorDescontoConfirmado` | number (double) |  | Valor confirmado de desconto da parcela recebida. |
| `ValorCorrecaoAtraso` | number (double) |  | Valor não confirmado de correção por atraso da parcela recebida. |
| `ValorCorrecaoAtrasoConfirmado` | number (double) |  | Valor confirmado de correção por atraso da parcela recebida. |
| `ValorCorrecaoEmbutida` | number (double) |  | Valor não confirmado de correção embutido da parcela recebida. |
| `ValorCorrecaoEmbutidaConfirmado` | number (double) |  | Valor confirmado de correção embutido da parcela recebida. |
| `ValorJurosAtraso` | number (double) |  | Valor não confirmado de juros por atraso da parcela recebida. |
| `ValorJurosAtrasoConfirmado` | number (double) |  | Valor confirmado de juros por atraso da parcela recebida. |
| `ValorJurosContrato` | number (double) |  | Valor não confirmado de juros contratual da parcela recebida. |
| `ValorJurosContratoConfirmado` | number (double) |  | Valor confirmado de juros contratual da parcela recebida. |
| `ValorJurosContratoEmbutido` | number (double) |  | Valor não confirmado de juros contratual embutido da parcela recebida. |
| `ValorJurosContratoEmbutidoConfirmado` | number (double) |  | Valor confirmado de juros contratual embutido da parcela recebida. |
| `ValorMulta` | number (double) |  | Valor não confirmado de multa por atraso da parcela recebida. |
| `ValorMultaConfirmado` | number (double) |  | Valor confirmado de multa por atraso da parcela recebida. |
| `ValorPrincipalPrice` | number (double) |  | Valor real do principal obtido após aplicar a amortização price na série da parcela. |
| `ValorJurosPrice` | number (double) |  | Valor real de juros obtido após aplicar a amortização price na série da parcela. |
| `ValorTaxaBoletoConfirmado` | number (double) |  | Valor da taxa dos boletos que foram confirmados. |
| `ValorCorrecao` | number (double) |  | Valor não confirmado de correção da parcela recebida. |
| `ValorCorrecaoConfirmado` | number (double) |  | Valor confirmado de correção da parcela recebida. |
| `ValorDescontoAdiantamento` | number (double) |  | Valor não confirmado de desconto por adiantamento da parcela recebida. |
| `ValorDescontoAdiantamentoConfirmado` | number (double) |  | Valor confirmado de desconto por adiantamento da parcela recebida. |
| `Recebimentos` | array de [`UAUApi.Models.Venda.Recebimento`](#uauapimodelsvendarecebimento) |  | Lista dos recebimentos da parcela recebida. |
| `Prorrogacoes` | array de [`UAUApi.Models.Venda.ProrrogacaoDaParcela`](#uauapimodelsvendaprorrogacaodaparcela) |  | Lista dos dados das prorrogações da parcela. |
| `UsuarioRecebeu` | string |  | Usuário que realizou o recebimento da parcela. |
| `UsuarioCedeuDesconto` | string |  | Usuário que condecedeu desconto na parcela ao realizar seu recebimento. |
| `DataInicioPeriodoAluguel` | string (date-time) |  | Data de competência da parcela. |
| `GrupoDescontoPontuacao` | integer (int32) |  | Númerod do grupo fechado de pontuação desconto última parcela |
| `RecebimentoPontuacao` | integer (int32) |  | 0 - Em dia 1 - Atraso 2 - Desconto total |
| `TotalRecebimentos` | number (double) |  | Total de recebimento. |
| `TotalRecebimentosDepositados` | number (double) |  | Total de recebimentos que já foram depositados. |
| `TotalRecebimentosParcela` | number (double) |  | Total de recebimento da parcela. |
| `TotalRecebimentosParcelaSemDesconto` | number (double) |  | Total de recebimentos sem desconto. |
| `TotalDescontosParcela` | number (double) |  | Total de descontos da parcela. |
| `ValorTotalDescontoImposto` | number (double) |  | Valor total de desconto de imposto. |
| `ValorPrincipalDaParcela` | number (double) |  | Valor principal da parcela. |

### UAUApi.Models.Venda.ProrrogacaoDaParcela

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `DataDeProrrogacao` | string (date-time) |  | Data do histórico da data de prorrogação da parcela. |
| `UsuarioProrrogacao` | string |  | Usuário de prorrogação. |

### UAUApi.Models.Venda.Recebimento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) |  | Número do recebimento. |
| `Contador` | integer (int32) |  | Contador. |
| `Tipo` | string |  | Tipo do item de recebimento. B - Bens C - Cheque D - Dinheiro E - Eletrônico |
| `DataDevolucao` | string (date-time) |  | Data de devolução do depósito do recebimento. |
| `BancoDeposito` | integer (int32) |  | Banco do depósito do recebimento. |
| `AgenciaDeposito` | string |  | Agência do depósito do recebimento. |
| `ContaDeposito` | string |  | Conta do depósito do recebimento. |
| `Valor` | number (double) |  | Valor do depósito do recebimento. |
| `NumeroDeposito` | integer (int32) |  | Número do depósito do recebimento. |
| `DataDeposito` | string (date-time) |  | Data de realização do depósito do recebimento. |
| `Depositado` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o recebimento está depositado. 0 - Não 1 - Sim |
| `Conciliado` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o recebimento está conciliado. 0 - Não 1 - Sim |
| `DataConciliacao` | string (date-time) |  | Data de conciliação do depósito do recebimento. |
| `ChequeNumero` | string |  | Número do cheque quando o item do recebimento for realizado através de cheque. |
| `ChequeBanco` | integer (int32) |  | Código do banco do cheque quando o item do recebimento for realizado através de cheque. |
| `ChequeAgencia` | string |  | Número da agência do cheque quando o item do recebimento for realizado através de cheque. |
| `ChequeConta` | string |  | Número da conta do cheque quando o item do recebimento for realizado através de cheque. |
| `Data` | string (date-time) |  | Data de recebimento do item de recebimento. |
| `DataCadastro` | string (date-time) |  | Data de cadastro do recebimento. |
| `UsuarioCadastro` | string |  | Usuário do cadastro. |
| `UsuarioResponsavel` | string |  | Usuário atual responsável pelo recebimento. |
| `Descricao` | string |  | Descrição do item de recebimento. |
| `ValorPercentualDoPrincipal` | number (double) |  | Valor principal recebido pelo item de recebimento. |
| `ValorPercentualDeCorrecao` | number (double) |  | Valor de correção recebido pelo item de recebimento. |
| `ValorPercentualDeCorrecaoEmbutido` | number (double) |  | Valor de correção embutida recebido pelo item de recebimento. |
| `ValorPercentualDaCorrecaoPorAtraso` | number (double) |  | Valor de correção por atraso recebido pelo item de recebimento. |
| `ValorPercentualDoJuros` | number (double) |  | Valor de juros recebido pelo item de recebimento. |
| `ValorPercentualDoJurosEmbutido` | number (double) |  | Valor de juros embutido recebido pelo item de recebimento. |
| `ValorPercentualDoJurosAtraso` | number (double) |  | Valor de juros por atraso recebido pelo item de recebimento. |
| `ValorPercentualDaMultaPorAtraso` | number (double) |  | Valor de multa por atraso recebido pelo item de recebimento. |
| `ValorPercentualDoAcrescimo` | number (double) |  | Valor de acréscimo recebido pelo item de recebimento. |
| `ValorPercentualDoDesconto` | number (double) |  | Valor de desconto recebido pelo item de recebimento. |
| `ValorPercentualDoDescontoPorAntecipacao` | number (double) |  | Valor de desconto por antecipação recebido pelo item de recebimento. |
| `ValorPercentualDoDescontoDeCustas` | number (double) |  | Valor de desconto de custas recebido pelo item de recebimento. |
| `ValorPercentualDoDescontoDeImposto` | number (double) |  | Valor de desconto de imposto recebido pelo item de recebimento. |
| `ValorPercentualDoDescontoCondicional` | number (double) |  | Valor de desconto condicional recebido pelo item de recebimento. |
| `ValorPercentualDaTaxaBoleto` | number (double) |  | Valor de taxa boleto recebido pelo item de recebimento. |
| `HistoricoContabil` | string |  | Histórico de lançamento contábil para o imposto da parcela da venda. |
| `ValorPercentualDoPrincipalPrice` | number (double) |  | Valor do principal price. |
| `ValorPercentualDoJurosPrice` | number (double) |  | Valor de juros do price. |

### UAUApi.Models.Venda.DescontoCondicional

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Valor` | number (double) |  | Valor do desconto condicional. |
| `TipoDeValor` | integer (int32) — valores possíveis: 0, 1 |  | Tipo do valor. 0 - Percentual 1 - Fixo |
| `ReferenciaDiaLimite` | integer (int32) — valores possíveis: 0, 1 |  | Referência do dia do limite. |
| `DiaLimite` | integer (int32) |  | Data do limite. |
| `Usuario` | string |  | Usuário cadastro. |
| `DataCadastro` | string (date-time) |  | Data do cadastro. |

### UAUApi.Models.Venda.DescontoDeImposto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `TipoImposto` | string |  | Tipo do imposto vinculado à parcela. |
| `CAP` | string |  | CAP de desconto de imposto vinculado à parcela. |
| `ValorBase` | number (double) |  | Valor base de incidência da alíquota do imposto. |
| `Aliquota` | number (double) |  | Percentual da alíquota do imposto. |
| `HistoricoLancamentoContabil` | string |  | Histórico de lançamento contábil para o imposto da parcela da venda. |

### UAUApi.Models.Venda.DescontoDeCustas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Valor` | number (double) |  | Valor do desconto de custa vinculado à parcela. |
| `UsuarioCadastro` | string |  | Usuário de cadastro do desconto de custa vinculado à parcela. |
| `DataDeCadastro` | string (date-time) |  | Data de cadastro do desconto de custa vinculado à parcela. |
| `Tipo` | integer (int32) |  | Código do tipo de custa para parcelas do tipo Custas. |
| `CobrarTaxaAdministracaoCusta` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá cobrar taxa de administração para o desconto de custa. 0 - Não 1 - Sim |
| `RepassarValorParaLocador` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá realizar repasse do valor do desconto de custa para o locador. 0 - Não 1 - Sim |
| `CobrarCPMF` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá cobrar CPMF para o desconto de custa. 0 - Não 1 - Sim |
| `Observacao` | string |  | Observação do desconto de custa vinculado à parcela. |
| `CapRepasse` | string |  | CAP de repasse do desconto de custa vinculado à parcela. |

### UAUApi.Models.Venda.ItemDaVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoProduto` | integer (int32) |  | Código do produto vendido. |
| `CodigoPersonalizacao` | integer (int32) |  | Código da personalização do produto vendido. |
| `Preco` | number (double) |  | Preço unitário da personalização/produto vendido. |
| `Quantidade` | number (double) |  | Quantidade vendida da personalização/produto. |
| `Contrato` | integer (int32) |  | Número do contrato do produto planejado. |
| `ValorComissaoDireta` | number (double) |  | Valor de comissão direta da personalização/produto vendido. |
| `PercentualComissao` | number (double) |  | Percentual de comissão cobrado no valor da personalização/produto vendido. |
| `PercentualDoItem` | number (double) |  | Percentual do item. |
| `NumeroItem` | string |  | Número do item. |

### UAUApi.Models.Venda.ClienteDaVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoCliente` | integer (int32) |  | Código do cliente vinculado à venda. |
| `CpfCnpjDoCliente` | string |  | CPF/CNPJ do cliente. |
| `EmitirBoleto` | integer (int32) — valores possíveis: 0, 1 |  | Indica se os boletos emitidos para venda serão em nome do cliente. 0 - Não 1 - Sim |
| `PercentualDoTitular` | number (double) |  | Percentual da venda correspondente aos titulares da venda. |
| `TipoDeCliente` | integer (int32) |  | Código que define o tipo de vínculo do cliente com o contrato de venda/aluguel. 0 - Titular 1 - Não titular 2 - Avalista |
| `Principal` | integer (int32) |  | Indica se o cliente é o titular principal do contrato da venda. 0 - Não 1 - Sim |

### UAUApi.Models.Venda.ParametrosDaVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) |  | Número. |
| `Tipo` | string |  | Tipo. |
| `QuantidadeDeParcelas` | integer (int32) |  | Quantidade de parcelas. |
| `Valor` | number (double) |  | Valor das parcelas. |
| `TaxaPrimeiroJuros` | number (double) |  | Taxa do primeiro juro. |
| `Frequencia` | string |  | Frequência de juros. |
| `Reajuste` | string |  | Reajuste. |
| `Amortizacao` | integer (int32) — valores possíveis: 0, 1, 2, 3 |  | Tipo da amortização. 0 - Gradiente 1 - Price 2 - SAC 3 - Simples |
| `ReferenciaAmortizacao` | integer (int32) — valores possíveis: 0, 1 |  | Referência da amortização. 0 - TipoBegin 1 - TipoEnd |
| `DataPrimeiraParcela` | string (date-time) |  | Data da primeira parcela. |
| `DataPrimeiroJuros` | string (date-time) |  | Data primeiro juros. |
| `DataDeReajuste` | string (date-time) |  | Data de reajuste. |
| `CobrarJurosPrimeiroPeriodo` | integer (int32) — valores possíveis: 0, 1 |  | Cobrar juros do primeiro período. 0 - Não 1 - Sim |
| `PercentualSegundoJuros` | number (double) |  | Percentual do segundo juros. |
| `DataSegundoJuros` | string (date-time) |  | Data do segundo juros. |
| `DiasDeCarenciaJurosPorAtraso` | integer (int32) |  | Dias de carência de juros por atraso. |
| `DiasDeCarenciaCorrecaoPorAtraso` | string |  | Dias de carência de correção por atraso. |
| `CobrarJurosProRata` | boolean |  | Cobrar juros pró-rata. 0 - Não 1 - Sim |
| `CobrarJurosProRataNoPrimeiroMes` | boolean |  | Cobrar juros pró-rata no primeiro mês. 0 - Não 1 - Sim |

### UAUApi.Models.Venda.VendaVinculada

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Empresa da venda vinculada. |
| `Obra` | string |  | Obra da venda vinculada. |
| `Numero` | integer (int32) |  | Número da venda vinculada. |
| `UsuarioDeCadastro` | string |  | Usuário que realizou o vínculo com a venda vinculada. |
| `DataDeCadastro` | string (date-time) |  | Data de cadastro do vínculo com a venda vinculada. |

### UAUApi.Models.Venda.AluguelDeShopping

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoAtividade` | string |  | Código da atividade. |
| `TipoDeContrato` | integer (int32) — valores possíveis: 0, 1, 2 |  | Tipo de contrato. 0 - Normal 1 - Exceção 2 - CTO |
| `BaseAluguelPercentual` | integer (int32) — valores possíveis: 0, 1 |  | Base percentual aluguel. 0 - Mensal mínimo 1 - Aluguel apurado |
| `Area` | number (double) |  | Área. |
| `Frente` | number (double) |  | Frente. |
| `Profundidade` | number (double) |  | Profundidade |
| `CodigoLocalizacao` | integer (int32) |  | Código da localização. |
| `PercentualAluguel` | number (double) |  | Percentual do aluguel. |
| `TipoDeReceita` | integer (int32) — valores possíveis: 0, 1 |  | Tipo de receita. 0 - Gradiente 1 - Price 2 - SAC 3 - Simples |
| `ValorBaseFPP` | number (double) |  | Valor base FPP. |

### UAUApi.Models.Venda.RetornoImportacaoVendaXml

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Status` | integer (int32) |  | Status da importação. 0 - Falha 1 - Sucesso |
| `Mensagem` | string |  | Mensagem importação. |

### UAUApi.Models.Venda.GerarVendaDePropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroProposta` | integer (int32) | ✓ | Número da proposta que será transformada em venda |
| `atualizaDatasDaVenda` | boolean | ✓ | Identifica se irá atualizar as datas da venda caso a proposta esteja com datas desatualizadas. TRUE - Irá atualizar as datas da venda FALSE - Não irá atualizar as datas da venda. |
| `dataVenda` | string (date-time) |  | Indica para qual data irá atualizar as datas da venda caso a proposta esteja com datas desatualizadas MM-dd-yyyy. |
| `atualizaInicioPrimeiroJuros` | boolean |  | Indica se a data de início do primeiro juros será alterada. |
| `atualizaInicioReajuste` | boolean |  | Indica se a data de início do reajuste será alterada. |
| `atualizaInicioSegundoJuros` | boolean |  | Indica se a data de início do segundo juros será alterada |
| `atualizaBaseResiduo` | boolean |  | Indica se a data da base resíduo será alterada |
| `atualizaPlanoIndexador` | boolean |  | Indica se a data dos planos indexadores serão alteradas |
| `dataPrimeiroJuros` | string (date-time) |  | Indica para qual data irá atualizar a data de 1º Juros. yyyy-MM-dd |
| `dataSegundoJuros` | string (date-time) |  | Indica para qual data irá atualizar a data de 2º Juros |
| `dataReajuste` | string (date-time) |  | Indica para qual data irá atualizar a data de início de reajuste |
| `dataBaseResiduo` | string (date-time) |  | Indica para qual data irá atualizar a data base de resíduo |
| `listaPlanoIndexador` | array de [`UAUApi.Models.Venda.PlanoIndexadorRequest`](#uauapimodelsvendaplanoindexadorrequest) |  | Indicam quais planos indexadores terão as datas alteradas |
| `desconsiderarNaoTitularesAvalista` | boolean |  | Indica que sistema vai desconsiderar todos os não titulares avalistas da proposta para geração da venda, ou seja, vai deixar apenas os titulares. Se informar a lista de NãoTitulares essa opção se torna nula, visto que o sistema irá utilizar os não titulares da lista. |
| `diasProrrogacaoParcVencidas` | integer (int32) |  | Quantidade de dias que será adicionado a nova data de vencimento das parcelas vencidas. |
| `usuarioCadVenda` | string |  | Usuário que está tranformado a proposta de venda em venda. |
| `listaNaoTitularAvalista` | array de [`UAUApi.Models.Venda.NaoTitularAvalistaRequest`](#uauapimodelsvendanaotitularavalistarequest) |  | Lista com os não titulares e avalista da venda, caso seja preenchida o sistema irá desconsiderar os cadastrados na proposta e colocar as pessoas informadas  dessa lista na venda. |

### UAUApi.Models.Venda.NaoTitularAvalistaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codPessoa` | integer (int32) |  | Código da pessoa no Uau. |
| `Tipo` | integer (int32) |  | Tipo de não titular ou avalista 1 - Não titular ou   2 - Avalista |

### UAUApi.Models.Venda.PlanoIndexadorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codGrupoPlanoIdx` | integer (int32) |  | número do grupo do plano indexador |
| `indice` | string |  | indice do plano indexador |
| `data` | string (date-time) |  | data do plano indexador antes da atualização. yyyy-MM-dd |
| `novaData` | string (date-time) |  | Nova data do plano indexador. yyyy-MM-dd |

### UAUApi.Models.Venda.EvolucaoSaldoDevedorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) | ✓ | Código da empresa da venda |
| `codigoObra` | string | ✓ | Código da obra da venda |
| `numeroVenda` | integer (int32) | ✓ | Número da venda |
| `tipoRelatorio` | integer (int32) | ✓ | Tipo do relatório a ser gerado.<br /> 0 - Relatório Detalhado.<br /> 1 - Relatório Simplificado. <br /> |

### UAUApi.Models.Venda.EvolucaoContratoVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Codigo da empresa da venda |
| `codigoObra` | string |  | Codigo da obra da venda |
| `numeroVenda` | integer (int32) |  | Numero da venda |

### UAU.VendasProxy.ParcelasBoletoRetorno

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Mensagens` | string |  |  |
| `Advertencias` | string |  |  |
| `BoletosGerados` | array de [`UAU.VendasProxy.BoletoGerado`](#uauvendasproxyboletogerado) |  |  |

### UAU.VendasProxy.BoletoGerado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Gerou` | boolean |  |  |
| `Banco` | string |  |  |
| `SeuNumero` | string |  |  |
| `NossoNumero` | string |  |  |
| `ImprimirBoleto` | boolean |  |  |
| `StatusCarteira` | string |  |  |

### UAUApi.Models.Venda.GerarBoletoBancarioRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `parcelas` | array de [`UAUApi.Models.Venda.ParcelasBoleto`](#uauapimodelsvendaparcelasboleto) | ✓ | Lista de objeto (ParcelasBoleto) com as parcelas geradas do tipo boleto ou carne e se existir, o valor do desconto |
| `data_calculo` | string (date-time) | ✓ | Data de cálculo |
| `antecipar` | boolean |  | Se o cálculo será antecipado TRUE - Sim FALSE - Não |
| `reajustar` | boolean |  | Se é para reajustar os valores TRUE - Sim FALSE - Não |
| `excluirboleto_expirado` | boolean |  | Se é para excluir os boletos expirados TRUE - Sim FALSE - Não |
| `formaarquivo_cobranca` | integer (int32) — valores possíveis: 0, 1 |  | Forma da cobrança Boleto = 0 Carnê = 1 |
| `boletosacado_detalhado` | boolean |  | Se o sacado será detalhado TRUE - Sim FALSE - Não |
| `carnetres_vias` | boolean |  | Se o carnê será em três vias TRUE - Sim FALSE - Não |
| `naovalidardados_pendentes` | boolean |  | Se não deve validar os dados pendentes da parcela TRUE - Não validar FALSE - Validar |
| `acrescentar_residuo` | boolean |  | Se vai acrescentar o valor de resíduo TRUE - Sim FALSE - Não |
| `usarpadraoboleto_avulso` | boolean |  | Indica qual o padrão de cobrança será utilizado TRUE - Irá usar o padrão de cobrança para boleto avulso cadastrado na obra FALSE - Irá usar o padrão de cobrança das parcelas <list type="bullet"><item>1. Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão AVULSO informado,  esse padrão irá sobrepor o padrão da obra, mantendo a configuração de grupo de cobrança.</item></list> |
| `agrupar_parcelas` | boolean |  | Se deve agrupar as parcelas informadas TRUE - Sim FALSE - Não |
| `formaagruparpor_vendas` | boolean |  | Forma de agrupamento do boleto TRUE  - Realiza o agrupamento das parcelas por venda FALSE - Realiza o agrupamento das parcelas por pessoa |
| `ValorBoleto` | number (double) |  | Valor do boleto, utilizado para geração de boletos parciais. |
| `PadraoCobranca` | integer (int32) |  | Nr. do padrão para cobrança <list type="bullet"><item>1. Caso a parcela informada no JSON, tenha vínculo com grupo de cobrança da venda de carteira, e tenha um padrão AVULSO informado,  esse padrão irá sobrepor o padrão informado no JSON, mantendo a configuração de grupo de cobrança.</item></list> |
| `ExcluirBoletosExistentes` | boolean |  | Se irá excluir boletos já emitidos ao gerar um novo boleto para a parcela |
| `ReaproveitarBoleto` | boolean |  | Se irá reaproveitar o boleto já gerado para alguma das parcelas enviadas |
| `ValorTaxaBoleto` | number (double) |  | Valor de taxa do boleto que será utilizada ao reaproveitar um boleto |

### UAUApi.Models.Venda.ParcelasBoleto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa_reaj` | integer (int32) | ✓ | Código da empresa |
| `Obra_reaj` | string | ✓ | Código da obra |
| `NumVenda_reaj` | integer (int32) | ✓ | Número da venda |
| `NumParc_reaj` | integer (int32) | ✓ | Número da parcela |
| `Tipo_reaj` | string | ✓ | Tipo da parcela |
| `NumParcGer_reaj` | integer (int32) | ✓ | Número geral da parcela |
| `ValorDescAnt_reaj` | number (double) |  | Valor do desconto |

### UAUApi.Models.Venda.FinalizarRenegociacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario_logado` | string |  | Usuário que está realizando a ação |
| `parc_geradas_json` | string |  | Tabela com as parcelas geradas na renegociação |
| `parcsel_reneg_json` | string |  | Tabela com as parcelas selecionadas para a renegociação |
| `grupo_parcelas_json` | string |  | Parametros dos grupos de parcelas utilizados(LogParc) |
| `valdesc_reneg` | number (double) |  | Valor de desconto utilizado na renegociação |
| `valacresc_reneg` | number (double) |  | Valor de acrescimo utilizado na renegociação |
| `val_reneg` | number (double) |  | Valor renegociado |
| `pendentevalidar_alcada` | boolean |  | Se está pendente a validação de alçada de desconto |
| `venda` | integer (int32) |  |  |
| `obra` | string |  |  |
| `empresa` | integer (int32) |  |  |
| `tabelaplano_idx_json` | string |  |  |

### UAUApi.Models.Venda.ExportarVendasXmlRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dados_vendas` | [`UAUApi.Models.Venda.ExportaVendas`](#uauapimodelsvendaexportavendas) | ✓ | Objeto com os dados das vendas |

### UAUApi.Models.Venda.ExportaVendas

Propiedades passadas para o webservice para exportar vendas para o SalesForce

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dataInicio` | string (date-time) |  | Data início para filtrar as vendas |
| `dataFim` | string (date-time) |  | Data fim para filtrar as vendas |
| `statusEscrituracao` | boolean |  | Permitir buscar vendas com alterações nas escriturações |
| `listaVendas` | array de [`UAUApi.Models.Venda.ExportaVendas.ChavesVendas`](#uauapimodelsvendaexportavendaschavesvendas) |  | Lista com as chaves das vendas (Venda, Obra, Empresa) |
| `InformarNovaVendaCessao` | boolean |  | Informa se irá indicar a nova venda gerada após a cessão |

### UAUApi.Models.Venda.ExportaVendas.ChavesVendas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Venda` | integer (int32) |  |  |

### UAUApi.Models.Venda.ExportarPessoasDaVendaXmlRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `lista_vendas` | array de [`UAUApi.Models.Venda.ChavesVendas`](#uauapimodelsvendachavesvendas) |  | Lista com as vendas |

### UAUApi.Models.Venda.ChavesVendas

Classe com as chaves referentes às vendas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Venda` | integer (int32) |  |  |

### UAUApi.Models.Venda.ListaBoletosExclusaoRequest

Lista com todos os boletos que serão excluídos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `listaBoletosExcluir` | array de [`UAUApi.Models.Venda.ExclusaoDeBoletos`](#uauapimodelsvendaexclusaodeboletos) | ✓ | Lista de custas. |

### UAUApi.Models.Venda.ExclusaoDeBoletos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `seuNumero` | integer (int64) | ✓ | Seu número do boleto |
| `numeroBanco` | integer (int32) | ✓ | Número do banco do boleto |

### UAUApi.Models.Venda.ExcluirPracelaCusta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ExcluirParcelaNoBanco` | boolean | ✓ | Parâmetro para identificar se e para excluir a parcela ou não, se ela estiver no banco. |
| `Lista` | array de [`UAUApi.Models.Venda.ExcluirParcelaCustaCampos`](#uauapimodelsvendaexcluirparcelacustacampos) | ✓ | Lista dos campos |

### UAUApi.Models.Venda.ExcluirParcelaCustaCampos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `Venda` | integer (int32) | ✓ | Código da Venda |
| `NumeroParcela` | integer (int32) | ✓ | Número da parcela |
| `TipoParcela` | string | ✓ | Tipo da parcela |
| `NumeroGeralParcela` | integer (int32) | ✓ | Número Geral da Parcela |

### UAUApi.Models.Venda.VendaIntegracao.UnidadeVendida

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Empresa da venda |
| `Obra` | string |  | Obra da venda |
| `Venda` | integer (int32) |  | Número da venda |
| `StatusVenda` | integer (int32) |  | Status da venda |
| `DataVenda` | string (date-time) |  | Data da venda |
| `Produto` | integer (int32) |  | Produto |
| `CodPerson` | integer (int32) |  | Código da personalização do produto |
| `DescPerson` | string |  | Descrição da personalização |
| `EmpUnid` | string |  | Empresa da unidade |
| `ProdUnid` | string |  | Produto da unidade |
| `NumPerson` | string |  | Núm. Personalização da unidade |
| `ObraUnid` | string |  | Obra da unidade |
| `QtdeUnid` | string |  | Quantidade da unidade |
| `VendidoUnid` | string |  |  |
| `CodigoUnid` | string |  | Código da unidade |
| `PorcentPrUnid` | string |  | Porcentagem da unidade |
| `C1Unid` | string |  |  |
| `C2Unid` | string |  |  |
| `C3Unid` | string |  |  |
| `C4Unid` | string |  |  |
| `C5Unid` | string |  |  |
| `C6Unid` | string |  |  |
| `C7Unid` | string |  |  |
| `C8Unid` | string |  |  |
| `C9Unid` | string |  |  |
| `C10Unid` | string |  |  |
| `C11Unid` | string |  |  |
| `C12Unid` | string |  |  |
| `C13Unid` | string |  |  |
| `C14Unid` | string |  |  |
| `C15Unid` | string |  |  |
| `C16Unid` | string |  |  |
| `C17Unid` | string |  |  |
| `C18Unid` | string |  |  |
| `C19Unid` | string |  |  |
| `C20Unid` | string |  |  |
| `C21Unid` | string |  |  |
| `C22Unid` | string |  |  |
| `C23Unid` | string |  |  |
| `C24Unid` | string |  |  |
| `C25Unid` | string |  |  |
| `C26Unid` | string |  |  |
| `C27Unid` | string |  |  |
| `C28Unid` | string |  |  |
| `C29Unid` | string |  |  |
| `C30Unid` | string |  |  |
| `C31Unid` | string |  |  |
| `C32Unid` | string |  |  |
| `C33Unid` | string |  |  |
| `C34Unid` | string |  |  |
| `C35Unid` | string |  |  |
| `C36Unid` | string |  |  |
| `C37Unid` | string |  |  |
| `C38Unid` | string |  |  |
| `C39Unid` | string |  |  |
| `C40Unid` | string |  |  |
| `C41Unid` | string |  |  |
| `C42Unid` | string |  |  |
| `C43Unid` | string |  |  |
| `C44Unid` | string |  |  |
| `C45Unid` | string |  |  |
| `AnexosUnid` | string |  | Anexos (fotos, ocorrências, comentários) da unidade |
| `IdentificadorUnid` | string |  | Identificador da unidade |
| `UsrCadUnid` | string |  | Usuário de cadastro da unidade |
| `DataCadUnid` | string |  | Data de cadastro da unidade |
| `ValPrecoUnid` | string |  | Valor da unidade |
| `FracaoIdealUnid` | string |  | Fração ideal da unidade |
| `NumObeUnid` | string |  |  |
| `ObjEspelhoTopUnid` | string |  |  |
| `ObjEspelhoLeftUnid` | string |  |  |
| `PorcentComissaoUnid` | string |  |  |
| `CodTipProdUnid` | string |  | Código do tipo de produto |
| `NumCategStatusUnid` | string |  |  |
| `FracaoIdealDecimalUnid` | string |  | Fração ideal decimal da unidade |
| `DataEntregChavesUnid` | string |  | Data de entrega das chaves da unidade |
| `DataRecReceitaMapaUnid` | string |  | Data de recolhimento da receita |
| `UnidadeVendidaDacao` | string |  |  |

### UAUApi.Models.Venda.ConsultarUnidadesCompradasPorCPFRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CpfCnpj` | string |  |  |

### UAUApi.Models.Venda.VendaIntegracao.ResumoVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Codigo da empresa do resumo de venda |
| `codigoObra` | string |  | Codigo da obra do resumo de venda |
| `numeroVenda` | integer (int32) |  | Numero da venda |
| `dataCalculo` | string (date-time) |  | Data do calculo do resumo de venda |
| `totalParcelas` | integer (int32) |  | Total das parcelas do resumo de venda |
| `totalDesconto` | number (double) |  | Total dos descontos do resumo de venda |
| `totalAPagarComDesconto` | number (double) |  | Total a pagar com os descontos |
| `parcelasportipo` | array de [`UAUApi.Models.Venda.VendaIntegracao.ParcelasPorTipo`](#uauapimodelsvendavendaintegracaoparcelasportipo) |  | Lista das parcelas do resumo de venda por tipo |
| `totaisareceber` | array de [`UAUApi.Models.Venda.VendaIntegracao.TotaisAReceber`](#uauapimodelsvendavendaintegracaototaisareceber) |  | Lista com os totais da venda a receber |
| `totaisrecebido` | array de [`UAUApi.Models.Venda.VendaIntegracao.TotaisRecebidos`](#uauapimodelsvendavendaintegracaototaisrecebidos) |  | Lista com os totais da venda já recebidos |
| `descontoantecipacao` | [`UAUApi.Models.Venda.VendaIntegracao.DescontoAntecipacao`](#uauapimodelsvendavendaintegracaodescontoantecipacao) |  | Lista com os descontos antecipação do resumo de venda |

### UAUApi.Models.Venda.VendaIntegracao.DescontoAntecipacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoCampanha` | integer (int32) |  | Codigo da campanha do desconto de antecipação |
| `descricaoCampanha` | string |  | Descrição da campanha do desconto de antecipação |
| `percentualDesconto` | number (double) |  | Percentual do desconto de antecipação da campanha |
| `tipoDesconto` | integer (int32) |  | Tipo do desconto de antecipação da campanha |
| `descricaoTipoDesconto` | string |  | Descrição do tipo de desconto |
| `descontoAteHabitese` | boolean |  | Define se o desconto é até a habitese |

### UAUApi.Models.Venda.VendaIntegracao.TotaisRecebidos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `valorTotalRecebido` | number (double) |  | Valor total recebido da venda |
| `valorPrincipal` | number (double) |  | Valor principal recebido da venda |
| `valorJuros` | number (double) |  | Valor dos juros recebidos da venda |
| `valorCorrecao` | number (double) |  | Valor da correção recebidos da venda |
| `valorMulta` | number (double) |  | Valor da multa recebidos da venda |
| `valorJurosAtraso` | number (double) |  | Valor dos juros atrasados recebidos da venda |
| `valorDescontoAcrescimo` | number (double) |  | Valor dos descontos/acrescimos recebidos da venda |
| `valorAcrescimo` | number (double) |  | Valor dos acrescimos recebidos da venda |
| `valorDesconto` | number (double) |  | Valor dos descontos recebidos da venda |
| `outrosValores` | number (double) |  | Outros valores recebidos da venda |
| `totalParcelas` | integer (int32) |  | total de parcelas recebidas |
| `totalRecebidasAtrasadas` | integer (int32) |  | total de parcelas recebidas atrasadas |
| `percentualRecebidasAtrasadas` | number (double) |  | Percentual das parcelas recebidas atrasadas |
| `totalRecebidasAdiantadas` | integer (int32) |  | Total de parcelas da venda recebidas adiantadas |
| `percentualRecebidasAdiantadas` | number (double) |  | Percentual de parcelas recebidas adiantadas |
| `mediaDiasAdiantamento` | integer (int32) |  | Media de dias de adiantamento das parcelas recebidas |

### UAUApi.Models.Venda.VendaIntegracao.TotaisAReceber

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `valorSaldoDevedor` | number (double) |  | Valor do saldo devedor que ainda falta receber |
| `valorPrincipal` | number (double) |  | Valor principal a receber |
| `valorJuros` | number (double) |  | Valor dos juros a receber |
| `valorCorrecao` | number (double) |  | Valor da correção a receber |
| `valorMulta` | number (double) |  | Valor da multa a receber |
| `valorJurosAtraso` | number (double) |  | Valor dos juros de atraso a receber |
| `valorResiduoNaoGerado` | number (double) |  | Valor do residuo não gerado. |
| `outrosValores` | number (double) |  | Outros valores a receber |
| `totalParcelas` | integer (int32) |  | Valor total das parcelas a receber |
| `totalParcelasAtrasadas` | integer (int32) |  | Valor total das parcelas atrasadas a receber |
| `percentualAtrasadas` | number (double) |  | Percentual de parcelas atrasadas |

### UAUApi.Models.Venda.VendaIntegracao.ParcelasPorTipo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoParcela` | string |  | Tipo da parcela da venda |
| `descricaoTipoParcela` | string |  | Descrição do tipo da parcela da venda |
| `quantidadeParcelaAPagar` | integer (int32) |  | Quantidades de parcelas a pagar da venda |
| `totalParcelaAPagar` | number (double) |  | Total das parcelas a pagar da venda |
| `quantidadeParcelaPaga` | integer (int32) |  | Quantidade de parcelas pagas da venda |
| `totalParcelaPaga` | number (double) |  | Total das parcelas pagas da venda |

### UAUApi.Models.Venda.ResumoVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa |
| `codigoObra` | string |  | Código da obra |
| `numeroVenda` | integer (int32) |  | Número da venda |
| `dataCalculo` | string (date-time) |  | Data do cálculo |
| `dataCorrecao` | string (date-time) |  | Data da correção |
| `antecipar` | boolean |  | Antecipar parcelas |
| `parcelas` | array de [`UAUApi.Models.Venda.ParcelasResumoVendaRequest`](#uauapimodelsvendaparcelasresumovendarequest) |  | Lista de parcelas para antecipação do resumo de venda |
| `aplicarDescontoGeral` | boolean |  | Aplicar desconto geral |
| `percentualDescontoGeral` | number (double) |  | Percentual de desconto geral a ser aplicado |
| `aplicarDescontoAntecipacao` | boolean |  | Aplicar desconto de antecipação |
| `descontoAntecipacao` | [`UAUApi.Models.Venda.DescontoAntecipacaoResumoVendaRequest`](#uauapimodelsvendadescontoantecipacaoresumovendarequest) |  | Dados do desconto de antecipação |

### UAUApi.Models.Venda.DescontoAntecipacaoResumoVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `percentualDescAntecipacao` | number (double) |  | Percentual de desconto de antecipação |
| `tipoDescAntecipacao` | integer (int32) |  | Tipo de desconto de antecipação |
| `descontoAteHabitese` | boolean |  | Configuração de até o habite-se |

### UAUApi.Models.Venda.ParcelasResumoVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroParcela` | integer (int32) |  | Numero da parcela |
| `numeroParcelaGeral` | integer (int32) |  | Numero geral da parcela |
| `tipoParcela` | string |  | Tipo da parcela |

### UAUApi.Models.Venda.ConsultarPlanoIndexadoresVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |
| `venda` | integer (int32) | ✓ | Número da venda |

### Globaltec.UAU.Vendas.DTOPedidoRecebimento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroPedidoRecebimento` | integer (int64) |  |  |
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `NumeroVenda` | integer (int32) |  |  |
| `NumeroParcela` | integer (int32) |  |  |
| `TipoParcela` | string |  |  |
| `NumeroParcelaGerada` | integer (int32) |  |  |
| `DataCalculo` | string (date-time) |  |  |
| `ValorReajustado` | number (double) |  |  |
| `DataVecimento` | string (date-time) |  |  |
| `NumeroPedido` | integer (int32) |  |  |
| `ValorTot` | number (double) |  |  |
| `Status` | integer (int32) |  |  |
| `NumeroProduto` | integer (int32) |  |  |
| `Referencia` | string |  |  |
| `Modalidade` | integer (int32) |  |  |
| `QtdMaxParcela` | integer (int32) |  |  |
| `Adquirente` | integer (int32) |  |  |
| `DataCadastro` | string (date-time) |  |  |
| `UsuarioCadastro` | string |  |  |
| `DataCancelamento` | string (date-time) |  |  |
| `UsuarioCancelamento` | string |  |  |
| `Estabelecimento` | integer (int32) |  |  |
| `ValorDesconto` | number (double) |  |  |
| `PartePac` | boolean |  |  |
| `Antecipacao` | boolean |  |  |
| `Origem` | integer (int32) |  |  |

### UAUApi.Models.Venda.PedidoRequestUAU

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroNTK` | integer (int32) |  | Número do pedido na NTK |
| `NumeroPedido` | integer (int32) |  | Número do pedido UAU |

### UAUApi.Models.Venda.ConsultarParcelasDaVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |
| `num_venda` | integer (int32) | ✓ | Número da venda |
| `data_calculo` | string (date-time) | ✓ | Data de cálculo |
| `boleto_antecipado` | boolean | ✓ | Indica se irá realizar cálculo de antecipação nas parcelas |
| `somenteParcelasAptasBoleto` | boolean |  | Retornar somente parcelas aptas para gerar boleto. |

### UAUApi.Models.Venda.HistoricoVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroHistorico` | integer (int32) |  | Número do histórico de manutenção |
| `TipoManutencao` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |  | Tipo da manutenção     0. Cancelar venda     1. Renegociar contrato     2. Cessão de direito     3. Simulação de distrato     4. Alterar parâmetros da venda     5. Alterar juros em parcelas price     6. Acerto final     7. Renegociação pendente     8. Cessão de direito pendente     9. Renegociação pendente com emissão de boleto     10. Renegociação de parcelas pendente     11. Renegociação de parcelas pendente com emissão de boleto     12. Renegociação de parcelas      13. Recebimento Parcial     14. Devolução de recebimento parcial     15. Devolução de recebimento parcial com estorno     16. Cancelamento de Aluguéis |
| `UsuarioManutencao` | string |  | Usuário que realizou a manutenção |
| `DataManutencao` | string (date-time) |  | Data da manutenção |
| `NumVendaCessao` | integer (int32) |  | Número da nova venda da cessão |
| `Empresa` | integer (int32) |  | Código da empresa. |
| `Obra` | string |  | Código da obra. |
| `Numero` | integer (int32) |  | Número da venda. |
| `ContratoDeMedicao` | integer (int32) |  | Número do contrato de medição. |
| `CodigoVendedor` | integer (int32) |  | Código do vendedor. |
| `CpfCnpjVendedor` | string |  | CPf ou Cnpj do vendedor. |
| `ValorTotal` | number (double) |  | Valor total da venda. |
| `PercentualJurosAtraso` | number (double) |  | Percentual dos juros de atraso. |
| `Multa` | number (double) |  | Valor da multa. |
| `Desconto` | number (double) |  | Valor do desconto. |
| `Usuario` | string |  | Código do usuário de cadastro da venda. |
| `DataDaVenda` | string (date-time) |  | Data da venda. |
| `StatusVenda` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4 |  | Status da venda. 0 - Normal 1 - Cancelada 2 - Alterada 3 - Quitada 4 - Em acerto |
| `Acrescimo` | number (double) |  | Valor de acréscimo. |
| `ContinuarCobrandoJurosContratualAoAtrasarParcela` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá continuar cobrando juros contratual ao atrasar as parcelas da venda. 0 - Não 1 - Sim |
| `StatusEscritura` | array de integer (int32) |  | Lista de status de escritura vinculados à venda. |
| `StatusCobranca` | array de integer (int32) |  | Lista de status de cobrança vinculados à venda. |
| `PossuiReajusteAnual` | integer (int32) |  | Indica se o cálculo do reajuste não será mensal. 0 - Não (significa que o cálculo de reajuste será mensal) 1 - Sim (significa que o cálculo de reajuste não será mensal, ou seja, será semestral ou anual |
| `GerarResiduo` | integer (int32) |  | Indica se irá gerar resíduo no caso de calcular reajuste não mensal. 0 - Não  1 - Sim |
| `CarenciaAtraso` | integer (int32) |  | Número de dias de carência para cobrança de juros e multa por atraso. |
| `QuantidadeMesesRetroagirCorrecao` | integer (int32) |  | Número de meses que irá retroagir a data de reajuste. |
| `DataBaseResiduo` | string (date-time) |  | Data base para geração das parcelas de resíduo. |
| `PossuiCorrecaoPorAtraso` | integer (int32) |  | Indica se irá cobrar correção por atraso. 0 - Não 1 - Sim |
| `PossuiCorrecaoProRata` | integer (int32) |  | Indica se o cálculo da correção será pró-rata. 0 - Não 1 - Sim |
| `DataCessaoDeDireito` | string (date-time) |  | Data de cessão de direitos. |
| `DataCancelamento` | string (date-time) |  | Data de cancelamento da venda. |
| `CodigoDeDivulgacao` | integer (int32) |  | Código do meio de divulgação que originou a venda. |
| `CodigoFinalidade` | integer (int32) |  | Código da finalidade da compra que originou a venda. |
| `CobrarTaxaDeBoleto` | integer (int32) — valores possíveis: 0, 1 |  | Indica se irá cobrar taxa de boleto para os boletos emitidos para a venda. 0 - Não 1 - Sim |
| `DataDeCadastro` | string (date-time) |  | Data de cadastro da venda. |
| `ObraFiscal` | string |  | Código da obra fiscal. |
| `TipoDeVenda` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5 |  | Código do tipo da venda. 0 - Venda 1 - Aluguel 2 - Aluguel Garantido 3 - Transação financeira 4 - Revenda 5 - Aluguel shopping |
| `AluguelShopping` | [`UAUApi.Models.Venda.AluguelDeShopping`](#uauapimodelsvendaalugueldeshopping) |  | Parâmetros de um aluguel shopping. |
| `DiaDoRepasse` | integer (int32) |  | Define o dia do mês que será repassado o valor de aluguel para o(s) proprietário(s). |
| `ValorProvisaoCurto` | number (double) |  | Valor de provisionamento de curto prazo. |
| `ValorProvisaoLongo` | number (double) |  | Valor de provisionamento de longo prazo. |
| `CapProvisaoCurto` | string |  | CAP do valor de provisionamento de curto prazo. |
| `CapProvisaoLongo` | string |  | CAP do valor de provisionamento de longo prazo. |
| `DiasCarenciaCorrecaoPorAtraso` | integer (int32) |  | Número de dias de carência para cobrança de correção por atraso. |
| `AnteciparCorrecao` | integer (int32) |  | Indica se será cobrado correção diária ao realizar antecipação das parcelas da venda. 0 - Não 1 - Sim |
| `CobrarJurosPosChave` | integer (int32) — valores possíveis: 0, 1 |  | Indica se uma parcela, cujo vencimento seja anterior ao início de juros, caso seja recebido após a data de início de juros, irá cobrar juros. 0 - Não 1 - Sim |
| `DataInicioContrato` | string (date-time) |  | Data do início do contrato de venda ou aluguel. |
| `DataFimContrato` | string (date-time) |  | Data do fim do contrato de venda ou aluguel. |
| `TipoDeFianca` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5, 6, 7 |  | Código que define o tipo da fiança da venda.  0 - Sem fiança 1 - Fiadores 2 - Fiança bancária 3 - Caução 4 - Seguro fiança locaticia 5 - Carta fiança 6 - Título de capitalização 7 - Imóvel em garantia |
| `DadosDaFianca1` | string |  | Informação do tipo de fiança da venda. |
| `DadosDaFianca2` | string |  | Informação do tipo de fiança da venda. |
| `DadosDaFianca3` | string |  | Informação do tipo de fiança da venda. |
| `DataDaFianca` | string (date-time) |  | Data da fiança. Seu contexto varia de acordo com o tipo da fiança . |
| `ValorDaFianca` | number (double) |  | Valor da fiança. Seu contexto varia de acordo com o tipo da fiança. |
| `NomeSeguroIncendio` | string |  | Nome da seguradora responsável pelo seguro contra incêndio. |
| `ApoliceSeguroIncendio` | string |  | Número da apólice do seguro contra incêndio. |
| `ValorSeguroIncendio` | number (double) |  | Valor da apólice do seguro contra incêndio. |
| `DataVencimentoSeguroIncendio` | string (date-time) |  | Data do vencimento do seguro contra incêndio. |
| `CobrarMultaFracionada` | integer (int32) — valores possíveis: 0, 1 |  | Indica se a multa cobrada em caso de atraso da parcela será cobrada fracionada por dia. 0 - Não 1 - sim |
| `AnteciparJurosLinear` | integer (int32) |  | Indica se a antecipação das parcelas com juros simples será realizada de forma linear. 0 - Não 1 - sim |
| `ValorDescontoImposto` | number (double) |  | Valor total de imposto lançado na venda. |
| `PeriodoDeReajuste` | integer (int32) |  | Indica a periodicidade de reajuste nos casos de correção não mensal. |
| `HistoricoLancamentoContabilVenda` | string |  | Histórico de lançamento contábil da venda. |
| `HistoricoLancamentoContabilParcela` | string |  | Histórico de lançamento contábil das parcelas da venda. |
| `HistoricoLancamentoContabilJurosCorrecao` | string |  | Histórico de lançamento contábil dos juros e correções da venda. |
| `ZerarCorrecaoNegativa` | integer (int32) |  | Indica se irá zerar o valor de correção da parcela nos casos que o valor líquido da mesma seja inferior ao valor principal. 0 - Não 1 - Sim |
| `CobrarJurosPorAtrasoMensal` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o cálculo de juros por atraso será realizado de forma mensal ou pró-rata. 0 - Não 1 - Sim |
| `CorrecaoCrescente` | integer (int32) |  | Indica se irá congelar o valor de correção da parcela caso o índice de correção da mesma possua deflação entre o mês anterior e o atual. 0 - Não 1 - Sim |
| `EnviarSpedPisCofins` | integer (int32) — valores possíveis: 0, 1 |  | Indica se a venda ou aluguel será enviado para o SPED PIS/CONFINS. 0 - Não 1 - Sim |
| `ContratoCaixaEconomicaFederal` | string |  | Número do contrato de financiamento associativo da venda na Caixa Econômica Federal. |
| `Atividade` | integer (int32) — valores possíveis: 0, 1, 2, 3 |  | Código do tipo de atividade da venda. 0 - Atividade imobiliária 1 - Prestação de serviço |
| `ValorProvisaoCurtoBaixa` | number (double) |  | Valor de provisionamento de curto prazo no momento da quitação/cancelamento da venda. |
| `ValorProvisaoLongoBaixa` | number (double) |  | Valor de provisionamento de longo prazo no momento da quitação/cancelamento da venda. |
| `ValorProvisaoCurtoCessao` | number (double) |  | Valor de provisionamento de curto prazo no momento da realização de cessão de direito da venda. |
| `ValorProvisaoLongoCessao` | number (double) |  | Valor de provisionamento de longo prazo no momento da realização de cessão de direito da venda. |
| `CapProvisaoCurtoBaixa` | string |  | CAP do valor de provisionamento de curto prazo no momento da quitação/cancelamento da venda. |
| `CapProvisaoLongoBaixa` | string |  | CAP do valor de provisionamento de longo prazo no momento da quitação/cancelamento da venda. |
| `HistoricoLancamentoBaixaProvisao` | string |  | Histórico de lançamento contábil do provisionamento no momento da quitação/cancelamento da venda. |
| `CobrarCorrecaoMaisProrataMesRecebimento` | integer (int32) — valores possíveis: 0, 1 |  | Indica se deverá cobrar correção mais prórata no mês de recebimento da parcela da venda. |
| `CobrarJurosAnual` | integer (int32) — valores possíveis: 0, 1 |  | Indica se o cálculo de juros contratual da venda será mensal. 0 - Não 1 - Sim |
| `PeriodoCobrancaDeJuros` | integer (int32) |  | Indica a periodicidade de reajuste nos casos de correção não mensal. |
| `ValorPrestacaoDeServicos` | number (double) |  | Valor de prestação de serviço da venda. |
| `AnteciparCorrecaoProximoPeriodo` | integer (int32) |  | Indica se o cálculo de correção ao antecipar as parcelas da venda será realizado apenas no próximo período da venda de acordo com a data de cálculo. 0 - Não 1 - Sim |
| `VendaVinculada` | [`UAUApi.Models.Venda.VendaVinculada`](#uauapimodelsvendavendavinculada) |  | Venda a qual a venda está vinculada. |
| `CodigoUltimaManutencao` | integer (int32) |  | Código da última manutenção. |
| `TributadoPeloRet` | integer (int32) — valores possíveis: 0, 1 |  | Tributado pelo retorno. 0 - Não 1 - Sim |
| `TributacaoRET` | string |  | Tributado do retorno. |
| `CodigoServico` | integer (int32) |  | Código do serviço. |
| `ValorTotalImposto` | number (double) |  | Valor total do imposto. |
| `ValorTotalComissao` | number (double) |  | Valor total da comissão. |
| `Parametros` | array de [`UAUApi.Models.Venda.ParametrosDaVenda`](#uauapimodelsvendaparametrosdavenda) |  | Parâmetros da venda. |
| `Clientes` | array de [`UAUApi.Models.Venda.ClienteDaVenda`](#uauapimodelsvendaclientedavenda) |  | Lista de clientes da venda. |
| `Itens` | array de [`UAUApi.Models.Venda.ItemDaVenda`](#uauapimodelsvendaitemdavenda) |  | Lista dos itens vendidos na venda. |
| `Parcelas` | array de [`UAUApi.Models.Venda.Parcela`](#uauapimodelsvendaparcela) |  | Lista de parcelas a receber e recebidas da venda. |
| `Impostos` | array de [`UAUApi.Models.Venda.ImpostoDaVenda`](#uauapimodelsvendaimpostodavenda) |  | Lista de impostos vinculados à venda. |
| `Comissoes` | array de [`UAUApi.Models.Venda.ControleDeComissaoDaVenda`](#uauapimodelsvendacontroledecomissaodavenda) |  | Lista de comissões geradas a partir da venda. |
| `Seguros` | array de [`UAUApi.Models.Venda.Seguro`](#uauapimodelsvendaseguro) |  | Lista de seguros vinculados à venda. |
| `PlanosIndexadores` | array de [`UAUApi.Models.Venda.PlanoIndexadorDaVenda`](#uauapimodelsvendaplanoindexadordavenda) |  | Lista de planos indexadores configurados na venda. |
| `Comentarios` | array de [`UAUApi.Models.Venda.ComentarioDaVenda`](#uauapimodelsvendacomentariodavenda) |  | Lista de comentários da venda. |
| `FinanciamentoImobiliario` | [`UAUApi.Models.Venda.VendasFinancImob`](#uauapimodelsvendavendasfinancimob) |  | Informação do financiamento imobiliário |

### UAUApi.Models.Venda.ConsultarHistoricosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Vendas` | array de [`UAUApi.Models.Venda.VendasComManutencao`](#uauapimodelsvendavendascommanutencao) |  | Lista de objeto (VendasComManutencao) com as vendas selecionadas para visualizar a manutenção se existir |
| `DataInicio` | string (date-time) |  | Data inicial da manutenção |
| `DataFim` | string (date-time) |  | Data final da manutenção |
| `TipoManutencao` | string |  | Tipo de manutenção     0. Cancelar venda     1. Renegociar contrato     2. Cessão de direito     3. Simulação de distrato     4. Alterar parâmetros da venda     5. Alterar juros em parcelas price     6. Acerto final     7. Renegociação pendente     8. Cessão de direito pendente     9. Renegociação pendente com emissão de boleto     10. Renegociação de parcelas pendente     11. Renegociação de parcelas pendente com emissão de boleto     12. Renegociação de parcelas      13. Recebimento Parcial     14. Devolução de recebimento parcial     15. Devolução de recebimento parcial com estorno     16. Cancelamento de Aluguéis |

### UAUApi.Models.Venda.VendasComManutencao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa da venda |
| `Obra` | string | ✓ | Código da obra da venda |
| `Venda` | integer (int32) |  | Código da venda, se não informar a venda, buscará todas as vendas da empresa e obra selecionada |

### UAUApi.Models.Venda.ConsultarEmpreendimentosClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo_usuario` | integer (int32) |  | Código do cliente do cadastro de pessoas |

### UAUApi.Models.Venda.ConsultarDescontoAntecipacaoParcelaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |
| `num_venda` | integer (int32) | ✓ | Número da venda |
| `num_parc` | integer (int32) |  | Número da parcela |
| `numparc_ger` | integer (int32) |  | Número geral da parcela |
| `tipo_parc` | string |  | Tipo da parcela |
| `data_calculo` | string (date-time) |  | Data de cálculo |
| `valor_parcela` | number (double) |  | Valor da parcela corrigido |
| `data_vencimento` | string (date-time) |  | Data de vencimento da parcela |
| `data_prorrogacao` | string (date-time) |  | Data de prorrogação da parcela |
| `totalparcelas_sel` | integer (int32) |  | Total de parcelas selecionadas |
| `antecipado` | boolean |  | Se o campo for verdadeiro (true), a data de cálculo informada na requisição será considerada para calcular o desconto. Caso contrário (false), será considerada a data de prorrogação. |
| `totalpara_quitacao` | integer (int32) |  | Total de parcelas para quitação |

### UAUApi.Models.Venda.VendaIntegracao.DemonstrativoCorrecao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoCliente` | integer (int32) |  | Código do cliente |
| `nomeCliente` | string |  | Nome do cliente |
| `codigoEmpresa` | integer (int32) |  | Código da empresa |
| `descricaoEmpresa` | string |  | Descrição da empresa |
| `codigoObra` | string |  | Código da obra |
| `descricaoObra` | string |  | Descrição da obra |
| `numeroVenda` | integer (int32) |  | Numero da venda |
| `dataVenda` | string (date-time) |  | Data da venda |
| `valorReajustado` | number (double) |  | Valor reajustado |
| `valorMulta` | number (double) |  | Valor da multa |
| `valorJurosAtraso` | number (double) |  | Valor dos juros de atraso |
| `valorCorrecao` | number (double) |  | Valor de correção |
| `valorCorrecaoAtraso` | number (double) |  | Valor de correção de atraso |
| `valorOutros` | number (double) |  | Outros valores |
| `valorDescontoAdiantamento` | number (double) |  | Valor do desconto de adiantamento |
| `valorDescontoImposto` | number (double) |  | Valor de desconto do imposto |
| `valorDescontoCusta` | number (double) |  | Valor de desconto da custa |
| `valorResiduo` | number (double) |  | Valor do resíduo |
| `valorDesconto` | number (double) |  | Valor do desconto |
| `valorJuros` | number (double) |  |  |
| `valorPrincipal` | number (double) |  |  |
| `valorBase` | number (double) |  |  |
| `parcelaRecebida` | boolean |  | Parcela recebida sim Não |
| `valorPago` | number (double) |  | Valor pago |
| `itens` | array de [`UAUApi.Models.Venda.VendaIntegracao.ItemDemonstrativoCorrecao`](#uauapimodelsvendavendaintegracaoitemdemonstrativocorrecao) |  | Itens da venda |
| `parametrosParcela` | [`UAUApi.Models.Venda.VendaIntegracao.ParametrosParcela`](#uauapimodelsvendavendaintegracaoparametrosparcela) |  | Parâmetros da parcela |
| `dadosCorrecao` | [`UAUApi.Models.Venda.VendaIntegracao.DadosCorrecao`](#uauapimodelsvendavendaintegracaodadoscorrecao) |  | Dados da correção |
| `demonstrativoCorrecao` | array de [`UAUApi.Models.Venda.VendaIntegracao.ValoresDemonstrativoCorrecao`](#uauapimodelsvendavendaintegracaovaloresdemonstrativocorrecao) |  | Demonstrativos da correção |

### UAUApi.Models.Venda.VendaIntegracao.ValoresDemonstrativoCorrecao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `correcaoAtraso` | boolean |  | Correção de atraso |
| `indice` | string |  | Índice |
| `dataCorrecao` | string |  | Data de correção |
| `valorIndice` | number (double) |  | Valor do índice |
| `coeficienteIndice` | number (double) |  | Coeficiente do índice |
| `valorCorrigido` | string |  | Valor corrigido |
| `dataInicial` | string |  | Data inicial |
| `dataFinal` | string |  | Data final |
| `valorDia` | number (double) |  | Valor do dia |
| `quantidadeDias` | integer (int32) |  | Quantidade de dias |
| `fator` | number (double) |  | Fator |

### UAUApi.Models.Venda.VendaIntegracao.DadosCorrecao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `reajusteNaoMensal` | integer (int32) |  | Reajuste não mensal 0 - Não 1 - Sim |
| `gerarResiduo` | integer (int32) |  | Gerar residuo 0 - Não 1 - Sim |
| `comPlanoIdx` | integer (int32) |  | Com plano idx 0 - Não 1 - Sim |
| `zerarCorrecaoNegativa` | integer (int32) |  | Zerar correção negativa 0 - Não 1 - Sim |
| `reatrocaoIdx` | integer (int32) |  | Retroação idx (Meses) |
| `frequenciaReajuste` | integer (int32) |  | Frequência de reajuste (Meses) |
| `correcaoProrata` | integer (int32) |  | Correção pro-rata 0 - Não 1 - Sim |
| `correcaoCrescente` | integer (int32) |  | Correção crescente 0 - Não 1 - Sim |

### UAUApi.Models.Venda.VendaIntegracao.ParametrosParcela

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipo` | string |  | Código do tipo da parcela |
| `descricaoTipo` | string |  | Descrição do tipo da parcela |
| `dataCalculo` | string (date-time) |  | Data de cálculo |
| `dataCorrecao` | string (date-time) |  | Data de correção |
| `primeiraTaxaJuros` | number (double) |  | Primeira taxa de juros |
| `segundaTaxaJuros` | number (double) |  | Segunda taxa de juros |
| `valorOriginal` | number (double) |  | Valor original |
| `dataVencimento` | string (date-time) |  | Data de vencimento |
| `multa` | number (double) |  | Valor da multa |
| `jurosAtraso` | number (double) |  | Valor dos juros de atraso |

### UAUApi.Models.Venda.VendaIntegracao.ItemDemonstrativoCorrecao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoProduto` | integer (int32) |  | Código do produto |
| `descricaoProduto` | string |  | Descrição do produto |
| `numeroPersonalizacao` | integer (int32) |  | Número da personalização |
| `identificador` | string |  | Código identificador |
| `quantidade` | number (double) |  | Quantidade |

### UAUApi.Models.Venda.DemonstrativoCorrecaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Codigo da empresa |
| `obra` | string |  | Codigo da obra |
| `venda` | integer (int32) |  | Numero da venda |
| `numeroParcela` | integer (int32) |  | Numero da parcela |
| `numeroParcelaGeral` | integer (int32) |  | Numero geral da parcela |
| `tipoParcela` | string |  | Tipo da parcela |
| `dataCalculo` | string (date-time) |  | Data de calculo do resumo de venda |
| `dataCorrecao` | string (date-time) |  | Data da correção do resumo de venda |
| `valorAntecipado` | boolean |  | Calcular com valor antecipado True - Sim False - Não |

### UAUApi.Models.Venda.VendaIntegracao.ContasReceberCalc

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Codigo da empresa |
| `descrEmpresa` | string |  | Descrição da empresa |
| `obra` | string |  | Codigo da obra |
| `descrObra` | string |  | Descrição da obra |
| `numeroVenda` | integer (int32) |  | Numero da venda |
| `numeroParcela` | integer (int32) |  | Numero da parcela |
| `numeroParcelaGeral` | integer (int32) |  | Numero da parcela geral |
| `tipoParcela` | string |  | Tipo da Parcela |
| `descrTipoParcela` | string |  | Descrição do tipo da parcela |
| `cliente` | integer (int32) |  | Codigo do cliente |
| `nomeCliente` | string |  | Descrição do cliente |
| `dataCalculo` | string (date-time) |  | Data do calculo de conta a receber |
| `dataVencimento` | string (date-time) |  | Data de vencimento |
| `valorReajustado` | number (double) |  | Valor reajustado |
| `valorPrincipal` | number (double) |  | Valor principal |
| `valorPrincipalPrice` | number (double) |  | Valor principal Price |
| `valorJuros` | number (double) |  | Valor do juros |
| `valorJurosPrice` | number (double) |  | Valor do juros price |
| `valorCorrecao` | number (double) |  | Valor de correção |
| `valorJurosAtraso` | number (double) |  | Valor juros por atraso |
| `valorMulta` | number (double) |  | Valor da multa |
| `valorCorrecaoAtraso` | number (double) |  | Valor de correção por atraso |
| `valorDescontoCusta` | number (double) |  | Valor desconto custa |
| `valorDescontoImposto` | number (double) |  | Valor desconto imposto |
| `valorTaxaBoleto` | number (double) |  | Valor da taxa do boleto |
| `valorRejustadoAntecipado` | number (double) |  | Valor reajustado atencipado |
| `valorJurosAntecipado` | number (double) |  | Valor juros antecipado |
| `valorJurosPriceAntecipado` | number (double) |  | Valor juros price antecipado |
| `valorCorrecaoAntecipado` | number (double) |  | Valor correção antecipado |
| `valorDescontoAvpPorFaixa` | number (double) |  | Valor desconto avp por faixa |

### UAUApi.Models.Venda.ConsultarContasReceberCalcRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `DataInicio` | string (date-time) |  | Data de Inicio - Para filtrar por data de vencimento. |
| `DataFim` | string (date-time) |  | Data Final - Para filtrar por data de vencimento. |
| `TiposParcela` | string |  | Código do tipo da parcela. Ex.: 'P', 'M' |
| `Vendas` | array de [`UAUApi.Models.Venda.VendasContasReceberCalcRequest`](#uauapimodelsvendavendascontasrecebercalcrequest) |  | Lista com as chaves das vendas (Venda, Obra, Empresa) |

### UAUApi.Models.Venda.VendasContasReceberCalcRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string |  | Código da obra |
| `Numero` | integer (int32) |  | Código da venda |

### UAUApi.Models.Venda.VendaIntegracao.CampanhaDescontoDisponivel

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoCampanha` | integer (int32) |  | Codigo da campanha |
| `descricaoCampanha` | string |  | Descrição da campanha |
| `valorTotalAPagar` | number (double) |  | Valor total a ser pago |
| `valorDesconto` | number (double) |  | Valor do desconto |
| `totalSimuladoQuitacao` | number (double) |  | Valor total para a quitação |
| `descontos` | array de [`UAUApi.Models.Venda.VendaIntegracao.DescontosCampanhaDisponiveis`](#uauapimodelsvendavendaintegracaodescontoscampanhadisponiveis) |  | Lista com os descontos da campanha |

### UAUApi.Models.Venda.VendaIntegracao.DescontosCampanhaDisponiveis

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipo` | integer (int32) |  | Tipo da campanha disponível |
| `descricaoTipoCampanha` | string |  | Descrição da campanha |
| `percentualDesconto` | number (double) |  | Percentual de desconto definido na campanha |
| `tipoDesconto` | integer (int32) |  | Tipo de desconto definido na campanha |
| `descricaoTipoDesconto` | string |  | Descrição do tipo de desconto |
| `tipoObra` | integer (int32) |  | Tipo da obra da venda |
| `numeroParcelaInicial` | integer (int32) |  | Numero inicial da parcela que irá aplicar o desconto |
| `numeroParcelaFinal` | integer (int32) |  | Numero final da parcela que irá aplicar o desconto |
| `descontoAteHabiteSe` | boolean |  | Define se o desconto é até a habitese |
| `DoMes` | integer (int32) |  | Quantidade de meses antecipados inicial (meses antecipação) |
| `AteMes` | integer (int32) |  | Quantidade de meses antecipados final (meses antecipação) |
| `DescontoTipo` | integer (int32) |  | 0 - Percentual 1 - Coeficiente (meses antecipação) |
| `DescrDescontoTipo` | string |  | Descrição     - 0 = "Percentual"    - 1 = "Coeficiente"  (meses antecipação) |
| `DescCoeficiente` | number (double) |  | Valor do desconto percentual ou coeficiente a se aplicado (meses antecipação) |

### UAUApi.Models.Venda.CampanhaDescontoDisponivelRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa da venda |
| `codigoObra` | string |  | Código da obra da venda |
| `numeroVenda` | integer (int32) |  | Numero da venda |
| `dataCalculo` | string (date-time) |  | Data do calculo da campanha da venda |
| `dataCorrecao` | string (date-time) |  | Data de correção das parcelas |

### UAUApi.Models.CalcularDesconto.ParcelaCalculadaCampanha

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Venda` | integer (int32) |  |  |
| `Numero` | integer (int32) |  |  |
| `NumeroGeral` | integer (int32) |  |  |
| `Tipo` | string |  |  |
| `DataVencimento` | string (date-time) |  |  |
| `DataProrrogacao` | string (date-time) |  |  |
| `ValorCorrigido` | number (double) |  |  |
| `DesconsiderarQuitacao` | boolean |  |  |
| `DataInicioJuros` | string (date-time) |  |  |
| `ValorDescontoCalculado` | number (double) |  |  |

### UAUApi.Models.CalcularDesconto.ParcelasCalculadasCampanhaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampanhaDeDesconto` | [`UAUApi.Models.CalcularDesconto.CampanhaVenda`](#uauapimodelscalculardescontocampanhavenda) |  |  |
| `ParcelasCalculadas` | array de [`UAUApi.Models.CalcularDesconto.ParcelaCalculadaCampanha`](#uauapimodelscalculardescontoparcelacalculadacampanha) |  |  |
| `DataCalculo` | string (date-time) |  |  |

### Globaltec.UAU.Vendas.ParcelasDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Tipo` | string |  |  |
| `Descricao` | string |  |  |

### Globaltec.UAU.Vendas.CustasTipoDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |

### Globaltec.UAU.Vendas.StatusDeEscrituraDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  |  |
| `Descricao` | string |  |  |

### Globaltec.UAU.Vendas.StatusCobrancaDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |

### UAUApi.Models.Venda.BuscarRecebimentosDaVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |
| `venda` | integer (int32) | ✓ | Código da venda |
| `parcelasnao_conciliadas` | boolean |  | Parcelas NÃO conciliadas: ("true": aceita, "false": recusa) |

### UAUApi.Models.Venda.BuscarParcelasRecebidasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra da venda |
| `num_ven` | integer (int32) | ✓ | Nº da venda |

### UAUApi.Models.Venda.BuscarParcelasAReceberRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `obra` | string |  | Código da obra da venda |
| `num_ven` | integer (int32) |  | Nº da venda |
| `data_calculo` | string (date-time) |  | Data para calcular o valor das parcelas a receber |
| `valor_presente` | boolean |  | Indica se irá calcular o valor das parcelas a receber a valor presente |

### Globaltec.UAU.Vendas.ParametroCobrancaDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Banco` | string |  |  |
| `NomeBanco` | string |  |  |
| `Conta` | string |  |  |
| `Agencia` | string |  |  |
| `Carteira` | string |  |  |
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |
| `Empresa` | string |  |  |
| `Cedente` | string |  |  |

### UAUApi.Models.Venda.ParametroCobrancaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa para filtrar parâmetros de cobrança (Não obrigatório) |
| `banco` | integer (int32) |  | Número do banco para filtrar parâmetros de cobrança (Não obrigatório) |

### UAUApi.Models.CalcularDesconto.CampanhaVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) |  |  |
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Venda` | integer (int32) |  |  |
| `TipoObraVenda` | integer (int32) |  | 0-Obra em contrução ; 1-Obra concluída |
| `TotalParaQuitacao` | integer (int32) |  | Quantidade total de parcelas da venda que pode ser considerada para saber se é uma quitação |
| `QuantidadeMinima` | integer (int32) |  |  |
| `TiposParcelasPermitidos` | string |  |  |
| `ValorMinimo` | number (double) |  |  |
| `TipoFaixa` | integer (int32) |  |  |
| `Aliquotas` | array de [`UAUApi.Models.CalcularDesconto.CampanhaAliquota`](#uauapimodelscalculardescontocampanhaaliquota) |  |  |

### UAUApi.Models.CalcularDesconto.CampanhaAliquota

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `FaixaInicio` | integer (int32) |  |  |
| `FaixaFinal` | integer (int32) |  |  |
| `TipoAliquota` | integer (int32) |  | 0-Fixo ; 1-Simples ; 2-Acumulado ; 3-Composto |
| `AteHabitese` | boolean |  | TRUE - Somente até habite-se (inicio cobrança de juros) |
| `Porcentagem` | number (double) |  |  |
| `TipoObra` | integer (int32) |  | 0-Obra em construção ; 1-Concluída ; 2-Ambas |
| `TipoDesconto` | object |  | 0-Antecipaçao ; 1-Quitação |
| `Faixa` | integer (int32) |  |  |
| `DoMes` | integer (int32) |  |  |
| `AteMes` | integer (int32) |  |  |

### UAUApi.Models.CalcularDesconto.CampanhaVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ |  |
| `Obra` | string | ✓ |  |
| `Venda` | integer (int32) | ✓ |  |
| `DataCalculo` | string (date-time) | ✓ |  |

### UAUApi.Models.Venda.BuscaParcRenegWebRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |
| `num_ven` | integer (int32) | ✓ | Código da venda |
| `exibirparcenv_cob` | boolean | ✓ | Retornar somente parcelas enviadas a cobrança: TRUE = sim, FALSE = não |
| `somenteparc_atraso` | boolean | ✓ | Retornar somente parcelas em atraso: TRUE = sim, FALSE = não |
| `parcelasenviadas_banco` | boolean | ✓ | Retornar parcelas enviadas ao banco: TRUE = sim, FALSE = não |

### Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoPedido

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Data` | string |  |  |
| `Pedido` | [`Globaltec.UAU.Vendas.DTOs.Cartao.Pedido`](#globaltecuauvendasdtoscartaopedido) |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.Pedido

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Referencia` | string |  |  |
| `Obs` | string |  |  |
| `Data` | string |  |  |
| `Hora` | string |  |  |
| `Valor` | number (double) |  |  |
| `ValorFormat` | string |  |  |
| `ValorAberto` | number (double) |  |  |
| `ValorAbertoFormat` | string |  |  |
| `ValorOriginalPago` | number (double) |  |  |
| `ValorOriginalPagoFormat` | string |  |  |
| `ValorOriginalEmPagamento` | number (double) |  |  |
| `ValorOriginalEmPagamentoFormat` | string |  |  |
| `Tipo` | string |  |  |
| `Quantidade` | integer (int32) |  |  |
| `QuantidadeTransacoes` | integer (int32) |  |  |
| `PedidoStatus` | [`Globaltec.UAU.Vendas.DTOs.Cartao.PedidoStatus`](#globaltecuauvendasdtoscartaopedidostatus) |  |  |
| `Pessoa` | [`Globaltec.UAU.Vendas.DTOs.Cartao.Pessoa`](#globaltecuauvendasdtoscartaopessoa) |  |  |
| `Produtos` | array de [`Globaltec.UAU.Vendas.DTOs.Cartao.Produtos`](#globaltecuauvendasdtoscartaoprodutos) |  |  |
| `NotaFiscal` | string |  |  |
| `IntencoesVenda` | array de [`Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoVendaPedido`](#globaltecuauvendasdtoscartaointencaovendapedido) |  |  |
| `PedidoFormasPagamento` | array de [`Globaltec.UAU.Vendas.DTOs.Cartao.PedidoFormasPagamento`](#globaltecuauvendasdtoscartaopedidoformaspagamento) |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.PedidoFormasPagamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `FormaPagamento` | [`Globaltec.UAU.Vendas.DTOs.Cartao.FormaPagamentoPedido`](#globaltecuauvendasdtoscartaoformapagamentopedido) |  |  |
| `QuantidadeMaximaParcelas` | integer (int32) |  |  |
| `Adquirente` | string |  |  |
| `quantidadeFixaParcelas` | integer (int32) |  |  |
| `tipoFinanciamento` | integer (int32) |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.FormaPagamentoPedido

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | string |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoVendaPedido

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Token` | string |  |  |
| `Data` | string |  |  |
| `Hora` | string |  |  |
| `Quantidade` | integer (int32) |  |  |
| `ValorOriginal` | number (double) |  |  |
| `ValorOriginalFormat` | string |  |  |
| `ValorAcrescimo` | number (double) |  |  |
| `ValorAcrescimoFormat` | string |  |  |
| `ValorDesconto` | number (double) |  |  |
| `ValorDescontoFormat` | string |  |  |
| `ValorFinal` | number (double) |  |  |
| `ValorFinalFormat` | string |  |  |
| `Gate2allToken` | string |  |  |
| `QuantidadeParcelas` | integer (int32) |  |  |
| `UrlPagamento` | string |  |  |
| `FormaPagamento` | [`Globaltec.UAU.Vendas.DTOs.Cartao.FormaPagamento`](#globaltecuauvendasdtoscartaoformapagamento) |  |  |
| `IntencaoVendaStatus` | [`Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoVendaStatus`](#globaltecuauvendasdtoscartaointencaovendastatus) |  |  |
| `Pedido` | [`Globaltec.UAU.Vendas.DTOs.Cartao.PedidoIntencaoVenda`](#globaltecuauvendasdtoscartaopedidointencaovenda) |  |  |
| `Cliente` | string |  |  |
| `Produtos` | array de [`Globaltec.UAU.Vendas.DTOs.Cartao.Produtos`](#globaltecuauvendasdtoscartaoprodutos) |  |  |
| `PagamentosExternos` | array de [`Globaltec.UAU.Vendas.DTOs.Cartao.PagamentoExternoPedido`](#globaltecuauvendasdtoscartaopagamentoexternopedido) |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.PagamentoExternoPedido

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Tipo` | integer (int32) |  |  |
| `DataAdquirente` | string |  |  |
| `DataAtualizacao` | string |  |  |
| `Origem` | integer (int32) |  |  |
| `TipoParcelamento` | string |  |  |
| `ComprovanteAdquirente` | string |  |  |
| `CodigoRespostaExecTransac` | string |  |  |
| `CodigoRespostaAdquirente` | string |  |  |
| `PagamentoExternoStatus` | [`Globaltec.UAU.Vendas.DTOs.Cartao.PagamentoExternoStatus`](#globaltecuauvendasdtoscartaopagamentoexternostatus) |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.PagamentoExternoStatus

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Nome` | string |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.PedidoIntencaoVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Referencia` | string |  |  |
| `PedidoStatus` | [`Globaltec.UAU.Vendas.DTOs.Cartao.PedidoStatus`](#globaltecuauvendasdtoscartaopedidostatus) |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.IntencaoVendaStatus

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Nome` | string |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.FormaPagamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | string |  |  |
| `Nome` | string |  |  |
| `Modalidade` | string |  |  |
| `FluxoPagamento` | [`Globaltec.UAU.Vendas.DTOs.Cartao.FluxoPagamento`](#globaltecuauvendasdtoscartaofluxopagamento) |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.FluxoPagamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Nome` | string |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.Produtos

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ItemProdutoId` | integer (int32) |  |  |
| `Id` | integer (int32) |  |  |
| `Nome` | string |  |  |
| `Descricao` | string |  |  |
| `NomeExibe` | string |  |  |
| `Quantidade` | integer (int32) |  |  |
| `Valor` | string |  |  |
| `ValorFormat` | string |  |  |
| `FotoThumbnail` | string |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.Pessoa

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `NomeRazaoSocial` | string |  |  |
| `SobrenomeNomeFantasia` | string |  |  |
| `CpfCnpjFormat` | string |  |  |
| `Email` | string |  |  |

### Globaltec.UAU.Vendas.DTOs.Cartao.PedidoStatus

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Nome` | string |  |  |

### UAUApi.Models.Venda.PedidoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empesa |
| `Obra` | string | ✓ | Código da obra |
| `Pedido` | integer (int32) | ✓ | Número do pedido da NTK |

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |

### UAUApi.Models.Venda.AprovDesaprovReneg

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codEmpresa` | integer (int32) | ✓ | Código da empresa |
| `codObra` | string | ✓ | Código da obra |
| `numVenda` | integer (int32) | ✓ | Código da venda |
| `aprovDesaprov` | boolean | ✓ | Aprovar ou desaprovar |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Venda.AlterarDataProrrogacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dados_prorrogacao` | [`UAUApi.Models.Venda.DadosProrrogacao`](#uauapimodelsvendadadosprorrogacao) | ✓ | Dados da prorrogação |

### UAUApi.Models.Venda.DadosProrrogacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `Venda` | integer (int32) | ✓ | Código da venda |
| `TipoParcela` | string | ✓ | Tipo da parcela |
| `Parcela` | integer (int32) | ✓ | Número da parcela |
| `ParcelaGeral` | integer (int32) | ✓ | Número geral da parcela |
| `DataAntiga` | string (date-time) | ✓ | Data de prorrogação original |
| `DataNova` | string (date-time) | ✓ | Nova data da prorrogação |
| `Usuario` | string | ✓ | Usuário da solicitação |
| `UsarDataUtil` | integer (int32) | ✓ | Considerar apenas datas úteis 0 - Não 1 - Sim |

### Globaltec.UAU.Repositorio.StatusCobranca

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `StringFormat` | string |  |  |
| `QuantidadeRegistros` | integer (int32) |  |  |
| `Codigo_stc` | integer (int32) |  |  |
| `Desc_stc` | string |  |  |
| `Anexos_stc` | integer (int32) |  |  |
| `Status_stc` | boolean |  |  |
| `DataCad_stc` | string (date-time) |  |  |
| `UsrCad_stc` | string |  |  |
| `s_Codigo_stc` | string |  |  |
| `s_Desc_stc` | string |  |  |
| `s_Anexos_stc` | string |  |  |
| `s_Status_stc` | string |  |  |
| `s_DataCad_stc` | string |  |  |
| `s_UsrCad_stc` | string |  |  |
| `Where` | [`Globaltec.UAU.Repositorio._StatusCobranca.WhereClause`](#globaltecuaurepositorio_statuscobrancawhereclause) |  |  |
| `Aggregate` | [`Globaltec.UAU.Repositorio._StatusCobranca.AggregateClause`](#globaltecuaurepositorio_statuscobrancaaggregateclause) |  |  |
| `Joins` | object |  |  |
| `QuerySource` | string |  |  |
| `MappingName` | string |  |  |
| `SchemaGlobal` | string |  |  |
| `SchemaTableView` | string |  |  |
| `SchemaStoredProcedure` | string |  |  |
| `NotRecommendedConnection` | [`UAUADODB.Connection`](#uauadodbconnection) |  |  |
| `ConnectionString` | string |  |  |
| `ConnectionStringConfig` | string |  |  |
| `Filter` | string |  |  |
| `Sort` | string |  |  |
| `RowCount` | integer (int32) |  |  |
| `DefaultView` | [`Globaltec.UAU.DAL.UAUrecordset`](#globaltecuaudaluaurecordset) |  |  |
| `UAURecordset` | [`Globaltec.UAU.DAL.UAUrecordset`](#globaltecuaudaluaurecordset) |  |  |
| `Query` | [`Globaltec.UAU.DAL.DynamicQuery`](#globaltecuaudaldynamicquery) |  |  |
| `GetTablePrimaryKeyFields` | array de string |  |  |

### Globaltec.UAU.DAL.DynamicQuery

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `LastQuery` | string |  |  |
| `Top` | integer (int32) |  |  |
| `Distinct` | boolean |  |  |
| `CountAll` | boolean |  |  |
| `CountAllAlias` | string |  |  |
| `WithRollup` | boolean |  |  |
| `ParameterCount` | integer (int32) |  |  |
| `AggregateCount` | integer (int32) |  |  |
| `Joins` | object |  |  |

### Globaltec.UAU.DAL.UAUrecordset

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `MyCommand` | [`UAUADODB.Command`](#uauadodbcommand) |  |  |
| `Properties` | array de object |  |  |
| `AbsolutePosition` | integer (int32) — valores possíveis: -3, -2, -1 |  |  |
| `ActiveConnection` | object |  |  |
| `BOF` | boolean |  |  |
| `Bookmark` | object |  |  |
| `CacheSize` | integer (int32) |  |  |
| `CursorType` | integer (int32) — valores possíveis: 0, 1, 2, 3, -1 |  |  |
| `EOF` | boolean |  |  |
| `Fields` | array de object |  |  |
| `LockType` | integer (int32) — valores possíveis: 1, 2, 3, 4, -1 |  |  |
| `MaxRecords` | integer (int32) |  |  |
| `RecordCount` | integer (int32) |  |  |
| `Source` | object |  |  |
| `AbsolutePage` | integer (int32) — valores possíveis: -3, -2, -1 |  |  |
| `EditMode` | integer (int32) — valores possíveis: 0, 1, 2, 4 |  |  |
| `Filter` | object |  |  |
| `PageCount` | integer (int32) |  |  |
| `PageSize` | integer (int32) |  |  |
| `Sort` | string |  |  |
| `Status` | integer (int32) |  |  |
| `State` | integer (int32) |  |  |
| `CursorLocation` | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `MarshalOptions` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `DataSource` | object |  |  |
| `ActiveCommand` | object |  |  |
| `StayInSync` | boolean |  |  |
| `DataMember` | string |  |  |
| `Index` | string |  |  |

### UAUADODB.Command

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Properties` | array de object |  |  |
| `ActiveConnection` | [`UAUADODB.Connection`](#uauadodbconnection) |  |  |
| `CommandText` | string |  |  |
| `CommandTimeout` | integer (int32) |  |  |
| `Prepared` | boolean |  |  |
| `Parameters` | array de object |  |  |
| `CommandType` | integer (int32) — valores possíveis: 1, 2, 4, 8, 256, 512, -1 |  |  |
| `Name` | string |  |  |
| `State` | integer (int32) |  |  |
| `CommandStream` | object |  |  |
| `Dialect` | string |  |  |
| `NamedParameters` | boolean |  |  |

### UAUADODB.Connection

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Properties` | array de object |  |  |
| `ConnectionString` | string |  |  |
| `CommandTimeout` | integer (int32) |  |  |
| `ConnectionTimeout` | integer (int32) |  |  |
| `Version` | string |  |  |
| `Errors` | array de object |  |  |
| `DefaultDatabase` | string |  |  |
| `IsolationLevel` | integer (int32) — valores possíveis: 16, 256, 256, 4096, 4096, 65536, 1048576, 1048576, -1 |  |  |
| `Attributes` | integer (int32) |  |  |
| `CursorLocation` | integer (int32) — valores possíveis: 1, 2, 3, 3 |  |  |
| `Mode` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 8, 12, 16, 4194304 |  |  |
| `Provider` | string |  |  |
| `State` | integer (int32) |  |  |

### Globaltec.UAU.Repositorio._StatusCobranca.AggregateClause

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `TearOff` | [`Globaltec.UAU.Repositorio._StatusCobranca.AggregateClause.TearOffAggregateParameter`](#globaltecuaurepositorio_statuscobrancaaggregateclausetearoffaggregateparameter) |  |  |
| `Codigo_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `Desc_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `Anexos_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `Status_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `DataCad_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `UsrCad_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |

### Globaltec.UAU.DAL.AggregateParameter

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `IsDirty` | boolean |  |  |
| `Column` | string |  |  |
| `Param` | [`UAUADODB.Parameter`](#uauadodbparameter) |  |  |
| `Value` | object |  |  |
| `Function` | integer (int32) — valores possíveis: 1, 2, 3, 4, 5, 6, 7 |  |  |
| `Alias` | string |  |  |
| `Distinct` | boolean |  |  |

### UAUADODB.Parameter

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Properties` | array de object |  |  |
| `Name` | string |  |  |
| `Value` | object |  |  |
| `Type` | integer (int32) — valores possíveis: 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 64, 72, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138, 139, 200, 201, 202, 203, 204, 205, 8192 |  |  |
| `Direction` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4 |  |  |
| `Precision` | integer (int32) |  |  |
| `NumericScale` | integer (int32) |  |  |
| `Size` | integer (int32) |  |  |
| `Attributes` | integer (int32) |  |  |

### Globaltec.UAU.Repositorio._StatusCobranca.AggregateClause.TearOffAggregateParameter

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `Desc_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `Anexos_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `Status_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `DataCad_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |
| `UsrCad_stc` | [`Globaltec.UAU.DAL.AggregateParameter`](#globaltecuaudalaggregateparameter) |  |  |

### Globaltec.UAU.Repositorio._StatusCobranca.WhereClause

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `TearOff` | [`Globaltec.UAU.Repositorio._StatusCobranca.WhereClause.TearOffWhereParameter`](#globaltecuaurepositorio_statuscobrancawhereclausetearoffwhereparameter) |  |  |
| `Codigo_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `Desc_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `Anexos_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `Status_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `DataCad_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `UsrCad_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |

### Globaltec.UAU.DAL.WhereParameter

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `IsDirty` | boolean |  |  |
| `Column` | string |  |  |
| `Param` | [`UAUADODB.Parameter`](#uauadodbparameter) |  |  |
| `Value` | object |  |  |
| `Operator` | integer (int32) — valores possíveis: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 |  |  |
| `Conjuction` | integer (int32) — valores possíveis: 1, 2, 3 |  |  |
| `BetweenBeginValue` | object |  |  |
| `BetweenEndValue` | object |  |  |
| `UseParameter` | boolean |  |  |

### Globaltec.UAU.Repositorio._StatusCobranca.WhereClause.TearOffWhereParameter

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `Desc_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `Anexos_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `Status_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `DataCad_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
| `UsrCad_stc` | [`Globaltec.UAU.DAL.WhereParameter`](#globaltecuaudalwhereparameter) |  |  |
