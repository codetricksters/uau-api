# Cotacao

## POST `/api/Cotacao/ContaCotacoesMob`

**Conto as cotações que possuem simulações que o usuário pode aprovar.**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `login_usuario` | query | string | ✓ | login do usuário. |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | integer (int32) |

---

## POST `/api/v{version}/Cotacao/AdicionarFornecedorCotacao`

**Adicionar fornecedor a uma cotação aberta.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AdicionarFornecedorCotacao
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Permite vincular um fornecedor a uma cotação em aberto de material ou serviço.
2. Para identificação do fornecedor, são aceitos o código ou CPF/CNPJ deste no sistema.
3. Para vínculo do fornecedor a uma cotação específica, o código dessa cotação, empresa e, o CPF/CNPJ ou código do fornecedor devem ser informados.
4. Para vínculo do fornecedor a uma cotação geral, somente o código da cotação geral e, o CPF/CNPJ ou código do fornecedor devem ser informados.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.AdicionarFornecedorCotacaoRequest`](#uauapimodelscotacaoadicionarfornecedorcotacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/AprovarConfirmacaoCotacaoPorObra`

**Aprovar confirmação de cotação por obra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Possibilita aprovar a confirmação da cotação de material ou serviço por obra.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.AprovacaoConfirmacaoCotacaoPorObraRequest`](#uauapimodelscotacaoaprovacaoconfirmacaocotacaoporobrarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/AprovarSimulacoesCompra`

**Aprovar simulações de compra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. É necessário permissão de aprovação para o programa ALSIMULCOT

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.AprovarSimulacoesCompraRequest`](#uauapimodelscotacaoaprovarsimulacoescomprarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/AtualizarCondicaoPagamentoEntrega`

**Atualizar as condições de entrega relacionado a cotação.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AtualizarCondicaoPagamentoEntrega
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Permite atualizar os dados de condição de entrega da cotação, bem como dias para entrega, quantidade de parcela, intervalo das parcelas, entre outros.
2. A condição de pagamento utilizada será sempre SOBRE A ENTREGA.
3. Para atualizar as condições de pagamento de uma cotação específica, o código dessa cotação e empresa devem ser informados.
4. Para atualizar as condições de pagamento de uma cotação geral, somente o código da cotação geral deve ser informado.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.AtualizarCondicaoPagamentoEntregaRequest`](#uauapimodelscotacaoatualizarcondicaopagamentoentregarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/AtualizarItemCotacao`

**Atualizar os dados dos itens de cotação de material, cotação de serviço e adiantamento de contrato.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Cotacao/AtualizarItemCotacao
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Permite atualizar os dados dos itens de cotação, seja ela de material ou de serviço.
2. Para cotações específicas que forem pertencentes à cotação geral, serão alteradas somente a quantidade e a marca (no caso de cotação de material). 
   Os demais valores só serão alterados se a cotação geral for informada na requisição.
3. Para cotações que forem pertencentes à cotação geral, durante a execução se não existir insumo para um dos itens da cotação informada a execução irá finalizar, efetivando somente a atualização dos itens de cotação anteriores.
4. Informações de IPI, ICMS e Marca só estão relacionadas às cotações de material, portanto podem ser omitidas na requisição.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.AtualizarItemCotacaoRequest`](#uauapimodelscotacaoatualizaritemcotacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/BuscarCotacaoAbertaFornecedor`

**Consultar as cotações abertas para o fornecedor, por CNPJ do fornecedor.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio: 
1. Permite consultar os dados de cotações de material ou serviço que estão disponíveis para o fornecedor. Os tipos de cotações retornadas são:
   - 0 - Cot. material regular
   - 1 - Cot. material adiant. contrato
   - 2 - Cot. serviço regular
   - 3 - Cot. patrimônio
   - 4 - Cot. material contrato
   - 5 - Cot. material emergencial
   - 6 - Cot. manutenção de patrimônio
   - 7 - Cot. material regularização
   - 8 - Cot. material complemento
   - 9 - Cot. serviço emergencial
   - 10 - Cot. serviço regularização
   - 11 - Cot. serviço complemento
   - 12 - Cot. serviço adiant. contrato
   - 13 - Cot. serviço contrato
