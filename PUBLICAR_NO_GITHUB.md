# Publicar no GitHub

Repositório autorizado: **`telco-customer-churn`** (público).

## 1. Preparar gráficos e notebook

No PowerShell, na pasta do projeto:

```powershell
cd "c:\Users\fwfco\Desktop\TREINOS BASES DE DADOS PYTHON\TELCO CUSTOMER CHURN"

# Renomear notebook (opcional, recomendado)
Rename-Item -Path ".\Untitled-1.ipynb" -NewName "telco_churn_analysis.ipynb"

# Extrair PNGs já salvos no notebook
python .\scripts\extract_notebook_plots.py

# OU rodar o setup completo
powershell -ExecutionPolicy Bypass -File .\setup_repo.ps1
```

## 2. Git — primeiro commit

```powershell
git init
git branch -M main
git add .
git status
git commit -m "feat: análise Telco Customer Churn com XGBoost e documentação"
```

## 3. Criar repositório e enviar

Com [GitHub CLI](https://cli.github.com/) instalado e logado (`gh auth login`):

```powershell
gh repo create telco-customer-churn --public --source=. --remote=origin --push
```

**Sem `gh`:** crie o repositório vazio em https://github.com/new (nome `telco-customer-churn`), depois:

```powershell
git remote add origin https://github.com/SEU_USUARIO/telco-customer-churn.git
git push -u origin main
```

## 4. Dados

O arquivo `data/Telco_customer_churn.xlsx` **não** vai no Git (está no `.gitignore`). Quem clonar deve seguir [data/README.md](data/README.md).
