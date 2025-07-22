# Atividade Cloud Pokémon

Este projeto processa uma lista de URLs da API do Pokémon, extrai informações relevantes e armazena no formato CSV.

## Como rodar
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute: `python src/main.py`
3. O resultado estará em `pokemons.csv`.

## Arquitetura Cloud sugerida
O processamento pode ser automatizado diariamente em um serviço serverless (AWS Lambda) e os dados salvos em um banco NoSQL (DynamoDB).

## Custo
O cálculo de custo anual está em calculo-custo.pdf.