2. É obrigatório informar o CNPJ do fornecedor para realizar a consulta.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.BuscarCotacaoAbertaFornecedorRequest`](#uauapimodelscotacaobuscarcotacaoabertafornecedorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Cotacao.DadosCotacao`](#uauapimodelscotacaodadoscotacao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/BuscarItensCotacaoFornecedor`

**Consultar itens de cotação por código do fornecedor.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Cotacao/BuscarItensCotacaoFornecedor
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Permite consultar os dados de itens de cotação de material ou serviço por código do fornecedor.
2. Somente cotações com status "0 - Criada" são retornadas.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.BuscarItensCotacaoFornecedorRequest`](#uauapimodelscotacaobuscaritenscotacaofornecedorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Cotacao.ItensCotacaoFornecedor`](#uauapimodelscotacaoitenscotacaofornecedor) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/ConsultarAprovacaoDaCotacaoPorObra`

**Consultar as aprovações da cotação por obra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. São consultadas as aprovações já realizadas para uma determinada cotação de material ou serviço.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.AprovacaoConfirmacaoSimulacaoRequest`](#uauapimodelscotacaoaprovacaoconfirmacaosimulacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Cotacao.CotacaoIntegracao.AprovacaoConfirmacaoSimulacao`](#uauapimodelscotacaocotacaointegracaoaprovacaoconfirmacaosimulacao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/ConsultarCotacoesConfirmacaoPendente`

**Consultar as cotações com confirmações pendentes**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta cotações de material e serviço que estão com as confirmações pendentes.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.CotacaoConfirmacaoPendenteRequest`](#uauapimodelscotacaocotacaoconfirmacaopendenterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Cotacao.CotacaoIntegracao.CotacoesConfirmacaoPendente`](#uauapimodelscotacaocotacaointegracaocotacoesconfirmacaopendente) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/ConsultarItensCotacaoPorObra`

**Consultar itens cotação por obra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Permite consultar itens da cotação de material ou serviço que esteja aguardando confirmação por obra, filtrando por empresa, obra e número da cotação.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.ConsultarItensCotacaoPorObraRequest`](#uauapimodelscotacaoconsultaritenscotacaoporobrarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Cotacao.ItensCotacaoPorObra`](#uauapimodelscotacaoitenscotacaoporobra) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/ConsultarJustificativasAprovacaoForaSequencia`

**Consultar as justificativas para aprovações de cotação fora da sequência do usuário.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consultar as justificativas que podem ser utilizadas em aprovações de confirmação de cotação de material ou serviço que esteja fora da sequência do usuário (Controle de aprovações).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.Cotacao.CotacaoIntegracao.JustificativaPadraoAprovacao`](#uauapimodelscotacaocotacaointegracaojustificativapadraoaprovacao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/ConsultarQuantidadeCotacaoPendentePorObra`

**Consultar a quantidade de cotações pendentes de aprovação por obra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Verifica a quantidade de cotações de material e serviço com pendência na aprovação filtrando por obra.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.ConsultarQuantidadeCotacaoPendentePorObraRequest`](#uauapimodelscotacaoconsultarquantidadecotacaopendenteporobrarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | integer (int32) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/ConsultarQuantidadeCotacaoPendentePorObraMob`

**Consultar a quantidade de cotações pendentes de aprovação para a obra selecionada**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consultar a quantidade de cotações de material e serviço com pendência na aprovação filtrando por obra.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.ConsultarQuantidadeCotacaoPendentePorObraRequest`](#uauapimodelscotacaoconsultarquantidadecotacaopendenteporobrarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | integer (int32) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/ContaCotacoesAprovMob`

**Conto as cotações que possuem simulações que o usuário pode aprovar.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/ContaCotacoesMob
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consultar a quantidade de cotações de material e serviço que possuem simulações que o usuário pode aprovar.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.ContaCotacoesMobRequest`](#uauapimodelscotacaocontacotacoesmobrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/InserirAlteraComentFornFrete`

**Esta rotina inseri um comentario ou atualizar um ja existente."), SoapHeader("TicketAuth**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/InserirAlteraComentFornFrete
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Inserir um comentário ou atualizar um já existente.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `tipoCarenciaFixa` | query | boolean |  |  |
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.InserirAlteraComentFornFreteRequest`](#uauapimodelscotacaoinseriralteracomentfornfreterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/RemoverAprovacaoSimulacoesCompra`

**Remover aprovações das simulações de compra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. É necessário permissão de exclusão para o programa ALCONFCOT caso a cotação esteja no fechamento de compra
e permissão exclusão para o programa ALANALISE caso a cotação esteja na confirmação de cotação por obra.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.RemoverAprovacaoSimulacoesCompraRequest`](#uauapimodelscotacaoremoveraprovacaosimulacoescomprarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Cotacao/ReprovarConfirmacoesCotacaoPorObra`

**Reprovar as confirmações de cotação por obra**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. É necessário permissão de exclusão para o programa ALCONFCOT caso a cotação esteja no fechamento de compra
e permissão exclusão para o programa ALANALISE caso a cotação esteja na confirmação de cotação por obra.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Cotacao.ReprovarConfirmacoesCotacaoPorObraRequest`](#uauapimodelscotacaoreprovarconfirmacoescotacaoporobrarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Cotacao.ReprovarConfirmacoesCotacaoPorObraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ConfirmacoesCotacao` | array de [`UAUApi.Models.Cotacao.ReprovarConfirmacaoCotacaoPorObraRequest`](#uauapimodelscotacaoreprovarconfirmacaocotacaoporobrarequest) |  | Reprovar confirmação de cotação. |
| `justificativaReprovacao` | string | ✓ | Justificativa para a reprovação da simulação. |

### UAUApi.Models.Cotacao.ReprovarConfirmacaoCotacaoPorObraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) | ✓ | Código da empresa. |
| `numeroSimulacao` | integer (int32) | ✓ | Número da simulação de compra. |
| `numeroCotacao` | integer (int32) | ✓ | Número da cotação. |

### UAUApi.Models.Cotacao.RemoverAprovacaoSimulacoesCompraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Simulacoes` | array de [`UAUApi.Models.Cotacao.RemoverAprovacaoSimulacaoCompraRequest`](#uauapimodelscotacaoremoveraprovacaosimulacaocomprarequest) |  | Simulações de compra para remoção das aprovações |

### UAUApi.Models.Cotacao.RemoverAprovacaoSimulacaoCompraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa. |
| `numeroSimulacao` | integer (int32) |  | Número da simulação de compra. |
| `numeroCotacao` | integer (int32) |  | Número da cotação. |

### UAUApi.Models.Cotacao.InserirAlteraComentFornFreteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa da cotação |
| `codigo_fornecedor` | integer (int32) |  | Código do fornecedor da cotação |
| `cotacao` | integer (int32) |  | Número da cotação |
| `cond_pagto` | integer (int32) |  | Condição de pagamento: 0, 1 ou 2 |
| `tipo_coment` | integer (int32) |  | Tipo de comentário: 0 - Fornecedor ou 1 - Frete |
| `efet_pgto_parc` | integer (int32) |  | Efetua pagamento em parcela sobre: 0 - Vencimento da 1ª parcela, 1 - Entrega, 2 - Cotação ou 3 - Emissão da nota fiscal |
| `dtvenc_ini` | string |  | Data de vencimento |
| `qtde_parc` | number (double) |  | Quantiade de Parcelas |
| `intev_parc` | number (double) |  | Intervalo das parcelas |
| `obs_pgto` | string |  | Observação de pagamento |
| `obs_entrega` | string |  | Observação de Entrega |
| `tipo_pgto` | integer (int32) |  | Tipo de Pagamento: 0 - Nenhum, 1 - Em carteira, 2 - Em cobrança bancária, 3 - Crédito em conta, 4 - Depósito em conta, 5 - Cartão de crédito ou 6 - PIX |
| `tem_frete` | integer (int32) |  | Informa o tipo de frete: 0 - FOB (material a retirar), 1 - CIF (Frete por conta do emitente), 2 - FOB (Frete a pagar incluso) ou 3 - FOB (Frete a pagar para transportadora) |
| `diaini_venc` | integer (int32) |  | Dia inicial do vencimento |
| `freteqtde_ent` | integer (int32) |  | Quantidade de Entrega |
| `interv_ent` | integer (int32) |  | Intervalo entre as Entregas |
| `diasEntrega` | integer (int32) |  | Dias para entrega |

### UAUApi.Models.Cotacao.ContaCotacoesMobRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  |  |

### UAUApi.Models.Cotacao.ConsultarQuantidadeCotacaoPendentePorObraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `loginUsuario` | string | ✓ | Login do usuário da aprovação |
| `codigoDepartamento` | string |  | Código do departamento que o usuário da aprovação está vinculado (opcional) |
| `codigoCargo` | string |  | Código do cargo que o usuário da aprovação está vinculado (opcional) |
| `listaEmpObras` | array de [`UAUApi.Models.Cotacao.ObraCotacaoRequest`](#uauapimodelscotacaoobracotacaorequest) |  | Lista das empresas e obras selecionadas que deseja consultar as aprovações pendentes (opcional) |

### UAUApi.Models.Cotacao.ObraCotacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |

### UAUApi.Models.Cotacao.CotacaoIntegracao.JustificativaPadraoAprovacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoJustificativa` | integer (int32) |  | Código da justificativa. |
| `descJustificativa` | string |  | Descrição da justificativa |
| `descTipo` | string |  | Descrição do tipo da justificativa |

### UAUApi.Models.Cotacao.ItensCotacaoPorObra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Empresa da cotação. |
| `DescrEmpresa` | string |  | Descrição da empresa. |
| `Obra` | string |  | Obra da cotação. |
| `DescrObra` | string |  | Descrição da obra. |
| `Cotacao` | integer (int32) |  | Número da cotação. |
| `DescrCotacao` | string |  | Descrição da cotação. |
| `Item` | string |  | Código do item da cotação. |
| `DescrItem` | string |  | Descrição do item. |
| `Quantidade` | number (double) |  | Quantidade do item na cotação. |
| `Preco` | number (double) |  | Preço do item na cotação |
| `PrecoSemIPI` | number (double) |  |  |
| `Total` | number (double) |  | Total do item na cotação. |
| `Marca` | string |  | Marca do item na cotação. |
| `Fornecedor` | integer (int32) |  | Código do fornecedor do item. |
| `NomeFornecedor` | string |  | Nome fornecedor |
| `CNPJ` | string |  | CNPJ do fornecedor. |
| `CidadeObra` | string |  | Cidade da obra. |
| `CidadeFornecedor` | string |  | Cidade do fornecedor. |
| `IPI` | number (double) |  | Valor do IPI do item da cotação |
| `ICMS` | number (double) |  | Valor do ICMS do item da cotação |
| `ValorDiferencaAliquota` | number (double) |  | Valor da diferença de aliquota do item da cotação |
| `TotalSemIPI` | number (double) |  | Valor do total do item da cotação sem o valor do IPI |
| `unidadeItem` | string |  | Unidade do item da cotação |
| `precoOrcado` | number (double) |  | Preco orçado do item no pedido |

### UAUApi.Models.Cotacao.ConsultarItensCotacaoPorObraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Empresa da cotação. |
| `obra` | string | ✓ | Obra da cotação. |
| `cotacao` | integer (int32) | ✓ | Número da cotação. |

### UAUApi.Models.Cotacao.CotacaoIntegracao.CotacoesConfirmacaoPendente

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa que a cotação pertence. |
| `descEmpresa` | string |  | Descrição da empresa que a cotação pertence. |
| `codigoObra` | string |  | Código da obra que a cotação pertence. |
| `descObra` | string |  | Descrição da obra que a cotação pertence. |
| `numeroCotacao` | integer (int32) |  | Número da cotação. |
| `descCotacao` | string |  | Descrição da cotação. |
| `numeroSimulacao` | integer (int32) |  | Número da simulação confirmada que a cotação pertence. |
| `tipoCotacao` | integer (int32) |  | Tipo da cotação 0 - Cot. material regular 1 - Cot. material adiant. contrato 2 - Cot. serviço regular 3 - Cot. patrimônio 4 - Cot. material contrato 5 - Cot. material emergencial 6 - Cot. manutenção de patrimônio 7 - Cot. material regularização 8 - Cot. material complemento 9 - Cot. serviço emergencial 10 - Cot. serviço regularização 11 - Cot. serviço complemento |
| `descTipoCotacao` | string |  | Descrição do tipo da cotação |
| `subTotal` | number (double) |  | Sub-Total da cotação |
| `valorDesconto` | number (double) |  | Valor de desconto da cotação |
| `valorTransporte` | number (double) |  | Valor de transporte |
| `valorTotal` | number (double) |  | Valor total da cotação Sub-Total + Transporte - desconto |
| `valorDifAliqICMS` | number (double) |  | Valor diferencial de alíquota ICMS |
| `totalDifAliqICMS` | number (double) |  | Valor total da cotação com diferencial de alíquota ICMS |
| `dataVencimento` | string (date-time) |  | Data de vencimento da cotação |
| `aprovacaoSeqUsuario` | integer (int32) |  | Indica se está na sequência da aprovação do usuário 0 - Fora da sequência do usuário 1 - Na sequência do usuário |
| `casaDecPreco` | integer (int32) |  | Número de casa decimal para o preço da cotação |
| `casaDecQtde` | integer (int32) |  | Número de casa decimal para a quantidade da cotação |
| `titleQuotation` | string |  | Armazenar a concatenação da descrição "Cotação " com o número da cotação para funcionamento de filtro na tela de aprovação de conf. de cotação. |

### UAUApi.Models.Cotacao.CotacaoConfirmacaoPendenteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string | ✓ | Usuário da aprovação. |
| `departamento` | string |  | Departamento do usuário |
| `cargo` | string |  | Cargo do usuário |
| `listaEmpObras` | array de [`UAUApi.Models.Cotacao.ObraCotacaoRequest`](#uauapimodelscotacaoobracotacaorequest) | ✓ | Lista das empresas e obras selecionadas pelo usuário |
| `cotacao` | integer (int32) |  |  |

### UAUApi.Models.Cotacao.CotacaoIntegracao.AprovacaoConfirmacaoSimulacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nomeUsuario` | string |  | Usuário que realizou a aprovação da cotação. |
| `dataAprovacao` | string (date-time) |  | Data que foi realizada a aprovação. |

### UAUApi.Models.Cotacao.AprovacaoConfirmacaoSimulacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa que a cotação pertence. |
| `codigoObra` | string |  | Código da obra que a cotação pertence. |
| `numeroSimulacao` | integer (int32) |  | Número da simulação confirmada que a cotação pertence. |
| `numeroCotacao` | integer (int32) |  | Número da cotação. |

### UAUApi.Models.Cotacao.ItensCotacaoFornecedor

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `insumo` | string | ✓ | Código do insumo do item da cotação |
| `descricaoInsumo` | string | ✓ | Descrição do insumo do item da cotação |
| `unidadeInsumo` | string | ✓ | Unidade do insumo do item da cotação |
| `cotacao` | integer (int32) | ✓ | Número da cotação |
| `fornecedor` | integer (int32) | ✓ | Código do fornecedor da cotação |
| `quantidade` | number (double) | ✓ | Quantidade do item da cotação |
| `preco` | number (double) | ✓ | Preço do item da cotação |
| `porcentagemIpi` | number (double) | ✓ | Percentual de imposto IPI do item da cotação |
| `valorIpi` | number (double) | ✓ | valor de imposto IPI do item da cotação |
| `marca` | string | ✓ | Marca do item da cotação |
| `porcentagemIcms` | number (double) | ✓ | Percentual de imposto ICMS do item da cotação |
| `valorIcms` | number (double) | ✓ | Valor do imposto ICMS do item da cotação |
| `empresaCotacaoEspecifica` | integer (int32) |  | Código da empresa da cotação específica |
| `cotacaoEspecifica` | integer (int32) |  | Número da cotação específica |
| `EspecificacaoItem` | array de [`UAUApi.Models.Cotacao.EspecificaoItem`](#uauapimodelscotacaoespecificaoitem) | ✓ | Lista dos campos |

### UAUApi.Models.Cotacao.EspecificaoItem

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Pedido` | integer (int32) | ✓ | Código da Pedido. |
| `Descricao` | string | ✓ | Especificação do insumo (Detalhes Adicionado Manualmente pelo Usuário). |

### UAUApi.Models.Cotacao.BuscarItensCotacaoFornecedorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa da cotação, sendo de informação obrigatória apenas para cotações específicas (origem: 0) |
| `cotacao` | integer (int32) | ✓ | Número da cotação |
| `fornecedor` | integer (int32) | ✓ | Código do fornecedor |
| `origem` | integer (int32) | ✓ | Origem da cotação: 0 - Específica; 1 - Geral; |

### UAUApi.Models.Cotacao.DadosCotacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `descricaoEmpresa` | string | ✓ | Descrição da empresa |
| `DDD` | string | ✓ | - DDD do telefone da empresa |
| `fone` | string | ✓ | Número de telefone da empresa |
| `endereco` | string | ✓ | Endereço da empresa |
| `enderecoEntrega` | string |  | Endereço de entrega |
| `enderecoFaturamento` | string |  | Endereço de faturamento |
| `dadosFaturamento` | array de [`UAUApi.Models.Cotacao.DadosFaturamento`](#uauapimodelscotacaodadosfaturamento) |  | Dados de faturamento para as obras dos itens dos pedidos da cotação. |
| `numeroEndereco` | string | ✓ | Número do endereço da empresa |
| `setor` | string | ✓ | Setor da empresa |
| `UF` | string | ✓ | UF da empresa |
| `cidade` | string | ✓ | Cidade em que está localizada a empresa |
| `CEP` | string | ✓ | CEP da empresa |
| `numeroCotacao` | integer (int32) | ✓ | Número da cotação específica |
| `numeroCotacaoGeral` | integer (int32) | ✓ | Número da cotação geral |
| `dataCad` | string (date-time) | ✓ | Data de cadastro da cotação |
| `usuarioCotacao` | string | ✓ | Usuário da cotação |
| `descricaoCotacao` | string | ✓ | Descrição da cotação |
| `observacaoCotacao` | string | ✓ | Observação da cotação |
| `codigoCotador` | string | ✓ | Código do usuário cotador |
| `nomeCotador` | string | ✓ | Nome do usuário cotador |
| `origem` | integer (int32) | ✓ | Origem da cotação: 0 -Específica; 1 - Geral; |
| `codigoFornecedor` | integer (int32) | ✓ | Código do fornecedor |
| `cnpjEmpresa` | string | ✓ | CNPJ da empresa |
| `inscricaoEstEmpresa` | string | ✓ | Inscrição estadual da empresa |
| `inscricaoMunEmpresa` | string | ✓ | Inscrição municipal da empresa |
| `cnpjFornecedor` | string | ✓ | CNPJ do fornecedor |
| `inscricaoEstFornecedor` | string | ✓ | Inscrição estadual do fornecedor |
| `inscricaoMunFornecedor` | string | ✓ | Inscrição municipal do fornecedor |

### UAUApi.Models.Cotacao.DadosFaturamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Obra` | string |  | Código da obra do item do pedido da cotação. |
| `CNPJFaturamento` | string |  | CNPJ faturamento |
| `razaoSocialFaturamento` | string |  | Razão Social faturamento |
| `inscricaoMunicipalFaturamento` | string |  | Inscrição Municipal faturamento |
| `inscricaoEstadualFaturamento` | string |  | Inscrição Estadual faturamento |

### UAUApi.Models.Cotacao.BuscarCotacaoAbertaFornecedorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | ✓ | CNPJ do fornecedor (sem pontuação). |

### UAUApi.Models.Cotacao.AtualizarItemCotacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `listaItensCotacao` | array de [`UAUApi.Models.Cotacao.ItensCotacaoForn`](#uauapimodelscotacaoitenscotacaoforn) | ✓ | Lista de itens de cotação. |

### UAUApi.Models.Cotacao.ItensCotacaoForn

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa da cotação, sendo de informação obrigatória apenas para cotações específicas (origem: 0) |
| `cotacao` | integer (int32) | ✓ | Número da cotação. |
| `origem` | integer (int32) | ✓ | Origem da cotação: 0 - Específica; 1- Geral; |
| `fornecedor` | integer (int32) | ✓ | Codigo do fornecedor. |
| `insumo` | string | ✓ | Código do insumo. |
| `quantidade` | number (double) |  | Quantidade cotada. |
| `preco` | number (double) | ✓ | Preço do item de cotação *Não adicionar o valor do IPI, ele é adicionado ao gravar na cotação* |
| `porcentagemIPI` | number (double) |  | Percentual IPI. |
| `valorIPI` | number (double) |  | Valor do IPI. |
| `marca` | string |  | Marca do item. |
| `porcentagemICMS` | number (double) |  | Percentual ICMS. |
| `valorICMS` | number (double) |  | Valor do ICMS. |

### UAUApi.Models.Cotacao.AtualizarCondicaoPagamentoEntregaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa da cotação. Necessário quando for cotação específica. |
| `cotacao` | integer (int32) |  | Número da cotação específica. |
| `numeroCotacaoGeral` | integer (int32) |  | Número da cotação geral/agrupada. |
| `fornecedor` | integer (int32) | ✓ | Código do fornecedor da cotação |
| `diasEntrega` | integer (int32) |  | Número de dias para entrega Obs.: Valor máximo = 1000. |
| `quantidadeEntrega` | integer (int32) | ✓ | Quantidade de entregas Obs.: Valor &gt;= 1 e valor máximo = 100. |
| `intervaloEntrega` | integer (int32) |  | Dias de intervalo entre uma entrega e outra Obs.: Valor &gt;= 0 e valor máximo = 1000. |
| `diasPagamento` | integer (int32) |  | Dias para pagamento após entrega Obs.: Valor &gt;= 0 e valor máximo = 1000. |
| `quantidadeParcela` | integer (int32) | ✓ | Quantidade de parcelas Obs.: Valor &gt;= 1 e valor máximo = 255. |
| `intervaloParcela` | integer (int32) |  | Dias de intervalo entre as parcelas Obs.: Valor &gt;= 0 e valor máximo = 1000. |
| `tipoFrete` | integer (int32) |  | Tipo do frete: CIF = 0 e FOB = 1 |
| `tipoPagamento` | integer (int32) |  | Tipo de pagamento: 0 -&gt; Nenhum, 1 -&gt; Em carteira, 2 -&gt; Em cobrança bancária, 3 -&gt; Crédito em conta, 4 -&gt; Depósito em conta, 5 -&gt; Cartão de crédito ou 6 -&gt; PIX Se não for informado então será considerado como 0 -&gt; Nenhum. |
| `CondicaoPagamento` | string |  | Condição de pagamento, quando preenchido irá sobrepor a condição gerada automaticamente. |

### UAUApi.Models.Cotacao.AprovarSimulacoesCompraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Simulacoes` | array de [`UAUApi.Models.Cotacao.AprovaSimulacaoCompraRequest`](#uauapimodelscotacaoaprovasimulacaocomprarequest) |  | Simulações a serem aprovadas |

### UAUApi.Models.Cotacao.AprovaSimulacaoCompraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa que a cotação pertence. |
| `numeroSimulacao` | integer (int32) |  | Número da simulação que a cotação pertence. |
| `numeroCotacao` | integer (int32) |  | Número da cotação. |
| `tipoAprovacaoCotacaoServico` | integer (int32) |  | Tipo de aprovação de simulação de cotação de serviço. Utilizado para controlar o status da simulação ao aprová-la. 0  - Aprovar e enviar para a confirmação por obra 1  - Confirmar e enviar para o fechamento de compra (Quando a empresa ou obra está configurada para confirmação por obra de forma automática) 2  - Aprovar para utilização em contrato de serviço |
| `Codigojustificativa` | integer (int32) |  | Código da justificativa de aprovacao fora de sequência |
| `Observacaojustificativa` | string |  | Observação da justificativa de aprovação fora de sequência |
| `departamento` | string |  | Código do departamento do usuário da aprovação |
| `cargo` | string |  | Código do cargo do usuário da aprovação |

### UAUApi.Models.Cotacao.AprovacaoConfirmacaoCotacaoPorObraRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `listaConfirmarAprovacaoCotacao` | array de [`UAUApi.Models.Cotacao.CotacoesConfirmacaoAprovacao`](#uauapimodelscotacaocotacoesconfirmacaoaprovacao) |  | Lista de dados de cotação para confirmar aprovação da mesma. |

### UAUApi.Models.Cotacao.CotacoesConfirmacaoAprovacao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa que a cotação pertence. |
| `obra` | string | ✓ | Código da obra que a cotação pertence. |
| `NumCotacao` | integer (int32) | ✓ | Número da cotação. |
| `numSimulacao` | integer (int32) | ✓ | Número da simulação confirmada que a cotação pertence. |
| `tipoCotacao` | integer (int32) |  | Tipo da cotação 0 - Cot. material regular 1 - Cot. material adiant. contrato 2 - Cot. serviço regular 3 - Cot. patrimônio 4 - Cot. material contrato 5 - Cot. material emergencial 6 - Cot. manutenção de patrimônio 7 - Cot. material regularização 8 - Cot. material complemento 9 - Cot. serviço emergencial 10 - Cot. serviço regularização 11 - Cot. serviço complemento |
| `totalCotacao` | number (double) |  | Valor total da cotação Sub-Total + Transporte - desconto |
| `departamentoUsr` | string |  | Código do departamento do usuário de aprovação |
| `cargoUsr` | string |  | Código do cargo do usuário de aprovação |
| `usuario` | string | ✓ | Código do usuário de aprovação. |
| `codJustificativa` | integer (int32) |  | Código da justificativa para aprovação fora da sequência do usuário |
| `obsJustificativa` | string |  | Observação da justificativa para aprovação para aprovação fora da sequência do usuário |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |

### UAUApi.Models.Cotacao.AdicionarFornecedorCotacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codFornecedor` | integer (int32) |  | Código do fornecedor. Necessário quando o CPF/CNPJ não for informado. |
| `CNPJFornecedor` | string |  | CPF ou CNPJ do fornecedor. Necessário quando o código do fornecedor não for informado. |
| `numeroCotacao` | integer (int32) |  | Número da cotação. Necessário para quando for cotação específica. |
| `numeroCotacaoGeral` | integer (int32) |  | Número da cotação geral. Necessário quando for cotação geral. |
| `empresa` | integer (int32) |  | Código da empresa. Necessário quando for cotação específica. |
