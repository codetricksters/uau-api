# Espelho

## POST `/api/v{version}/Espelho/AlterarDataEntregaChavesUnidade`

**Alterar a data de entrega das chaves da unidade**

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
Esquema: [`UAUApi.Models.Espelho.AlterarDataEntregaChavesRequest`](#uauapimodelsespelhoalterardataentregachavesrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Espelho/AlterarStatusUnidade`

**Atualizar unidade personalizada do produto**

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
Esquema: [`UAUApi.Models.Espelho.AlterarUnidadePersonalizadaRequest`](#uauapimodelsespelhoalterarunidadepersonalizadarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Espelho/AtualizarCamposCustomizados`

**Rotina responsável por atualizar campos customizados**

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
Esquema: [`UAUApi.Models.Espelho.AtualizarCamposCustomizadosRequest`](#uauapimodelsespelhoatualizarcamposcustomizadosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Espelho/BuscaUnidadesDeAcordoComWhere`

**Rotina responsável por buscar os dados das unidades de acordo com o WHERE passado por parâmetro.**

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
Esquema: [`UAUApi.Models.Espelho.BuscaUnidadesDeAcordoComWhereRequest`](#uauapimodelsespelhobuscaunidadesdeacordocomwhererequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Espelho/BuscaUnidadesDeAcordoComWhereDetalhado`

**Consultar unidades de aacordo com o "where" informado**

- parâmetros de request da classe BuscaUnidadesDeAcordoComWhereDetalhadoRequest

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Espelho.BuscaUnidadesDeAcordoComWhereDetalhadoRequest`](#uauapimodelsespelhobuscaunidadesdeacordocomwheredetalhadorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | object |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Espelho/ConsultarEspelhosVenda`

**Consulta espelhos de venda as empresas que o usuário tem permissão.**

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
Esquema: [`UAUApi.Models.Espelho.ConsultarEspelhosVendaRequest`](#uauapimodelsespelhoconsultarespelhosvendarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Espelho/ConsultarPersonalizacoesComPrecos`

**Consulta uma personalização com preços.**

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
Esquema: [`UAUApi.Models.Espelho.ConsultarPersonalizacoesComPrecosRequest`](#uauapimodelsespelhoconsultarpersonalizacoescomprecosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Espelho/ConsultarUnidadePerPorChave`

**Consultar unidade personalizada do produto**

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
Esquema: [`UAUApi.Models.Espelho.UnidadePersonalizadaProdutoRequest`](#uauapimodelsespelhounidadepersonalizadaprodutorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Espelho.Espelho.UnidadePersonalizada`](#uauapimodelsespelhoespelhounidadepersonalizada) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de pendência. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Espelho/RetornarMenorPrecoPerson`

**Busca o valor do menor preço que pode ser inserido em um produto.**

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
Esquema: [`UAUApi.Models.Espelho.RetornarMenorPrecoPersonRequest`](#uauapimodelsespelhoretornarmenorprecopersonrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Menor preço personalização | number (double) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Espelho.RetornarMenorPrecoPersonRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tipoContrato` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5 |  | tipo de contrato  0 - Venda, 1 - Aluguel, 2 - PropostaVenda, 3 - MedicaoContratoVenda, 4 - Revenda, 5 - Todos |
| `codProduto` | integer (int32) |  | código do produto |
| `codCategPreco` | string |  | código da categoria de preço |
| `numeroPerson` | integer (int32) |  | número da personalização |
| `empresa` | integer (int32) |  | código da empresa |
| `dataCategPrecoProduto` | string (date-time) |  | data de cadastro da categoria de preço do produto |
| `porcPrecoMinimo` | number (double) |  | Porcentagem do preço mínimo |

### UAUApi.Models.Espelho.Espelho.UnidadePersonalizada

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresaPersonalizacao` | integer (int32) |  | Codigo da emrpesa da unidade personalizada |
| `produtoPersonalizacao` | integer (int32) |  | Codigo do produto da unidade personalizada |
| `numeroPersonalizacao` | integer (int32) |  | Numero da unidade personalizada |
| `obraPersonalizacao` | string |  | Codigo da obra da unidade personalizada |
| `quantidadePersonalizacao` | number (double) |  | Quantidade da unidade personalizada |
| `Vendido` | integer (int32) |  | Estágio da unidade personalizada |
| `codigoPersonalizacao` | string |  | Codigo da unidade personalizada |
| `porcentagemPersonalizacao` | number (double) |  | Percentual da unidade personalizada |
| `campoPersonalizado1` | string |  | Campo personalizado 1 da unidade personalizada |
| `campoPersonalizado2` | string |  | Campo personalizado 2 da unidade personalizada |
| `campoPersonalizado3` | string |  | Campo personalizado 3 da unidade personalizada |
| `campoPersonalizado4` | string |  | Campo personalizado 4 da unidade personalizada |
| `campoPersonalizado5` | string |  | Campo personalizado 5 da unidade personalizada |
| `campoPersonalizado6` | string |  | Campo personalizado 6 da unidade personalizada |
| `campoPersonalizado7` | string |  | Campo personalizado 7 da unidade personalizada |
| `campoPersonalizado8` | string |  | Campo personalizado 8 da unidade personalizada |
| `campoPersonalizado9` | string |  | Campo personalizado 9 da unidade personalizada |
| `campoPersonalizado10` | string |  | Campo personalizado 10 da unidade personalizada |
| `campoPersonalizado11` | string |  | Campo personalizado 11 da unidade personalizada |
| `campoPersonalizado12` | string |  | Campo personalizado 12 da unidade personalizada |
| `campoPersonalizado13` | string |  | Campo personalizado 13 da unidade personalizada |
| `campoPersonalizado14` | string |  | Campo personalizado 14 da unidade personalizada |
| `campoPersonalizado15` | string |  | Campo personalizado 15 da unidade personalizada |
| `campoPersonalizado16` | string |  | Campo personalizado 16 da unidade personalizada |
| `campoPersonalizado17` | string |  | Campo personalizado 17 da unidade personalizada |
| `campoPersonalizado18` | string |  | Campo personalizado 18 da unidade personalizada |
| `campoPersonalizado19` | string |  | Campo personalizado 19 da unidade personalizada |
| `campoPersonalizado20` | string |  | Campo personalizado 20 da unidade personalizada |
| `campoPersonalizado21` | string |  | Campo personalizado 21 da unidade personalizada |
| `campoPersonalizado22` | string |  | Campo personalizado 22 da unidade personalizada |
| `campoPersonalizado23` | string |  | Campo personalizado 23 da unidade personalizada |
| `campoPersonalizado24` | string |  | Campo personalizado 24 da unidade personalizada |
| `campoPersonalizado25` | string |  | Campo personalizado 25 da unidade personalizada |
| `campoPersonalizado26` | string |  | Campo personalizado 26 da unidade personalizada |
| `campoPersonalizado27` | string |  | Campo personalizado 27 da unidade personalizada |
| `campoPersonalizado28` | string |  | Campo personalizado 28 da unidade personalizada |
| `campoPersonalizado29` | string |  | Campo personalizado 29 da unidade personalizada |
| `campoPersonalizado30` | string |  | Campo personalizado 30 da unidade personalizada |
| `campoPersonalizado31` | string |  | Campo personalizado 31 da unidade personalizada |
| `campoPersonalizado32` | string |  | Campo personalizado 32 da unidade personalizada |
| `campoPersonalizado33` | string |  | Campo personalizado 33 da unidade personalizada |
| `campoPersonalizado34` | string |  | Campo personalizado 34 da unidade personalizada |
| `campoPersonalizado35` | string |  | Campo personalizado 35 da unidade personalizada |
| `campoPersonalizado36` | string |  | Campo personalizado 36 da unidade personalizada |
| `campoPersonalizado37` | string |  | Campo personalizado 37 da unidade personalizada |
| `campoPersonalizado38` | string |  | Campo personalizado 38 da unidade personalizada |
| `campoPersonalizado39` | string |  | Campo personalizado 39 da unidade personalizada |
| `campoPersonalizado40` | string |  | Campo personalizado 40 da unidade personalizada |
| `campoPersonalizado41` | string |  | Campo personalizado 41 da unidade personalizada |
| `campoPersonalizado42` | string |  | Campo personalizado 42 da unidade personalizada |
| `campoPersonalizado43` | string |  | Campo personalizado 43 da unidade personalizada |
| `campoPersonalizado44` | string |  | Campo personalizado 44 da unidade personalizada |
| `campoPersonalizado45` | string |  | Campo personalizado 45 da unidade personalizada |
| `Anexos` | integer (int32) |  | Anexos da unidade personalizada |
| `Identificador` | string |  | Identificador da unidade personalizada |
| `usuarioCadastrou` | string |  | Usuario que cadastrou a unidade personalizada |
| `dataCadastro` | string (date-time) |  | Data de cadastro da unidade personalizada |
| `valorPreco` | number (double) |  | Valor da unidade personalizada |
| `fracaoIdeal` | number (double) |  | Fração ideal da unidade personalizada |
| `numeroObjeto` | integer (int32) |  | Numero do objeto da unidade personalizada |
| `objetoEspelhoTop` | integer (int32) |  | Objeto espelho cima da unidade personalizada |
| `objetoEspelhoLeft` | integer (int32) |  | Objeto espelho esquerda da unidade personalizada |
| `porcentagemComissao` | number (double) |  | Percentual da comissão da unidade personalizada |
| `codigoTipoProduto` | string |  | Codigodo tipo de produto da unidade personalizada |
| `numeroCategoriaStatus` | integer (int32) |  | Numero da categoria da unidade personalizada |
| `dataEntregaChaves` | string (date-time) |  | Data da entrega das chaves da unidade personalizada |

### UAUApi.Models.Espelho.UnidadePersonalizadaProdutoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Codigo da empresa do produto personalizado |
| `codigoProduto` | integer (int32) |  | Codigo do produto personalizado |
| `numeroPersonalizacao` | integer (int32) |  | Numero da personalização do produto |

### UAUApi.Models.Espelho.ConsultarPersonalizacoesComPrecosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario` | string |  | Usuário |
| `empresa` | integer (int32) |  | Código da empresa |
| `num_produto` | integer (int32) |  | Número do produto |
| `cod_obra` | string |  | Código da obra |
| `num_personalizacao` | integer (int32) |  | Número da personalização |
| `consultarapenasnao_vendidos` | boolean |  |  |
| `tipo_contrato` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5 |  | Tipo de contrato |
| `datatabela_preco` | string (date-time) |  | Tabela de preço |
| `campos_person` | string |  | Campos da personalização |
| `status_person` | string |  | Status da personalização |
| `num_espelho` | integer (int32) |  | Número do espelho |
| `tipocontrato_grafico` | integer (int32) — valores possíveis: 0, 1, 2 |  | Filtro tipo de contrato - gráfico estatístico |

### UAUApi.Models.Espelho.ConsultarEspelhosVendaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `usuario_logado` | string |  |  |

### UAUApi.Models.Espelho.BuscaUnidadesDeAcordoComWhereDetalhadoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `where` | string | ✓ | Cláusula Where |
| `retorna_venda` | boolean |  |  |
| `data_tabela_preco` | string (date-time) | ✓ | Data da tabela de Preço |

### UAUApi.Models.Espelho.BuscaUnidadesDeAcordoComWhereRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `where` | string |  |  |
| `retorna_venda` | boolean |  |  |

### UAUApi.Models.Espelho.AtualizarCamposCustomizadosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `campos_custom` | [`UAUApi.Models.Espelho.CamposCustom`](#uauapimodelsespelhocamposcustom) |  | Objeto que contém as informações necessárias para atualizar os campos customizados |

### UAUApi.Models.Espelho.CamposCustom

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ListChavesUnid` | array de [`UAUApi.Models.Espelho.ListChavesUnid`](#uauapimodelsespelholistchavesunid) |  |  |
| `ListValoresUnid` | array de [`UAUApi.Models.Espelho.ListValoresUnid`](#uauapimodelsespelholistvaloresunid) |  |  |

### UAUApi.Models.Espelho.ListValoresUnid

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoCustom` | string |  |  |
| `CampoCustomValor` | string |  |  |

### UAUApi.Models.Espelho.ListChavesUnid

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  |  |
| `Obra` | string |  |  |
| `Produto` | integer (int32) |  |  |
| `CodPerson` | integer (int32) |  |  |

### UAUApi.Models.Espelho.AlterarUnidadePersonalizadaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Codigo da empresa do produto personalizado |
| `codigoProduto` | integer (int32) |  | Codigo do produto personalizado |
| `numeroPersonalizacao` | integer (int32) |  | Numero da personalização do produto |
| `novoStatusUnidade` | integer (int32) |  | Novo status que será alterada a unidade de personalização Apenas 0 - Disponível         7 - Suspenso        8  - Fora de venda        10 - Dação. |
| `motivoAlteracao` | string |  | Motivo da alteração do status da unidade de personalização |
| `categoriaStatusPersonalizacao` | integer (int32) |  | Categoria do status da unidade de personalização. |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Espelho.AlterarDataEntregaChavesRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) |  | Codigo da empresa do produto personalizado |
| `codigoProduto` | integer (int32) |  | Codigo do produto personalizado |
| `numeroPersonalizacao` | integer (int32) |  | Numero da personalização do produto |
| `dataEntregaChaves` | string (date-time) |  | Data de entrega das chaves |
| `observacao` | string |  | Observação para a alteração da data de entrega das chaves |
