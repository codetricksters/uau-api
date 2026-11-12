# Reserva

## POST `/api/v{version}/Reserva/ConsultaReservaPorProposta`

**Consulta as reservas da personalização filtrando po código**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Valida usuário e permissões

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Reserva.ConsultaReservaPorPropostaRequest`](#uauapimodelsreservaconsultareservaporpropostarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD`](#globaltecuauobrasimportadadoslogprocpagamentoxsd) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Reserva/ConsultarDadosControleReserva`

**Cosulta dados da reserva**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Valida usuário e permissões.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Reserva.ConsultarDadosControleReservaRequest`](#uauapimodelsreservaconsultardadoscontrolereservarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD`](#globaltecuauobrasimportadadoslogprocpagamentoxsd) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Reserva/ConsultarReservaPorCodigo`

**Consulta as reservas da personalização filtrando pelo código**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta todas as reservas da personalização que tem o código informado.
2. Valida usuário e suas permissões.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Reserva.ConsultarReservaPorCodigoRequest`](#uauapimodelsreservaconsultarreservaporcodigorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD`](#globaltecuauobrasimportadadoslogprocpagamentoxsd) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Reserva/ConsultarReservaVendedor`

**Consulta a reserva da personalização filtrando pelo vendedor**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint

Definição de Negócio:
1. Valida usuário e permissões

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Reserva.ConsultarReservaVendedorRequest`](#uauapimodelsreservaconsultarreservavendedorrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD`](#globaltecuauobrasimportadadoslogprocpagamentoxsd) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Reserva/ConsultarReservas`

**Consulta as reservas da personalização filtrando por status**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do endpoint.

Definição de Negócio:
1. Consulta reservas da personalização que possuem o status informado na request.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Reserva.ConsultarReservasRequest`](#uauapimodelsreservaconsultarreservasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD`](#globaltecuauobrasimportadadoslogprocpagamentoxsd) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Reserva/ExcluirReserva`

**Excluir uma reserva**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Valida usuário e permissões

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Reserva.ExcluirReservaRequest`](#uauapimodelsreservaexcluirreservarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD`](#globaltecuauobrasimportadadoslogprocpagamentoxsd) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Reserva/GravarReserva`

**Grava ou altera uma reserva

Rotina de persistência responsável por gerenciar gravação/alteração de uma reserva**

Definição técnica:  

1. Preencher os parâmetros de request para uso do método.
 - As contrabarras são impotantes para não encerrar a string antes do fim.
 - As datas devem estar no formato: AAAA-MM-DD.
 - SE O VALOR A SER PASSADO É NULL OU VAZIO, NÃO O INFORME NO JSON.
 - Troque apenas os ❌ pelos valores desejados.
 - o JSON deve ser uma string no seguinte formato:
         {
           "dados_reserva_json": 
           "[
             {
               \"reserva\": [
                 {
                   \"Empresa_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"NumProd_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"NumPer_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Num_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"CodDvg_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Vendedor_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Login_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Data_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Periodo_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Cliente_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Fone_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"TempoIndet_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Status_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"NumProposta_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"DataConfir_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"UsrConfir_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"UsrCancel_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"DataCancel_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"NumConf_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"CodPesConfir_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"GeraTaxaReserva_rsv\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"ValReserva_rsv\": \"System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"ReservaPaga_rsv\": \"System.Byte, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Banco_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Conta_rsv\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"NumEs_rsv\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"EntSai_rsv\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"DataCad_rsv\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"
                 },
                 {
                   \"Empresa_rsv\": \"❌\",
                   \"NumProd_rsv\": \"❌\",
                   \"NumPer_rsv\": \"❌\",
                   \"Num_rsv\": \"❌\",
                   \"CodDvg_rsv\": \"❌\",
                   \"Vendedor_rsv\": \"❌\",
                   \"Login_rsv\": \"❌\",
                   \"Data_rsv\": \"❌\",
                   \"Periodo_rsv\": \"❌\",
                   \"Cliente_rsv\": \"❌\",
                   \"Fone_rsv\": \"❌\",
                   \"TempoIndet_rsv\": \"❌\",
                   \"Status_rsv\": \"❌\",
                   \"NumProposta_rsv\": \"❌\",
                   \"DataConfir_rsv\": \"❌\",
                   \"UsrConfir_rsv\": \"❌\",
                   \"UsrCancel_rsv\": \"❌\",
                   \"DataCancel_rsv\": \"❌\",
                   \"NumConf_rsv\": \"❌\",
                   \"CodPesConfir_rsv\": \"❌\",
                   \"GeraTaxaReserva_rsv\": \"❌\",
                   \"ValReserva_rsv\": \"❌\",
                   \"ReservaPaga_rsv\": \"❌\",
                   \"Banco_rsv\": \"❌\",
                   \"Conta_rsv\": \"❌\",
                   \"NumEs_rsv\": \"❌\",
                   \"EntSai_rsv\": \"❌\",
                   \"DataCad_rsv\": \"❌\"
                 }
               ]
             },
             {
               \"Taxa\": [
                 {
                   \"Empresa_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Banco_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Conta_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Num_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"EntSai_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Obra_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Data_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Usuario_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Valor_es\": \"System.Double, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Natureza_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Cap_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"MesPL_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"NumDoc_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"Emissao_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"HistLanc_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"CategMovFin_es\": \"System.String, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"NumAplic_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"StatusAplic_es\": \"System.Int16, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"NumSeq_es\": \"System.Int32, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\",
                   \"DataCad_es\": \"System.DateTime, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089\"
                 },
                 {
                   \"Empresa_es\": \"❌\",
                   \"Banco_es\": \"❌\",
                   \"Conta_es\": \"❌\",
                   \"Num_es\": \"❌\",
                   \"EntSai_es\": \"❌\",
                   \"Obra_es\": \"❌\",
                   \"Data_es\": \"❌\",
                   \"Usuario_es\": \"❌\",
                   \"Valor_es\": \"❌\",
                   \"Natureza_es\": \"❌\",
                   \"Cap_es\": \"❌\",
                   \"MesPL_es\": \"❌\",
                   \"NumDoc_es\": \"❌\",
                   \"Emissao_es\": \"❌\",
                   \"HistLanc_es\": \"❌\",
                   \"CategMovFin_es\": \"❌\",
                   \"NumAplic_es\": \"❌\",
                   \"StatusAplic_es\": \"❌\",
                   \"NumSeq_es\": \"❌\",
                   \"DataCad_es\": \"❌\"
                 }
               ]
             }
           ]"
         }

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Reserva.GravarReservaRequest`](#uauapimodelsreservagravarreservarequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD`](#globaltecuauobrasimportadadoslogprocpagamentoxsd) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.Reserva.GravarReservaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dados_reserva_json` | string |  | Objeto que contém as tabelas 'reserva' e 'taxa'. |

### UAUApi.Models.Reserva.ExcluirReservaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `obra` | string |  | Código da obra |
| `num_proposta` | integer (int32) |  | Número da proposta |
| `cod_produto` | integer (int32) |  | Código do produto |
| `cod_person` | integer (int32) |  | Código da personalização |
| `cod_reserva` | integer (int32) |  | Codígo da reserva |

### UAUApi.Models.Reserva.ConsultarReservasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `cod_produto` | integer (int32) |  | Código do produto |
| `cod_person` | integer (int32) |  | Código da personalização |
| `status` | string |  | Status da unidade |

### UAUApi.Models.Reserva.ConsultarReservaVendedorRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `num_prod` | integer (int32) |  | Código do produto |
| `num_per` | integer (int32) |  | Código da personalização |
| `vendedor` | integer (int32) |  | Código do vendedor |

### UAUApi.Models.Reserva.ConsultarReservaPorCodigoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `cod_produto` | integer (int32) |  | Código do produto |
| `cod_person` | integer (int32) |  | Código da personalização |
| `cod_reserva` | integer (int32) |  | Código da reserva |

### UAUApi.Models.Reserva.ConsultarDadosControleReservaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `cod_produto` | integer (int32) |  | Código do produto |
| `cod_person` | integer (int32) |  | Código da personalização |
| `status` | string |  | Status da unidade |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `data_importacaoField` | string (date-time) |  |  |
| `sucessoField` | boolean |  |  |
| `mensagemField` | string |  |  |

### UAUApi.Models.Reserva.ConsultaReservaPorPropostaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | integer (int32) |  | Código da empresa |
| `obra` | string |  | Obra |
| `num_proposta` | integer (int32) |  | Código da proposta |
