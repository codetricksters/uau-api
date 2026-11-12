# ProcessoPagamento

## POST `/api/ProcessoPagamento/ConsultarQuantidadeProcessosAprovarDVQ`

**Retorna a quantidade de processos a ser aprovado do processo DVQ**

Criação  : Nelson Plínio       Data: 10/04/2019
Projeto  : 310963

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `login_usuario` | query | string | ✓ | login do usuário |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | integer (int32) |

---

## POST `/api/ProcessoPagamento/ContaProcessoEmissaoPagamentoResumido`

**Conta os Processo de Emissão de Pagamento**

Criação  : Nelson Plínio      Data: 10/04/16
Projeto  : 310963 -
Propósito: Contar os processos de emissão de pagamento

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

## POST `/api/ProcessoPagamento/ValidaDadosPagamentoParaAceitarCodigoDeBarras`

**Validações dos dados de pagamento para o aceite da inserção do Código de Barras no processo de pagamento.**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `banco` | query | string | ✓ |  |
| `conta` | query | string | ✓ |  |
| `tipoEmissao` | query | string | ✓ |  |
| `formaPagamento` | query | string | ✓ |  |
| `tipoPagamento` | query | string | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |

---

## POST `/api/ProcessoPagamento/ValidaDadosPagamentoParaAceitarPixCopiaCola`

