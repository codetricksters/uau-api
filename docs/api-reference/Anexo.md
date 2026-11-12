# Anexo

## POST `/api/v{version}/Anexo/AnexarArquivo`

**Anexa um arquivo**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
1. Anexa arquivo dentro do UAU, utilizando a chave identificadora para fazer o vinculo desse arquivo com algum parametro dentro do sistema. 

Parâmetros da request
1. arquivo: Conteúdo do arquivo em base 64
2. nome: Nome do arquivo
3. caminho: Caminho do arquivo
4. identificador: Chave identificadora do arquivo no formato "STRING STRING"
5. usuario: Login do usuário
6. caminhoExclusivo: String correspondente a configuração em configGerais do caminho exclusivo

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.AnexarArquivoRequest`](#uauapimodelsanexoanexararquivorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Anexo |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/AnexarArquivosBase64Request`

**Anexar um arquivo**

Definição técnica:
- Realiza o anexo de um arquivo de acordo com os parâmetros enviados na requisição.

Pré requisito:
- Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
    - URL + /api/v{version}/Anexo/ConsultarChavesComentario

Parâmetros da request:
1. Arquivo: Conteúdo do arquivo em Base64 sem prefixos.
2. Nome: Nome do arquivo.
3. Caminho: Caminho de armazenamento do arquivo.
4. Identificador: Chave identificadora no formato "STRING STRING". (Exemplo de padrão de utilização do identificador: "PROCESSO 123-1234-OBRA1")
5. Usuario: Usuário logado responsável pela operação.
6. Extensao: Extensão do arquivo (png, jpeg, etc.).
7. CaminhoExclusivo (Opcional): Configuração de caminho exclusivo em ConfigGerais.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.AnexarArquivosBase64Request`](#uauapimodelsanexoanexararquivosbase64request)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Anexo |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/AnexarBase64Imagem`

**Anexa uma imagem na base64**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Definição de Negócio:
Possibilita anexar imagem no formato Base64

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.AnexarBase64ImagemRequest`](#uauapimodelsanexoanexarbase64imagemrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Anexo |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/BaixarArquivos`

**Retorna um arquivo ZIP contendo os arquivos informados por caminho.**

<b>Definição Técnica:</b>
<list type="number">
  <item>Autenticar o usuário cliente via URI: /api/v{version}/Autenticador/AutenticarUsuario</item>
  <item>Preencher os parâmetros de request para uso do método.</item>
  <item>Utilizar a rota Anexo/ListaArquivoPorChave para obter os caminhos completos dos arquivos.</item>
</list>
<b>Parâmetros do Request:</b>
<list type="bullet">
  <item>
    CaminhoCompleto: Caminho completo do arquivo que deverá ser compactado para ZIP.</item>
  <item>
    Origem (Obrigatório):
    <list type="bullet">
      <item>
        1 - Caminho local / rede</item>
      <item>
        2 - Caminho AWS.</item>
    </list>
  </item>
</list>

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.BaixarArquivosRequest`](#uauapimodelsanexobaixararquivosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Arquivo |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/ConsultarChavesComentario`

**Retorna as chaves, seus campos e exemplo, que podem ser utilizadas para gravação de comentario em anexo.**

Definição técnica:
- Este endpoint oferece suporte para o seguinte endpoint: [URI + /api/v{version}/Anexo/GravarComentarioAnexo]
- Retorna objetos com:
    - Possíveis chaves que podem ser utilizadas.
    - Ordem dos parâmetros aceitos.
    - Exemplo de utilização e formatação dos parâmetros.
 Anexos:
- Exemplo Postman: https://ajuda.globaltec.com.br/download/777152/

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso | [`UAUApi.Models.ResultadoExecucao`](#uauapimodelsresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/ExcluirAnexos`

**Exclui o vinculo do anexo ao arquivo.**

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.       

Parâmetros da request
1. identificador: Chave identificadora do arquivo no formato "STRING STRING".
2. nome_arquivo: Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
3. origem: Indica o tipo de armazenamento será utilizado para excluir o vinculo ao arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.ExcluirAnexosRequest`](#uauapimodelsanexoexcluiranexosrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Operação concluída (success/partial). |  |
| 400 | Requisição inválida. |  |
| 404 | Nenhum anexo localizado. |  |
| 500 | Erro ao processar a requisição. |  |

---

## POST `/api/v{version}/Anexo/GravarComentarioAnexo`

**Anexar um comentario**

Definição técnica:
- Adiciona comentário anexo de acordo com os parâmetros passados na requisição.

Pré requisito:
- Verifique o endpoint abaixo para obter informações dos parametros de entrada aceitos:
    - URL + /api/v{version}/Anexo/ConsultarChavesComentario
    
Parâmetros da request
1. Chave: Chave para consulta.
2. Campos: Campos obrigatórios para a chave="Venda" (empresa, obra, venda). Campos obrigatórios para a chave="Contrato" (Empresa, Contrato) Deve ser inserido juntos, separados por virgula.
3. Usuario: Usuário logado.
4. Comentario: Comentário a ser anexado.
5. TipoComentario: Armazena o tipo do comentário ( 0-Publico, 1-Privado, 2-Interna).
6. UsuarioPrivado: Armazena a lista de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -&gt; /Usuarios/ConsultarUsuariosAtivos ).
7. GrupoPrivado: Armazena a lista de grupos de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -&gt; /Usuarios/ConsultarGruposDeUsuario ).

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.AnexarComentarioRequest`](#uauapimodelsanexoanexarcomentariorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Requisição realizada com sucesso | [`UAUApi.Models.ResultadoExecucao`](#uauapimodelsresultadoexecucao) |
| 400 | Não foi possível realizar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/ListaArquivoPorChave`

**Retorna todos os arquivos relacionados com a chave, incluindo nome e caminho completo.**

<b>Definição Técnica:</b>
<list type="number">
  <item>Autenticar o usuário cliente via URI: /api/v{version}/Autenticador/AutenticarUsuario</item>
  <item>Preencher os parâmetros de request para uso do método.</item>
</list>
<b>Parâmetros da Request:</b>
<list type="bullet">
  <item>
    chave: Identificador do arquivo.</item>
  <item>
    valores: Valores identificadores do arquivo.</item>
</list>
 
 Para obter as chaves de utilização na requisição, utilize a rota:  
 Anexo/ConsultarChavesComentario

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.ListaArquivoPorChaveRequest`](#uauapimodelsanexolistaarquivoporchaverequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Arquivo |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/ListarArmazenamentos`

**Retorna a lista de armazenamentos ativos**

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Lista de armazenamentos de arquivos | array de [`Globaltec.UAU.Geral.AppService.Integracao.Armazenamento.Interfaces.ITipoArmazenamento`](#globaltecuaugeralappserviceintegracaoarmazenamentointerfacesitipoarmazenamento) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/ListarDiretorios`

### DEFINIÇÕES TÉCNICAS
    * Status 200 - Retorna uma lista de diretórios

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.DiretorioRequest`](#uauapimodelsanexodiretoriorequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Lista de diretorios | array de [`Globaltec.UAU.Geral.AppService.Arquivos.Interfaces.IArquivo`](#globaltecuaugeralappservicearquivosinterfacesiarquivo) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/RetornaArquivoEmBytes`

**Retorna um determinado arquivo em base64.**

Em Modulo UAU &gt;&gt; Utilitários &gt;&gt; Configurações do sistema &gt;&gt; ( Em "Arquivo" &gt;&gt; Arquivos(Anexos): ) Esse e o caminho padrão que a rota usar na consulta para retorna o arquivo em base64.


Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.

Parâmetros da request
1. nome_arquivo: Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )
2. origem: Indica o tipo de armazenamento será utilizado para buscar o arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão.

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.RetornaArquivoEmBytesRequest`](#uauapimodelsanexoretornaarquivoembytesrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Arquivo em bytes |  |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## POST `/api/v{version}/Anexo/RetornarArquivosEmListaBytes`

**Retorna uma lista com os dados dos arquivos e o conteúdo do mesmo em base64.**

Baseado no ‘’código identificador do documento’’ passado ele já retorna os arquivos tanto disponível localmente e na nuvem, sem a necessidade de passar o parâmetro “origem” no body do request.
        

Definição Técnica:
1. Autenticar o usuário cliente URI + /api/v{version}/Autenticador/AutenticarUsuario
2. Preencher os parâmetros de request para uso do método.       

Parâmetros da request
1. empresa: Número da empresa.
2. identificador: Chave identificadora do arquivo no formato "STRING STRING".
3. listanomes_arquivos:  Lista de 'string' com o nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png )

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|---|---|---|---|---|
| `version` | path | string | ✓ |  |
| `Authorization` | header | string | ✓ | Token Authentication |
| `X-INTEGRATION-Authorization` | header | string | ✓ | Token De Integração |

### Corpo da requisição

Obrigatório: ✓  
Esquema: [`UAUApi.Models.Anexo.RetornarArquivosEmListaBytesRequest`](#uauapimodelsanexoretornararquivosemlistabytesrequest)

### Respostas

| Status | Descrição | Esquema |
|---|---|---|
| 200 | Lista com os dados dos arquivos e o conteúdo do mesmo em base64. | array de [`Globaltec.UAU.Comp.GerAnexo.EstruturaAnexo`](#globaltecuaucompgeranexoestruturaanexo) |
| 500 | Ocorreu um erro ao processar sua requisição. | [`UAUApi.ResponseHandler`](#uauapiresponsehandler) |

---

## Esquemas

### Globaltec.UAU.Comp.GerAnexo.EstruturaAnexo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ConteudoArquivo` | string (byte) |  |  |
| `NomeArquivo` | string |  |  |
| `CaminhoArquivo` | string |  |  |
| `Identificador` | string |  |  |
| `Origem` | integer (int32) |  |  |
| `NomeBucker` | string |  |  |

### UAUApi.Models.Anexo.RetornarArquivosEmListaBytesRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `empresa` | string |  | Número da empresa |
| `identificador` | string | ✓ | Chave identificadora do arquivo no formato "STRING STRING" |
| `listanomes_arquivos` | array de string |  | Lista de 'string' com o nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png ) |

