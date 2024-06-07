Introdução

Trabalho executado para acompanhamento do preço médio de venda da gasolina na 
cidade de São Paulo nos 10 primeiros dias de Julho de 2021.

Desenvolvimento

Foi realizada extração de dados do arquivo gasolina.csv, onde conta tabela com a
informação do preço médio de venda da gasolina na cidade de São Paulo nos 10 
primeiros dias de Julho de 2021.

import pandas as pd

gasolina_df = pd.read_csv('gasolina.csv') gasolina_df.head()

Com dados extraídos, foi gerado gráfico de linha com os valores obtidos.

import seaborn as sns

with sns.axes_style('whitegrid'): 
grafico_gasolina = sns.lineplot(x='dia', y='venda', data=gasolina_df)