**Validações dos dados de pagamento para o aceite da inserção do Pix Copia e Cola no processo de pagamento.**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `banco` | query | string | ✓ |  |
| `conta` | query | string | ✓ |  |
| `tipoEmissao` | query | string | ✓ |  |
| `formaPagamento` | query | string | ✓ |  |
| `tipoPagamento` | query | string | ✓ |  |
| `api-version` | query | string |  |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | OK | [`Globaltec.UAU.Comp.ResultadoExecucao`](#globaltecuaucompresultadoexecucao) |

---

## POST `/api/v{version}/ProcessoPagamento/AcrescimoDesconto`

**Aplicar um novo acréscimo ou desconto fixo em um processo de pagamento**

Sempre é lançado um novo acréscimo/desconto
**Parâmetros do Request:**
Empresa, Obra, NumeroDoProcesso e NumeroDaParcela são obrigatórios e identificam o processo;
Data: Data do acréscimo a ser inserido no processo;
Valor: Valor do acréscimo ou desconto. Positivo = acréscimo, negativo = desconto. Percentuais não são aceitos;
Descricao: Texto livre limitado conforme tabela do banco de dados;
CAP: Código fiscal a ser utilizado no processamento contábil do ajuste;
HistoricoContabil: Texto opcional que será enviado à contabilidade como histórico da movimentação.
TipoCalculo: Campo opcional que define entre 0 - Compõe base de cálculo e 1 - Não compõe base de cálculo para o cadastro de desconto
**Definição Técnica:**
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
Esquema: [`UAUApi.Models.ProcessoPagamento.GravarAcrescimoDescontoRequest`](#uauapimodelsprocessopagamentogravaracrescimodescontorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/AprovarDVQ`

**Realiza a aprovação DVQ de uma ou várias parcelas.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
Permite a aprovação DVQ de parcelas específicas.
1. No request [dvq] deve ser informado qual a letra que será aprovada ou não.
   - Os seguintes parâmetros obrigatórios para aprovação da letra "D":  Confirmação de data
        - usrConfirmou
        - codigoEmpresa
        - codigoObra
        - numeroProcesso
        - numeroParcela 
   - Os seguintes parâmetros obrigatórios para aprovação da letra "V" : Confirmação do valor
        - usrConfirmou
        - codigo_empresa
        - codigo_obra
        - numero_processo
        - codigo_departamento
        - numero_parcela
        - status_processo
        - valor_parcela      
   - Os seguintes parâmetros obrigatórios para aprovação da letra "Q" : Confirmação da quantidade
        - usrConfirmou
        - codigo_empresa
        - codigo_obra
        - numero_processo
        - numero_parcela
        - status_processo
        - tipo_Docprocesso
        - adiantamento_parcela       
3. Será validado as permissões do usuário informado. Verifique as permissões caso esteja sendo retornado erro na requisição;
    - FID : Permissão para aprovar "D"
    - FIV : Permissão para aprovar "V"
    - FIQ : Permissão para aprovar "Q"
4. O usuário autenticado precisa ter acesso a empresa e a obra da qual está fazendo a requisição.   
5. Será apenas validado a aprovação DVQ das parcelas informadas. Recomendado utilizar a API [RetornarParcelasDVQ] para retornar as informações das parcelas.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.DVQGravarRequest`](#uauapimodelsprocessopagamentodvqgravarrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/AprovarProcessos`

**Realiza a aprovação de parcelas de um processo de pagamento.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
2. O Usuário informado precisa ter a permissão [FICHEQUE] para aprovar as parcelas do processo.
3. A(s) parcela(s) precisam estar no "Emissão de Pagamentos" para serem aprovadas.
4. Todos os parâmetros são obrigatórios.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.AprovarProcessosRequest`](#uauapimodelsprocessopagamentoaprovarprocessosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucaoResponse`](#globaltecuaucompresultadoexecucaoresponse) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/ConfirmarProcessoParaEmissao`

**Enviar processo de pagamento para emissão de pagamentos**

**Definição Técnica:**
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Valida se foram selecionadas parcelas de processos diferentes com tipos de Internos e Externos, ou seja, só pode confirmar parcelas de processos com mesmo tipo, ou todos internos ou todos externos;

**Definição de negócio:**
1. Valida se parcela tem confirmação de DVQ;
2. Valida se a parcela tem banco e conta informado, e Tipo de emissão;
3. Valida fechamento fiscal de banco e conta para a data de prorrogação;
5. Valida configuração geral de provisionamento de documento fiscal, onde se a config estiver marcada, só pode confirmar se todas as parcelas forem provisionado ou se as parcelas foram de adiantamento;
6. Valida se o processo é transação financeira, ou seja, vinculado a alguma venda;
7. Valida se o processo é transação financeira (Processo de REEMBOLSO), e caso seja, só pode confirmar se o tipo de emissão for Débito Eletrônico;
8. Valida se a parcela possui chave da Nfe e caso tenha, valida o status da NF, e se estiver pendente não permite gerar;
9. Validações para tipo de emissão Débito Eletrônico;
    - Valida se tem alguma forma de pagamento informada;
    - Valida se tem algum tipo de pagamento informado;
    - Valida se o banco informado na parcela com emissão débito eletrônico, tem opção de geração de arquivo de pagamento;
    - Valida se a conta informada na parcela com emissão débito eletrônico é do tipo conta corrente e se existe agência cadastrada;
    - Valida se o fornecedor ou beneficiário está cadastrado ou se possui endereço principal;
    - Valida caracteres especiais nos dados do fornecedor ou beneficiário;
    - Validações das formas de pagamento 
         - CRÉDITO C/C; CRÉDITO C/ POUPANÇA; DOC ; TED (01,03,05,06,07,08,09 e 10);
             - Caso existe dados bancários para a parcela do processo, valida se existe conta cadastrada como padrão para o beneficiário ou fornecedor da parcela;
             - Valida se o banco creditado é IGUAL do banco debitado para as formas ((01,06,07 e 09);
             - Valida se o banco creditado é DIFERENTE do banco debitado para as formas ((03,05,08 e 10);
             - Para os bancos 341 e 444 e para as formas 06, 08 ou 10, valida se o fornecedor possui CPF ou CPNJ e valida se o CPF/CNPJ do creditado é IGUAL ao debitado;
         - PAG TÍTULOS; CONCECIONÁRIAS; TRIBUTOS; e PIX; (30, 31, 13, 29, 19, 91, 35, 47)
             - Valida se o código de barras foi preenchido;
             - Valida se o Pix copia e cola foi preenchido;
             - Valida duplicidade de código de barras ou pix copia e cola, caso a configuração geral esteja marcada;
             - Valida se o valor ou a data no código de barras é diferente do valor ou data do processo;
             - Para a forma 21, valida se o banco creditado é diferente do banco debitado;
             - Para os banco 356;291;389 e as formas 29 e 30, valida se o banco creditado é igual ao banco debitado;
             - Para a forma de pagamento 35 - FGTS, valida o tamanho máximo do campo identificador do FGTS, onde é 20 para o banco 237, e para os bancos 1, 8, 33, 104, 341, 353, 756, 748, 444, o tamanho máximo é 16;
         - CARTÃO SALÁRIO (14) para o Banco 409
             - Valida se o fornecedor possui um cartão salário cadastrado;
10. Validações processo do tipo folha - Tipo processo 18:
    - Caso processo seja gerado na tela de Gerar arquivo de pagamento folha, só pode confirmar como Débito C/C;
    - Valida se o processo folha tem o status do tipo "4 - Gerar arquivo" na tela de Gerar arquivo de pagamento folha, e se tiver mesmo que seja debito eletrônico, permite confirmar sem a forma de pagamento informada na parcela;
    - Caso o projeto esteja com o status do tipo "4 - Gerar arquivo", permite confirmar mesmo sem informar tipo de pagamento;
    - Processos de folha, que estão agrupados e com status "4 - Gerar arquivo", só podem ser confirmados como Débito eletrônico;
    - Valida se os processos do tipo folha tem cálculo gerado para o mesmo, no modulo Folha de pagamento;
11. Valida se os processos são do tipo tributo, e se estão vinculados a algum tributo;
12. Valida se o pagamento está DUPLICADO, caso a config geral esteja marcada, onde valida se existem a mesma parcela em emissão ou em contas pagas;
13. Valida se a parcela já está confirmada, para evitar a concorrência; 
14. Valida se existem notas fiscais vinculadas ao processo que está com o total menor que o total de todos processos vinculados, caso a config geral esteja marcada;
15. Valida se a nota fiscal está conferida, caso config geral esteja marcada;
16. Valida se existe nota fiscal na parcela, caso config geral de provisionamento seja marcada;

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.ConfirmarParcelasRequest`](#uauapimodelsprocessopagamentoconfirmarparcelasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Comp.ResultadoExecucaoResponse`](#globaltecuaucompresultadoexecucaoresponse) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/ConsultarProcessos`

**Consultar processos de pagamento por empresa(s), obra(s) e número(s) do(s) processo(s) e/ou empresa, obra e período(data de cadastro do processo) e/ou CNPJ do fornecedor e período(data de cadastro do processo).**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario

Definição de Negócio:
Permite que você consulte o(s) processo(s) de pagamento por um número e/ou período específico.
1. Você pode consultar informando uma lista dos números dos processos de pagamento, código da empresa e código da obra cadastrados no UAU.
2. Você pode consultar processos de pagamento informado uma lista de código da empresa e código da obra cadastrado no UAU por um determinado período.
3. Você pode consultar processos de pagamento informado uma lista de fornecedores cadastrado no UAU por um determinado período.
4. O usuário autenticado precisa ter acesso as empresas e obras das quais ele está fazendo a requisição.   
5. Caso consulte vários processos ou informe um longo período, sugerimos que consulte o serviço de maneira assíncrona. 
6. NovoBeneficiario: O campo Parametro/NovoBeneficiario sempre retornará o valor null. A informação é retornada no campo Parcelas/NovoBeneficiario.
7. Caso passe uma mistura de todos os filtros, o filtro de data que será utilizado será o do busca por cnpj a frente do busca por empresas e obras.
7.1 Caso queria buscar por períodos diferentes recomendamos utilizar requests separados para respeitar os períodos por grupo separado.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.ConsultarProcessoRequest`](#uauapimodelsprocessopagamentoconsultarprocessorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.ProcessoPagamento.ProcessoPagamento`](#uauapimodelsprocessopagamentoprocessopagamento) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/EmissaoPagamento`

**Enviar processo de pagamento em emissão para o banco**

**Definição Técnica:**
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Rota destinada para emitir processos de pagamento que estão prontos (aprovados) para serem emitidos.

**Definição de negócio:**
1. Emissão será realizada somente para processos aprovados com Tipo de Emissão "Débito CC";
2. Validar status da parcela como 2 - Reprovado, não deve enviar;
3. Verifica se existe alguma restrição(Ocorrência) para o fornecedor/beneficiário;
4. Valida programa de permissão;
5. Valida se o processo é vinculado a algum tributo, e se for, valida se o tributo está confirmado;
      - Caso esteja confirmado, atualiza o status do tributo para 2 - Pago; - Ação;
6. Valida se o processo é de retenção contratual, tipos 16 ou 13, e se for, valida o configuração da empresa, se está para realizar retenção contratual e valida a situação do contrato vinculado;

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.EmitirParcelasRequest`](#uauapimodelsprocessopagamentoemitirparcelasrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.ProcessoPagamento.ProcessoPagamento`](#uauapimodelsprocessopagamentoprocessopagamento) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/GerarNotaFiscal`

**Gerar nota fiscal com base nos dados do processo informado. A nota será vinculada ao processo.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Gerar nota fiscal de entrada de acordo com os dados do processo
 
1. É obrigatório informar os dados básicos da nota fiscal.
2. O usuário autenticado precisa ter acesso a empresa e obra que está fazendo a requisição;
3. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção;
4. Serão utilizadas as informações fiscais de tributo cadastradas no produto ou na empresa.
5. Especies disponíveis para geração do documento fiscal (NF - Nota fiscal, CT - Conhecimento de transporte, RE - Recibo, OU - Outros, CF - Cupom fiscal)

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.GerarNotaFiscalRequest`](#uauapimodelsprocessopagamentogerarnotafiscalrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/GerarNotaFiscalProdutoPeloXML`

**Gerar NF-e com base nos dados informado, xml do diretório.**

Criação   : Augusto Rabelo Barbosa                 Data: 28/05/2022
Projeto   : 442112
Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
Projeto   : 443200
Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.

Alteração  : Augusto Rabelo Barbosa      data: 04/01/2023
Projeto    : 443200
Manutenção  : Alterei o enumerador de importação de nota, passando a utilizar o TiposImportacao do EnumeradoresGerais

Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
Projeto   : 454022
Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.

Alteração : Juliana Oliveira Souza    Data: 19/06/2023
Projeto   : 467593
Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário

	
Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
Projeto   : 442322 - SPT 10-2024 - US 359545
Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.GerarNotaFiscalProdutoPeloXMLRequest`](#uauapimodelsprocessopagamentogerarnotafiscalprodutopeloxmlrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/GerarNotaFiscalServicoPeloXML`

**Gerar NFS-e com base nos dados informado, xml do diretório ou arquivo.**

Criação   : Augusto Rabelo Barbosa                 Data: 03/11/2022
Projeto   : 442112

Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
Projeto   : 443200
Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.

Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
Projeto   : 454022
Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.


Alteração : Juliana Oliveira Souza    Data: 19/06/2023
Projeto   : 467593
Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário

Alteração : Rogério Adriano           Data: 31/07/2023
Projeto   : 475869
Manutenção: Foi inserido validação após o preenchimento da classe de nota fiscal
            para verificar se foi preenchido com sucesso, caso contrario irá retornar o erro.

Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
Projeto   : 442322 - SPT 10-2024 - US 359545
Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].

Alteração : Daniel Eugenio Vaz          Data: 11/08/2025
Projeto   : 381359 - NFse Nacional - Contas a Pagar - US 380751
Manutenção: Ajuste para consulta do novo padrão NFs-e Nacional

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.GerarNotaFiscalServicoPeloXMLRequest`](#uauapimodelsprocessopagamentogerarnotafiscalservicopeloxmlrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/GerarNotaFiscalTransportePeloXML`

**Gerar CT-e com base nos dados informado, xml do diretório.**

Criação   : Augusto Rabelo Barbosa                 Data: 03/11/2022
Projeto   : 442112

Alteração : Elenildo Barbosa de Sousa    Data: 03/01/2023
Projeto   : 443200
Manutenção: Foi alterado a passagem de parâmetro do metodo BuscarArquivoDiretorioChave.

Alteração: Augusto Rabelo Barbosa      data: 04/01/2023
Projeto: 443200
Manutenção: Alterei o enumerador de importação de nota, passando a utilizar o TiposImportacao do EnumeradoresGerais

Alteração : Augusto Rabelo Barbosa    Data: 01/06/2023
Projeto   : 454022
Manutenção: Inserido a validação VerificarSeProcessoFrete, para que seja feito a validação do processo de frete.

Alteração : Juliana Oliveira Souza    Data: 19/06/2023
Projeto   : 467593
Manutenção: - Adicionada na chamada do método AtualizarInfoChaveNFeStatus o usuário

Alteração : João Henrique Ribeiro Leite                         Data: 23/10/2024
Projeto   : 442322 - SPT 10-2024 - US 359545
Manutenção: Alterada a classe da chamada do método [BuscarChaveArquivoXML].

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.GerarNotaFiscalTransportePeloXMLRequest`](#uauapimodelsprocessopagamentogerarnotafiscaltransportepeloxmlrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | string |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/GerarProcesso`

**Gera um processo de pagamento.**

<b>Definição Técnica:</b>
<br>Dados básicos para o funcionamento da API.</br>
<list type="bullet">
  <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
  <item>2. Preencher os parâmetros de request para uso do método.</item>
  <item>3. <a href="https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2024/11/ProcessoPagamento_GerarProcesso-3.pdf" target="_blank">Documentação API - Gerar Processo (Clique Aqui)</a></item>
</list>
<b>Definição de Negócio:</b>
<br>Gera um processo de pagamento.</br>
<list type="bullet">
  <item>1. É obrigatório informar os dados básicos do processo de pagamento.</item>
  <item>2. O usuário autenticado precisa ter acesso à empresa e obra que está fazendo a requisição.</item>
  <item>3. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a inserção.</item>
  <item>4. Só aceita os tipos de processo de pagamento: composições e insumos, insumos planejados, adiantamento de caixa de obra, patrimônio vinculado ao planejamento.</item>
  <item>5. Você pode informar uma parcela ou uma lista de parcelas.</item>
  <item>6. Você pode vincular documento fiscal ao processo de pagamento, informe os dados da nota no objeto de DocumentoFiscal; o documento deve existir.</item>
  <item>7. Você pode aplicar desconto normal à parcela, informe os dados de desconto no objeto Descontos.</item>
  <item>8. Quando o insumo PL for do tipo 1 - quantidade, será considerado o preço do item.</item>
  <item>9. Somente podem ser gerados processos dos tipos: 1 - Processo de Pagamento, 11 - Compra de patrimônio, 13 - Adiantamento de caixa de obra.</item>
  <item>10. Processos de pagamento de serviços gerarão automaticamente os descontos vinculados (impostos) caso estejam configurados.</item>
  <item>11. Categoria de movimentação financeira na propriedade de Item:
 <list type="bullet"><item><description>Deve adicionar a propriedade CategoriaMovimentacaoFinanceira na propriedade de Item, para armazenar o código da categoria de movimentação financeira.</description></item><item><description>Não é obrigatório informar o parâmetro CategoriaMovimentacaoFinanceira.</description></item></list></item>
  <item>12. Caso não seja informado o tipo de pagamento TipoPagamento ou tipo de emissão TipoEmissao, será considerada a configuração padrão do processo de pagamento.</item>
</list>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.GravarProcessoRequest`](#uauapimodelsprocessopagamentogravarprocessorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.ProcessoPagamento.ProcessoPagamento`](#uauapimodelsprocessopagamentoprocessopagamento) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/GerarProcessoMedicao`

**Gerar processo de pagamento de medição de contrato de material/serviço**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Gerar processo de pagamento de medição de contrato de material/serviço
 
1. É obrigatório informar os dados básicos do processo de pagamento;
2. O usuário autenticado precisa ter acesso a empresa e obra que está fazendo a requisição;
3. O usuário autenticado precisa ter acesso a aos programas de permissão necessários para fazer a inserção;
4. Você pode informar uma parcela ou uma lista de parcelas;
5. Você pode vincular documento fiscal ao processo de pagamento, informe os dados da nota no objeto de “DocumentoFiscal”, o documento deve existir;
6. Você pode aplicar desconto normal a parcela, informe os dados de desconto no objeto “Descontos”;
7. Quando o insumo PL for do tipo 1 - quantidade será considerado o preço do item;

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.GravarProcessoMedicaoRequest`](#uauapimodelsprocessopagamentogravarprocessomedicaorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.ProcessoPagamento.ProcessoPagamento`](#uauapimodelsprocessopagamentoprocessopagamento) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/IntegrarProcessoPagamentoUAUWS`

**Realizar a integração do processo de pagamento utilizando arquivo XML**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.
3. Deve seguir arquivo XSD como formato aceito.
4. Os campos do tipo data devem obedecer o formato específico (yyyy-MM-dd).

Definição de negócio:
1. Realiza a importação dos dados de processo de pagamento para o UAU de acordo com o arquivo XML.
2. Será validado os dados do XML para realizar a importação, bem como tipagem de dados, dados obrigatórios, entre outros. 
3. Virtuau: https://ajuda.globaltec.com.br/virtuau/como-integrar-meus-processos-de-pagamento/

Anexos:
1. XML: https://ajuda.globaltec.com.br/download/777734/
2. XSD: https://ajuda.globaltec.com.br/download/777719/
3. Postman: https://ajuda.globaltec.com.br/download/777737/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.IntegrarProcessoPagamentoUAUWSRequest`](#uauapimodelsprocessopagamentointegrarprocessopagamentouauwsrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD`](#globaltecuauobrasimportadadoslogprocpagamentoxsd) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/ManutencaoParcelasProcesso`

**Realiza manutenção em parcelas de processo de pagamento. Será simulado e gerado automaticamente as novas parcelas conforme os parâmetros informados.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Permite dar manutenção nas parcelas do processo de pagamento. Ao informar os dados para as novas parcelas, será simulado e gerado automaticamente as novas parcelas
com novas numerações, valores e data de vencimento. Será excluido a(s) parcela(s) informadas no request, pois foram substituídas pelas novas parcelas geradas.

1. É obrigatório informar os dados básicos da parcela e do processo de pagamento;
2. O usuário autenticado precisa ter acesso aos programas de permissão necessários (FIANALISE) para fazer a alteração.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.ManutencaoParcelasProcessoRequest`](#uauapimodelsprocessopagamentomanutencaoparcelasprocessorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.ProcessoPagamento.ManutencaoParcelas`](#uauapimodelsprocessopagamentomanutencaoparcelas) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/ManutencaoProcesso`

**Executa manutenção básica em uma etapa do processo de pagamento.**

<b>Definição Técnica:</b>
<br>Dados básicos para o funcionamento da API.</br>
<list type="bullet">
  <item>1. Autenticar o usuário cliente: URI + /api/v{version}/Autenticador/AutenticarUsuario</item>
  <item>2. Consultar os dados de um processo de pagamento: URI + /api/v{version}/ProcessoPagamento/ConsultarProcessos</item>
  <item>3. Preencher os parâmetros de request para uso do método.</item>
  <item>4. <a href="https://ajuda.globaltec.com.br/wp-content/uploads/dlm_uploads/2024/11/ProcessoPagamento_ManutencaoProcesso-1.pdf" target="_blank">Documentação API - Manutenção de Processo (Clique Aqui)</a></item>
</list>
<b>Definição de Negócio:</b>
<br>Permite ajustar informações básicas do processo de pagamento, como vencimento, data de prorrogação, novo beneficiário, fornecedor, etc.
 Consulte a documentação do objeto de request.</br>
<list type="bullet">
  <item>1. É obrigatório informar os dados básicos do processo de pagamento.</item>
  <item>2. Para alterar informações da parcela do processo, preencha o objeto de Parcelas.</item>
  <item>3. Todas as alterações gerarão um comentário de alteração no processo.</item>
  <item>4. O usuário autenticado precisa ter acesso aos programas de permissão necessários para fazer a alteração.</item>
  <item>5. O parâmetro CodigoNovoBeneficiario altera todas as parcelas a pagar do processo informado, independentemente da parcela informada.
 <list type="bullet"><item><description>Ao informar esse valor no processo, na resposta da request o valor será null, mas estará indicado nas parcelas. Isso ocorre porque esse campo pertence à parcela.</description></item></list></item>
  <item>6. O parâmetro NovoBeneficiario altera apenas a parcela informada, se ela estiver a pagar.
 <list type="bullet"><item><description>Se preencher o parâmetro de beneficiário no processo e na parcela, o parâmetro do processo será desconsiderado, alterando apenas os beneficiários das parcelas informadas.</description></item></list></item>
  <item>7. Se preencher o valor zero ou vazio para o novo beneficiário, a alteração não será considerada. A API não limpa valores de novo beneficiário.</item>
</list>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.ManutencaoProcessoRequest`](#uauapimodelsprocessopagamentomanutencaoprocessorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. | [`UAUApi.Models.ProcessoPagamento.ProcessoPagamento`](#uauapimodelsprocessopagamentoprocessopagamento) |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/ProcessoPagamento/RetornarParcelasDVQ`

**Retorna parcelas com alguma possibilidade de aprovação DVQ.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Os campos empresa, obra e usuário são obrigatórios.
2. É validado se o usuário existe no banco de dados, e se tem permissão na empresa e obra informada.
3. Data e Fornecedor devem está vazio ou sem o parâmetro informado na requisição para não serem considerados na consulta.
4. Número processo(numeroproc) e notafiscal devem está como 0 ou sem o parâmetro informado na requisição para não serem considerados na consulta.
5. O parâmetro nota fiscal é o número de controle interno da nota fiscal.
6. Status atual da aprovação status_d, status_v e status_q.
    - Valor [A]: aprovado
    - Valor [D]: não aprovado

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.ProcessoPagamento.RetornarParcelasDVQRequest`](#uauapimodelsprocessopagamentoretornarparcelasdvqrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso. |  |
| 400 | Não foi possível realizar sua requisição. Verifique as mensagens de retorno. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### UAUApi.Models.ProcessoPagamento.RetornarParcelasDVQRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Usuario` | string | ✓ | Login do usuário |
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |
| `numeroproc` | integer (int32) |  | Número processo |
| `fornecedor` | string |  | Código da pessoa(Fornecedor) |
| `notafiscal` | integer (int32) |  | Número nota fiscal |
| `inicial` | string |  | Data inicio |
| `final` | string |  | Data final |

### UAUApi.Models.ProcessoPagamento.ManutencaoProcessoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) | ✓ | <list type="bullet">   <item>Número do processo de pagamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Empresa` | integer (int32) | ✓ | <list type="bullet">   <item>Empresa do processo de pagamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Obra` | string | ✓ | <list type="bullet">   <item>Código da obra que foi gerado o processo a ser pago.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `CodigoFornecedor` | integer (int32) |  | <list type="bullet">   <item>Número do código do fornecedor.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CodigoNovoBeneficiario` | integer (int32) |  | <list type="bullet">   <item>Código do novo beneficiário, dados sobre o cedente responsável pela emissão do título original,<br> sacador avalista.</br></item>   <item>     Informar valor "0" para limpar o beneficiário existente.   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Antecipado` | boolean |  | Define se é antecipado ou não, é utilizado para poder parametrizar um processo como antecipado,<br> ou seja, efetuar a confirmação Q da parcela e pagar sem a necessidade do Acompanhamento de Entrega. </br><list type="bullet"><item><br>True  - Antecipado.</br></item><item><br>False - Não antecipado.</br></item><item><b>Campo não obrigatório.</b></item></list> |
| `Retroacao` | integer (int32) |  | <list type="bullet">   <item>Número de meses de retroação para o pagamento do processo.</item>   <item>     Valor pode ser entre 0 a 999   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CodigoDepartamento` | string |  | <list type="bullet">   <item>Código do departamento do processo de pagamento.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TipoJuros` | integer (int32) |  | <list type="bullet">   <item>Tipo de juros, cobrado por atraso, o sistema já calcula usando os valores digitados nos campos %Multa e %Juros Dia,<br>e pode ser calculado dois tipos de juros: Juros Simples e Juros Composto.</br></item>   <item>     0 - Juro simples percentual.   </item>   <item>     1 - Juro composto percentual   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TaxaJurosAtraso` | number (double) |  | <list type="bullet">   <item>Percentual de juros a ser aplicado em caso de atraso.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TaxaMultaAtraso` | number (double) |  | <list type="bullet">   <item>Percentual de multa a ser aplicado em caso de atraso.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `ChaveNfe` | string |  | <list type="bullet">   <item>Chave da nota fiscal eletrônica.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Parcela` | [`UAUApi.Models.ProcessoPagamento.ManutencaoProcessoParcela`](#uauapimodelsprocessopagamentomanutencaoprocessoparcela) |  | <list type="bullet">   <item>Dados da parcela.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `NumeroProtocolo` | integer (int32) |  | <b>Número do protocolo</b> <list type="bullet">   <item>     <br>Informe o número do protocolo que deseja atribuir ao processo de pagamento.</br>   </item>   <item>     <br>Se desejar limpar o campo, informe o valor -1 neste parâmetro</br>   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `PermiteBoletoVencido` | boolean |  | <b>Permite Boleto Vencido</b> <list type="bullet">   <item>     <br>       True  - Permite alterar o processo se a data de vencimento for menor que a data de prorrogação.</br>   </item>   <item>     <br>       False - Não permite alterar.</br>   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |

### UAUApi.Models.ProcessoPagamento.ManutencaoProcessoParcela

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) | ✓ | <list type="bullet">   <item>Número da parcela.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Prioridade` | integer (int32) |  | <list type="bullet">   <item>Prioridade de pagamento da parcela.</item>   <item>     0 - nenhuma   </item>   <item>     1 - baixa   </item>   <item>     2 - média   </item>   <item>     3 - alta   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Provisionado` | integer (int32) |  | <list type="bullet">   <item>Provisionado.</item>   <item>     0 - Não provisionado   </item>   <item>     1 - Provisionado   </item>   <item>     2 - Adiantamento   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TipoEmissao` | string |  | <list type="bullet">   <item>Identifica se é débito C/C, débito eletrônico, cheque, borderô.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `DataVencimento` | string (date-time) |  | <list type="bullet">   <item>Data de vencimento do processo.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `DataProrrogacao` | string (date-time) |  | <list type="bullet">   <item>Data de prorrogação (Pagamento).</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `FormaPagamento` | string |  | <list type="bullet">   <item>Código da forma de pagamento eletrônico.</item>   <item>     01 - CRÉDITO C/C   </item>   <item>     03 - DOC   </item>   <item>     05 - TED - STR   </item>   <item>     09 - CRÉDITO C/C REAL TIME   </item>   <item>     30 - PAG. TÍTULOS DO MESMO BANCO   </item>   <item>     31 - PAG. TÍTULOS DE OUTROS BANCOS   </item>   <item>     16 - DARF   </item>   <item>     17 - GPS   </item>   <item>     19 - IPTU   </item>   <item>     22 - GARE-ICMS   </item>   <item>     35 - FGTS   </item>   <item>     91 - GNRE e Tributos estaduais   </item>   <item>     13 - PAG. CONCESSIONÁRIAS   </item>   <item>     11 - PIX Agência e Conta   </item>   <item>     12 - Pix Chave   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TipoPagamento` | string |  | <list type="bullet">   <item>Tipo de pagamento eletrônico.</item>   <item>     Valor informado depende da forma de pagamento selecionada.   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Nominal` | string |  | <list type="bullet">   <item>Nominal do processo de pagamento/cheque.</item>   <item>     Nome do fornecedor   </item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CodigoDeBarras` | string |  | <list type="bullet">   <item>Código de barras.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `ObservacaoPagamento` | string |  | <list type="bullet">   <item>Observação do pagamento.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `ObservacaoEntrega` | string |  | <list type="bullet">   <item>Observação da entrega.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `ObraFiscal` | string |  | <list type="bullet">   <item>Código da obra fiscal.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `HistoricoLancContabil` | string |  | <list type="bullet">   <item>Histórico de lançamento contábil.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CategoriaMovFinanceira` | string |  | <list type="bullet">   <item>Categoria de movimentação financeiro do processo.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `HistoricoLancContabilPago` | string |  | <list type="bullet">   <item>Histórico de lançamento contábil pago.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Banco` | integer (int32) |  | <list type="bullet">   <item>Código do banco.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Conta` | string |  | <list type="bullet">   <item>Conta.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Convenio` | string |  | <list type="bullet">   <item>Convênio.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `DataInicioReajuste` | string (date-time) |  | <list type="bullet">   <item>Data base de início do reajuste.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `IndiceReajuste` | string |  | <list type="bullet">   <item>Data índice de reajuste.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `NovoBeneficiario` | integer (int32) |  | <list type="bullet">   <item>Código do novo beneficiário, dados sobre o cedente responsável pela emissão do título original,<br> sacador avalista.</br></item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `PixCopiaCola` | string |  | <list type="bullet">   <item>Pix copia e cola do pagamento.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |

### UAUApi.Models.ProcessoPagamento.ManutencaoParcelas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) | ✓ | Código da empresa do processo de pagamento |
| `codigoObra` | string | ✓ | Código da obra do processo de pagamento |
| `numeroProcesso` | integer (int32) | ✓ | Número do processo de pagamento |
| `listaNovasParcelas` | array de [`UAUApi.Models.ProcessoPagamento.Parcelas`](#uauapimodelsprocessopagamentoparcelas) | ✓ | Lista das novas parcelas geradas. |

### UAUApi.Models.ProcessoPagamento.Parcelas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Numero` | integer (int32) | ✓ | Número da parcela |
| `DataVencimento` | string (date-time) | ✓ | Data de vencimento |
| `DataPagamento` | string (date-time) | ✓ | Data de pagamento |
| `Valor` | number (double) | ✓ | Valor da parcela |
| `Provisionado` | integer (int32) | ✓ | Provisionado (0 - Não provisionado, 1 - Provisionado, 2 - Adiantamento) |
| `ValorTotalDocumentoFiscal` | number (double) | ✓ | Valor total dos documentos fiscais |
| `Status` | integer (int32) | ✓ | Status da parcela (0 - Contas a pagar, 1 - Em emissão, 2 - Contas pagas, 3 - Emitido ao banco) |
| `FormaPagamento` | string | ✓ | Código da forma de pagamento eletrônico. 01 - CRÉDITO C/C 03 - DOC 05 - TED - STR 08 - TED DE MESMA TITULARIDADE 09 - CRÉDITO C/C REAL TIME 30 - PAG. TÍTULOS DO MESMO BANCO 31 - PAG. TÍTULOS DE OUTROS BANCOS 16 - DARF  17 - GPS 19 - IPTU 22 - GARE-ICMS 35 - FGTS 91 - GNRE e Tributos estaduais 13 - PAG. CONCESSIONÁRIAS |
| `Prioridade` | integer (int32) | ✓ | Prioridade de pagamento da parcela (0-nenhuma, 1-baixa, 2-média, 3-alta) |
| `UsuarioConfirmouData` | string | ✓ | Usuário que confirmou a data do processo |
| `UsuarioConfirmouValor` | string | ✓ | Usuário que confirmou o valor |
| `UsuarioConfirmouQuantidade` | string | ✓ | Usuário que confirmou a quantidade do processo |
| `UsuarioConfirmouEmissao` | string | ✓ | Usuário que enviou o processo para emissão |
| `ConfirmarDVQ` | string | ✓ | Contém as confirmações DVQ da parcela |
| `ConfirmarEmissao` | integer (int32) | ✓ | Se está confirmado para emissão (0 - Não 1 - Sim) |
| `TipoEmissao` | string | ✓ | Identifica se é débito C/C, débito eletrônico, cheque, borderô |
| `Nominal` | string | ✓ | Nominal do processo de pagamento/cheque (nome do fornecedor) |
| `Acrescimo` | number (double) | ✓ | Valor do acréscimo |
| `Desconto` | number (double) | ✓ | Valor do desconto |
| `DocumentoFiscalEntregue` | integer (int32) | ✓ | Documento fiscal entregue (0 - Não, 1 - Sim) |
| `DataConferenciaDataProcesso` | string (date-time) | ✓ | Data de conferência da data do processo |
| `DataConferenciaValor` | string (date-time) | ✓ | Data de conferência do valor |
| `DataConferenciaQuantidade` | string (date-time) | ✓ | Data de conferência da quantidade |
| `CodigoDeBarras` | string | ✓ | Código de barras |
| `PixCopiaCola` | string | ✓ | PIX Copia e Cola do pagamento |
| `TXID` | string | ✓ | TXID |
| `AgenciaCedente` | string | ✓ | Agência do cedente do código de barras |
| `CodigoCedente` | integer (int32) | ✓ | Código do cedente do código de barras |
| `TipoPagamento` | integer (int32) | ✓ | Tipo de pagamento eletrônico.  ** Valor informado depende da forma de pagamento selecionada ** |
| `GrupoParcelas` | string | ✓ | Código para agrupamento de parcelas (cheques) |
| `NumeroDocumentofiscal` | string | ✓ | Número do documento fiscal |
| `ObservacaoPagamento` | string | ✓ | Observação do pagamento |
| `ObservacaoEntrega` | string | ✓ | Observação da entrega |
| `DataDocumentoFiscal` | string (date-time) | ✓ | Data do documento fiscal |
| `DataEnvioAoBanco` | string (date-time) | ✓ | Data de envio ao banco |
| `NossoNumero` | string | ✓ | Nosso número código de barras |
| `ObraFiscal` | string | ✓ | Código da obra fiscal |
| `EnderecoEntrega` | string | ✓ | Endereço de entrega |
| `EnderecoPagamento` | string | ✓ | Endereço de entrega usado para cotação |
| `NumeroRegistro` | integer (int32) | ✓ | Número do registro do arquivo que foi enviado ao banco |
| `HistoricoLancamentoContabil` | string | ✓ | Histórico de lançamento contábil |
| `CategoriaMovimentacaoFinanceira` | string | ✓ | Categoria de movimentação financeira |
| `HistoricoLancamentoContabilPago` | string | ✓ | Histórico de lançamento contábil pago |
| `Convenio` | string | ✓ | Convênio |
| `DataAprovacaoEmissao` | string (date-time) | ✓ | Data de aprovação de emissão |
| `UsuarioAprovouEmissao` | string | ✓ | Usuário que aprovou a emissão |
| `DataInicioReajuste` | string (date-time) | ✓ | Data de início do reajuste |
| `IndiceReajuste` | string | ✓ | Índice de reajuste |
| `EnviadoComoRiscoSacado` | boolean | ✓ | Enviado como risco sacado (True - Sim, False - Não) |
| `Banco` | integer (int32) | ✓ | Código do banco |
| `Conta` | string | ✓ | Conta do banco |
| `NovoBeneficiario` | integer (int32) | ✓ | Código de novo beneficiário da parcela |

### UAUApi.Models.ProcessoPagamento.ManutencaoParcelasProcessoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codigoEmpresa` | integer (int32) | ✓ | Código da empresa do processo de pagamento |
| `codigoObra` | string | ✓ | Código da obra do processo de pagamento |
| `numeroProcesso` | integer (int32) | ✓ | Número do processo de pagamento |
| `dataVencimento` | string (date-time) | ✓ | Data de vencimento da primeira parcela |
| `qtdeParcelas` | integer (int32) | ✓ | Quantidade de novas parcelas a serem geradas |
| `intervaloParcelas` | integer (int32) | ✓ | Intervalo das parcelas |
| `listaParcelasManutencao` | array de [`UAUApi.Models.ProcessoPagamento.ParcelaManutencaoRequest`](#uauapimodelsprocessopagamentoparcelamanutencaorequest) | ✓ | Lista de parcelas para manutenção. |
| `listaValoresNovasParcelas` | array de [`UAUApi.Models.ProcessoPagamento.ValorParcelaManutencaoRequest`](#uauapimodelsprocessopagamentovalorparcelamanutencaorequest) |  | Lista com Valores das novas parcelas.  A lista de valores das parcelas quando informada, deve ter a quantidade de valores igual a quantidade das novas parcelas a serem geradas. Caso não seja informada, será calculado o valor das parcelas de forma proporcional. |
| `listaValoresAcrescimoNovasParcelas` | array de [`UAUApi.Models.ProcessoPagamento.AcrescimoParcelaManutencaoRequest`](#uauapimodelsprocessopagamentoacrescimoparcelamanutencaorequest) |  | Lista com valores de acréscimo das parcelas |
| `listaDataVencimentoNovasParcelas` | array de [`UAUApi.Models.ProcessoPagamento.DataVencimentoParcelaManutencaoRequest`](#uauapimodelsprocessopagamentodatavencimentoparcelamanutencaorequest) |  | Lista com data de vencimento das parcelas |

### UAUApi.Models.ProcessoPagamento.DataVencimentoParcelaManutencaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dataVencimento` | string (date-time) |  | Data de vencimento da parcela |
| `sequenciaParcela` | integer (int32) |  | Sequência da parcela a qual será definido a data de vencimento. |

### UAUApi.Models.ProcessoPagamento.AcrescimoParcelaManutencaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `valorAcrescimo` | number (double) |  | Valor de acréscimo da parcela |
| `sequenciaParcela` | integer (int32) |  | Sequência da parcela a qual será inserido o acréscimo. |

### UAUApi.Models.ProcessoPagamento.ValorParcelaManutencaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `valorParcela` | number (double) |  | Valor da parcela |

### UAUApi.Models.ProcessoPagamento.ParcelaManutencaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numeroParcela` | integer (int32) | ✓ | Número da parcela |

### Globaltec.UAU.Obras.ImportaDados.LogProcPagamentoXSD

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `data_importacaoField` | string (date-time) |  |  |
| `sucessoField` | boolean |  |  |
| `mensagemField` | string |  |  |

### UAUApi.Models.ProcessoPagamento.IntegrarProcessoPagamentoUAUWSRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `xml_proc` | string | ✓ | Arquivo XML com os processos a serem incluidos, de acordo com o XSD |

### UAUApi.Models.ProcessoPagamento.GravarProcessoMedicaoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa no UAU |
| `Contrato` | integer (int32) | ✓ | Código do contrato de material e serviço |
| `Medicao` | integer (int32) | ✓ | Código da medição |
| `MesPlanejamento` | string (date-time) | ✓ | Mês do planejamento |
| `ControlarEstoque` | integer (int32) |  | Controlar estoque (0 -Não 1-Sim). Se vai ter controle de estoque para os itens de material. |
| `AcompanhaEntrega` | integer (int32) |  | Acompanha entrega (0 - Não 1 - Sim). Se vai acompanhar entrega dos itens de material. |
| `DataPrevisaoEntrega` | string (date-time) |  | Data de previsão para entrega do itens de material. |
| `HistoricoLancContabilApagar` | string |  | Histórico de lançamento contábil a pagar |
| `HistoricoLancContabilPago` | string |  | Histórico de lançamento contábil pago |
| `HistoricoLancContabilDescNormalMed` | string |  | Histórico de lançamento contábil do desconto normal já existente na medição |
| `CategoriaMovimentacaoFinanceira` | string |  | Código da categoria de movimentação financeira |
| `Parametro` | [`UAUApi.Models.ProcessoPagamento.ParametroProcesso`](#uauapimodelsprocessopagamentoparametroprocesso) | ✓ | Parametro do processo de pagamento |
| `DocumentoFiscal` | [`UAUApi.Models.ProcessoPagamento.DocumentoFiscalMedicao`](#uauapimodelsprocessopagamentodocumentofiscalmedicao) |  | Objeto com os dados da nota fiscal para o processo de serviço/material da medição. |
| `Parcelas` | array de [`UAUApi.Models.ProcessoPagamento.ParcelaProcessoMedicao`](#uauapimodelsprocessopagamentoparcelaprocessomedicao) | ✓ | Parcelas do processo de pagamento |
| `Itens` | array de [`UAUApi.Models.ProcessoPagamento.ItensProcessoMedicao`](#uauapimodelsprocessopagamentoitensprocessomedicao) |  | Itens do processo de pagamento.  É obrigatório quando o contrato não possui vínculos por item.  Se informar os itens mesmo o contrato sendo vinculado por item, serão coletadas apenas as informações de Cap e categoria de movimentação financeira. As demais informações serão preenchidas com o resultado da consulta dos itens da medição. |

### UAUApi.Models.ProcessoPagamento.ItensProcessoMedicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroItemContrato` | integer (int32) | ✓ | Número do item no contrato |
| `ItemMedicao` | string | ✓ | Código do item da medição |
| `Quantidade` | number (double) | ✓ | Quantidade do item |
| `Preco` | number (double) | ✓ | Preço unitário do item |
| `Cap` | string |  | código do cap |
| `CategoriaMovimentacaoFinanceira` | string |  | Código da categoria de movimentação financeira |
| `VinculoPL` | array de [`UAUApi.Models.ProcessoPagamento.VinculoPLMedicao`](#uauapimodelsprocessopagamentovinculoplmedicao) |  | Vínculo com planejamento. É obrigatório quando o contrato não possui vínculos por item.  Quando o contrato é vinculado por item, as informações dos vínculos serão preenchidas  com o resultado da consulta dos vínculos dos itens do contrato. Os valores dos vínculos também serão calculados de forma automática. |

### UAUApi.Models.ProcessoPagamento.VinculoPLMedicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Item` | string | ✓ | Item do planejamento |
| `CodigoProduto` | integer (int32) | ✓ | Código do produto do planejamento |
| `Contrato` | number (double) | ✓ | Código do contrato do planejamento |
| `Servico` | string | ✓ | Código do serviço no planejamento |
| `Insumo` | string | ✓ | Código do insumo no planejamento |
| `Quantidade` | number (double) | ✓ | Quantidade vinculada |
| `Preco` | number (double) | ✓ | Preço aprovado |
| `numeroItemContrato` | integer (int32) |  | Numero do item que pertence ao contrato, para vincular a Si como adiantamento de contrato. |

### UAUApi.Models.ProcessoPagamento.ParcelaProcessoMedicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Datavencimento` | string (date-time) | ✓ | Data de vencimento |
| `Valor` | number (double) | ✓ | Valor da parcela |
| `Descontos` | array de [`UAUApi.Models.ProcessoPagamento.DescontoParcela`](#uauapimodelsprocessopagamentodescontoparcela) |  | Objeto com descoto da parcela |
| `Banco` | string |  | Código do banco |
| `Conta` | string |  | Código da conta |
| `Convenio` | string |  | Convênio |
| `TipoEmissao` | string |  | Código do tipo de emissão |
| `FormaPagamento` | string |  | Código da forma de pagamento |
| `TipoPagamento` | string |  | Código do tipo de pagamento |

### UAUApi.Models.ProcessoPagamento.DescontoParcela

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Descricao` | string |  | Descrição do desconto |
| `Valor` | number (double) | ✓ | Valor do desconto |
| `DataVencimento` | string (date-time) | ✓ | Data de vencimento |
| `Cap` | string |  | Cap |
| `HistoricoLancamentoContabil` | string |  | Histórico lançamento contábil |

### UAUApi.Models.ProcessoPagamento.DocumentoFiscalMedicao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `DocumentoFiscalServico` | [`UAUApi.Models.ProcessoPagamento.DocumentoFiscal`](#uauapimodelsprocessopagamentodocumentofiscal) |  | Objeto com os dados da nota fiscal para processo de serviço da medição. |
| `DocumentoFiscalMaterial` | [`UAUApi.Models.ProcessoPagamento.DocumentoFiscal`](#uauapimodelsprocessopagamentodocumentofiscal) |  | Objeto com os dados da nota fiscal para processo de material da medição. |

### UAUApi.Models.ProcessoPagamento.DocumentoFiscal

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroNota` | integer (int32) |  | Número auxiliar da nota fiscal |
| `SerieNota` | string |  | Série da nota fiscal |
| `EspecieNota` | string | ✓ | Espécie da nota fiscal  ( NF, CT, RE, OU, CF) |
| `TipoNota` | integer (int32) | ✓ | Tipo da nota: (0 - Estadual, 1 - Municipal, 2 - Mista) |
| `NFEletronica` | integer (int32) | ✓ | Nota fiscal eletrônica: (0 - Não, 1 - Sim) |
| `ChaveNFe` | string |  | Chave NFe da nota fiscal |

### UAUApi.Models.ProcessoPagamento.ParametroProcesso

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoDepartamento` | string |  | Código do departamento |
| `TaxaJuros` | number (double) |  | Percentual do juros |
| `TaxaMulta` | number (double) |  | Percentual de multa. |
| `TipoJuros` | integer (int32) |  | Tipo de juros (0 = Juros simples , 1 =  Juros composto). |
| `Retroagir` | integer (int32) |  | Valor retroagir |
| `IndiceReajuste` | string |  | Índice de reajuste |
| `DataIncioReajuste` | string (date-time) |  | Data que inicia o reajuste |
| `CodigoMunicipio` | integer (int32) |  | Código do município de prestação de serviço |
| `VincularDocFiscalTodosProcessos` | boolean |  | Indicar se irá vincular documento fiscal em todos os processos/descontos vinculados. True    : Vincula. False   : Não vincula. |

### UAUApi.Models.ProcessoPagamento.GravarProcessoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | <list type="bullet">   <item>Código da empresa no UAU.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Obra` | string | ✓ | <list type="bullet">   <item>Código da obra no UAU.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `CodigoFornecedor` | integer (int32) | ✓ | <list type="bullet">   <item>Código do fornecedor no UAU.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `TipoProcesso` | integer (int32) | ✓ | <list type="bullet">   <item>Tipos de processo de pagamento no UAU.</item>   <item>     1 - Processo de Pagamento   </item>   <item>     11 - Compra de patrimônio   </item>   <item>     13 - Adiantamento de caixa de obra   </item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `ControlarEstoque` | integer (int32) | ✓ | <list type="bullet">   <item>Controlar estoque. Se vai controlar estoque e o tipo de processo for 1 - Processo de pagamento,<br> então o tipo de processo passa a ser 2 - Compra rápida.</br></item>   <item>     0 - Não   </item>   <item>     1 - Sim   </item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `AcompanhaEntrega` | integer (int32) | ✓ | <list type="bullet">   <item>Acompanha entrega. Se vai acompanhar entrega e o tipo de processo for 1 - Processo de pagamento,<br> então o tipo de processo passa a ser 10 - Tipo Solicit. Pagamento c/ Acomp. de Entrega.</br></item>   <item>     0 - Não   </item>   <item>     1 - Sim   </item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `DataPrevisaoEntrega` | string (date-time) |  | <list type="bullet">   <item>Data de previsão para entrega. Caso o tipo de processo seja igual a 13 - Adiantamento de caixa,<br> a data de previsão para entrega não será considerada.</br></item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TipoItem` | integer (int32) | ✓ | <list type="bullet">   <item>Tipo do item:</item>   <item>     0 - Insumos gerais   </item>   <item>     1 - Insumos planejados   </item>   <item>     2 - Composições gerais   </item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `HistoricoLancContabil` | string |  | <list type="bullet">   <item>Histórico de lançamento contábil.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `HistoricoLancContabilPago` | string |  | <list type="bullet">   <item>Histórico de lançamento contábil pago.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CategoriaMovimentacaoFinanceira` | string |  | <list type="bullet">   <item>Código da categoria de movimentação financeira.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `NumeroContrato` | integer (int32) |  | <list type="bullet">   <item>Código do contrato de material e serviço, onde o processo será adicionado como adiantamento de contrato.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Parametro` | [`UAUApi.Models.ProcessoPagamento.ParametroProcesso`](#uauapimodelsprocessopagamentoparametroprocesso) | ✓ | <list type="bullet">   <item>Parâmetros do processo de pagamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Parcelas` | array de [`UAUApi.Models.ProcessoPagamento.ParcelaProcesso`](#uauapimodelsprocessopagamentoparcelaprocesso) | ✓ | <list type="bullet">   <item>Parcelas do processo de pagamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Itens` | array de [`UAUApi.Models.ProcessoPagamento.ItensProcesso`](#uauapimodelsprocessopagamentoitensprocesso) | ✓ | <list type="bullet">   <item>Itens do processo de pagamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `DescontoVinculado` | array de [`UAUApi.Models.ProcessoPagamento.ProcessoVinculado`](#uauapimodelsprocessopagamentoprocessovinculado) |  | <list type="bullet">   <item>Descontos vinculados.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `SolicitacaoCaixaObra` | [`UAUApi.Models.ProcessoPagamento.AprovarSolicitacaoCXO`](#uauapimodelsprocessopagamentoaprovarsolicitacaocxo) |  | <list type="bullet">   <item>Aprovar Solicitação.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `PermiteBoletoVencido` | boolean |  | <b>Permite Boleto Vencido</b> <list type="bullet">   <item>     True - Permite alterar o processo se a data de vencimento for menor que a data de prorrogação.</item>   <item>     False - Não permite alterar.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |

### UAUApi.Models.ProcessoPagamento.AprovarSolicitacaoCXO

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroSolicitacao` | integer (int32) |  | <list type="bullet">   <item>Número da solicitação.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `UsuarioAprovacao` | string |  | <list type="bullet">   <item>Usuário responsável pela aprovação.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Empresa` | integer (int32) |  | <list type="bullet">   <item>Código da empresa.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Obra` | string |  | <list type="bullet">   <item>Código da obra.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `NumeroProcesso` | integer (int32) |  | <list type="bullet">   <item>Número do processo.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |

### UAUApi.Models.ProcessoPagamento.ProcessoVinculado

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Descricao` | string |  | <list type="bullet">   <item>Descrição do desconto.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `DataVencimento` | string (date-time) |  | <list type="bullet">   <item>Data de vencimento do desconto.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Valor` | number (double) |  | <list type="bullet">   <item>Valor do desconto.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Cap` | string |  | <list type="bullet">   <item>CAP do desconto.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CodigoFornecedor` | integer (int32) |  | <list type="bullet">   <item>Código do fornecedor do desconto.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Nominal` | string |  | <list type="bullet">   <item>Pessoa a qual o cheque será nominal.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `ItemProcesso` | string |  | <list type="bullet">   <item>Código do item do processo a vincular no desconto.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `ObraFiscal` | string |  | <list type="bullet">   <item>Código da obra fiscal.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `HistoricoLancamentoContabilPagar` | string |  | <list type="bullet">   <item>Histórico de lançamento contábil a pagar.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `HistoricoLancamentoContabilPago` | string |  | <list type="bullet">   <item>Histórico de lançamento contábil pago.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CategoriaMovimentacaoFinanceira` | string |  | <list type="bullet">   <item>Código da categoria de movimentação financeira do desconto.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |

### UAUApi.Models.ProcessoPagamento.ItensProcesso

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Item` | string | ✓ | <list type="bullet">   <item>Código do item.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Quantidade` | number (double) | ✓ | <list type="bullet">   <item>Quantidade do item.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Preco` | number (double) | ✓ | <list type="bullet">   <item>Preço unitário do item.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Cap` | string |  | <list type="bullet">   <item>Código do CAP.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CategoriaMovimentacaoFinanceira` | string |  | <list type="bullet">   <item>Código da categoria de movimentação financeira.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Unidade` | string | ✓ | <list type="bullet">   <item>Código da unidade do item.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `VinculoPL` | array de [`UAUApi.Models.ProcessoPagamento.VinculoPL`](#uauapimodelsprocessopagamentovinculopl) | ✓ | <list type="bullet">   <item>Vínculo com planejamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `CodJustificativa` | integer (int32) |  | <list type="bullet">   <item>Código da justificativa do insumo extrapolado.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Justificativa` | string |  | <list type="bullet">   <item>Descrição da justificativa do insumo extrapolado.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |

### UAUApi.Models.ProcessoPagamento.VinculoPL

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Item` | string | ✓ | <list type="bullet">   <item>Item do planejamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `CodigoProduto` | integer (int32) | ✓ | <list type="bullet">   <item>Código do produto do planejamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Contrato` | number (double) | ✓ | <list type="bullet">   <item>Código do contrato do planejamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Servico` | string | ✓ | <list type="bullet">   <item>Código do serviço no planejamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Insumo` | string | ✓ | <list type="bullet">   <item>Código do insumo no planejamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `MesPlanejamento` | string (date-time) | ✓ | <list type="bullet">   <item>Mês do planejamento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Quantidade` | number (double) | ✓ | <list type="bullet">   <item>Quantidade vinculada.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Preco` | number (double) | ✓ | <list type="bullet">   <item>Preço aprovado.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `NumeroItemContrato` | integer (int32) |  | <list type="bullet">   <item>Número do item que pertence ao contrato, para vincular a Si como adiantamento de contrato.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |

### UAUApi.Models.ProcessoPagamento.ParcelaProcesso

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Datavencimento` | string (date-time) | ✓ | <list type="bullet">   <item>Data de vencimento.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Valor` | number (double) | ✓ | <list type="bullet">   <item>Valor da parcela.</item>   <item>     <b>Campo obrigatório.</b>   </item> </list> |
| `Descontos` | array de [`UAUApi.Models.ProcessoPagamento.DescontoParcela`](#uauapimodelsprocessopagamentodescontoparcela) |  | <list type="bullet">   <item>Objeto com desconto da parcela.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `DocumentoFiscal` | [`UAUApi.Models.ProcessoPagamento.DocumentoFiscal`](#uauapimodelsprocessopagamentodocumentofiscal) |  | <list type="bullet">   <item>Objeto com os dados da nota fiscal do processo.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Banco` | string |  | <list type="bullet">   <item>Código do banco.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Conta` | string |  | <list type="bullet">   <item>Código da conta.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `Convenio` | string |  | <list type="bullet">   <item>Convênio.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TipoEmissao` | string |  | <list type="bullet">   <item>Código do tipo de emissão.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `FormaPagamento` | string |  | <list type="bullet">   <item>Código da forma de pagamento.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TipoPagamento` | string |  | <list type="bullet">   <item>Código do tipo de pagamento.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `CodigoDeBarras` | string |  | <list type="bullet">   <item>Código de barras de pagamento da parcela.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `PixCopiaCola` | string |  | <list type="bullet">   <item>Pix Copia e Cola.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |
| `TXID` | string |  | <list type="bullet">   <item>TXID decodificado do Pix Copia e Cola.</item>   <item>     <b>Campo não obrigatório.</b>   </item> </list> |

### UAUApi.Models.ProcessoPagamento.GerarNotaFiscalTransportePeloXMLRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ChaveCTe` | string |  | Chave da NFe. Obrigatório apenas quando não for informado o ArquivoXML. |
| `ArquivoXML` | string |  | Arquivo xml. Obrigatório apenas quando não for informado a ChaveCTe. |
| `Empresa` | integer (int32) | ✓ | Número da empresa |
| `Obra` | string | ✓ | código da obra |
| `Processo` | integer (int32) | ✓ | Número do processo |
| `Parcela` | integer (int32) |  | Número da parcela |
| `VincularADescontos` | boolean | ✓ | Vincular a descontos |

### UAUApi.Models.ProcessoPagamento.GerarNotaFiscalServicoPeloXMLRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoFornecedor` | integer (int32) | ✓ | Código do fornecedor da nota fiscal. |
| `Numero` | string |  | Número da nota fiscal. Obrigatório apenas quando não for informado o ArquivoXML. |
| `ChaveNFSe` | string |  | Chave da nota fiscal. Obrigatório apenas quando não for informado o ArquivoXML. |
| `ArquivoXML` | string |  | Arquivo xml. Obrigatório apenas quando não for informado o Número. |
| `Empresa` | integer (int32) | ✓ | Número da empresa |
| `Obra` | string | ✓ | Código da obra |
| `Processo` | integer (int32) | ✓ | Número do processo |
| `Parcela` | integer (int32) |  | Número da parcela |
| `VincularADescontos` | boolean | ✓ | Vincular a descontos |

### UAUApi.Models.ProcessoPagamento.GerarNotaFiscalProdutoPeloXMLRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ChaveNFe` | string |  | Chave da NFe. Obrigatório apenas quando não for informado o ArquivoXML. |
| `ArquivoXML` | string |  | Arquivo xml. Obrigatório apenas quando não for informado o a ChaveNFe. |
| `Empresa` | integer (int32) | ✓ | Número da empresa |
| `Obra` | string | ✓ | Código da obra |
| `Processo` | integer (int32) | ✓ | Número do processo |
| `Parcela` | integer (int32) |  | Número da parcela |
| `VincularADescontos` | boolean | ✓ | Vincular a descontos |

### UAUApi.Models.ProcessoPagamento.GerarNotaFiscalRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Número da empresa |
| `Obra` | string | ✓ | código da obra |
| `NumeroProcesso` | integer (int32) | ✓ | Número do processo |
| `Parcela` | integer (int32) |  | Número da parcela |
| `TipoNF` | integer (int32) — valores possíveis: 0, 1 | ✓ | Tipo da nota fiscal 0 - Estadual 1 - Municipal |
| `Especie` | string | ✓ | Espécie da nota fiscal (NF - Nota fiscal, CT - Conhecimento de transporte, RE - Recibo, OU - Outros, CF - Cupom fiscal) |
| `Serie` | string | ✓ | Série da nota fiscal |
| `NFEletronica` | boolean | ✓ | Indica se a nota fiscal é eletrônica TRUE - É nota fiscal eletrônica FALSE - Não é nota fiscal eletrônica |
| `ChaveNfe` | string |  | Chave da nota fiscal eletrônica |
| `NumeroNotaFiscal` | string | ✓ | Número da nota fiscal |
| `CodigoRemetente` | integer (int32) | ✓ | Código do remetente/destinatário da nota fiscal. |
| `DataEmissao` | string (date-time) | ✓ | Date de emissão da nota fiscal |
| `DataDeEmissaoMaiorQueCadastro` | boolean | ✓ | Permitir que a data de emissão da nota seja maior que a data de cadastro |
| `DataEntrada` | string (date-time) | ✓ | Data de entrada da nota fiscal |
| `DataDeEntradaMaiorQueCadastro` | boolean | ✓ | Permitir que a data de entrada da nota seja maior que a data de cadastro |
| `ModeloNF` | integer (int32) |  | Modelo da nota fiscal (Código controlado pelo UAU). Obrigatório para espécies NF, CT, CF. |
| `ArqNotaFiscal` | string |  | Arquivo da nota nota fiscal convertido em string base 64 para anexar ao processo de pagamento. Para conseguir anexar o arquivo informado, deverá informar o nome do arquivo obrigatoriamente. (Propriedade NomeArquivo) |
| `CaminhoOrigemArquivoLocal` | string |  | Caminho onde o arquivo se encontra na rede local do cliente. Para conseguir mover o arquivo da pasta, deverá informar o nome do arquivo obrigatoriamente. (Propriedade NomeArquivo) (Deverá ser informado o caminho com o dobro de barras para cada barra informada.  EXEMPLO: Caso o caminho do arquivo for \\\\Servidor\documentos\notasFiscais, deverá ser informado \\\\\\\\Servidor\\\\documentos\\\\notasFiscais ao requisitar o serviço) |
| `CaminhoDestinoArquivo` | string |  | Pasta onde o arquivo será salvo.  Caso não informe a pasta, o arquivo será na pasta padrão de arquivos(anexos). Caso seja informado a pasta, será concatenado a pasta informada à pasta padrão de arquivos(anexos). Exemplo: \\\\Servidor\PastaPadrao + \CaminhoDestinoArquivo (Deverá ser informado o caminho da pasta com o dobro de barras para cada barra informada.  EXEMPLO: Caso o caminho da pasta do arquivo for \documentos\notasFiscais, deverá ser informado \\\\documentos\\\\notasFiscais ao requisitar o serviço) |
| `NomeArquivo` | string |  | Nome do arquivo que será anexado. Deverá informar o nome e a extensão do arquivo. |
| `CopiarArquivo` | boolean |  | Identifica se irá copiar o arquivo ao invés de mover TRUE - Irá copiar o arquivo da nota  FALSE - Irá mover o arquivo da nota |
| `VincularADescontos` | boolean |  | Indica ser irá vincular a nota fiscal gerada nos processos vinculados TRUE  - Irá vincular as notas nos demais processos vinculados FALSE - Não irá vincular as notas nos processos vinculados Obs.: Por padrão o valor sempre será TRUE, assim mesmo que não seja informado será vinculado a nota nos processos vinculados. |

### UAUApi.Models.ProcessoPagamento.EmitirParcelasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `parcelas` | array de [`UAUApi.Models.ProcessoPagamento.EmitirParcelaRequest`](#uauapimodelsprocessopagamentoemitirparcelarequest) | ✓ | Lista de processos para serem Aprovados ou Desaprovados. |

### UAUApi.Models.ProcessoPagamento.EmitirParcelaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codEmpresa` | integer (int32) | ✓ | Código da empresa |
| `codObra` | string | ✓ | Código da obra |
| `numeroProcesso` | integer (int32) | ✓ | Número do processo de pagamento |
| `numeroParcela` | integer (int32) | ✓ | Número da parcela |

### UAUApi.Models.ProcessoPagamento.ProcessoPagamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) |  | Código da empresa no UAU |
| `DescrEmpresa` | string |  | Descrição da empresa |
| `Obra` | string |  | Código da obra |
| `DescrObra` | string |  | Descrição da obra |
| `NumeroProcesso` | integer (int32) |  | Número do processo de pagamento |
| `ObraFiscal` | string |  | Código da obra fiscal. (Obs.: Caso o processo tenha parcelamento e existam obras fiscais diferentes nas parcelas do processo, o sistema irá retornar a obra fiscal de uma das parcelas. Validar coerência das obras divergentes.) |
| `CodigoFornecedor` | integer (int32) |  | Código do fornecedor |
| `NomeFornecedor` | string |  | Descrição do fornecedor |
| `CnpjFornecedor` | string |  | CNPJ do fornecedor. |
| `CnpjEmpresa` | string |  | CNPJ da empresa. |
| `InternoExterno` | string |  | Indica se o processo é: (I - Interno ou E - Externo) |
| `TipoProcesso` | integer (int32) |  | Tipo de origem do processo de pagamento 0 - Cotação 1 - Processo de pagamento 2 - Compra rápida 3 - Processo vinculado 4 - Processo transporte 5 - Processo interno 6 - Folha 7 - Medição 8 - Cotação sem estoque 9 - Inicialização de estoque 10 - Acomp. entr. s/ estoque 11 - Compra de patrimônio 12 - Manutenção de patrimônio 13 - Adiantamento de caixa de obra 14 - Repasse de aluguel 15 - Comissão 16 - Retenção contratual 17 - Distrato de venda 18 - Módulo folha de pagamento 19 - Medição complementar 20 - Adiantamento de comissão 21 - Contas e tributos 22 - Processo de securitização 23 - Impostos 24 - Devolução do sinal pago na proposta 25 - Devolução de receita 26 - Acomp. ordem de serviço |
| `EmpresaPagadora` | integer (int32) |  | Código da empresa que irá pagar a ordem de compra |
| `CNPJEmpresaPagadora` | string |  | CNPJ da empresa que irá pagar a ordem de compra |
| `EmpresaFaturar` | integer (int32) |  | Código da empresa responsável pelo faturamento da ordem de compra |
| `CNPJEmpresaFaturar` | string |  | CNPJ da empresa responsável pelo faturamento da ordem de compra |
| `Contato` | string |  | Contato da compra. |
| `Cotacao` | integer (int32) |  | Número da cotação no UAU |
| `Medicao` | integer (int32) |  | Código da medição no UAU |
| `OrdemCompra` | integer (int32) |  | Número da ordem de compra no UAU |
| `NumeroEntrega` | integer (int32) |  | Código da entrega que originou o processo |
| `Usuario` | string |  | Usuário de cadastro do processo |
| `Data` | string (date-time) |  | Data de cadastro do processo |
| `Contrato` | integer (int32) |  | Número do contrato |
| `Parcelas` | array de [`UAUApi.Models.ProcessoPagamento.Parcelas`](#uauapimodelsprocessopagamentoparcelas) |  | Lista com dados das parcelas |
| `Parametro` | [`UAUApi.Models.ProcessoPagamento.DadosParametro`](#uauapimodelsprocessopagamentodadosparametro) |  | Dados dos parâmetros do processo |
| `Itens` | array de [`UAUApi.Models.ProcessoPagamento.Itens`](#uauapimodelsprocessopagamentoitens) |  | Lista com os dados dos itens |

### UAUApi.Models.ProcessoPagamento.Itens

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Item` | string |  | Código do item |
| `DescrItem` | string |  | Descrição do item |
| `NumeroCotacao` | integer (int32) |  | Número de cotação do insumo |
| `Quantidade` | number (double) |  | Quantidade do item |
| `Preco` | number (double) |  | Preço unitário do item |
| `Cap` | string |  | Código do cap |
| `CategoriaMovimentacaoFinanceira` | string |  | Código da categoria de movimentação financeira |
| `Unidade` | string |  | Código da unidade do item |
| `ValorDiferenca` | number (double) |  | Valor da diferença do item a ser somado para bater o total do processo |
| `SubTotal` | number (double) |  | Valor do item sem a somatória da diferença |
| `Total` | number (double) |  | Total do item considerando a diferença. |
| `CodigoItemContrato` | integer (int32) |  | Código do item do no contrato. |
| `VinculosPL` | array de [`UAUApi.Models.ProcessoPagamento.VinculosPL`](#uauapimodelsprocessopagamentovinculospl) |  | Lista com dados do planejamento |

### UAUApi.Models.ProcessoPagamento.VinculosPL

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CodigoInsumo` | string |  | Código do insumo vinculado do processo |
| `Item` | string |  | Item do planejamento |
| `Produto` | integer (int32) |  | Produto do planejamento |
| `Contrato` | integer (int32) |  | Código do contrato do planejamento |
| `Servico` | string |  | Código do serviço no planejamento |
| `Insumo` | string |  | Código do insumo no planejamento |
| `MesPlanejamento` | string (date-time) |  | Mês de planejamento |
| `Quantidade` | number (double) |  | Quantidade vinculada |
| `Preco` | number (double) |  | Preço |
| `TaxaAprovacao` | number (double) |  | Porcentagem aprovada por serviço |
| `Desconto` | number (double) |  | Valor do desconto |
| `Acrescimo` | number (double) |  | Valor acréscimo |
| `ValorExcluido` | number (double) |  | Valor da parcela excluída do processo |
| `TaxaItem` | number (double) |  | Porcentual da SI sobre o item do processo ao qual ele pertence. |

### UAUApi.Models.ProcessoPagamento.DadosParametro

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `QtdeCasaDecimais` | integer (int32) |  | Quantidade de casas decimais para o campo de quantidade. |
| `QtdeCasaDecimaisPreco` | integer (int32) |  | Quantidade de casas decimais para o campo de preço unitário. |
| `CodigoDepartamento` | string |  | Código do departamento |
| `ReterImposto` | boolean |  | Define se vai reter imposto (true - Sim, False - Não). |
| `TipoImposto` | integer (int32) |  | Define o tipo do imposto (0 - IRRF, 1 - IRPJ ,2 - PIS, 3 - COFINS , 4 - Contribuição Social, 5 - INSS , 6 - ISS ). |
| `Aliquota` | number (double) |  | Alíquota que foi usada para calcular o valor do imposto. |
| `DataBaseImposto` | string (date-time) |  | Data base do imposto, mês e ano. |
| `Protocolo` | integer (int32) |  | Número do protocolo de entrega de documentos. |
| `Antecipado` | boolean |  | Indica se é antecipado (True - Sim, False - Não). |
| `TipoFolha` | integer (int32) |  | Tipo de folha (1 - Empréstimo 2 - Encargos) |
| `MedicaoZero` | boolean |  | Medição zero (True - Sim, False - Não). |
| `TaxaJurosAtraso` | number (double) |  | Percentual de juros a ser aplicado em caso de atraso. |
| `TaxaMultaAtraso` | number (double) |  | Percentual de multa a ser aplicada em caso de atraso. |
| `TipoJuros` | integer (int32) |  | Tipo de juros (0 = Juro simples percentual, 1 =  Juro composto percentual). |
| `QtdeParcelas` | integer (int32) |  | Quantidade total de parcelas. |
| `Retroagir` | integer (int32) |  | Valor retroagir |
| `CodigoServicoFiscal` | integer (int32) |  | Número do código do serviço fiscal |
| `CidadePracaPgto` | integer (int32) |  | Número da cidade da praça de pagamento da prestação de serviço |
| `ChaveNFe` | string |  | Número da chave de acesso da NFe. |
| `StatusNFe` | integer (int32) |  | Status da NFe (0 - Sem pendência; 1 - Pendente de Geração; 2 - Pendente de validação). |
| `EmpresaPaiReembolso` | integer (int32) |  | Código da empresa pai para processo de reembolso. |
| `ObraPaiReembolso` | string |  | Código da obra pai pra processo de reembolso |
| `ProcessoPaiReembolso` | integer (int32) |  | Número do processo pai para reembolso |
| `NovoBeneficiario` | integer (int32) |  | Código do novo beneficiário |
| `ApropriarDataPgto` | boolean |  | Apropriar por data de pagamento(True - Sim, False - Não) |

### UAUApi.Models.ProcessoPagamento.ConsultarProcessoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Processos` | array de [`UAUApi.Models.ProcessoPagamento.Processo`](#uauapimodelsprocessopagamentoprocesso) |  | Lista de processos de pagamento |
| `EmpresaObraPeriodo` | [`UAUApi.Models.ProcessoPagamento.EmpresaObraPeriodo`](#uauapimodelsprocessopagamentoempresaobraperiodo) |  | Consulta por empresa, obra e período(data de cadastro do processo) |
| `FornecedorPeriodo` | [`UAUApi.Models.ProcessoPagamento.FornecedorPeriodo`](#uauapimodelsprocessopagamentofornecedorperiodo) |  | Buscar os processos de pagamento específicos de um fornecedor pelo seu CNPJ ou CPF |

### UAUApi.Models.ProcessoPagamento.FornecedorPeriodo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Fornecedor` | array de [`UAUApi.Models.ProcessoPagamento.Fornecedor`](#uauapimodelsprocessopagamentofornecedor) |  | Lista com o CNPJ ou CPF |
| `PeriodoInicial` | string (date-time) | ✓ | Data inicial para aplicar o filtro |
| `PeriodoFinal` | string (date-time) | ✓ | Data final para aplicar o filtro |

### UAUApi.Models.ProcessoPagamento.Fornecedor

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpjFornecedor` | string | ✓ | CNPJ do fornecedor |

### UAUApi.Models.ProcessoPagamento.EmpresaObraPeriodo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `EmpresaObra` | array de [`UAUApi.Models.ProcessoPagamento.EmpresaObra`](#uauapimodelsprocessopagamentoempresaobra) |  | Lista com código de empresa e código da obra |
| `PeriodoInicial` | string (date-time) | ✓ | Data inicial para aplicar o filtro |
| `PeriodoFinal` | string (date-time) | ✓ | Data final para aplicar o filtro |

### UAUApi.Models.ProcessoPagamento.EmpresaObra

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |

### UAUApi.Models.ProcessoPagamento.Processo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `NumeroProcesso` | integer (int32) | ✓ | Número do processo de pagamento |
| `Empresa` | integer (int32) | ✓ | Código da empresa |
| `Obra` | string | ✓ | Código da obra |

### UAUApi.Models.ProcessoPagamento.ConfirmarParcelasRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `parcelas` | array de [`UAUApi.Models.ProcessoPagamento.ConfirmaParcelaRequest`](#uauapimodelsprocessopagamentoconfirmaparcelarequest) | ✓ | Lista de processos para serem Aprovados ou Desaprovados. |

### UAUApi.Models.ProcessoPagamento.ConfirmaParcelaRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `codEmpresa` | integer (int32) | ✓ | Código da empresa |
| `codObra` | string | ✓ | Código da obra |
| `numeroProcesso` | integer (int32) | ✓ | Número do processo de pagamento |
| `numeroParcela` | integer (int32) | ✓ | Número da parcela |
| `confirmaBoletoDivergenteProcesso` | boolean | ✓ | Define confirmação do código de barras com valor ou data divergente do processo |
| `confirmaProcessoPagamentoDuplicado` | boolean | ✓ | Define confirmação quando existe outro processo em emissão pago, onde o documento fiscal vínculado a ele possui mesmo VALOR e FORNECEDOR do documento fiscal vínculado ao processo da empresa |

### Globaltec.UAU.Comp.ResultadoExecucaoResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `sucesso` | boolean |  |  |
| `mensagem` | string |  |  |

### UAUApi.Models.ProcessoPagamento.AprovarProcessosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `processos` | array de [`UAUApi.Models.ProcessoPagamento.AprovarProcessoRequest`](#uauapimodelsprocessopagamentoaprovarprocessorequest) | ✓ | Lista de processos para serem Aprovados ou Desaprovados. |

### UAUApi.Models.ProcessoPagamento.AprovarProcessoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cod_empresa` | integer (int32) |  | Código da empresa |
| `cod_obra` | string |  | Código da obra |
| `numero_processo` | string |  | Número do processo de pagamento |
| `numero_parcela` | string |  | Número da parcela |
| `tipo_processo` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27 |  | Tipo de origem das parcelas do processo geradas: - [0]: Cotação - [1]: Processo de pagamento - [2]: Compra rápida - [3]: Processo vinculado - [4]: Processo transporte - [5]: Processo interno - [6]: Folha - [7]: Medição - [8]: Cotação sem estoque - [9]: Inicialização de estoque - [10]: Acompanhamento entr. s/ estoque - [11]: Compra de patromônio - [12]: Manutenção de patromônio - [13]: Adiantamento de caixa de obra - [14]: Repasse de aluguel - [15]: Comissão - [16]: Retenção contratual - [17]: Distrato de venda - [18]: Módulo folha de pagamento - [19]: Medição complementar - [20]: Adiantamento de comissão - [21]: Contas e tributos - [22]: Processo de securitização  - [23]: Impostos - [24]: Devolução do sinal pago na proposta - [25]: Devolução de receita - [26]: Acompanhamento de ordem de serviço - [27]: Distribuição de lucros/dividendos - [28]: Venda de carteira |
| `aprovaro_processo` | integer (int32) — valores possíveis: 0, 1, 2 |  | Indica se o usuário quer ([0] - Desaprovar, [1] - Aprovar e [2] - Reprovar) as parcelas do processo. |
| `login_usuario` | string |  | Login do usuário |
| `departamento` | string |  | Departamento do usuário que irá realizar a aprovação |
| `cargo` | string |  | Cargo do usuário que irá realizar a aprovação |
| `codigoJustificativa` | integer (int32) |  | Código da justificativa, caso esteja aprovando fora da sequência definida de aprovações |
| `observacaoJustificativa` | string |  | Observação da justificativa quando estiver aprovando fora da sequência |

### UAUApi.Models.ProcessoPagamento.DVQGravarRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `dvq` | string | ✓ | DVQ (Confirmação de [D]ata, [V]alor e [Q]uantidade da parcela do processo). |
| `aprovar` | boolean | ✓ | Define se irá aprovar a parcela. |
| `usuario` | string | ✓ | Login do usuário. |
| `sobreporAprovacoesDeOutrosUsuarios` | boolean | ✓ | Define se a aprovação do usuário atual irá sobrepor as outras aprovações existentes. |
| `parcelas` | array de [`UAUApi.Models.ProcessoPagamento.DVQParcelas`](#uauapimodelsprocessopagamentodvqparcelas) | ✓ | Lista com a confirmação DVQ das parcelas. |

### UAUApi.Models.ProcessoPagamento.DVQParcelas

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_processo` | integer (int32) |  | Número do processo. |
| `numero_parcela` | integer (int32) |  | Número da parcela. |
| `codigo_empresa` | integer (int32) |  | Código da empresa. |
| `nome_empresa` | string |  | Nome da empresa. |
| `codigo_obra` | string |  | Código da obra. |
| `nome_obra` | string |  | Nome da obra. |
| `valor_total` | number (double) |  | Valor total do processo. |
| `status_d` | string |  | Status atual da aprovação "D" - Valor [A]: aprovado - Valor [D]: não aprovado |
| `status_v` | string |  | Status atual da aprovação "V" - Valor [A]: aprovado - Valor [D]: não aprovado |
| `status_q` | string |  | Status atual da aprovação "Q" - Valor [A]: aprovado - Valor [D]: não aprovado |
| `codigo_departamento` | string |  | Código do Departamento |
| `status_processo` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4 |  | Referente ao status do processo. - [0]: Contas a pagar - [1]: Emissão de pagamentos - [2]: Contas pagas - [3]: Enviado ao Banco - [4]: Todos |
| `tipo_DocProcesso` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27 |  | Tipo de origem das parcelas do processo geradas: - [0]: Cotação - [1]: Processo de pagamento - [2]: Compra rápida - [3]: Processo vinculado - [4]: Processo transporte - [5]: Processo interno - [6]: Folha - [7]: Medição - [8]: Cotação sem estoque - [9]: Inicialização de estoque - [10]: Acompanhamento entr. s/ estoque - [11]: Compra de patromônio - [12]: Manutenção de patromônio - [13]: Adiantamento de caixa de obra - [14]: Repasse de aluguel - [15]: Comissão - [16]: Retenção contratual - [17]: Distrato de venda - [18]: Módulo folha de pagamento - [19]: Medição complementar - [20]: Adiantamento de comissão - [21]: Contas e tributos - [22]: Processo de securitização  - [23]: Impostos - [24]: Devolução do sinal pago na proposta - [25]: Devolução de receita - [26]: Acompanhamento de ordem de serviço - [27]: Distribuição de lucros/dividendos |
| `adiantamento_parcela` | integer (int32) |  | Adiantamento da parcela |
| `valor_parcela` | number (double) |  | Valor da parcela |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.ProcessoPagamento.GravarAcrescimoDescontoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Empresa` | integer (int32) | ✓ | <list type="bullet">   <item>Código da empresa no UAU.</item>   <item>Campo obrigatório.</item> </list> |
| `Obra` | string | ✓ | <list type="bullet">   <item>Código da obra no UAU.</item>   <item>Campo obrigatório.</item> </list> |
| `NumeroDoProcesso` | integer (int32) | ✓ | <list type="bullet">   <item>Número do processo de pagamento no UAU.</item>   <item>Campo obrigatório.</item> </list> |
| `NumeroDaParcela` | integer (int32) | ✓ | <list type="bullet">   <item>Número da parcela do processo de pagamento no UAU.</item>   <item>Campo obrigatório.</item> </list> |
| `Data` | string (date-time) | ✓ | <list type="bullet">   <item>Data do acréscimo a ser inserido no processo.</item>   <item>Campo obrigatório.</item> </list> |
| `Valor` | number (double) | ✓ | <list type="bullet">   <item>Valor do acréscimo ou desconto. Positivo = acréscimo, negativo = desconto. Percentuais não são aceitos.</item>   <item>Campo obrigatório.</item> </list> |
| `Descricao` | string |  | <list type="bullet">   <item>Texto livre limitado conforme tabela do banco de dados.</item> </list> |
| `CAP` | string |  | <list type="bullet">   <item>Código fiscal a ser utilizado no processamento contábil do ajuste.</item> </list> |
| `HistoricoContabil` | string |  | <list type="bullet">   <item>Texto opcional que será enviado à contabilidade como histórico da movimentação</item> </list> |
| `TipoCalc` | integer (int32) |  | <list type="bullet">   <item>Campo opcional que irá definir se o desconto entra ou não na base de cálculo</item> </list> |

### Globaltec.UAU.Comp.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CampoValidado` | string |  |  |
| `Tipo` | integer (int32) — valores possíveis: 0, 1 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `QuantidadeMensagens` | integer (int32) |  |  |
| `Continua` | boolean |  |  |
