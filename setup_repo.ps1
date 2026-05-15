$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
Set-Location $root

New-Item -ItemType Directory -Force -Path notebooks, docs\images | Out-Null

Copy-Item -Force '.\Untitled-1.ipynb' '.\notebooks\telco_churn_analysis.ipynb'

python '.\scripts\extract_notebook_plots.py' 2>&1 | Tee-Object -FilePath '.\setup_log.txt'

if (-not (Test-Path '.\.git')) {
    git init
    git branch -M main
}

Write-Host 'Setup concluido. Veja setup_log.txt'