### UAUApi.Models.Anexo.RetornaArquivoEmBytesRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome_arquivo` | string |  | Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png ) |
| `origem` | integer (int32) |  | Indica o tipo de armazenamento será utilizado para buscar o arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão. |

### Globaltec.UAU.Geral.AppService.Arquivos.Interfaces.IArquivo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `bytes` | string (byte) |  |  |
| `Diretorio` | string |  |  |
| `Nome` | string |  |  |
| `Tamanho` | string |  |  |
| `Tipo` | string |  |  |
| `Url` | string |  |  |
| `Origem` | integer (int32) |  |  |
| `Extensao` | string |  |  |
| `isArquivo` | boolean |  |  |
| `Parent` | string |  |  |
| `CaminhoExclusivo` | string |  |  |
| `ControlaAnexoUAUWeb` | boolean |  |  |
| `Usuario` | string |  |  |
| `Identificador` | string |  |  |
| `Empresa` | integer (int32) |  |  |
| `IsRenomear` | boolean |  |  |
| `Caminho` | string |  |  |
| `CaminhoPadrao` | string |  |  |

### UAUApi.Models.Anexo.DiretorioRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Caminho` | string |  |  |
| `Origem` | integer (int32) |  |  |

### Globaltec.UAU.Geral.AppService.Integracao.Armazenamento.Interfaces.ITipoArmazenamento

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Codigo` | integer (int32) |  |  |
| `Status` | boolean |  |  |
| `Padrao` | boolean |  |  |
| `Pasta` | string |  |  |
| `Origem_arq` | integer (int32) |  |  |
| `Nome` | string |  |  |
| `Descr_int` | string |  |  |

### UAUApi.Models.Anexo.ListaArquivoPorChaveRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Chave` | string |  | Identificador do arquivo. Exemplo: "Contrato" |
| `Valores` | array de string |  | Valores de identificação do arquivo. Exemplo: "123", "1234" |

