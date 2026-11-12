# UAU-API
Simplificação da API de comunicação do sistema UAU Globaltec

---

## Uso básico

```python
from uau_api import UauAPI

uau = UauAPI(
    base_url="https://<host>/uauAPI/api/v1.0/",
    api_key="<api_key>",
)
uau.authenticate("<login>", "<senha>")

response = uau.Obras.obter_obras_ativas()
print(response.json())
```

---

## Linha de comando (`uau`)

Os subcomandos são gerados a partir do catálogo de endpoints
(`uau_api/catalog/endpoints.json`, construído do `swagger.json`).

```bash
uau config init                      # URL, token de integração (oculto), usuário e senha opcionais
uau config show                      # segredos mascarados
uau search obras ativas              # busca no catálogo
uau describe obras obter-obras-ativas
uau obras obter-obras-ativas
uau chave-pix consultar --cpf-cnpj 12345678900
uau venda <endpoint> --body @payload.json --campo valor   # opções sobrepõem o --body
uau --raw obras obter-obras-ativas | jq .                 # saída compacta
```

**Credenciais.** O token de integração fica **obrigatoriamente** no arquivo de
configuração (`~/.config/uau-api/config.toml`, ou `%APPDATA%\uau-api\` no
Windows; sobrescreva com `--config` ou `UAU_CONFIG`; permissão 600). Usuário e
senha são opcionais no arquivo; se ausentes, são pedidos a cada chamada, e a
senha usa prompt oculto. Não existe opção de linha de comando para senha ou
token.

Para regenerar o catálogo após atualizar o `swagger.json`:
`uv run python -m helpers.build_catalog`.

**Agentes de IA:** use o CLI seguindo o
[guia para agentes](docs/cli-agent-guide.md) (também referenciado em
[AGENTS.md](AGENTS.md)).

## Instalação

O pacote compila extensões C durante a instalação. É necessário ter um compilador C:

```bash
# Debian / Ubuntu / WSL
sudo apt-get install -y gcc python3-dev

# macOS
xcode-select --install

# Windows — instale o Visual C++ Build Tools:
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

### uv (recomendado)

```bash
uv add git+https://github.com/hy-brazil-energia/uau-api.git
```

### pip

```bash
pip install git+https://github.com/hy-brazil-energia/uau-api.git
```

---

## IntelliSense no VS Code (Pylance)

Adicione ao `.vscode/settings.json` do seu projeto:

```json
{
  "python.analysis.extraPaths": ["."],
  "python.analysis.stubPath": ".",
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
}
```

Após salvar, execute **Python: Restart Language Server** (`Ctrl+Shift+P`).

---

## Publicando uma nova versão (maintainers)

Quando houver mudanças em `master` que devem ser distribuídas, execute o procedimento abaixo para compilar e publicar na branch `minified`:

### Pré-requisitos (única vez)

```bash
sudo apt-get install -y gcc python3-dev   # Debian / Ubuntu / WSL
uv sync --group dev                        # instala Cython, mypy, etc.
```

### Procedimento

```bash
# 1. Garantir que master está limpo e atualizado
git checkout master
git pull origin master

# 2. Ir para minified e trazer os arquivos-fonte do master
git checkout minified
git checkout master -- uau_api/

# 3. Corrigir bugs conhecidos de f-string (nomes camelCase em .py gerados)
#    O Cython rejeita f-strings com variáveis não declaradas. Verifique:
python3 -c "
import ast, glob
for path in sorted(glob.glob('uau_api/**/*.py', recursive=True)):
    if path.endswith('__init__.py'): continue
    tree = ast.parse(open(path).read())
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)): continue
        params = {a.arg for a in node.args.args} | {'self','type','str','int','bool','e','version'}
        for child in ast.walk(node):
            if not isinstance(child, ast.JoinedStr): continue
            for part in ast.walk(child):
                if isinstance(part, ast.Name) and part.id not in params:
                    print(f'{path}:{child.lineno}: {part.id}')
"

# 4. Transpilação: Python → C  (requer Cython no venv)
#    Gera os arquivos .c dentro de uau_api/ — NÃO compila para .so
PATH="/usr/bin:$PATH" .venv/bin/python compile.py build_ext --inplace

# 5. Remover .py (exceto __init__.py) e artefatos de compilação
find uau_api -name "*.py" ! -name "__init__.py" -delete
rm -rf build/

# 6. Regenerar stubs de tipo (.pyi) com mypy/stubgen
uv run stubgen -p uau_api -o .

# 7. Atualizar uau_api/client.pyi manualmente:
#    stubgen não captura atributos definidos dinamicamente (_init_api_groups).
#    Adicione qualquer novo grupo seguindo o padrão existente no arquivo.

# 8. Commit e push para hy-brazil/minified
git add -A
git commit -m "minified: rebuild from master — <descrição breve>"
git push hy-brazil minified
```

Os arquivos `.c` são distribuídos no repositório. Ao instalar com `uv add` ou `pip install`, o `gcc` local compila os `.c` em extensões nativas (`.so`/`.pyd`) para a versão Python do ambiente de destino.
