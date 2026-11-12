# Comissao

## POST `/api/v{version}/Comissao/AtualizarStatusComissao`

**Atualizar status de pagamento da comissão.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Alterar os status de pagamento das comissões de uma pessoa(beneficiário).
2. Não é possível cancelar ou reativar status de pagamento da comissão via Endpoint.
3. Todos os campos são obrigatórios informar.
4. Os dados informados passam por validações.
5. Não é permitido marcar como "pago" comissões que geram processos de pagamento
6. Não é permitido reativar ou cancelar status de pagamento da comissão.
7. Status disponíveis:
    - 0 - Não liberada
    - 1 - Liberada
    - 2 - Paga
    - 4 - Bloqueada

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: array de [`UAUApi.Models.Comissao.AtualizarStatusComissaoRequest`](#uauapimodelscomissaoatualizarstatuscomissaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Controle de status da comissão |  |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Comissao/ConsultarEstruturaComissao`

**Consulta a estrutura de comissão do vendedor**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta a estrutura de comissão do vendedor.
2. A propriedade SobreRecebimento está descontinuada, mas continuará retornando as informações nela conforme o preenchimento da nova propriedade, chamada RegraLiberacao.
3. A propriedade codigo da hierarquia se tornou obsoleta, precisamos apenas do número da comissão que é um número único no sistema.
4. A propriedade numModelo é referente a nova estrutura de modelos de comissão.
5. Caso seja informado uma pessoa que não participa do modelo de comissão, o sistema não irá montar a estrutura;

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Comissao.ConsultarEstruturaComissaoRequest`](#uauapimodelscomissaoconsultarestruturacomissaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Estrutura de comissao | array de [`UAUApi.Models.Comissao.EstruturaComissao`](#uauapimodelscomissaoestruturacomissao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Comissao/ConsultarModeloComissao`

**Consulta os Modelos de Comissão disponíveis**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario;
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta o Modelo de Comissão disponível para utilização em uma proposta de venda.

Informação:
1. A propriedade "Padrão" no retorno indica o modelo de comissão padrão utilizado pelo vendedor, no entanto, ela será retornada como True.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Comissao.ConsultarModeloComissaoRequest`](#uauapimodelscomissaoconsultarmodelocomissaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Modelo Comissao | array de [`UAUApi.Models.Comissao.ModeloComissao`](#uauapimodelscomissaomodelocomissao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Comissao/ConsultarVendedores`

**Consulta os vendedores da estrutura de comissão.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario;
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta os vendedores da estrutura de comissão;
2. Caso não seja informado o código da comissão retornará todos os vendedores relacionados à estrutura de comissão;
3. Caso seja informado um código que não esteja relacionado a estrutura de comissão o sistema retornará "vazio".

Informação:
1. Cuidado ao alterar, compartilhar e/ou distribuir informações pessoais do cliente, fornecedor, funcionário e/ou prospect, considere avaliar se o processo que esta realizando esta de acordo com os termos da Lei geral de proteção de dados LGPD (N.13.709).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Comissao.ConsultaVendedorRequest`](#uauapimodelscomissaoconsultavendedorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.Comissao.ConsultaVendedor`](#uauapimodelscomissaoconsultavendedor) |
| 400 | Verifique se a condição para realizar a consulta está correta. - Os campos string devem conter as aspas simples. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Comissao.ConsultaVendedor

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoVendedor` | integer (int32) |  | Código do vendedor |
| `nomeVendedor` | string |  | Nome do vendedor |
| `cpf` | string |  | CPF/CNPJ do Vendedor |

### UAUApi.Models.Comissao.ConsultaVendedorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoModeloComissao` | integer (int32) |  | Código do modelo de comissão |

### UAUApi.Models.Comissao.ModeloComissao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoComissao` | integer (int32) |  | Código do modelo de comissão |
| `descricaoComissao` | string |  | Descrição do modelo de comissão |
| `padrao` | boolean |  | Sinalizar qual o modelo de comissão padrão/prioritário para o vendedor |

### UAUApi.Models.Comissao.ConsultarModeloComissaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) | ✓ | Código da empresa |
| `codigoObra` | string | ✓ | Código da Obra |
| `codigoVendedor` | integer (int32) |  | Código do Vendedor |
| `dataVenda` | string |  | Data da Venda |
| `qtdeParcelas` | integer (int32) |  | Quantidade de Parcelas |
| `listaUnidades` | array de [`UAUApi.Models.Comissao.ListaUnidades`](#uauapimodelscomissaolistaunidades) |  | Lista de Unidades |

### UAUApi.Models.Comissao.ListaUnidades

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoProduto` | integer (int32) | ✓ | Codigo do Produto |
| `codigoPersonalizacao` | integer (int32) |  | Código da Personalização |

### UAUApi.Models.Comissao.EstruturaComissao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroControle` | integer (int32) |  | Número de controle |
| `codigoPessoa` | integer (int32) |  | Código da pessoa |
| `nomePessoa` | string |  | Nome da pessoa |
| `codigoCargo` | string |  | Código do cargo |
| `descricaoCargo` | string |  | Descrição do cargo |
| `porcentual` | number (double) |  | Porcentual |
| `valorComissao` | number (double) |  | Valor |
| `pagamentoDireto` | boolean |  | Aceita pagamento direto |
| `tipoLancamento` | integer (int32) |  | Tipo de lançamento |
| `sobreRecebimento` | boolean |  | Sobre o recebimento |
| `regraLiberacao` | boolean |  | regra de liberação |
| `geraProcessoPgto` | boolean |  | Gerar processo de pagamento |
| `pertenceEstrutura` | boolean |  | Pertence a estrutura |
| `captador` | boolean |  | Captador |
| `geraComissao` | boolean |  | Gerar comissão |
| `cpfCnpjPessoa` | string |  | CPF/CNPJ da Pessoa |
| `comissaoParcelamento` | array de [`UAUApi.Models.Comissao.DadosComissaoParcelamento`](#uauapimodelscomissaodadoscomissaoparcelamento) |  | Comissão de parcelamento |

### UAUApi.Models.Comissao.DadosComissaoParcelamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroControle` | integer (int32) |  | Número de controle |
| `numeroParcela` | integer (int32) |  | Número de parcelas |
| `porcentualRecebido` | number (double) |  | Percentual sobre o recebido |
| `porcentualParcela` | number (double) |  | Percentual sobre parcela |
| `FormaLiberacao` | integer (int32) |  | forma de liberação da parcela |
| `NumeroParcelaVenda` | integer (int32) |  | número da parcela da proposta |
| `TipoParcela` | string |  | tipo da parcela |
| `DescricaoTipoParcela` | string |  | Descrição tipo da parcela |
| `CodigoStatusescritura` | integer (int32) |  | status da escritura |
| `DescricaoStatusescritura` | string |  | Descrição do status da escritura |

### UAUApi.Models.Comissao.ConsultarEstruturaComissaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Código da empresa |
| `obra` | string | ✓ | Código da obra |
| `codigoVendedor` | integer (int32) | ✓ | Código do vendedor |
| `codigoHierarquia` | integer (int32) |  | Código da hierarquia de comissão *Obsoleto* Utilizamos apenas o numero da comissão. |
| `numeroComissao` | integer (int32) | ✓ | Código do modelo de comissão. |
| `valorComissao` | number (double) | ✓ | Valor da comissão |
| `produtos` | array de [`UAUApi.Models.Comissao.DadosProdutosComissao`](#uauapimodelscomissaodadosprodutoscomissao) | ✓ | Lista de produtos - Utilizamos para verificar se há captadores no produto. |

### UAUApi.Models.Comissao.DadosProdutosComissao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoProduto` | integer (int32) |  | Código do produto |
| `codigoPersonalizacao` | integer (int32) |  | Código da personalização |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Comissao.AtualizarStatusComissaoRequest

Classe modelo de request para Atualizar status do controle de comissão

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) | ✓ | Código da empresa |
| `codigoObra` | string | ✓ | Código da obra |
| `numeroVenda` | integer (int32) | ✓ | Número da venda |
| `codigoPessoa` | integer (int32) | ✓ | Código da pessoa(Beneficiário) |
| `numeroComissao` | integer (int32) | ✓ | Número da comissão |
| `statusControleComissao` | integer (int32) | ✓ | Status do controle de comissão (0 - Não liberada, 1 - Liberada, 2 - Paga, 4 - Bloqueada) |
| `loginUsuario` | string | ✓ | Login do usuário |
