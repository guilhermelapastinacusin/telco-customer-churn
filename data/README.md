# Dados — Telco Customer Churn

O notebook utiliza o dataset **IBM Telco Customer Churn** (versão estendida, com colunas geográficas, `Churn Reason`, `CLTV`, etc.).

## Como obter o arquivo

1. Acesse o dataset no [IBM Sample Data Sets](https://www.ibm.com/docs/en/cognos-analytics/11.2.0?topic=samples-sample-data-sets) ou no portal de dados que você utilizou no treinamento.
2. Baixe o arquivo **`Telco_customer_churn.xlsx`**.
3. Coloque-o nesta pasta: `data/Telco_customer_churn.xlsx`.

## Estrutura esperada

O notebook espera colunas como: `CustomerID`, `Contract`, `Payment Method`, `Monthly Charges`, `Total Charges`, `Churn Label`, `Churn Value`, `Churn Reason`, entre outras.

> **Nota:** O arquivo `WA_Fn-UseC_-Telco-Customer-Churn.csv` na raiz do projeto (se existir) é o dataset clássico do Kaggle, com schema diferente. Ele **não** substitui o `.xlsx` usado no notebook principal.