### UAUApi.Models.Anexo.AnexarComentarioRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Chave` | string | ✓ | Chave para consulta |
| `Campos` | string | ✓ | Campos obrigatórios para a chave="Venda" (empresa, obra, venda). Campos obrigatórios para a chave="Contrato" (Empresa, Contrato) Deve ser inserido juntos, separados por virgula. |
| `Usuario` | string | ✓ | Usuário logado |
| `Comentario` | string | ✓ | Comentário a ser anexado. |
| `TipoComentario` | string |  | Armazena o tipo do comentário ( 0-Publico, 1-Privado, 2-Interna). |
| `UsuarioPrivado` | array de [`UAUApi.Models.Anexo.Usuario`](#uauapimodelsanexousuario) |  | Armazena a lista de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -&gt; /Usuarios/ConsultarUsuariosAtivos ) |
| `GrupoPrivado` | array de [`UAUApi.Models.Anexo.Grupo`](#uauapimodelsanexogrupo) |  | Armazena a lista de grupos de usuários que podem visualizar o comentário. ( Rota que retorna as informações necessárias -&gt; /Usuarios/ConsultarGruposDeUsuario ) |

### UAUApi.Models.Anexo.Grupo

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Cod_cad` | string |  | Codigo do grupo |

### UAUApi.Models.Anexo.Usuario

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Login_usr` | string |  | Nome do login. |

### UAUApi.Models.Anexo.ExcluirAnexosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `identificador` | string | ✓ | Chave identificadora do arquivo no formato "STRING STRING" |
| `nome_arquivo` | string |  | Nome do arquivo + extensão. ( Exemplo: nomeDoArquivo.png ) |
| `origem` | integer (int32) |  | Indica o tipo de armazenamento será utilizado para excluir o vinculo ao arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão. |

### UAUApi.Models.ResultadoExecucao

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Mensagens` | array de [`UAUApi.Models.Mensagem`](#uauapimodelsmensagem) |  |  |
| `CampoValidado` | string |  | Campo para informar deteminado situação, Ex.: Controle que está sendo validado no momento |
| `Tipo` | integer (int32) — valores possíveis: 0, 1, 2, 3 |  |  |
| `Sucesso` | boolean |  |  |
| `Mensagem` | string |  |  |
| `Continua` | boolean |  | Esta propriedade é utilizada para controlar se ocorreu um erro (Sucesso = False) e poderá continuar a execução do metodo que retorna esta classe. |
| `MensagensHtml` | object |  | Lista de mensagens formatado em HTML com cores de acordo com o tipo de mensagem |

### UAUApi.Models.Mensagem

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `TipoMens` | integer (int32) — valores possíveis: 0, 1, 2, 3 |  | Tipo de mensagem a ser exibida para o usuário |
| `TipoAcao` | integer (int32) — valores possíveis: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 |  | Tipo de ação a ser realizada com determinada mensagem a ser exibida para o usuário |
| `Descricao` | string |  | Descrição da mensagem |

### UAUApi.Models.Anexo.BaixarArquivosRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Arquivos` | array de [`UAUApi.Models.Anexo.ArquivoResponse`](#uauapimodelsanexoarquivoresponse) | ✓ |  |

### UAUApi.Models.Anexo.ArquivoResponse

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `CaminhoCompleto` | string | ✓ |  |
| `Origem` | integer (int32) | ✓ |  |

### UAUApi.Models.Anexo.AnexarBase64ImagemRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `arquivo` | string |  | Deve estar no formato Base64 sem os prefixos |
| `nome` | string |  | Nome do arquivo |
| `caminho` | string |  | Caminho do arquivo |
| `identificador` | string |  | Chave identificadora do arquivo no formato "STRING STRING" |
| `usuario` | string |  | Login do usuário |
| `extensaoImagem` | string |  | Extensao da imagem. ex: 'png' ou 'jpeg', etc |
| `caminhoExclusivo` | string |  | String correspondente a configuração em configgerais do caminho exclusivo |
| `controlaAnexoUAUWeb` | boolean |  | Indica se deverá gravar os arquivos no caminho de configuração padrão para arquivos do UAUWeb |
| `origem` | integer (int32) |  | Indica o tipo de armazenamento será utilizado para gravar o arquivo. Pode ser 1-Local ou 2-AWS S3. Caso não informe será obtido da configuração padrão. |

### UAUApi.Models.Anexo.AnexarArquivosBase64Request

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `lista_arquivos` | array de [`UAUApi.Models.Anexo.EstruturaAnexoBase64`](#uauapimodelsanexoestruturaanexobase64) |  |  |
| `empresa` | integer (int32) |  |  |
| `usuario` | string |  |  |

### UAUApi.Models.Anexo.EstruturaAnexoBase64

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ConteudoArquivo` | string |  | Arquivo em formato string base64 |
| `NomeArquivo` | string |  | Nome do arquivo |
| `CaminhoArquivo` | string |  | Caminho onde o arquivo será salvo.  Deve ser informando apenas os subdiretórios a partir do caminho de configuração para gravação de anexos. Por ex: No UAU está configurago o caminho de gravação de anexos no diretório \\AnexosUAU\Arquivos\ e você deseja gravar o arquivo 1475.pdf no diretório Vendas O valor do CaminhoArquivo então deverá ser "\\Vendas\\1475.pdf"  e o arquivo será gravado dentro do diretório \\AnexosUAU\Arquivos\Vendas" |
| `Extension` | string |  | Extensão do arquivo |
| `Identificador` | string |  | Chave identificadora do anexo |
| `Origem` | integer (int32) |  | Qual o tipo de armazenamento será utilizado para gravar o arquivo. Pode ser 1-Local ou 2-AWS S3 |
| `CaminhoPadrao` | string |  |  |

### UAUApi.ResponseHandler

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `Detalhe` | string |  | Detalhamento da Exception StrackTrace |
| `Mensagem` | string |  | Mensagem da Exception |
| `Descricao` | string |  | Descrição personalizada |

### UAUApi.Models.Anexo.AnexarArquivoRequest

| Propriedade | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `arquivo` | string (byte) |  | Conteúdo do arquivo em bytes |
| `nome` | string |  | Nome do arquivo |
| `caminho` | string |  | Caminho do arquivo |
| `identificador` | string |  | Chave identificadora do arquivo no formato "STRING STRING" |
| `usuario` | string |  | Login do usuário |
| `caminhoExclusivo` | string |  | String correspondente a configuração em configGerais do caminho exclusivo |
| `controlaAnexoUAUWeb` | boolean |  |  |
