import pandas as pd

# Carregando o arquivo CSV
gasolina_df = pd.read_csv('gasolina.csv')

gasolina_df.head()#Visualizando colunas

import seaborn as sns
#gerando gráfico em linha
with sns.axes_style('whitegrid'):
  grafico_gasolina = sns.lineplot(x='Jul/2021', y='Valor venda', data=gasolina_df)