# RotinasGerais

## POST `/api/v{version}/RotinasGerais/BuscaCAPVendaEmpresa`

**Consulta e detalha as configurações de CAPs de determinada empresa.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Irá retornar as configurações de CAPs de uma determinada empresa.
2. Existem dois estados para o request:
    1. Caso o request seja nulo, irá retornar todas as configurações de CAPs existentes no sistema.
    2. Caso seja determinado um número de empresa, irá retornar as configurações de CAPs dessa empresa.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.RotinasGerais.BuscaCAPVendaEmpresaRequest`](#uauapimodelsrotinasgeraisbuscacapvendaempresarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.RotinasGerais.ConfigCap`](#uauapimodelsrotinasgeraisconfigcap) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/BuscaCamposPerson`

**Busca campos personalizados de uma empresa e produto**

Definição Técnica:

1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:

1. Consulta campos personalizados de empresa e produto.
2. Valida permissão de consulta (2) para o usuário autenticado

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.RotinasGerais.BuscaCamposPersonRequest`](#uauapimodelsrotinasgeraisbuscacampospersonrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/BuscarCategoriasDeProduto`

**Retornar a lista de categorias de produto ativos**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Consulta a lista de categorias de produtos com status ativos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Comp.CategoriaDeProdutoDTO`](#globaltecuaucompcategoriadeprodutodto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/BuscarFinalidadesDeCompra`

**Retornar com finalidades de compra ativas**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Este endpoint não necessita de parâmetros no request.

Definição de Negócio:
1. Consulta a lista de finalidades para compras com status ativo.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Comp.FinalidadeDeCompraDTO`](#globaltecuaucompfinalidadedecompradto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/BuscarIndicesDeReajuste`

**Retornar a lista de índices de reajuste ativos**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Busca a lista de índices de reajuste ativos do sistema

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Comp.IndiceDTO`](#globaltecuaucompindicedto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/BuscarTiposDeVencimento`

**Consulta os tipos de vencimento ativos**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Possibilita consultar os tipo de vencimento que estão ativos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Comp.TipoDeVecimentoDTO`](#globaltecuaucomptipodevecimentodto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/BuscarVeiculosDeDivulgacao`

**Retornar veículos de divulgação ativos**

<returns>Lista de Veículos de divulgação.</returns>
 Definição Técnica:
 1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
 2. Preencher os parâmetros de request para uso do método.
 
 Definição de Negócio:
 1. Consulta veículos de divulgação que estão ativos.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`Globaltec.UAU.Comp.VeiculoDeDivulgacaoDTO`](#globaltecuaucompveiculodedivulgacaodto) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/ConsultarPadroesCobranca`

**Consultar os padrões de cobrança disponíveis**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. O único campo obrigatório do request é o Status.
2. Irá retornar os padrões de cobrança de acordo com o(s) filtro(s).
3. As informações personalizadas da cobrança virão como Configuracao_01 até a Configuracao_08.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.RotinasGerais.ConsultarPadroesCobrancaRequest`](#uauapimodelsrotinasgeraisconsultarpadroescobrancarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | array de [`UAUApi.Models.RotinasGerais.PadroesDeCobranca`](#uauapimodelsrotinasgeraispadroesdecobranca) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/ConsultarParamConsultaGeral`

**Consutar parâmetros necessários e seus atributos da ConsultaGeral**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher json do request com o devido Id e se é personalizado ou não (0 ou 1) sendo considerados como interno e externo respectivamente
3. Retorna uma lista de parâmetros dinâmicos, apresentando o nome do parâmetro e sua descrição, se ele é restrito, multiseleção e OrigemDados
com pressuposição do uso dessas informações em "ExecutarConsultaGeral

Definição de Negócio:

1. Permite visualizar o padrão de parâmetros da ConsultaGeral informada de forma detalhada
2. Valida permissão de consulta (2) para o usuário autenticado

 VirtUau:

- https://ajuda.globaltec.com.br/virtuau/consultas-gerais/

 Exemplo:
 
- Json request: 

{
"Id": "1",
"Personalizado": "0",
"Parameters":["P01", "1"]
}

"Personalizado": 1 - True / 0 - False

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.APIs.RotinasGerais.ConsultaGeralResquest`](#uauapiapisrotinasgeraisconsultageralresquest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.APIs.RotinasGerais.ConsultarParamConsultaGeral`](#uauapiapisrotinasgeraisconsultarparamconsultageral) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/ExecutarConsultaGeral`

**Executa query armazenada**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher json do request com o devido Id e se é personalizado ou não (0 ou 1) sendo considerados como interno e externo respectivamente

Definição de Negócio:
1. Consulta campos personalizados de empresa e produto.
2. Valida permissão de consulta (2) para o usuário autenticado 
3. Os parâmetros de cada consulta geral podem ser consultados através da rota RotinasGerais/ConsultarParamConsultaGeral
4. Retorna valores dinâmicos da respectiva query armazenada como ConsultaGeral.

Deve ser enviado o ID da ConsultaGeral e seus respectivos parâmetros, sendo o preenchimento da propriedade Parameters,
um array de string, e se necessário notações sql que atribuem características de tipagem. Por exemplo, apóstrofo entre uma string, considerando que 
em situações que usam um inteiro, podem funcionar com apóstrofo ou sem, mas em cláusulas como IN(params), 
o uso de apóstrofo pode gerar um erro, e ainda para atribuir uma lista de inteiros nesta, deve ser usado a vírgula.
Seguindo esta padrão comum,   "Parameters":["Nome do parâmetro", "Valor do parâmetro", "Nome do segundo parâmetro", "valor do segundo parâmetro"]

Apóstrofo = '

Datas devem ser acompanhadas de Apóstrofo, exceto em ocasiões especiais que devem ser analisadas na query, sendo
um destes, o uso da cláusula IN

Exemplo formato json da body

{
"Id": "1",
"Personalizado": "0",
"Parameters":["P01", "1"]
}

{
 "Id": "2",
 "Personalizado": "0",
 "Parameters":["EmpresaObra", " '1|1' ", "Status", "1"]
}

"Personalizado": 1 - True / 0 - False

VirtUau:

- https://ajuda.globaltec.com.br/virtuau/consultas-gerais/

 Anexos:
 
- Exemplo Postman json request:

<a href="http://www.globaltec.com.br/wp-content/uploads/2019/09/ExecutarConsultaGeral.postman_collection.zip">ExecutarConsultaGeral</a>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.APIs.RotinasGerais.RotinasGeraisController.ConsultarParamConsultaGeralRequest`](#uauapiapisrotinasgeraisrotinasgeraiscontrollerconsultarparamconsultageralrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.APIs.RotinasGerais.RotinasGeraisController.ConsultarParamConsultaGeralRequest`](#uauapiapisrotinasgeraisrotinasgeraiscontrollerconsultarparamconsultageralrequest) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RotinasGerais/InserirConsultaGeral`

**Inserir consulta geral**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

A Globaltec não se responsabiliza:
1. Pela compatibilidade entre as alterações do banco de dados e as consultas personalizadas efetuadas pelos clientes.
2. Pelos dados informados nos geradores de resultado que utilizam consultas personalizadas criadas pelos clientes.

Definição de Negócio:

1. Irá realizar a inserção da consulta geral.
2. Será necessario permissão de INCLUSÃO no programa GECONSGER.
  
VirtUau:
- https://ajuda.globaltec.com.br/virtuau/como-realizar-o-cadastro-de-consultas-gerais/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.RotinasGerais.ConsultaGeralRequest`](#uauapimodelsrotinasgeraisconsultageralrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | integer (int32) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.RotinasGerais.ConsultaGeralRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ClausulaSql` | string | ✓ | Clausula SQL |
| `Descricao` | string | ✓ | Descrição da consulta |
| `CodigoPasta` | string | ✓ | Código da pasta |
| `Status` | integer (int32) | ✓ | Status da consulta [0 - Ativo, 1 - Inativo] |
| `Parametros` | array de [`UAUApi.Models.RotinasGerais.Parametros`](#uauapimodelsrotinasgeraisparametros) |  | Lista de parâmetros |

### UAUApi.Models.RotinasGerais.Parametros

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Parametro` | string | ✓ | Nome do parâmetro |
| `Descricao` | string | ✓ | Descrição do parâmetro |
| `Tipo` | integer (int32) | ✓ | Tipo do parâmetro |
| `Origem` | integer (int32) | ✓ | Origem dos dados |
| `Restrito` | integer (int32) | ✓ | Define se o parâmetro é restrito [0 - Não, 1 - Sim] |
| `MultiSelecao` | integer (int32) | ✓ | Define se o parâmetro é multiseleção [0 - Não, 1 - Sim] |
| `Valor` | string |  | Define o valor do parâmetro O valor é utilizado para testar o parâmetro incluído, o mesmo não é salvo no banco de dados |

### UAUApi.APIs.RotinasGerais.RotinasGeraisController.ConsultarParamConsultaGeralRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Personalizado` | integer (int32) |  |  |
| `Parameters` | array de string |  |  |

### UAUApi.APIs.RotinasGerais.ConsultarParamConsultaGeral

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Table` | array de [`UAUApi.APIs.RotinasGerais.Table`](#uauapiapisrotinasgeraistable) |  |  |

### UAUApi.APIs.RotinasGerais.Table

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Restrito` | object |  |  |
| `Descricao` | string |  |  |
| `Tipo` | object |  |  |
| `MultiSelecao` | object |  |  |
| `Parametro` | string |  |  |

### UAUApi.APIs.RotinasGerais.ConsultaGeralResquest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Id` | integer (int32) |  |  |
| `Personalizado` | integer (int32) |  |  |

### UAUApi.Models.RotinasGerais.PadroesDeCobranca

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa |
| `DescricaoEmpresa` | string |  | Descrição da empresa |
| `NumeroPadrao` | integer (int32) |  | Número do padrão de cobrança |
| `DescricaoPadrão` | string |  | Descrição do padrão de cobrança |
| `Banco` | integer (int32) |  | Número do banco |
| `DescricaoBanco` | string |  | Descrição do banco |
| `Conta` | string |  | Conta de cobrança |
| `DescricaoConta` | string |  | Descrição da conta de cobrança |
| `StatusPadrao` | integer (int32) — valores possíveis: 0, 1, 2 |  | Status do padrão de cobrança [0 - Ativo, 1 - Inativo] |
| `TipoCobranca` | integer (int32) |  | Tipo de cobrança |
| `DescricaoTipoCobranca` | string |  | Descrição do tipo de cobrança |
| `Carteira` | string |  | Carteira do padrão de cobrança |
| `CobrancaCompartilhada` | boolean |  | Se irá utilizar cobrança compartilhada TRUE - Irá utilizar FALSE - Não irá utilizar |
| `Configuracao_01` | string |  | Configuração 01 |
| `Configuracao_02` | string |  | Configuração 02 |
| `Configuracao_03` | string |  | Configuração 03 |
| `Configuracao_04` | string |  | Configuração 04 |
| `Configuracao_05` | string |  | Configuração 05 |
| `Configuracao_06` | string |  | Configuração 06 |
| `Configuracao_07` | string |  | Configuração 07 |
| `Configuracao_08` | string |  | Configuração 08 |
| `GeraArqAuxComMensagem` | boolean |  | Se irá gerar arquivo auxiliar com mensagem TRUE - Irá gerar FALSE - Não irá gerar |
| `ImprimeBoleto` | boolean |  | Se irá imprimir o boleto TRUE - Irá imprimir FALSE - Não irá imprimir |
| `UsuarioCadastro` | string |  | Usuário que realizou o cadastro |
| `DataCadastro` | string (date-time) |  | Data de cadastro do padrão de cobrança |
| `NumMensagemImpressaPeloBanco` | integer (int32) |  | Número da mensagem do boleto enviada para banco |
| `NumMensagemImpressaPeloUAU` | integer (int32) |  | Número da mensagem do boleto impressa pelo UAU |
| `EmpresaEnviadaNoArqDeRemessa` | integer (int32) |  | Número da empresa enviada no arquivo de remessa |
| `CedenteRemessa` | string |  | Cedente alterado para |

### UAUApi.Models.RotinasGerais.ConsultarPadroesCobrancaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa |
| `Status` | integer (int32) — valores possíveis: 0, 1, 2 | ✓ | Status do padrão de cobrança [0 - Ativo, 1 - Inativo, 2 - Ambos] |
| `Banco` | integer (int32) |  | Número do banco |

### Globaltec.UAU.Comp.VeiculoDeDivulgacaoDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  |  |
| `Descricao` | string |  |  |

### Globaltec.UAU.Comp.TipoDeVecimentoDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |

### Globaltec.UAU.Comp.IndiceDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |
| `Tipo` | integer (int32) |  |  |

### Globaltec.UAU.Comp.FinalidadeDeCompraDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  |  |
| `Descricao` | string |  |  |

### Globaltec.UAU.Comp.CategoriaDeProdutoDTO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | string |  |  |
| `Descricao` | string |  |  |

### UAUApi.Models.RotinasGerais.BuscaCamposPersonRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | string | ✓ | Código da empresa |
| `produto` | string | ✓ | Código do produto |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.RotinasGerais.ConfigCap

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Código da empresa |
| `codigoConfig` | integer (int32) |  | Código da configuração de CAP |
| `descricaoConfigCAP` | string |  | Descrição da configuração de CAP |
| `padrao` | boolean |  | Define se a configuração é Padrão ou não:     1. True: Padrão     2. False: Não é padrão |
| `tipoParcelaPadrao` | string |  | Tipo de parcelamento padrão da configuração de CAP |
| `CAPS` | [`UAUApi.Models.RotinasGerais.CapsPadrao`](#uauapimodelsrotinasgeraiscapspadrao) |  | Lista de CAPs definidos dentro da configuração padrão |

### UAUApi.Models.RotinasGerais.CapsPadrao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `principal` | string |  |  |
| `jurosContratual` | string |  |  |
| `correcao` | string |  |  |
| `multaAtraso` | string |  |  |
| `JurosAtraso` | string |  |  |
| `Acrescimo` | string |  |  |
| `desconto` | string |  |  |
| `correcaoAtraso` | string |  |  |
| `descontoAntecipacao` | string |  |  |
| `taxaBoleto` | string |  |  |
| `almoxarifadoCentral` | string |  |  |
| `custasAdministracao` | string |  |  |
| `descontoCusta` | string |  |  |
| `provisaoCurtoPrazo` | string |  |  |
| `provisaoLongoPrazo` | string |  |  |
| `Repasse` | string |  |  |
| `baixaProvisaoCurtoPrazo` | string |  |  |
| `baixaProvisaoLongoPrazo` | string |  |  |
| `descontoCondicional` | string |  |  |
| `taxaAdministracao` | string |  |  |

### UAUApi.Models.RotinasGerais.BuscaCAPVendaEmpresaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoEmpresa` | integer (int32) |  | Código da Empresa |
