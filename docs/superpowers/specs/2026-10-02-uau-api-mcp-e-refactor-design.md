# uau-api: refactor da biblioteca e MCP server

**Data:** 2026-10-02
**Status:** design parcial — decisões de escopo e arquitetura do catálogo aprovadas; seções de detalhe pendentes (ver "Pendências")

---

## Intenção

A biblioteca existe para facilitar a comunicação com a API do ERP UAU Globaltec e
hoje funciona. O objetivo deste trabalho é duplo:

1. Melhorar o código e a arquitetura do projeto.
2. Criar e distribuir um MCP server que permita a qualquer agente de IA usar a API.

**Sucesso** significa: um agente de IA descobre o endpoint correto e o chama com os
parâmetros certos sem que um humano precise consultar o swagger; e a biblioteca
deixa de carregar módulos mortos e quebrados.

### Decisões do parceiro humano

| Tema | Decisão |
|------|---------|
| Público do MCP | Distribuição pública multi-cliente; agentes automatizados sem humano no loop; serviço remoto hospedado como aspiração futura |
| Dores prioritárias | Respostas sem tipagem; descoberta de endpoints; duplicação/legado; build da branch `minified` |
| Superfície do MCP | Poucas tools genéricas + catálogo (não uma tool por endpoint) |
| Escrita no ERP | Somente leitura por padrão, escrita habilitada por opt-in explícito |
| Distribuição | Abrir o código e publicar no PyPI (abandona Cython/`minified`) |
| Transporte | stdio na Fase 1; HTTP remoto em fase posterior, mas arquitetura preparada |
| Repositório | Monorepo, pacote separado (workspace `uv`): `uau_api/` + `uau_api_mcp/` |
| Ordem | Limpeza mínima → MCP → tipagem |

### Suposições (não confirmadas pelo parceiro)

- A instância UAU de cada cliente expõe o mesmo swagger; o índice de endpoints
  embarcado no pacote serve a todos. Se instâncias divergirem por versão, o índice
  precisa ser versionado ou gerável pelo usuário.
- "Somente leitura" pode ser derivado do swagger. **Risco:** 403 dos 407 endpoints
  são POST, logo o verbo HTTP **não** distingue leitura de escrita. Ver Pendências.

---

## Estado atual (levantamento de 2026-10-02)

### Núcleo

- `uau_api/requestsapi.py` (69 linhas) — wrapper sobre `requests.Session`. Retry em
  408/429/500/502/503/504 aplicado a **todos** os métodos, incluindo POST não
  idempotente. Sem `raise_for_status`, sem timeout default, sem logging. Usa
  `urljoin`, que descarta o último segmento se `base_url` não terminar em `/`.
- `uau_api/client.py` (163 linhas) — `UauAPI(RequestsApi)`. `_init_api_groups()` são
  98 linhas de boilerplate manual com 49 imports locais, já contendo o bug de nome
  `self.RelatorioIR_p_f`. `authenticate()` não verifica o status final: um 401 ou 500
  grava o corpo de erro no header `Authorization` e marca `is_authenticated = True`.
- `uau_api/settings.py` (10 linhas) — segredos como `str` puro, não `SecretStr`. O
  campo `USERNAME` colide com a variável de ambiente homônima no Windows/WSL.

### Código gerado

`uau_api/groups/` — 50 módulos, 32.876 linhas, 456 métodos. 403 POST contra 4
outros verbos. **0** ocorrências de `.json()`, **0** de `raise_for_status`. Todos os
métodos retornam `requests.Response` cru.

As 456 docstrings estão incorretas em massa: prometem `dict` como retorno e
`HTTPError`/`ValueError` que nunca são levantados, e os exemplos são inválidos
(`>>> api = Obras()` quando o construtor exige `api`; chamadas a nomes com
underscore que não existem). Combinado com `addopts = --doctest-modules`, isso é
quebra garantida da suíte.

Os paths são relativos e sem versão (`"Obras/ObterObrasAtivas"`) enquanto o swagger
define `/api/v{version}/Obras/...`. O prefixo `/api/v1/` precisa estar em
`API_URL` — acoplamento implícito e não documentado.

Arquivos maiores: `venda.py` 4.211, `planejamento.py` 2.199, `proposta.py` 1.872,
`pessoas.py` 1.817, `processo_pagamento.py` 1.775.

