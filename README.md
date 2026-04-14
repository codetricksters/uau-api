# UAU-API
Simplificação da API de comunicação do sistema UAU Globaltec

## Instalação

```bash
uv sync
# ou
pip install .
```

## Uso básico

```python
from uau_api import UauAPI

uau = UauAPI(base_url="https://<host>/uauAPI/api/v1.0/", api_key="<api_key>")
uau.authenticate("<login>", "<senha>")

response = uau.Obras.obter_obras_ativas()
print(response.json())
```

## IntelliSense no VS Code (Pylance)

Os módulos estão compilados como extensões nativas (`.so`). Para que o Pylance reconheça os tipos e exiba autocomplete, adicione as configurações abaixo ao seu `.vscode/settings.json`:

```json
{
  "python.analysis.extraPaths": ["."],
  "python.analysis.stubPath": ".",
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
}
```

- **`extraPaths`** — garante que o Pylance encontre o pacote `uau_api` na raiz do workspace.
- **`stubPath`** — aponta para a raiz do workspace onde os arquivos `.pyi` estão co-localizados com os `.so`.
- **`defaultInterpreterPath`** — seleciona o ambiente virtual criado pelo `uv`.

Após salvar o arquivo, execute **Python: Restart Language Server** na paleta de comandos (`Ctrl+Shift+P`) para aplicar as mudanças.
