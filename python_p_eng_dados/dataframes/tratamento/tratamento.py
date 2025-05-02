import pandas as pd

# 1- Ler o arquivo dados_sujos.csv
df = pd.read_csv("C:/Users/vinyc/OneDrive/Área de Trabalho/Backup/Pessoal/Cursos/Python/Engenharia_Dados/python_p_eng_dados/dataframes/tratamento/dados_sujos.csv", na_values=["", " ", "N/A", None, "NaN"])

# 2- Corrigir nomes das colunas (deixar em minúsculo e sem espaços)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 3- Verificar e exibir os valores nulos
print("Valores nulos antes do tratamento:")
print(df.isnull().sum())

# 4- Substituir valores nulos da coluna cliente_vip por False
df['cliente_vip'] = df['cliente_vip'].replace({'TRUE': True, 'FALSE': False, 'True': True, 'False': False, 'NaN' : False, None : False})

# 5- Substituir valores nulos da coluna quantidade por 0
df['quantidade'] = df['quantidade'].fillna(0)

# 6- Substituir valores nulos da coluna preco_unitario por 0.0
df['preco_unitario'] = df['preco_unitario'].fillna(0.0)

# 7- Substituir valores nulos da coluna data por "01/01/1900"
df['data'] = df['data'].fillna("01/01/1900")

# 8- Imprimir o DataFrame limpo
print("\nDataFrame limpo:")
print(df)