### Módulos mortos ou quebrados (~1.000 linhas)

| Arquivo | Linhas | Problema |
|---------|--------|----------|
| `operations.py` | 668 | Legado. `exception_handler` engole exceções e retorna `None`. Importa `aiofiles`/`aiohttp`/`tqdm` não declarados → `ImportError`. Configura logging em arquivo no import |
| `utils.py` | 112 | Importa `aiofiles`/`aiohttp` não declarados; `logging.basicConfig` global no import |
| `base.py` | 48 | `BaseAPI` duplica `RequestsApi`; ninguém importa |
| `models.py` | 29 | Importa `sqlalchemy` não declarado |
| `database.py` | 16 | Usa `Settings().DATABASE_URL`, campo inexistente → `AttributeError`. Executa `create_engine` + `create_all` no import |
| `app.py` | 19 | Autentica em escopo de módulo: importar dispara chamada de rede |

### Ferramental e documentação

- `swagger.json` (2.9 MB) não versionado. **Causa raiz:** `.gitignore:5` contém
  `*.json`, que o ignora junto com todo outro JSON. Os geradores não são
  reprodutíveis a partir de um clone limpo.
- Dois geradores concorrentes: `generate_api_classes_from_swagger.py` (432 linhas,
  preferido) e `generate_api_classes.py` (215 linhas, legado), com
  `clean_method_name`/`get_type_hint` duplicados.
- `generate_markdown_from_swagger.py` (225 linhas) não versionado, mas já produziu
  os 52 arquivos de `docs/api-reference/`.
- Três gerações de docs coexistem: `docs/index.md` (2 linhas), `docs/api/` (2 de 50
  arquivos, órfão) e `docs/api-reference/` (52 arquivos, untracked). `mkdocs.yml` não
  tem `nav:`.
- Seis markdowns sobrepostos na raiz: `README`, `QUICK_START`, `TESTING`, `CLAUDE`,
  `DOCUMENTATION_INDEX`, `IMPLEMENTATION_SUMMARY`.
- `docs/api-reference/` nomeia `CessaoRecebiveis`, `DocumentosDigitais` e
  `RelatorioIRPF` — tags do swagger sem módulo correspondente em `groups/`,
  evidenciando drift entre spec e código gerado.
- Config de lint inconsistente: `[tool.isort] line_lenght` com typo (ignorado
  silenciosamente), `[tool.ruff.format]` presente sem ruff instalado, mypy citado no
  fluxo da `minified` mas ausente do `pyproject.toml`.

### Testes

`tests/test_login.py` — 8 testes, 1 skipado. Os 7 ativos só validam `.env` e headers;
nenhum cobre `groups/`, logo a cobertura efetiva dos 456 métodos é ~0. Todos falham
sem um `.env` real. O teste skipado está escrito errado: chama
`api_client.autenticador` (minúsculo; o atributo é `Autenticador`) e afirma
`isinstance(response, dict)` quando o retorno é `Response`.

---

## Arquitetura do MCP

### Abordagem escolhida: índice compilado do swagger

Avaliadas três origens para o catálogo que alimenta as tools de descoberta:

- **A — índice compilado (escolhida).** Um passo de build transforma o `swagger.json`
  num índice compacto: por endpoint, nome do método, grupo, path, verbo, parâmetros
  com tipo e obrigatoriedade, schema do body com `$ref` resolvidos, e resumo curto. O
  índice é artefato gerado, versionado e embarcado no pacote.
- **B — introspecção em runtime.** `inspect` sobre as 50 classes geradas. Sempre em
  sincronia, mas a única informação disponível é `Optional[str]` em quase tudo mais as
  docstrings — que estão erradas em massa. O agente herdaria a desinformação. Torna-se
  viável só depois da Fase 3.
- **C — swagger cru em runtime.** 2.9 MB de parse e `$ref` a resolver por consulta, e
  os schemas crus são verbosos demais para caber na resposta de uma tool. É a Opção A
  sem a etapa que a torna utilizável.

**Justificativa de A:** entrega ao agente informação correta — tipos e campos
obrigatórios vindos da fonte da verdade, não das docstrings. A validação
pré-chamada converte erro de parâmetro em mensagem acionável em vez de um 500 opaco
do ERP. O índice ataca as duas dores prioritárias (descoberta e tipagem) sem
depender da Fase 3, e vira infraestrutura reutilizável: alimenta o MCP, a geração de
docs e um teste de drift entre spec e código.

