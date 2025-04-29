# 1- Importe o pandas.
import pandas as pd

# 2- leia o arquivo pedidos_exemplo.csv
df = pd.read_csv('C:/Users/vinyc/OneDrive/Área de Trabalho/Backup/Pessoal/Cursos/Python/Engenharia_Dados/python_p_eng_dados/dataframes/leitura_csv/pedidos_exemplo.csv')
print(df)
print('--------------------------------------------------------------------')

# 3- imprima:

# As 3 primeiras linhas
print(df.head(3))
print('--------------------------------------------------------------------')

# As colunas produto e data
print(df[["produto", "data"]])
print('--------------------------------------------------------------------')

# A quantidade de pedidos de "Café"
print(df[df["produto"] == "Café"].shape[0])