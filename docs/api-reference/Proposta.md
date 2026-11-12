# Proposta

## POST `/api/Proposta/TraduzirRequestParcelasGeradas`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `proposta` | query | integer (int32) | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: array de [`UAUApi.Models.Proposta.ParcelaRenegociacaoRequest`](#uauapimodelspropostaparcelarenegociacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | array de [`Globaltec.UAU.Comp.PropostaParcelasGeradas`](#globaltecuaucomppropostaparcelasgeradas) |

---

## POST `/api/Proposta/TraduzirRequestParcelasSelecionadas`

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `numProposta` | query | integer (int32) | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: array de [`UAUApi.Models.Proposta.ParcelaSelRenegociacaoRequest`](#uauapimodelspropostaparcelaselrenegociacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | array de string |

---

## POST `/api/v{version}/Proposta/AtualizarPedidoDeRecebimento`

**Atualizar o(s) pedido(s) de recebimento  junto a NTK**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
1. Serão atualizadas as parcelas do pedido que ainda estão com status: 0 - Em aberto 
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

## POST `/api/v{version}/Proposta/CancelarPedidoDeRecebimento`

**Cancelar o pedido de recebimento junto a NTK**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

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

## POST `/api/v{version}/Proposta/CancelarProposta`

**Cancelar determinada proposta**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. É obrigatório informar o código da proposta.
2. Caso ela esteja vendida, deve informar se é para cancela-la ou não.
3. A proposta não pode estar cancelada ou expirada
4. Ao enviar ExcluirBoletos como TRUE, irá excluir os boletos ativos da proposta e permitir o cancelamento.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.CancelarPropostaRequest`](#uauapimodelspropostacancelarpropostarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/ConsultarHierarquiaParcelas`

**Consulta parcelas a desconsiderar que estão vinculadas a hierarquia informada**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.ParcelasHierarquiaRequest`](#uauapimodelspropostaparcelashierarquiarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.ComissaoHierarquia.HierarquiaParcelaDTO`](#uauapimodelscomissaohierarquiahierarquiaparceladto) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/ConsultarPedidoDeRecebimento`

**Consultar o pedido de recebimento  junto a NTK**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
1. Possibilita consultar pedido de recebimento junto a NTK
2. As informações retornadas serão informações do pedido na NTK.

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

## POST `/api/v{version}/Proposta/ConsultarPedidoDeRecebimentoUAU`

**Consultar o pedido de recebimento no UAU.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
1. Possibilita consultar pedido de recebimento regisrado no UAU por número do pedido junto a NTK ou pelo número do pedido no UAU.
2. As informações retornadas são referentes a como o UAU registrou o pedido internamente.

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

## POST `/api/v{version}/Proposta/ConsultarPropostaPorId`

**Consulta dados da proposta por ID**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
 Definição de Negócio:
 1. Busca determinada proposta filtrando por ID.
 2. Valida usuário e suas permissões.
 3. O campo valorAntecipado e dataCalculo são opcionais, mas caso informado algum deles, precisa informar valor nos dois campos.
     - valorAntecipado deve ser preenchido com 0 para falso ou 1 para verdadeiro.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.ConsultarDadosPropostaVendaRequest`](#uauapimodelspropostaconsultardadospropostavendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar proposta de venda. | [`UAUApi.Models.Proposta.GravarPropostaRequest`](#uauapimodelspropostagravarpropostarequest) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/ExpirarBoletos`

**Excluir boletos expirados de proposta e venda**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Exclui todos os boletos expirados, propostas e vendas, de acordo com a configuração da empresa.

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
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/GerarBoleto`

**Gerar boleto**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 3. Retorna string do tipo Base64. Para obter o boleto utilize um conversor: Base64 para PDF.
 
 Definição de Negócio:
 1. Gera boleto com os dados informados na request.
 2. O usuário autenticado deve ter permissão de inclusão no programa de permissão VEBOLETOAVULSO.
 3. Para gerar boleto parcial é necessário informar a propriedade ValorBoleto.
     - Não pode ser um valor negativo nem inferior a 0,01 centavo.
     - Se informar um valor igual ao valor total das parcelas enviadas, será gerado um boleto normal.
     - Se informar um valor menor que o valor total da parcela enviada, será gerado um boleto parcial.
         - Apenas uma parcela das enviadas deverá ser parcial
         - Não será gerado boleto caso informe um valor que não cubra todas as parcelas enviadas
         - Irá validar se as parcelas enviadas podem gerar o boleto parcial de acordo com a regra de dias para vencimento.
     - Será possível gerar boleto parcial somente para parcelas de uma única empresa, obra e proposta.
     - Só é possível gerar boleto parcial para mais de uma parcela quando for antecipação.
     - É obrigatório reajustar ao gerar o boleto parcial.
 4. Padrão de cobrança    
     - Não é obrigatório informá-lo.
     - Caso informado, o sistema irá desconsiderar a configuração do parâmetro usarpadraoboleto_avulso e irá gerar o boleto pelo padrão informado.
     - Caso informado, será desconsiderado o padrão de cobrança de todas as parcelas, incluindo custas administrativas, e boleto será gerado com o padrão de cobrança informado.
     - Apenas os padrões de cobrança ativos serão aceitos.
     - Será possivel gerar boleto com o padrão de informado somente para parcelas de uma única empresa.
 5. Excluir Boletos Existentes
     - Não é obrigatório informar o parâmetro ExcluirBoletosExistentes.
     - Caso não seja informado será mantido a opção padrão de não excluir.
     - Caso informado, irá executar as mesmas ações que a configuração 'Excluir boletos já emitidos ao gerar um novo boleto para a parcela' no cadastro de empresas &gt; config. vendas.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.GerarBoletoRequest`](#uauapimodelspropostagerarboletorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Proposta.BoletoProposta`](#uauapimodelspropostaboletoproposta) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/GravarPedidoDeRecebimento`

**Gravar pedido de recebimento  junto a NTK**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. É obrigatório ter o ambiente de integração com a NTK configurado, só após o registro junto a eles que o registro será gerado no UAU.
2. É necessário ter permissão de inclusão no programa VEPEDIDORECEBIMENTO
3. Não é possível gerar pedido para receber todas as parcelas de uma proposta, o sistema irá validar juntamente com boletos gerados.
4. Somente propostas com status 2 - confirmadas podem gerar pedido de recebimento.
5. É necessário que o prospect esteja migrado para geração do pedido.

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

## POST `/api/v{version}/Proposta/GravarProposta`

**Grava os dados da proposta de venda**

Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
 Definição de Negócio:
 1. O usuário autenticado deve ter permissão de inclusão e alteração em CRPROPOSTAVENDA.
     - Se não precisar de alterar propostas, basta ter apenas de inclusão.
 2. A alteração de uma proposta é feita respeitando todas informações enviadas, ou seja, deve reeniviar o mesmo objeto da proposta totalmente para alterar apenas 1 campo por exemplo.
     - O sistema identifica que é uma alteração de proposta quando o código da proposta está preenchido [numProposta].
 3. A propriedade de propostaPacelasGeradas, Não precisa ser preenchida pois suas informações serão regeradas pela API.
 4. As validações de propriedades obrigatórias podem validar para o tipo de proposta que está sendo recebido.
     - Os campos marcados como obrigatórios são os campos obrigatórios gerais, para gravar o básico de uma proposta de venda.
         - Aluguel, aluguel garantido e aluguel shopping, tem mais propriedades obrigatórias ou até mesmo opcionais.
 6. Mais informações sobre as propriedades e como elas devem ser preenchidas estão na documentação dos models.
 7. Tornou-se obsoleto ó código da hierarquia, agora pelo numeroComissao(modelo) nos iremos achar a hierarquia e validar.
 8. O cálculo da comissão é feito da seguinte forma.
 9. Ao informar a propriedade percentualSegundoJuros ou a propriedade dataSegundoJuros, ambas serão obrigatórias em propostaParamParcelas e propostaParamModeloParcelas.
 10. O parâmetro opcional TermoReserva, quando preenchido, precisa ter o valor 0 ou 1. (0-Não, 1-Sim).
 11. Os parâmetros opcionais ValorCurtoPrazo e ValorLongoPrazo, se não preenchidos, serão calculados automaticamente.
     - O valor de provisão de venda curto prazo será a soma das parcelas que irão vencer em ate 12 meses após a data da venda;
     - O valor de provisão de venda longo prazo será a soma das parcelas que irão vencer após 12 meses após a data da venda.
 Obs: Arredondar o valor calculado para duas casas decimais.
 
     Propriedade propostaItens : Valor geral de comissão.
         - Valor da comissão = (Preço do produto x quantidade x Porcentual da comissão) / 100.
             - 81831,038 = (492.37 x 2936.17 x 5.660376) / 100.
             - Após o cálculo o valor da comissão é arredondado considerando duas casas decimais depois da virgula. Valor da comissão = 81831.04.
             - O Preço do produto, quantidade e Porcentual da comissão são referentes aos seguintes campos respectivamente 'precoProduto', 'qtdeProduto' e 'porcentualComissao'.
             - Dados referente ao objeto 'propostaItens'.
     Propriedade propostaComissao : Valor da comissão.             
         - Valor da comissão = (Valor da comissão x Porcentual da comissão)/100.
             - 27822,5536  = (81831.04 x 34.000000) / 100.
             - O Valor da comissão e Porcentual da comissão são referentes aos seguintes campos respectivamente 'valorComissao' e 'PorcComissao'.
             - Dados referente ao objeto 'propostaComissao'.
         - O resultado do cálculo da comissão é referente ao campo 'valorComissao' e também é o valor que deve ser informado.
 
 Planilha com exemplo do cálculo do valor total e comissão:
 https://drive.google.com/file/d/14IW7aoBkT91FFOJBB5LVth-eerIxnqLP/view
 
 Anexos:
 Exemplo do body json: 
 https://ajuda.globaltec.com.br/wp-content/uploads/2019/12/exemploGravarProposta.txt

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.GravarPropostaRequest`](#uauapimodelspropostagravarpropostarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/ProcessarRecebimentoParcelas`

**Processa o recebimento de parcelas referentes a propostas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Processa as parcelas recebidas
2. O valor do desconto aplicado ao recebimento será sempre do objeto de recebimento, o valor do desconto da parcela será aplicado somente pela tela de recebimento avulso.
3. Não é possível realizar recebimento para todas as parcelas da proposta! Ao realizar o recebimento de parcelas o sistema verifica se possui boleto gerado e pedido de recebimento para outra parcelas da proposta.

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
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique a mensagem de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/RenegociarProposta`

**Realiza a renegociação de parcelas de uma proposta de venda com as validações necessárias**

Definição Técnica:

1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite renegociar parcelas de uma proposta
1. O usuário deverá estar autenticado e validado.
2. Informar os dados da proposta.
3. Informar as parcelas a serem geradas.
4. Informar as parcelas escolhidas para renegociação.
6. Será realizada validação referente as informações preenchidas que irão permitir a renegociação, caso não esteja de acordo
   retorna mensagem informando a inconsistência encontrada para que seja analisada.
7. Após as validações realiza a renegociação das parcelas.
8. Será registrado comentário na proposta sobre a renegociação realizada.
9. O parâmetro opcional TermoReserva, quando preenchido, precisa ter o valor 0 ou 1. (0-Não, 1-Sim).
10. Os parâmetros opcionais ValorCurtoPrazo e valorLongoPrazo, se não preenchidos, serão calculados automaticamente.
    - O valor de provisão de venda curto prazo será a soma das parcelas que irão vencer em ate 12 meses após a data da venda;
    - O valor de provisão de venda longo prazo será a soma das parcelas que irão vencer após 12 meses após a data da venda.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.RenegociarPropostaRequest`](#uauapimodelspropostarenegociarpropostarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/RetornaValorComissaoDeducaoParcelas`

**Retorna o valor da comissão deduzido**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Calcula o valor da comissão deduzido.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.ComissaoParcelasRequest`](#uauapimodelspropostacomissaoparcelasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/RetornarValoresEstruturaComissao`

**Retorna a comissão calculada**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Realiza cálculos da comissão e retorna os valores
2. Parâmetros:
    - Grupo de parcelas
    - Estrutura de comissão

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.RetornaComissaoRequest`](#uauapimodelspropostaretornacomissaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.IntegranteEstruturaComissao`](#uauapimodelsintegranteestruturacomissao) |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Proposta/VincularArquivoProposta`

**Vincular arquivo a proposta**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Realiza a vinculadção de arquivo com determinada proposta.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Proposta.VincularArquivoPropostaRequest`](#uauapimodelspropostavinculararquivopropostarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 401 | Usuário não está logado! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Proposta.VincularArquivoPropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `arquivo` | string (byte) | ✓ | Arquivo em bytes |
| `nome_arquivo` | string |  | Nome do arquivo |
| `proposta` | integer (int32) | ✓ | Número da proposta |
| `usuario` | string |  | Usuário que vai anexar o arquivo |

### UAUApi.Models.IntegranteEstruturaComissao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoPessoa` | number (double) |  | Código Pessoa |
| `NomePessoa` | string |  | Nome Pessoa |
| `DescricaoCargo` | string |  | Descrição do Cargo Pessoa |
| `PercentualComissao` | number (double) |  | % de comissão para o nível da hierarquia |
| `ValorComissao` | number (double) |  | Valor da Comissão |
| `TipoPagamento` | integer (int32) |  | O tipo de comissão (0 - Direto, 1 - Indireto) |
| `TipoLancamento` | integer (int32) |  | Tipo Lançamento (0 - Comissão, 1 - Bonificação) |
| `CodigoCargo` | string |  | Código do cargo |
| `Recebimento` | integer (int32) |  | Se o pagamento das comissões serão feitas sobre o recebimento da venda (1 - Sim, 0 - Não) ** Obsoleto ** |
| `RegraLiberacao` | integer (int32) |  | Identifica se há regra de liberação para o pagamento dessa comissão. |
| `ProcessaPagamento` | integer (int32) |  | Gerar Processo (1 - Sim, 0 - Não) |
| `Estrutura` | integer (int32) |  | Se a comissão pertence a Estrutura (1 - Sim, 0 - Não) |
| `Captador` | integer (int32) |  | Indica o Captador (0 - Não, 1 - Sim) |
| `GerarComissao` | integer (int32) |  | Gerar Comissão (0 - Não, 1 - Sim) |

### UAUApi.Models.Proposta.RetornaComissaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) | ✓ | Código da Empresa |
| `codigoObra` | string | ✓ | Código da Obra |
| `codigoVendedor` | integer (int32) | ✓ | Código do Vendedor |
| `codigoHierarquia` | integer (int32) | ✓ | Código da Hierarquia - Estrutura de Comissão |
| `codigoComissao` | integer (int32) | ✓ | Código da comissão do modelo da comissão. |
| `valorTotalComissao` | number (double) |  | Valor Total da Comissão |
| `valorComissaoDireta` | number (double) |  | Valor Total da Comissão Direta |
| `valorCurtoPrazoProposta` | number (double) |  | Valor curto prazo |
| `valorLongoPrazoProposta` | number (double) |  | Valor de longo prazo |
| `produtos` | array de [`UAUApi.Models.Proposta.itensProposta`](#uauapimodelspropostaitensproposta) |  | Produtos da proposta |
| `parcelas` | array de [`UAUApi.Models.Proposta.ParcelaGeradasDeducao`](#uauapimodelspropostaparcelageradasdeducao) | ✓ | Parcelas do Grupo |

### UAUApi.Models.Proposta.ParcelaGeradasDeducao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroParcela` | integer (int32) | ✓ | Número da Parcela |
| `valorParcela` | number (double) | ✓ | Valor total deste grupo de parcelas |
| `tipoParcela` | string | ✓ | Tipo de Parcela |
| `quantidadeParcela` | integer (int32) | ✓ | Quantidade deste tipo de Parcela no Grupo |
| `grupoParcela` | integer (int32) | ✓ | Numero do Grupo da Parcela |
| `tipoValor` | integer (int32) | ✓ | Tipo do valor da Parcela 0 - Percentual, 1 - Valor |

### UAUApi.Models.Proposta.itensProposta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codEmpresa` | integer (int32) | ✓ | código da empresa |
| `codProduto` | integer (int32) | ✓ | código do produto |
| `NumPersonalizacao` | integer (int32) | ✓ | número da personalização |
| `precoProduto` | number (double) | ✓ | preço do produto |
| `qtdeProduto` | number (double) | ✓ | quantidade do Produto |
| `Contrato` | integer (int32) | ✓ | Contrato do produto (do planejamento do mesmo) |
| `itemProduto` | string | ✓ | item do produto (Do planejamento do mesmo) |
| `valComissaoDireta` | number (double) |  | valor da comissão pago diretamente |
| `porcentualComissao` | number (double) |  | porcentagem de Comissão no Produto |

### UAUApi.Models.Proposta.ComissaoParcelasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoHierarquia` | integer (int32) | ✓ | Código da hierarquia. |
| `CodigoModeloVenda` | integer (int32) | ✓ | Código do modelo da venda. |
| `ValorTotalProduto` | number (double) | ✓ | Valor total do produto. |
| `ValorTotalComissao` | number (double) | ✓ | Valor total da comissão. |
| `ValorTotalComissaoDireta` | number (double) | ✓ | Valor total da comissão direta. |
| `ParcelasGeradas` | array de [`UAUApi.Models.ComissaoHierarquia.ParcelaGerada`](#uauapimodelscomissaohierarquiaparcelagerada) | ✓ | Parcelas geradas. |
| `PorcentagemComissao` | number (double) | ✓ | Porcentagem da comissão. |
| `ValorItemProposta` | number (double) | ✓ | Valor do item da proposta. |

### UAUApi.Models.ComissaoHierarquia.ParcelaGerada

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroParcela` | integer (int32) |  |  |
| `Valor` | number (double) |  |  |
| `TipoParcela` | string |  |  |
| `QuantidadeParcela` | integer (int32) |  |  |
| `GrupoParcela` | integer (int32) |  |  |
| `TipoValor` | integer (int32) |  |  |
| `Porcentagem` | number (double) |  |  |

### UAUApi.Models.Proposta.RenegociarPropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumProposta` | integer (int64) | ✓ | Número da proposta |
| `PropostaParcelasGeradas` | array de [`UAUApi.Models.Proposta.ParcelaRenegociacaoRequest`](#uauapimodelspropostaparcelarenegociacaorequest) | ✓ | Novas parcelas geradas após realizar a renegociação |
| `ParcelasSelecionadas` | array de [`UAUApi.Models.Proposta.ParcelaSelRenegociacaoRequest`](#uauapimodelspropostaparcelaselrenegociacaorequest) | ✓ | Tabela com as parcelas originais, selecionadas para serem renegociadas (somente chave) |
| `ValorDesconto` | number (double) |  | Valor de desconto utilizado na renegociação |
| `ValorAcrescimo` | number (double) |  | Valor de acréscimo utilizado na renegociação |
| `valorCurtoPrazo` | number (double) |  | Valor curto prazo |
| `valorLongoPrazo` | number (double) |  | Valor longo prazo |
| `NumPadraoCobranca` | integer (int32) |  | Número do padrão de cobrança as ser usado nas novas parcelas geradas após renegociação |
| `TermoReserva` | integer (int32) |  | Define se a proposta é de termo reserva ou não (0 - Não, 1 - Sim) |

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

### UAUApi.Models.Proposta.BoletoProposta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `boletoPDF` | string |  | Stringbase64 do boleto em PDF. |

### UAUApi.Models.Proposta.GerarBoletoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `parcelas` | array de [`UAUApi.Models.Proposta.ParcelasBoleto`](#uauapimodelspropostaparcelasboleto) | ✓ | lista de objeto com as parcelas da proposta que serão geradas o boleto / carne e valor do desconto se existir |
| `datacalculo` | string (date-time) | ✓ | Data para o calculo e vencimento do boleto |
| `antecipar` | boolean |  | Se o cálculo das parcelas será antecipado TRUE - Sim FALSE - Não |
| `reajustar` | boolean |  | Se é para reajustar os valores TRUE - Sim FALSE - Não |
| `excluirboletoexpirado` | boolean |  | Se é para excluir os boletos expirados TRUE - Sim FALSE - Não |
| `formacobranca` | integer (int32) — valores possíveis: 0, 1 |  | Tipo de geração: 0 - Boleto, 1 - Carnê |
| `boletosacadodetalhado` | boolean |  | Se o boleto sacado será detalhado  TRUE - Sim FALSE - Não |
| `carnetresvias` | boolean |  | Se o carne será em três vias TRUE - Sim FALSE - Não |
| `validardadospendentes` | boolean |  | Se não deve validar os dados pendentes de preenchimento do endereço do cliente.  False - Não irá travar a geração do boleto, caso os dados do endereço do cliente estejam incompletos. True - Irá travar a geração do boleto, caso os dados do endereço do cliente estejam incompletos. |
| `acrescentarresiduo` | boolean |  | Se vai acrescentar o valor de resíduo ou não TRUE - Sim FALSE - Não |
| `usarpadraoboletoavulso` | boolean |  | Indica qual o padrão de cobrança será utilizado     TRUE - Sim FALSE - Não |
| `agruparparcelas` | boolean |  | Se deve agrupar as parcelas enviadas para gerar o boleto TRUE - Sim FALSE - Não |
| `ValorBoleto` | number (double) |  | Valor do boleto, utilizado para geração de boletos parciais. |
| `PadraoCobranca` | integer (int32) |  | Nr. do padrão para cobrança |
| `ExcluirBoletosExistentes` | boolean |  | Se irá excluir boletos já emitidos ao gerar um novo boleto para a parcela |

### UAUApi.Models.Proposta.ParcelasBoleto

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |
| `numproposta` | integer (int32) | ✓ | Número da proposta |
| `numparcela` | integer (int32) | ✓ | Número da parcela |
| `tipoparcela` | string | ✓ | Tipo parcela |
| `numparcelagerada` | integer (int32) | ✓ | Número geral da parcela. |
| `valordescontoantecipacao` | number (double) |  | Valor do desconto por antecipação |

### UAUApi.Models.Proposta.GravarPropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `proposta` | [`UAUApi.Models.Proposta.Proposta`](#uauapimodelspropostaproposta) | ✓ | Contém todas informações da proposta |
| `propostaPacelasGeradas` | array de [`UAUApi.Models.ModeloVenda.PropostaParcelasGeradas`](#uauapimodelsmodelovendapropostaparcelasgeradas) |  | Deve conter as parcelas que foram geradas pela proposta.  Ao gravar ou alterar uma proposta o sistema sempre vai gerar essas parcelas novamente, logo elas são descartadas. |
| `propostaParamModeloParcelas` | array de [`UAUApi.Models.ModeloVenda.PropostaParamModeloVenda`](#uauapimodelsmodelovendapropostaparammodelovenda) | ✓ | Deve conter os parametros de modelo dos grupos de parcela da proposta |
| `propostaParamParcelas` | array de [`UAUApi.Models.Proposta.propostaParametroParcelas`](#uauapimodelspropostapropostaparametroparcelas) | ✓ | Deve conter os parametros dos grupos de parcela da proposta |
| `propostaComissao` | array de [`UAUApi.Models.Proposta.comissaoProposta`](#uauapimodelspropostacomissaoproposta) |  | Deve conter as comissões que serão pagas na proposta, caso tenha. |
| `propostaComissaoParc` | array de [`UAUApi.Models.Proposta.ComissaoParcelamento`](#uauapimodelspropostacomissaoparcelamento) |  | Deve conter o parcelamento da comissão, caso tenha comissão. |
| `propostaItens` | array de [`UAUApi.Models.Proposta.itensProposta`](#uauapimodelspropostaitensproposta) | ✓ | Deve conter 1 ou mais itens da proposta |
| `propostaCliente` | array de [`UAUApi.Models.Proposta.propostaCliente`](#uauapimodelspropostapropostacliente) | ✓ | Deve conter 1 ou mais clientes (prospects) da proposta |
| `propostaPlanoIndex` | array de [`UAUApi.Models.Proposta.propostaPlanoIndex`](#uauapimodelspropostapropostaplanoindex) |  | Deve conter os planos indexadores da proposta, caso tenha. |
| `propostaSeguro` | array de [`UAUApi.Models.Proposta.propostaSeguro`](#uauapimodelspropostapropostaseguro) |  | Deve conter 1 ou mais seguros da proposta, caso tenha. |
| `propostaCustasRetencao` | [`UAUApi.Models.Proposta.CustasRetencaoProposta`](#uauapimodelspropostacustasretencaoproposta) |  | Válida apenas para propostas de aluguel ou aluguel garantido, armazena as informações do valor de retenção do aluguel. |
| `propostaCustasRetencaoParcela` | array de [`UAUApi.Models.Proposta.PropostaCustasRetencaoParc`](#uauapimodelspropostapropostacustasretencaoparc) |  | Válida apenas para propostas de aluguel ou aluguel garantido, armazena o parcelamento das retenções. |
| `propostaCap` | array de [`UAUApi.Models.Proposta.capProposta`](#uauapimodelspropostacapproposta) |  | Armazena os CAPS padrões da proposta. |
| `propostaShopping` | [`UAUApi.Models.Proposta.shoppingProposta`](#uauapimodelspropostashoppingproposta) |  | Informações de shopping da proposta, válido apenas para propostas para aluguel shopping. |

### UAUApi.Models.Proposta.shoppingProposta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoAtividade` | string | ✓ | código de atividade |
| `tipoContrato` | integer (int32) | ✓ | tipo  contrato (0 - Normal, 1 - Execução, 2 - CTO) |
| `basePercentualAluguel` | integer (int32) | ✓ | base aluguel é percentual  (0 - Aluguel mínimo 1 - Aluguel apurado) |
| `area` | number (double) | ✓ | área do aluguel shopping |
| `frente` | number (double) | ✓ | frente do aluguel shopping |
| `profundidade` | number (double) | ✓ | profundidade do aluguel shopping |
| `numLocal` | integer (int32) | ✓ | número do localização da unidade. |
| `percententualAluguel` | number (double) | ✓ | percentual do aluguel shopping |
| `ReceitaInformada` | integer (int32) | ✓ | tipo de reiceita informada ( 0 - Bruto, 1 - Líquida) |
| `PercentualFPP` | number (double) | ✓ | base para percentual FPP |

### UAUApi.Models.Proposta.capProposta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoCap` | integer (int32) | ✓ | número do tipo de cap |
| `codigoCAP` | string | ✓ | código do cap para proposta |

### UAUApi.Models.Proposta.PropostaCustasRetencaoParc

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumParcela` | string | ✓ | número da parcela |
| `codigoCap` | string | ✓ | código do cap |
| `dataVencimento` | string (date-time) | ✓ | data de vencimento da parcela. |
| `valorRetencao` | number (double) | ✓ | valor que sera retido na parcela. |
| `cobrarTaxaAdm` | integer (int32) |  | cobrar taxa administrativa (0 - Não, 1 - Sim) |
| `CobrarCPMF` | integer (int32) |  | cobrar CPMF (0 - Não, 1 - Sim) |

### UAUApi.Models.Proposta.CustasRetencaoProposta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `valorRetencao` | number (double) | ✓ | valor retenção |

### UAUApi.Models.Proposta.propostaSeguro

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoSeguro` | integer (int32) | ✓ | tipo do seguro ( 0 - MIP (Morte e invalidez permanente do mutuário), 1 - DFI (Danos físicos ao imóvel)) |
| `porTaxa` | boolean | ✓ | se o valor do seguro é uma taxa em relação ao saldo devedor da venda ( 0 - Não, 1 - Sim) |
| `valor` | number (double) | ✓ | valor  do seguro. |
| `usuarioCadastro` | string | ✓ | login do usuário que cadastrou o seguro |
| `dataCadastro` | string (date-time) | ✓ | data de cadastro do seguro |
| `cap` | string | ✓ | cap do seguro |

### UAUApi.Models.Proposta.propostaPlanoIndex

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dataReajuste` | string (date-time) | ✓ | Data de início de reajuste |
| `numGrupoPlanoIdx` | integer (int32) | ✓ | Grupo de indexação do plano indexador |
| `codigoPlanoIndexador` | string | ✓ | Código (símbolo) do índice/moeda, de reajuste |

### UAUApi.Models.Proposta.propostaCliente

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numCliente` | integer (int32) | ✓ | número do cliente/prospect |
| `tipocliente` | integer (int32) |  | tipo de cliente (0-Titular; 1- Cliente(Titular auxiliar), 2- Avalista) |
| `porcTitular` | number (double) |  | porcentagem que o titular possui da unidades vendidas. |
| `emiteBoleto` | boolean |  | definir para qual dos titulares da proposta será emitodo o boleto de cobrança |

### UAUApi.Models.Proposta.ComissaoParcelamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumComissaoParc` | integer (int32) | ✓ | código da comissão parcelamento |
| `NumeroParcela` | integer (int32) | ✓ | número de parcela |
| `porcentagemRecebimento` | number (double) |  | porcentagem de recebimento |
| `porcentualComissao` | number (double) |  | porcentagem da comissão liberada |
| `FormaLiberacao` | integer (int32) |  | forma de liberação da parcela |
| `NumeroParcelaProposta` | integer (int32) |  | número da parcela da proposta |
| `TipoParcela` | string |  | tipo da parcela |
| `CodigoStatusescritura` | integer (int32) |  | status da escritura |

### UAUApi.Models.Proposta.comissaoProposta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numComissao` | integer (int32) | ✓ | número comissão |
| `codPessoa` | integer (int32) | ✓ | código da pessoa que receberá a comissão |
| `PorcComissao` | number (double) | ✓ | percentual de comissão |
| `valorComissao` | number (double) | ✓ | valor comissão |
| `tipoPagamento` | integer (int32) |  | tipo pagamento (0 - Direto, 1 - Indireto) |
| `tipoLancamento` | integer (int32) |  | tipo Lançamento (0 - Comissão, 1 - Bonificação) |
| `sobreRecebimento` | integer (int32) |  | sobre recebimento (1 - Sim, 0 - Não) |
| `regraLiberacao` | integer (int32) |  | sobre recebimento (1 - Sim, 0 - Não) |
| `gerarProcesso` | integer (int32) |  | gerar Processo (1 - Sim, 0 - Não) |
| `indicaCaptador` | integer (int32) |  | indica o captador (0 - Não, 1 - Sim) |
| `codigoCargo` | string |  | código do cargo |
| `parteHierarquia` | boolean |  | se a distribuição faz parte da estrutura da hierarquia  Configuração não é utilizada, em via de regra, toda comissão que possui cargo faz parte da hierarquia. |
| `gerarComissao` | boolean |  | gerar controle de comissão (0 - Não, 1 - Sim) |
| `valorAcrescimo` | number (double) |  | valor acréscimo |
| `usrAcrescimo` | string |  | usuario cadastro acréscimo |
| `dataAcrescimo` | string (date-time) |  | data cadastro acréscimo |
| `valorDesconto` | number (double) |  | valor desconto |
| `usrDesconto` | string |  | usuario cadastro desconto |
| `dataDesconto` | string (date-time) |  | data cadastro desconto |

### UAUApi.Models.Proposta.propostaParametroParcelas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumParametro` | integer (int32) | ✓ | número do prametro do modelo de venda |
| `tipoParcela` | string | ✓ | tipo de parcela |
| `numParcela` | integer (int32) | ✓ | número de parcelas |
| `valorParcela` | number (double) |  | valor parcela |
| `valorTotalParcela` | number (double) |  | valor total da parcela |
| `percentualParcela` | number (double) |  | percentual da parcela |
| `dataParcela` | string (date-time) | ✓ | data de cadastro da parcela |
| `dataJuros` | string (date-time) | ✓ | data início do juros |
| `dataReajuste` | string (date-time) | ✓ | data de inicio do reajuste |
| `juros` | number (double) |  | Porcentual juros |
| `dataSegundoJuros` | string (date-time) |  | data início segundo juros |
| `percentualSegundoJuros` | number (double) |  | percentual segundo juros |
| `frequencia` | string | ✓ | código frequencia |
| `reajuste` | string |  | índice de reajuste da parcela quando não for utilizar um plano indexador |
| `amortizacao` | integer (int32) |  | amortização da parcela: 0 - Gradiente, 1 - Price, 2 - SAC ou 3 - Simples. |
| `beginEnd` | integer (int32) |  | 0 - Begin  1 - End |
| `jurosComJuros` | integer (int32) |  | Cobrar juros caso a parcelas esteja no mesmo mês ou no mesmo dia da data de inicio do juros |
| `planoIndexParcela` | integer (int32) | ✓ | grupo de indexação do plano indexador, quando não tiver plano informar 1. |
| `tipoValor` | integer (int32) |  | tipo do valor da parcela (0 - percentual, 1 - valor) |
| `carenciaAtraso` | integer (int32) |  | cobrar carência por atraso |
| `carenciaAtrasoCorrecao` | integer (int32) |  | quantidade de dias para cobrar carência para cobrança de correção por atraso |
| `cobrarJurosProRata` | integer (int32) |  | juros pro rata |
| `cobrarJurosProRataPrimeiroMes` | integer (int32) |  | realizar o cálculo de juros no primeiro mês como pró-rata. (0 - Não,  1 - Sim") |
| `competencia` | integer (int32) |  | parcela possui competencia : 0 - Mês anterior, 1 - Mês atual ou 2 - Mês de geração. |

### UAUApi.Models.ModeloVenda.PropostaParamModeloVenda

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numParametro` | integer (int32) | ✓ | número do prametro do modelo de venda |
| `numParcela` | integer (int32) | ✓ | quantidade de parcelas |
| `valorParcela` | number (double) |  | valor da parcela |
| `valorTotalParcela` | number (double) |  | valor total da parcela |
| `percentualParcela` | number (double) |  | percentual da parcela |
| `dataParcela` | string (date-time) | ✓ | data de cadastro da parcela |
| `dataReajuste` | string (date-time) | ✓ | data de inicio do reajuste |
| `dataJuros` | string (date-time) | ✓ | data de inicio do juros |
| `juros` | number (double) |  | valor do juros |
| `dataSegundoJuros` | string (date-time) |  | data de inicio do segundo juros |
| `percentualSegundoJuros` | number (double) |  | percentual segundo juros |
| `tipoParcela` | string | ✓ | tipo de parcela |
| `frequencia` | string | ✓ | código frequencia |
| `amortizacao` | integer (int32) |  | amortização da parcela 0 - Gradiente, 1 - Price, 2 - SAC ou 3 - Simples. |
| `beginEnd` | integer (int32) |  | 0 - Begin  1 - End |
| `reajuste` | string | ✓ | índice de reajuste da parcela quando não for utilizar um plano indexador |
| `JurosComJuros` | integer (int32) |  | Aceita valores de 0 e 1. Indica se as parcelas que possuem amortização Price ou SAC terão juros calculados nos casos que a data de vencimento esteja no mesmo mês(frequências mensais ou anuais) ou dia(frequência diária) da data de início de juros |
| `planoIndexParcela` | integer (int32) |  | plano indexador da parcela, quando não tiver plano informar 1. |
| `tipoValor` | integer (int32) |  | tipo do valor da parcela (0 - percentual, 1 - valor) |
| `carenciaAtraso` | integer (int32) |  | quantidade de dias carência por atraso |
| `carenciaAtrasoCorrecao` | integer (int32) |  | quantidade de dias de carência para cobrança de correção por atraso |
| `cobrarJurosProRata` | integer (int32) |  | juros pro rata |
| `cobrarJurosProRataPrimeiroMes` | integer (int32) |  | realizar o cálculo de juros no primeiro mês como pró-rata. (0 - Não,  1 - Sim") |
| `competencia` | integer (int32) |  | Qual a competência da parcela: 0 - Mês anterior, 1 - Mês atual ou 2 - Mês de geração. |
| `numModeloVenda` | integer (int32) |  | Número do modelo de venda. |
| `tipoContrato` | integer (int32) |  | Tipo de contrato: 0 - Contrato, 1 - Custas, 2 - Seguro, 3 - Honorarios |
| `cap` | string |  | Cap do valor principal da parcela |
| `capCorrecaoAtraso` | string |  | Cap do valor de correção por atraso da parcela |
| `capJuros` | string |  | Cap do valor de juros da parcela |
| `capCorrecao` | string |  | Cap do valor de correção/reajuste da parcela |
| `capMulta` | string |  | Cap do valor de multa da parcela |
| `capJurosAtraso` | string |  | Cap do valor de juros por atraso da parcela |
| `capAcrescimo` | string |  | Cap do valor de acréscimo da parcela |
| `capDesconto` | string |  | Cap do valor de desconto da parcela |
| `capDescontoAntecipado` | string |  | Cap do valor de desconto antecipado (do juros) da parcela |
| `capTaxaBoleto` | string |  | Cap do valor de taxa de boleto da parcela |
| `capDescontoCusta` | string |  | Cap do valor de desconto de custas da parcela |
| `capRepasse` | string |  | Cap do repasse da parcela |
| `capDescontoCondicional` | string |  | Cap do valor de desconto condicional da parcela |
| `tipoParcelamento` | integer (int32) |  | tipo de parcelamento     0 - Contrato     1 - Custas     2 - Seguro     3 - Honorário |
| `NumCtp` | integer (int32) |  | Tipo de custas |
| `OrigemCusta` | integer (int32) |  | Tipo da origem de custas |
| `cobrarMulta` | integer (int32) |  | Cobrar multa ou não para custas |
| `cobrarJurosAtraso` | integer (int32) |  | Cobrar juros por atraso ou não para custas |
| `cobrarImposto` | integer (int32) |  | Cobrar imposto ou não para custas |
| `cobrarCorrecao` | integer (int32) |  | Cobrar correção/reajuste para custas |
| `cobrarCPMF` | integer (int32) |  | cobrar CPMF para custas |
| `repassarLocador` | integer (int32) |  | Repassar ao locador valor das custas |
| `tipoSeguro` | integer (int32) |  | Tipo de seguro |
| `CobrarTaxaAdm` | integer (int32) |  | Cobrar taxa administrativa de aluguel |

### UAUApi.Models.ModeloVenda.PropostaParcelasGeradas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `chaveParcelaGerada` | integer (int32) |  | chave da parcela gerada |
| `numeroParcela` | integer (int32) |  | número da parcela gerada |
| `dataVencimento` | string (date-time) |  | data de vencimento da parcela |
| `valorParcela` | number (double) |  | valor da parcela |
| `tipoParcela` | string |  | tipo de parcela |
| `planoIndexReajuste` | string |  | plano indexador para reajueste |
| `jurosParcela` | number (double) |  | valor do juros da parcela |
| `dataJurosParcela` | string (date-time) |  | data de inicio do juros da parcela |
| `dataPlanoIndexParcela` | string (date-time) |  | data inicio do plano indexador da parcela |
| `valorReajustadoParcela` | number (double) |  | valor reajustado da parcela |
| `tipoVencimentoParcela` | string |  | tipo de vencimento da parcela |
| `amortizacaoParcela` | integer (int32) |  | amortização da parcela |
| `beginEndParcela` | integer (int32) |  | 0 - Begin  1 - End da parcela |
| `qtdTotalParcela` | integer (int32) |  | quantidade total de parcela |
| `dataIncioParcela` | string (date-time) |  | data de incio da parcela |
| `planoIndexParcela` | integer (int32) |  | plano indexador da parcela |
| `grupoParcela` | integer (int32) |  | código do grupo de parcela |
| `qtdTotalGrupo` | number (double) |  | quantidade total de parcelas do grupo |
| `jurosComJuros` | integer (int32) |  | Cobrar juros caso a parcelas esteja no mesmo mês ou no mesmo dia da data de inicio do juros |
| `dataSegundoJuros` | string (date-time) |  | data de incio do segundo juros |
| `percentualSegundoJuros` | number (double) |  | percentual do sengundo juros |
| `carenciaAtraso` | integer (int32) |  | quantidade de dias carência por atraso |
| `carenciaAtrasoCorrecao` | integer (int32) |  | quantidade de dias de carência para cobrança de correção por atraso |
| `cobrarJurosProRata` | integer (int32) |  | cobrar juros pro rata |
| `cobrarJurosProRataPrimeiroMes` | integer (int32) |  | cobrar juros no primeiro mês como pró-rata. (0 - Não,  1 - Sim") |
| `dataInicioAluguel` | string (date-time) |  | data de competência do aluguel |
| `cobrarTaxaAdministrativa` | integer (int32) |  | cobrar taxa administrativa |
| `cap` | string |  | Cap do valor de principal da parcela |
| `capCorrecaoAtraso` | string |  | Cap do valor de correção por atraso da parcela |
| `capJuros` | string |  | Cap do valor de juros da parcela |
| `capCorrecao` | string |  | Cap do valor de correção da parcela |
| `capMulta` | string |  | Cap do valor de multa da parcela |
| `capJurosAtraso` | string |  | Cap do valor de juros por atraso da parcela |
| `capAcrescimo` | string |  | Cap do valor de acréscimo da parcela |
| `capDesconto` | string |  | Cap do valor de desconto da parcela |
| `capDescontoAntecipado` | string |  | Cap do valor de desconto antecipado (juros) da parcela |
| `capTaxaBoleto` | string |  | Cap do valor de taxa de boleto da parcela |
| `capDescontoCusta` | string |  | Cap do valor de desconto de custa da parcela |
| `capRepasse` | string |  | Cap do repasse da parcela |
| `capDescontoCondicional` | string |  | Cap do valor de desconto condicional da parcela |
| `tipoParcelamento` | integer (int32) |  | 0 - Contrato 1 - Custas 2 - Seguro 3 - Honorário |
| `NumCtp` | integer (int32) |  | Tipo da custa |
| `OrigemCusta` | integer (int32) |  | Tipo da origem de custas |
| `cobrarMulta` | integer (int32) |  | Cobrar multa por atraso em parcela de custa |
| `cobrarJurosAtraso` | integer (int32) |  | Cobrar juros por atraso em parcela de custa |
| `cobrarImposto` | integer (int32) |  | Cobrar imposto em parcela de custa |
| `cobrarCorrecao` | integer (int32) |  | Cobrar correção/reajuste em parcela de custa |
| `cobrarCPMF` | integer (int32) |  | Cobrar CPMF em parcela de custa |
| `repassarLocador` | integer (int32) |  | Repassar valor da custa para o locador no repasse |
| `tipoSeguro` | integer (int32) |  | Tipo de seguro da parcela de seguro |
| `meioPreferencialRecebimento` | integer (int32) |  | Meio preferencial de recebimento |

### UAUApi.Models.Proposta.Proposta

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numProposta` | integer (int32) |  | número da proposta |
| `codigoEmpresa` | integer (int32) | ✓ | código da empresa |
| `codigoObra` | string | ✓ | código da obra |
| `tipoContrato` | integer (int32) | ✓ | tipo de contrato (0 - Venda, 1 - Aluguel, 2 - Aluguel garantido e 5 - Aluguel shopping) |
| `dataProposta` | string (date-time) | ✓ | data da proposta |
| `codigoCliente` | integer (int32) | ✓ | Número do prospect principal da proposta |
| `codigoVendedor` | integer (int32) | ✓ | código do vendedor da proposta (pessoa) |
| `valorTotalProposta` | number (double) | ✓ | valor total bruto proposta |
| `desconto` | number (double) |  | desconto em caso de adiantamento |
| `acrescimo` | number (double) |  | valor do acréscimo na Venda |
| `periodoValidade` | integer (int32) | ✓ | período de validade da proposta, em minutos |
| `usuarioCadastro` | string | ✓ | login do usuário que cadastrou a proposta |
| `dataCadastro` | string (date-time) |  | Data de cadastro da proposta. Não será considerada ao gravar uma proposta. Sempre será considerada a data atual |
| `codigoHierarquia` | integer (int32) |  | código da hierarquia de comissão (Obsoleto, utilizamos agora apenas o número da comissão) |
| `numComissao` | integer (int32) |  | número do modelo de comissão |
| `juros` | number (double) |  | juros da proposta |
| `multa` | number (double) |  | multa |
| `jurosContrato` | integer (int32) |  | cobrar juros do contrato |
| `reajusteAnual` | integer (int32) |  | cobrar reajuste anual (0 - Mensal ou 1 - Anual) |
| `gerarResiduo` | integer (int32) |  | a proposta vai gerar  resíduo |
| `qtdeDiasCarenciaAtraso` | integer (int32) |  | Números de dias de carência para cobrança de multa por atraso |
| `numMesRetroagirIdx` | integer (int32) |  | número de meses que irá retroagir a data de reajuste |
| `correcaoAtraso` | integer (int32) |  | Cobrar correção pró-rata |
| `correcaoProRata` | integer (int32) |  | O cálculo de reajuste será pró-rata |
| `cobrarTaxaBoleto` | integer (int32) |  | cobrar taxa boleto |
| `carenciaAtrasoCorrecao` | integer (int32) |  | caso uma parcela esteja atrasada, cobrar a correção por atraso apenas após acarência definida nesse campo |
| `antecipaCorrecao` | integer (int32) |  | caso a venda seja correção anual e o cliente esteja antecipando a parcela será cobrado correção diária nas parcelas antecipadas |
| `cobrarJurosRecPosChave` | integer (int32) |  | caso uma parcela com vencimento antes do início de juros, seja recebida após a data de inicio de juros. Será cobrado juros |
| `zerarCorrecaoNegativa` | boolean |  | zerar correção negativa |
| `antecipaJurosLinear` | boolean |  | antecipar juros linear |
| `juroAtrasoMensal` | boolean |  | cobrar juros por atraso mensal |
| `correcaoCrescente` | boolean |  | cobrar correção crescente (0-Não, 1-Sim) |
| `correcaoAtrasoPerson` | boolean |  | cobrar correção dos dias de atraso, será cobrado a correção do mês mais os dias de atraso |
| `jurosAnual` | integer (int32) |  | o juros serão mensais (0 - Mensais, 1 - Não Mensais) |
| `periodoMesJuros` | integer (int32) | ✓ | período do juros caso não seja mensal (12 - Anual, 6 - Semestral) |
| `multaFracionada` | boolean |  | a multa será fracionada diáriamente (0-Não fracionada, 1-fracionada) |
| `periodoMesReajuste` | integer (int32) | ✓ | frequencia da correção será anual ou semestral (12 meses, 6 meses) |
| `anteciparCorrecaoAniverCont` | boolean |  | Calcular correção por antecipação apenas no próximo aniversário de contrato |
| `hitoricoLancamento` | string |  | historico do lançamento da venda |
| `historicoParcRecebidas` | string |  | historico do lançamento para parcelas recebidas |
| `historicoLancJurosCorrecao` | string |  | historico do lançamento de provisão de juros e correção |
| `usurAprovouProposta` | string |  | login do usuário que aprovou a proposta |
| `dataAprovouProposta` | string (date-time) |  | data de aprovação da proposta |
| `usrCancelouProposta` | string |  | login do usuário que efetuou o cancelamento |
| `datacancelamentoProposta` | string (date-time) |  | data de cancelamento da proposta |
| `usrConfirmouProposta` | string |  | login do usuário que confirmou a proposta |
| `dataConfirmacaoProposta` | string (date-time) |  | data de confirmação da proposta |
| `statusAprovacaoProposta` | integer (int32) | ✓ | Status de aprovação da proposta (1 -  Não aprovada, 2 - Aprovada pelo sistema, 3 -  Aprovada pelo usuário) |
| `statusProposta` | integer (int32) | ✓ | Status da proposta (1 - Ativa, 2 - Confirmada, 3 - Expirada, 4 - Cancelada, 5 - Vendida, 6 - Quitada) |
| `planoIndexador` | integer (int32) |  | possui plano Indexador |
| `dataBaseResiduo` | string (date-time) | ✓ | data base de resíduo |
| `valorProvisaoLongoPrazo` | number (double) |  | Valor que será utilizado para realizar o provisionamento de lançamentos de longo prazo da venda |
| `valorProvisaoCurtoPrazo` | number (double) |  | valor que será utilizado para realizar o provisionamento lançamentos de curto prazo da venda. |
| `codVeiculoDivulgacao` | integer (int32) |  | código do veículo de divulgação |
| `numFinalidade` | integer (int32) |  | código da finalidade |
| `spedPisCofins` | boolean |  | SPED PIS Cofins |
| `observacao` | string |  | observação da proposta de venda |
| `procOportunidade` | number (double) |  | porcentagem de oportunidade |
| `AteHabiteSe` | boolean |  | calcular o valor presente até o habite-se |
| `diaRepasseAluguel` | integer (int32) |  | dia do mês que será repassado o valor do aluguel. |
| `cobrarImposto` | integer (int32) |  | cobrar honorário (0 - Não, 1 - Sim) |
| `cobrarTaxaAdmin` | integer (int32) |  | cobrar taxa administrativa |
| `dataIniContrato` | string (date-time) |  | data início do contrato |
| `dataFimContrato` | string (date-time) |  | data fim de contrato |
| `fianca1` | string |  | fiança |
| `fianca2` | string |  | fiança |
| `fianca3` | string |  | fiança |
| `valorFianca` | number (double) |  | valor fiança |
| `dataFianca` | string (date-time) |  | data fiança |
| `nomeSeguradora` | string |  | nome da seguradora |
| `numApoliceSeguroIncendio` | string |  | número da apólice seguro incêdio |
| `valorSeguroIncendio` | number (double) |  | valor do seguro incêndio |
| `dataSeguroIncendio` | string (date-time) |  | data do seguro incêndio |
| `tipoFianca` | integer (int32) |  | tipo de fiança (0 - Sem Fiança, 1 - Fiadores, 2 - Fiança bancária, 3 - Caução, 4 - Seguro fiança locatícia, 5 - Carta fiança, 6 - Título de capitalização ou 7 - Imóvel em garantia) |
| `atividade` | integer (int32) |  | atividade (0 - Atividade imobiliária, 1 - Prestação de serviço, 2 - Ativo imobilizado, 3 - Locação de equipamento ) |
| `numContratoCEF` | string |  | número do contrato de financiamento junto a CEF |
| `numPadraoCobranca` | integer (int32) |  | número padrão de cobrança |
| `numServicoFiscal` | integer (int32) |  | código do serviço fiscal para cálculo da taxa de administração |
| `tributadoRET` | boolean |  | Tributado pelo RET(Regime Especial de Tributação) |
| `numTributacaoRET` | integer (int32) |  | Código da tributação RET(Regime Especial de Tributação) |
| `UtilizarDescontoUltimaParc` | boolean |  | Define se irá participar da campanha de quitação da última parcela |
| `TipoContratoRec` | integer (int32) |  | Defino o tripo de contrato que será utilizado no registro de recebíveis |
| `MetodoAmortizacaoRec` | integer (int32) |  | Defino o tipo de amortização que será utilizado no registro de recebíveis |
| `IndicePrecoPreObraRec` | integer (int32) |  | Defino o tipo de índice de valores pre obra que será utilizado no registro de recebíveis |
| `IndicePrecoPosObraRec` | integer (int32) |  | Defino o tipo de índice de valores pos obra que será utilizado no registro de recebíveis |
| `AplicacaoJurosRec` | integer (int32) |  | Defino o tipo de Aplicação de juros que será utilizado no registro de recebíveis |
| `JurosAnualPercentualRec` | integer (int32) |  | Defino o percentual de juros anual que será utilizado no registro de recebíveis |
| `TermoReserva` | integer (int32) |  | Define se a proposta é de termo reserva ou não (0 - Não, 1 - Sim) |

### UAUApi.Models.Proposta.ConsultarDadosPropostaVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numProposta` | integer (int32) | ✓ | Número da proposta |
| `valorAntecipado` | integer (int32) |  | Informar se buscará valor antecipado ou não. |
| `dataCalculo` | string (date-time) |  | Data cálculo para obter valores reajustados. |

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

### UAUApi.Models.ComissaoHierarquia.HierarquiaParcelaDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  | Código de identificação da parcela no Banco de Dados |
| `CodigoHierarquia` | integer (int32) |  | Código da Hierarquia de comissão |
| `TipoParcela` | string |  | Código do tipo da parcela (Ex.: P) |
| `DescricaoParcela` | string |  | Descrição da Parcela |
| `Situacao` | integer (int32) |  | Situação da Parcela (0 - Ativa, 1 - Inativa) |
| `DataCadastro` | string (date-time) |  | Data de cadastro da parcela |
| `UsuarioCadastro` | string |  | Usuário que cadastrou a parcela |

### UAUApi.Models.Proposta.ParcelasHierarquiaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo` | integer (int32) | ✓ | Código da Hierarquia |

### UAUApi.Models.Proposta.CancelarPropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroProposta` | integer (int32) | ✓ | Número da proposta a ser cancelada |
| `cancelarVendida` | boolean |  | Permitir cancelar proposta vendida |
| `ExcluirBoletos` | boolean |  | Permitir excluir os boletos ativos da proposta |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

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

### UAUApi.Models.Proposta.ParcelaSelRenegociacaoRequest

Dados das parcelas selecionadas para renegociação pela API

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumParc` | integer (int32) | ✓ | Número da parcela |
| `NumParcGer` | integer (int32) | ✓ | Número geral da parcela (identificador) |
| `Tipo` | string | ✓ | Tipo da parcela |

### Globaltec.UAU.Comp.PropostaParcelasGeradas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `chaveParcelaGerada` | integer (int32) |  |  |
| `numeroParcela` | integer (int32) |  |  |
| `dataVencimento` | string (date-time) |  |  |
| `valorParcela` | number (double) |  |  |
| `tipoParcela` | string |  |  |
| `planoIndexReajuste` | string |  |  |
| `jurosParcela` | number (double) |  |  |
| `dataJurosParcela` | string (date-time) |  |  |
| `dataPlanoIndexParcela` | string (date-time) |  |  |
| `valorReajustadoParcela` | number (double) |  |  |
| `tipoVencimentoParcela` | string |  |  |
| `amortizacaoParcela` | integer (int32) |  |  |
| `beginEndParcela` | integer (int32) |  |  |
| `qtdTotalParcela` | integer (int32) |  |  |
| `dataIncioParcela` | string (date-time) |  |  |
| `planoIndexParcela` | integer (int32) |  |  |
| `grupoParcela` | integer (int32) |  |  |
| `qtdTotalGrupo` | number (double) |  |  |
| `jurosComJuros` | integer (int32) |  |  |
| `dataSegundoJuros` | string (date-time) |  |  |
| `percentualSegundoJuros` | number (double) |  |  |
| `carenciaAtraso` | integer (int32) |  |  |
| `carenciaAtrasoCorrecao` | integer (int32) |  |  |
| `cobrarJurosProRata` | integer (int32) |  |  |
| `cobrarJurosProRataPrimeiroMes` | integer (int32) |  |  |
| `dataInicioAluguel` | string (date-time) |  |  |
| `cobrarTaxaAdministrativa` | integer (int32) |  |  |
| `TipoParcContrato` | integer (int32) |  |  |
| `meioPreferencialRecebimento` | integer (int32) |  |  |

### UAUApi.Models.Proposta.ParcelaRenegociacaoRequest

Dados das parcelas renegociados pela API

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) | ✓ | Número da parcela |
| `Tipo` | string | ✓ | Tipo da parcela |
| `Valor` | number (double) | ✓ | Valor principal |
| `DtVencimento` | string (date-time) | ✓ | Data de vencimento |
| `DtParc` | string (date-time) | ✓ | Data da primeira parcela do grupo Preencher com a data de vencimento da primeira parcela |
| `Amortizacao` | integer (int32) | ✓ | Tipo de amortização 0-Gradiente 1-Price 2-SAC 3-Simples |
| `BeginEnd` | integer (int32) | ✓ | 0-Begin ou 1-End (quando for amortização PRICE) |
| `NumGrupo` | integer (int32) | ✓ | Número do grupo que a parcela pertence |
| `TotalParcGrupo` | integer (int32) | ✓ | Total de parcelas do grupo |
| `Frequencia` | string | ✓ | Frequência de vencimento (mensal, semestral, anual etc...) |
| `DtIniJuros` | string (date-time) | ✓ | Data de início de cobrança da 1ª taxa de juros contratuais |
| `TxJuros` | number (double) | ✓ | 1ª Taxa de juros contratual |
| `DataSegJuros` | string (date-time) |  | Data de início de cobrança da 2ª taxa de juros contratuais |
| `TxSegJuros` | number (double) |  | 2ª Taxa de juros contratual |
| `DtIniIdx` | string (date-time) | ✓ | Data do início da correção indexada |
| `IdxReaj` | string | ✓ | Código do índice de reajuste |
| `GrupoIdx` | integer (int32) | ✓ | Número do plano indexador utilizado no cálculo |
| `DtJurosComJuros` | integer (int32) | ✓ | Cobrar juros no mês/dia da data de juros |
| `CobrarJurosProRata` | integer (int32) | ✓ | Cobrar juros pró-rata |
| `CobrarJurosProRataPrimeiroMes` | integer (int32) | ✓ | Cobrar juros pró-rata 1º mês |
| `CarenciaAtraso` | integer (int32) | ✓ | Dias de carência para multa e juros por atraso |
| `CarenciaAtrasoCorrecao` | integer (int32) | ✓ | Dias de carência para cobrar correção atraso |
| `TotalParc` | integer (int32) | ✓ | Total de parcelas |
| `MeioPreferencialRecebimento` | integer (int32) | ✓ | Meio preferencial de recebimento da parcela |
