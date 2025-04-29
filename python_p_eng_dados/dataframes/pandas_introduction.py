# 1- Importe o pandas.
import pandas as pd

# 2- Crie um data-frame com os dados de pedidos:
dicionario = {
    "produto" : ["Café", "Pão", "Suco"],
    "quantidade" : [3, 5, 2],
    "preco_unitario" : [6.50, 1.20, 8.00],
    "cliente_vip" : [True, False, True],
    "data" : ["01/04/2025", "02/04/2025", "02/04/2025"]
}
data_frame = pd.DataFrame(dicionario)

# 3- Imprima o data-frame.
print(data_frame)

# 4- Imprima apenas as colunas "produto" e "quantidade".
print(data_frame[["produto","quantidade"]])
