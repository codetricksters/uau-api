# Guia para agentes de IA: chamando a API UAU pelo CLI `uau`

Este guia é para um agente que executa comandos de shell. Siga na ordem:
descobrir o endpoint, entender os parâmetros, chamar, interpretar a saída.

## Regras de segurança (leia primeiro)

1. **Nunca leia, imprima ou edite** o arquivo de configuração
   (`~/.config/uau-api/config.toml`, ou o caminho em `UAU_CONFIG`/`--config`).
   Ele contém o token de integração e possivelmente a senha. Para conferir se
   está configurado, use `uau config show`, que mascara os segredos.
2. **Nunca rode `uau config init`.** É interativo e pede segredos; é tarefa do
   usuário. Se faltar configuração, pare e peça que o usuário rode
   `uau config init` num terminal.
3. **Nunca passe senha ou token em argumentos, `--body` ou variáveis de
   ambiente.** O CLI não tem flag para isso, por desenho.
4. **Quase todos os endpoints são POST, e o verbo não indica se escreve.** Não
   existe modo somente leitura. Trate como **escrita** qualquer endpoint cujo
   nome comece por `Gravar`, `Incluir`, `Inserir`, `Alterar`, `Atualizar`,
   `Excluir`, `Cancelar`, `Aprovar`, `Reprovar`, `Baixar`, `Emitir`, `Enviar`
   ou similar, e **peça confirmação explícita ao usuário antes de executar**.
   Endpoints `Obter*`, `Consultar*`, `Listar*` e `Buscar*` costumam ser
   leitura, mas confirme lendo o `summary` em `uau describe`.
5. Nunca invente valores de campos obrigatórios (códigos de empresa, obra,
   contrato, CPF/CNPJ). Pergunte ao usuário ou obtenha de uma consulta anterior.

## Pré-requisito: modo não interativo

O CLI pede **usuário** e **senha** na chamada quando não estão no arquivo de
configuração. Um agente não consegue responder a prompts, e o comando trava ou
falha. Antes de começar, rode:

```bash
uau config show
```

- Se `username` e `password` aparecem como `********`/valor definido, está
  pronto.
- Se aparecer `(perguntar)` em `username` ou `password`, **não execute
  chamadas**: peça ao usuário para gravar usuário e senha na configuração
  (`uau config init`, respondendo "sim" para salvar a senha), ou para rodar
  o comando ele mesmo.
- Se o comando falhar com "Configuração não encontrada" ou campo obrigatório
  ausente (`api_key`), pare e peça ao usuário para rodar `uau config init`.

## Fluxo de trabalho

### 1. Descobrir o endpoint

```bash
uau search obras ativas          # todos os termos precisam aparecer
uau search --help
uau --help                       # lista os grupos (um por tag do swagger)
uau obras --help                 # lista os endpoints de um grupo
```

A primeira coluna da busca é o comando exato: `<grupo> <endpoint>`
(ex.: `obras obter-obras-ativas`). Nomes são em kebab-case; o CLI também
aceita `ObterObrasAtivas` e `obter_obras_ativas`.

### 2. Entender parâmetros e corpo

```bash
uau describe obras obter-obras-ativas
```

Mostra método HTTP, path, descrição de negócio, parâmetros (query/rota) e os
campos do corpo com tipo e se são obrigatórios. **Sempre rode `describe`
antes de chamar um endpoint que você ainda não usou**, e preencha todos os
campos marcados como obrigatórios.

### 3. Chamar

```bash
# sem parâmetros
uau --raw obras obter-obras-ativas

# parâmetro de rota/query vira opção --kebab-case
uau --raw chave-pix consultar --cpf-cnpj 12345678900

# campos escalares do corpo viram opções
uau --raw <grupo> <endpoint> --campo-um valor --campo-dois 10

# corpo completo (necessário para objetos aninhados e arrays)
uau --raw <grupo> <endpoint> --body '{"Campo": "valor", "Lista": [1, 2]}'
uau --raw <grupo> <endpoint> --body @/tmp/payload.json

# combinação: opções individuais sobrepõem chaves do --body
uau --raw <grupo> <endpoint> --body @/tmp/payload.json --campo-um novo
```

Dicas:
- Coloque `--raw` e `--config` **antes** do grupo (são opções globais).
- Para JSON com aspas ou acentos, grave o payload em um arquivo temporário e
  use `--body @arquivo` em vez de escapar no shell.
- Opções booleanas aceitam `true`/`false`; números são validados pelo tipo.
- Propriedades que são objetos ou listas só podem ser passadas via `--body`.
- Não existe paginação automática: se o `describe` mostrar parâmetros de
  página/limite, passe-os explicitamente.

### 4. Interpretar a resposta

- Com `--raw`, a saída em stdout é JSON compacto (uma linha), pronto para
  `jq`. Sem `--raw`, é JSON formatado com cores, ruim para processar.
- Se a resposta não for JSON, o texto cru é impresso.
- Mensagens de erro do próprio CLI vão para stderr.

| Código de saída | Significado | O que fazer |
|---|---|---|
| 0 | Sucesso (HTTP < 400) | Ler o JSON de stdout |
| 1 | Autenticação recusada, falha de rede ou HTTP ≥ 400 (o corpo do erro ainda sai em stdout) | Ler o corpo do erro; corrigir parâmetros; não repetir às cegas |
| 2 | Uso incorreto ou configuração ausente/inválida; endpoint não encontrado | Ver a mensagem; `uau search`/`describe`; pedir configuração ao usuário |

Autenticação recusada (HTTP 401) significa usuário/senha/token errados: **não
tente de novo em loop** (risco de bloquear o usuário no ERP); reporte ao
usuário.

Filtrar resultados grandes:

```bash
uau --raw obras obter-obras-ativas | jq '.[0:5]'
uau --raw obras obter-obras-ativas | jq 'length'
```

Respostas podem ser grandes. Filtre com `jq` e resuma, em vez de colar tudo
no contexto.

## Exemplo completo

Pedido do usuário: "liste as obras ativas".

```bash
uau config show                       # confirma configuração e credenciais
uau search obras ativas               # -> obras obter-obras-ativas (POST)
uau describe obras obter-obras-ativas # sem campos obrigatórios; é consulta
uau --raw obras obter-obras-ativas | jq 'length'
uau --raw obras obter-obras-ativas | jq '.[0:10]'
```

## Cada chamada autentica de novo

O CLI autentica a cada execução (um POST em `Autenticador/AutenticarUsuario`
antes da chamada pedida). Evite laços com centenas de invocações; prefira um
único comando com `--body` quando o endpoint aceitar lote.

## Problemas comuns

| Sintoma | Causa provável |
|---|---|
| Comando trava esperando entrada | Usuário/senha não estão na configuração (ver "modo não interativo") |
| `Configuração não encontrada` | Falta o arquivo; peça ao usuário `uau config init` |
| `Endpoint não encontrado` | Nome errado; use `uau search <termos>` |
| `Parâmetro de rota obrigatório ausente: --x` | Endpoint com `{x}` no path; passe `--x valor` |
| HTTP 400/500 com mensagem do ERP | Campo obrigatório faltando ou valor inválido; reveja `describe` |
| Catálogo desatualizado (endpoint novo no ERP) | Maintainer deve rodar `uv run python -m helpers.build_catalog` |