**Custo aceito:** mais um artefato gerado a manter em sincronia, mitigado por um
teste que falha quando índice e `groups/` divergirem.

**Consequência explícita:** com `call_endpoint` despachando via `RequestsApi`, o MCP
**não depende das 50 classes geradas**. Índice + `RequestsApi` bastam. As classes
geradas permanecem como a API ergonômica para humanos escrevendo Python — as duas
superfícies coexistem, mas não são interdependentes.

### Tools previstas

Quatro tools genéricas, em vez de uma por endpoint (centenas estourariam o limite de
contexto da maioria dos clientes MCP):

- `search_endpoints` — busca textual sobre o índice.
- `describe_endpoint` — assinatura completa com schema de parâmetros e body.
- `call_endpoint` — valida contra o schema e despacha.
- `authenticate` — estabelece a sessão.

### Credencial por contexto de sessão

Mesmo entregando apenas stdio na Fase 1, a resolução de credencial deve ser
**session-scoped desde o início** — nunca um `UauAPI` global de módulo. Essa é a
única decisão que, se adiada, gera retrabalho na migração para HTTP: em stdio o
processo pertence a um usuário, mas em HTTP um processo serve N usuários e um cliente
jamais pode herdar o header `Authorization` de outro.

O que fica adiado para a fase HTTP (subsistema, não entrypoint): credencial por
requisição ou OAuth, isolamento de sessão, ciclo de vida e expiração de token,
deploy, TLS, rate limit e logs que não vazem segredo.

---

## Fases

### Fase 1 — limpeza mínima

Objetivo: base confiável sem reescrever o código gerado.

- Remover os módulos mortos e quebrados listados acima (~1.000 linhas).
- Corrigir `authenticate()` para verificar o status antes de gravar o header e marcar
  `is_authenticated`.
- Adicionar timeout default; restringir o retry a métodos idempotentes.
- Versionar `swagger.json`, corrigindo o `*.json` do `.gitignore`.
- Versionar `generate_markdown_from_swagger.py`; remover o gerador legado.
- Corrigir `_init_api_groups` (incluindo `RelatorioIR_p_f`).
- Resolver o conflito entre `--doctest-modules` e as 456 docstrings inválidas.
- Corrigir a config de lint (`line_lenght`, ruff ausente, mypy).

### Fase 2 — MCP server

- Gerador do índice de endpoints a partir do swagger.
- Pacote `uau_api_mcp/` no workspace `uv`, com as quatro tools e transporte stdio.
- Guardrail de somente-leitura com opt-in de escrita.
- Publicação no PyPI de `uau-api` e `uau-api-mcp` (`uvx uau-api-mcp`).

### Fase 3 — tipagem

- Modelos de resposta tipados substituindo os 407 retornos de `Response` cru.
- Regenerar docstrings corretas a partir do swagger.
- Consolidar as três gerações de docs e os seis markdowns da raiz.

---

## Pendências

Resolver antes de escrever o plano de implementação:

1. **Como distinguir leitura de escrita.** 403 dos 407 endpoints são POST, então o
   verbo HTTP não serve. Alternativas: heurística sobre o nome do método
   (`Obter*`/`Consultar*` versus `Gravar*`/`Incluir*`/`Excluir*`), curadoria manual
   do índice, ou allowlist explícita. **Esta é a pendência de maior risco:** o
   guardrail de somente-leitura depende dela, e os endpoints são consumidos por
   agentes automatizados sem humano no loop.
2. **Destino da branch `minified`.** Abrir o código no PyPI a torna obsoleta.
   Confirmar se é descontinuada, e o que acontece com os clientes já instalados por
   ela.
3. **Drift spec/código.** `CessaoRecebiveis`, `DocumentosDigitais` e `RelatorioIRPF`
   existem no swagger sem módulo correspondente. Regenerar tudo ou tratar caso a caso?
4. **Destino de `keys.cs`** na raiz do repositório — untracked e não ignorado, nome
   sugere material sensível. Não foi incluído em nenhum commit.
5. **Seções de design não detalhadas:** formato exato do índice, estratégia de
   testes do MCP, tratamento de erro e mapeamento de erros do ERP para respostas de
   tool. Foram adiadas a pedido do parceiro humano.
