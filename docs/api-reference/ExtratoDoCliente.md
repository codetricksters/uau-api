# ExtratoDoCliente

## POST `/api/v{version}/ExtratoDoCliente/ConsultarDadosDemonstrativoPagtoCliente`

**Consulta os dados das parcelas pagas, informações do cliente e as unidades/produtos de uma determinada venda.
Contém as chamadas dos métodos ConsultarItensRecebidas e ConsultarParcelasRecebidasCliente retornando um dataset e suas tabelas.
OBS.: A instruçãoa [tipos_parc] se refere à parcelas que não devem ser mostradas no extrato do cliente, se enviar vazio, vai mostrar todas.**

Retorna informações das parcelas pagas, informações do cliente e unidades/produtos de uma determinada venda.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ExtratoDoCliente.ConsultarDadosDemonstrativoPagtoClienteRequest`](#uauapimodelsextratodoclienteconsultardadosdemonstrativopagtoclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ExtratoDoCliente/ConsultarSaldoCessoesDireitoAnteriores`

**Consulta as vendas anteriores a essa, gerada por cessão de direito, retornando o saldo já pago nas vendas anteriores**

Retorna o somatório do saldo já pago das vendas anteriores de cessão de direito

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ExtratoDoCliente.ConsultarSaldoCessoesDireitoAnterioresRequest`](#uauapimodelsextratodoclienteconsultarsaldocessoesdireitoanterioresrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ExtratoDoCliente/GerarPDFExtratoCliente`

**Método utilizado gerar os extratos em arquivos PDF e converte-los para string base64.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Preencher as opções de visualização do extrato nos módulos Vendas/Shopping, menu Utilitários, submenu Configurações extrato da venda (Visão Cliente)

Obs.: Parâmetros para impressão deste extrato são configurados na tela descrita neste virtuau: https://ajuda.globaltec.com.br/virtuau/configuracao-extrato-de-vendas-visao-cliente

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ExtratoDoCliente.GerarPDFExtratoClienteRequest`](#uauapimodelsextratodoclientegerarpdfextratoclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | O tipo de ordenação só permite valores entre 0 e 1! | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ExtratoDoCliente/GerarPDFExtratoClienteV2`

**Método utilizado gerar os extratos em arquivos PDF e converte-los para string base64.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Preencher as opções de visualização do extrato nos módulos Vendas/Shopping, menu Utilitários, submenu Configurações extrato da venda (Visão Cliente)

Obs.: Parâmetros para impressão deste extrato são configurados na tela descrita neste virtuau: https://ajuda.globaltec.com.br/virtuau/configuracao-extrato-de-vendas-visao-cliente

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ExtratoDoCliente.GerarPDFExtratoClienteRequest`](#uauapimodelsextratodoclientegerarpdfextratoclienterequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.ExtratoDoCliente.GerarPDFExtratoClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) | ✓ | Número da empresa |
| `obra` | string | ✓ | Código da obra |
| `numVenda` | integer (int32) | ✓ | Número da venda |
| `tipoOrdenacao` | integer (int32) |  | Verifica se irá ordernar por data de vencimento. 0 - Ordenação padrão, 1 - Ordenação por data de vencimento |
| `valorAntecipado` | boolean |  | Verifica se irá mostrar o extrato antecipado. TRUE - Irá mostrar. FALSE - Não irá mostrar |
| `dataProrrogacao` | boolean |  | Verifica se irá mostrar a data de prorrogação. TRUE - Irá mostrar. FALSE - Não irá mostrar |
| `ocultarPersonalizacao` | boolean |  | Verifica se irá as personalizações. TRUE - Irá ocultar. FALSE - Não irá ocultar |
| `ocultarUsuario` | boolean |  | Verifica se irá ocultar o usuário. TRUE - Irá ocultar. FALSE - Não irá ocultar |
| `dataCalculo` | string (date-time) | ✓ | Data de cálculo a ser utilizada para calcular as parcelas do relatório. |
| `residuoIraComporValorTotal` | boolean |  | Indica se o valor do resíduo será somado ao valor total. TRUE - Irá somar; FALSE - Não irá somar |

### UAUApi.Models.ExtratoDoCliente.ConsultarSaldoCessoesDireitoAnterioresRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da Empresa |
| `obra` | string |  | Código da Obra |
| `num_venda` | integer (int32) |  | Número da venda |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.ExtratoDoCliente.ConsultarDadosDemonstrativoPagtoClienteRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Número da empresa |
| `obra` | string |  | Código da obra |
| `num_venda` | integer (int32) |  | Número do contrato de venda |
| `tipos_parc` | string |  | Tipos de parcelas a NÃO serem exibidos no relatório |
| `tipo_ordenacao` | integer (int32) |  | Tipo ordenação |
| `mostrara_pagas` | boolean |  | Identifica se deve mostrar dados a pagar |
| `princ_juros` | boolean |  | Identifica se deve mostrar principal com juros |
| `descontopor_adiantamento` | boolean |  | Identifica se deve aplicar desconto por adiantamento |
| `valor_antecipado` | boolean |  | Identifica se os valores devem vir com antecipação ou não |
| `nome_fantasia` | boolean |  | Nome Fantasia |
| `ocultapref_custas` | boolean |  | Identifica se deve ocultar o prefixo "Custa-"  das descrições de custas |
| `dataCalculo` | string (date-time) |  | Data de cálculo a ser calculado as parcelas |
| `exibirDataDeposito` | boolean |  | Exibe data de depósito |
