# Você recebeu um dicionário com informações de uma venda. Crie variáveis separadas e calcule o total da venda:

venda = {
    "produto": "Café",
    "quantidade": 4,
    "preco_unitario": 6.50,
    "cliente_vip": True
}

# Tarefa:

# 1. Crie variáveis separadas com os dados de 'venda'
produto = venda["produto"]
quantidade = venda["quantidade"]
preco_unitario = venda["preco_unitario"]
cliente_vip = venda["cliente_vip"]

# 2. Calcule o valor total da venda
valor_total = quantidade * preco_unitario

# 3. Imprima uma frase como:
# "Venda realizada: 4x Café por R$6.5. Total: R$26.0"
print(f"Venda realizada: {quantidade} x {produto} por R${preco_unitario}. Total: R${valor_total}")
