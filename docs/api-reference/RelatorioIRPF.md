# RelatorioIRPF

## POST `/api/v{version}/RelatorioIRPF/GerarPDFRelIRPF`

**Método responsável por gerar o PDF do IRPF**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.
    - A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
    - Substituir cada parâmetro pelo valor correspondente:
        - "Venda" - Número da Venda.
        - "Obra" - Código da Obra.
        - "Empresa" - Número da Empresa.
        - "ano_base" - ano base para geração do IRPF.
        - "naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).

                {
                    "vendasobras_empresa" [
                        [
                        "Venda", 
                        "Obra", 
                        "Empresa"
                        ]
                    ],
                        "ano_base": 2018,
                        "naomostradados_venda": true
                }
    - Segue exemplo  após substituição dos parâmetros:
    
                {
                     "vendasobras_empresa" [
                       [
                       "838",
                       "424V",
                       "308"
                       ]
                   ],
                     "ano_base": 2021,
                     "naomostradados_venda": false
                }

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.RelatorioIRPF.GerarPDFRelIRPFRequest`](#uauapimodelsrelatorioirpfgerarpdfrelirpfrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/RelatorioIRPF/GerarPDFRelIRPFV2`

**Método responsável por gerar o PDF do IRPF**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Seguir o modelo abaixo para preenchimento dos parâmetros de request para uso do método.
    - A ordem dos parâmetros "Venda", "Obra" e "Empresa" é obrigatória.
    - Substituir cada parâmetro pelo valor correspondente:
        - "Venda" - Número da Venda.
        - "Obra" - Código da Obra.
        - "Empresa" - Número da Empresa.
        - "ano_base" - ano base para geração do IRPF.
        - "naomostradados_venda" - se informado "true", não mostra os dados da venda no relatório (data, valor, saldo devedor, dentre outros).

                {
                    "vendasobras_empresa" [
                        [
                        "Venda", 
                        "Obra", 
                        "Empresa"
                        ]
                    ],
                        "ano_base": 2018,
                        "naomostradados_venda": true
                }
    - Segue exemplo  após substituição dos parâmetros:
    
                {
                     "vendasobras_empresa" [
                       [
                       "838",
                       "424V",
                       "308"
                       ]
                   ],
                     "ano_base": 2021,
                     "naomostradados_venda": false
                }

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.RelatorioIRPF.GerarPDFRelIRPFRequest`](#uauapimodelsrelatorioirpfgerarpdfrelirpfrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.RelatorioIRPF.GerarPDFRelIRPFRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `vendasobras_empresa` | array de object |  | Lista de Empresa, Obra e Venda |
| `ano_base` | integer (int32) |  | Ano base |
| `naomostradados_venda` | boolean |  | Se irá mostrar ou não os dados consolidados da venda |
