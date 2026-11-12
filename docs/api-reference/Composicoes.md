# Composicoes

## POST `/api/v{version}/Composicoes/AlterarInsumoComposicoesGeral`

**- Método com finalidade de alterar dados dos insumos na composição geral (composição civil).**

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
Esquema: [`UAUApi.Models.Composicoes.InsumoComposicaoGeralRequest`](#uauapimodelscomposicoesinsumocomposicaogeralrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Alterar insumos nas composições | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/AlterarInsumoComposicoesGeralPesada`

**- Método com finalidade de alterar dados dos insumos na composição geral (para composições pesadas).**

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
Esquema: [`UAUApi.Models.Composicoes.InsumoComposicaoGeralPesadaRequest`](#uauapimodelscomposicoesinsumocomposicaogeralpesadarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Alterar insumos nas composições pesadas. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/AtualizarComposicoes`

**- Método com finalidade de atualizar dados das composições.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Utilize "" (vazio) caso queira limpar os campos do cadastro sendo que, código, descrição e unidade padrão, não podem ficar vazios.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Composicoes.ComposicoesAtualizacaoRequest`](#uauapimodelscomposicoescomposicoesatualizacaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Atualizar composições | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/ConsultarComposicoesComFiltroLivre`

**Consultar registros de composições gerais utilizando um filtro livre com qualquer um dos campos desta**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de negócio:
Permite consultar os registros de composições gerais utilizando um filtro livre com qualquer um dos campos existentes

Exemplo de filtro a ser utilizado: 
1. "filtro": "Cod_comp = '10.50'"
2. "filtro": "Descr_comp LIKE 'TERRAPLANAGEM%'" 
3. "filtro": "Cod_comp = '10.50' AND Descr_comp LIKE 'TERRAPLANAGEM%'" 
4. "filtro": "Cod_comp = '10.50' OR Descr_comp LIKE 'TERRAPLANAGEM%'"

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Composicoes.ComposicaoComFiltroRequest`](#uauapimodelscomposicoescomposicaocomfiltrorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Composicoes | array de [`UAUApi.Models.Composicoes.Composicoes`](#uauapimodelscomposicoescomposicoes) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/ConsultarComposicoesPorChave`

**- Método com finalidade de consultar dados das composições por chave.**

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
Esquema: [`UAUApi.Models.Composicoes.ComposicoesRequest`](#uauapimodelscomposicoescomposicoesrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar composições por chave | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/ConsultarComposicoesPorDescricao`

**Consultar a tabela Composicoes pela sua descrição**

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
Esquema: [`UAUApi.Models.Composicoes.ComposicaoRequest`](#uauapimodelscomposicoescomposicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Composicoes | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/ConsultarInsumosDaComposicao`

**- Método com finalidade de consultar os insumos para uma determinada composição.**

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
Esquema: [`UAUApi.Models.Composicoes.ComposicoesRequest`](#uauapimodelscomposicoescomposicoesrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Consultar insumos das composições. | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/ConsultarTodasComposicoes`

**Método responsável por retornar todas as composições gerais.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Composicoes todas as composições | object |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/InserirComposicoes`

**- Método com finalidade de inserir dados das composições.**

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
Esquema: [`UAUApi.Models.Composicoes.InserirComposicoesRequest`](#uauapimodelscomposicoesinserircomposicoesrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir composições | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/InserirInsumoComposicoesGeral`

**- Método com finalidade de inserir dados dos insumos na composição geral.
- Método com finalidade de inserir dados dos insumos na composição geral (composição civil).**

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
Esquema: [`UAUApi.Models.Composicoes.InsumoComposicaoGeralRequest`](#uauapimodelscomposicoesinsumocomposicaogeralrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir insumos nas composições | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Composicoes/InserirInsumoComposicoesGeralPesada`

**- Método com finalidade de inserir dados dos insumos na composição geral (para composições pesadas).**

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
Esquema: [`UAUApi.Models.Composicoes.InsumoComposicaoGeralPesadaRequest`](#uauapimodelscomposicoesinsumocomposicaogeralpesadarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Inserir insumo nas composições pesadas | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Composicoes.InserirComposicoesRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo` | string | ✓ | Código da composição |
| `descricao` | string | ✓ | Descrição da composição |
| `unidade` | string | ✓ | Unidade da composição |
| `prodEquipe` | number (double) | ✓ | Produção de equipe |
| `tipoCusto` | string | ✓ | Tipo de custo da composição, onde: D - Direto; I - Indireto |
| `civilPes` | integer (int32) | ✓ | Tipo da composição, onde: 0 - Civil; 1 - Pesada |
| `status` | integer (int32) |  | Status do insumo, onde: 0 - Ativo; 1 - Inativo |
| `categoria` | string |  | Categoria da composição |
| `categoriaMovFin` | string |  | Categoria de movimentação financeira. |
| `CAP` | string |  | O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP principal) |
| `CAPEstorno` | string |  | O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para estorno) |
| `CAPTransacaoFinanceira` | string |  | O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para transacao financeira) |
| `NCM` | string |  | Nomenclatura comum do MERCOSUL |
| `CEST` | string |  | Código Especificador da Substituição Tributária |
| `aplicacao` | string |  | Código da aplicação fiscal da composição |
| `codigoServicoFiscal` | string |  | Número do código de serviço fiscal |
| `controlaFVS` | boolean |  | Controle de ficha de verififação de serviço (FVS), onde: true - Controla; false - Não controla Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE Por tanto, ao informar um valor diferente de Zero sempre será gravado TRUE. |
| `confirmado` | integer (int32) |  | Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado |
| `porcQtdeExcedidaEntrega` | string |  | Percentual de tolerância para entregas com quantidade superior à que foi solicitada.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |
| `porcPrecoExcedidoEntrega` | string |  | Percentual de tolerância para entregas com preços superiores ao que foi solicitado.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |
| `porcPrecoReduzidoEntrega` | string |  | Percentual de tolerância para entregas com preços reduzidos ao que foi solicitado.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |

### UAUApi.Models.Composicoes.ComposicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `descricao` | string |  |  |

### UAUApi.Models.Composicoes.ComposicoesRequest

Obs&gt;: Para os campos que são possíveis de serem limpados, o parâmetro deve ser preenchido com "" (vazio) para que seja possível realizar esse tipo de atualização.

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigo` | string | ✓ | Código da composição |
| `descricao` | string |  | Descrição da composição |
| `unidade` | string |  | Unidade da composição |
| `status` | integer (int32) |  | Status do insumo, onde: 0 - Ativo; 1 - Inativo |
| `prodEquipe` | number (double) |  | Produção de equipe |
| `tipoCusto` | string |  | Tipo de custo da composição, onde: D - Direto; I - Indireto |
| `civilPes` | integer (int32) |  | Tipo da composição, onde: 0 - Civil; 1 - Pesada |
| `categoria` | string |  | Categoria da composição |
| `categoriaMovFin` | string |  | Categoria de movimentação financeira. |
| `CAP` | string |  | O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP principal) |
| `CAPEstorno` | string |  | O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para estorno) |
| `CAPTransacaoFinanceira` | string |  | O CAP é o que fará o link (ligação) das compras e pagamentos dos insumos referidos com a contabilidade (CAP para transacao financeira) |
| `NCM` | string |  | Nomenclatura comum do MERCOSUL |
| `CEST` | string |  | Código Especificador da Substituição Tributária |
| `aplicacao` | string |  | Código da aplicação fiscal da composição |
| `codigoServicoFiscal` | string |  | Número do código de serviço fiscal |
| `controlaFVS` | boolean |  | Controle de ficha de verififação de serviço (FVS), onde: true - Controla; false - Não controla Pela notação do tipo Boolean, qualquer outro valor diferente de Zero (0) é considerado TRUE Por tanto, ao informar um valor diferente de Zero sempre será gravado TRUE. |
| `confirmado` | integer (int32) |  | Status de confirmação do insumo, onde: 0 - Pendente/Não confirmado; 1 - Confirmado |
| `porcQtdeExcedidaEntrega` | string |  | Percentual de tolerância para entregas com quantidade superior à que foi solicitada.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |
| `porcPrecoExcedidoEntrega` | string |  | Percentual de tolerância para entregas com preços superiores ao que foi solicitado.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |
| `porcPrecoReduzidoEntrega` | string |  | Percentual de tolerância para entregas com preços reduzidos ao que foi solicitado.  Informe valores de 0 à 100 ou vazio para deixar de utilizar a configuração. |

### UAUApi.Models.Composicoes.Composicoes

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Cod_comp` | string |  | Código da composição |
| `Descr_comp` | string |  | Descrição da composição |
| `Unid_comp` | string |  | Identificador da unidade da composição |
| `Prod_comp` | number (double) |  | Indicador da produção de equipe da composição |
| `Custo_comp` | string |  | Identificador do tipo de custo da composição, onde: D - Direto; I - Indireto |
| `Status_comp` | integer (int32) |  | Situação da composição, onde: 0 - Pendente; 1 - Confirmado |
| `UsrCad_comp` | string |  | Login do usuário quem cadastrou a composição |
| `NomeUsuarioCadastrou` | string |  | Nome do usuário quem cadastrou a composição |
| `CivilPes_comp` | integer (int32) |  | Indicador do tipo da composição, onde: 0 - Civil; 1 - Pesada |
| `AtInat_comp` | integer (int32) |  | Status da compsição, onde: 0 - Ativa; 1 - Inativa |
| `DataCad_comp` | string (date-time) |  | Data de cadastro da composição. Formato MM/DD/YYYY |
| `UsrAlt_comp` | string |  | Login do usuário quem alterou a composição por último |
| `nomeUsuarioAlterou` | string |  | Nome do usuário quem alterou a composição por último |
| `DataAlt_comp` | string (date-time) |  | Data da última alteração da composição |
| `Anexos_Comp` | integer (int32) |  | Indicador de vínculo de anexo à composição |
| `Categ_comp` | string |  | Categoria da composição |
| `DescricaoCategoriaComposicao` | string |  | Descrição da categoria da composição |
| `Cap_Comp` | string |  | CAP da composição |
| `DescricaoCAP` | string |  | Descrição do CAP da composição |
| `NCM_comp` | string |  | NCM (Nomenclatura comum do MERCOSUL) da composição |
| `DescricaoNCM` | string |  | Descrição do NCM da composição |
| `CapEstorno_comp` | string |  | CAP para estorno da composição |
| `DescricaoCAPEstorno` | string |  | Descrição do CAP para estorno da composição |
| `NumApi_comp` | integer (int32) |  | Código da aplicação fiscal |
| `DescricaoAplicacaoFiscal` | string |  | Descrição da aplicação fiscal |
| `NumCsf_comp` | integer (int32) |  | Número do código de serviço fiscal vinculado à composição |
| `DescricaoServicoFiscal` | string |  | Descrição do código de serviço fiscal vinculado à composição |
| `CEST_comp` | string |  | Identificador do CEST (código especificador da substituição tributária) |
| `CapTransacaoFin_comp` | string |  | Identificador do CAP para transação financeira |
| `CategMovFin_comp` | string |  | Identificador da categoria de movimentação financeira |
| `DescricaoCategoriaMovFinanceira` | string |  | Descrição da categoria de movimentação financeira |

### UAUApi.Models.Composicoes.ComposicaoComFiltroRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `filtro` | string |  |  |

### UAUApi.Models.Composicoes.ComposicoesAtualizacaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `listaComposicoesAtualizar` | array de [`UAUApi.Models.Composicoes.ComposicoesRequest`](#uauapimodelscomposicoescomposicoesrequest) |  | Lista dos insumos gerais para atualização dos dados. |

### UAUApi.Models.Composicoes.InsumoComposicaoGeralPesadaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codComposicao` | string |  |  |
| `codInsumo` | string |  |  |
| `tipoItem` | integer (int32) |  |  |
| `coeficiente` | number (double) |  |  |
| `preco` | number (double) |  |  |
| `coefProd` | number (double) |  |  |
| `coefImProd` | number (double) |  |  |
| `dMT` | number (double) |  |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Composicoes.InsumoComposicaoGeralRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codComposicao` | string |  |  |
| `codInsumo` | string |  |  |
| `tipoItem` | integer (int32) |  |  |
| `coeficiente` | number (double) |  |  |
| `preco` | number (double) |  |  |
