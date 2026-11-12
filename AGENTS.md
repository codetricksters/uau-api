# AGENTS.md

Para chamar a API UAU pelo CLI `uau`, leia e siga
[docs/cli-agent-guide.md](docs/cli-agent-guide.md) antes de executar qualquer
comando. Regras essenciais:

- Nunca leia nem imprima o arquivo de configuração (contém token e senha); use
  `uau config show`.
- Nunca rode `uau config init` (interativo); peça ao usuário.
- Descubra com `uau search`, entenda com `uau describe`, chame com `uau --raw`.
- Endpoints de escrita (`Gravar*`, `Incluir*`, `Excluir*`, ...) exigem
  confirmação do usuário antes de executar.

Para desenvolver neste repositório, veja [CLAUDE.md](CLAUDE.md).
