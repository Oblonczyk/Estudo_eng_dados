# Imagine que agora temos vários pedidos a serem processados:

pedidos = [
    {"produto": "Café", "quantidade": 2, "preco_unitario": 6.50},
    {"produto": "Pão", "quantidade": 5, "preco_unitario": 1.20},
    {"produto": "Suco", "quantidade": 1, "preco_unitario": 8.00}
]

# Tarefa:

# 1- Crie um for que percorra cada pedido.
for p in pedidos:
    produto = p["produto"]
    quantidade = p["quantidade"]
    preco_unitario = p["preco_unitario"]

    # 2- Para cada pedido, calcule o valor total (quantidade * preco_unitario).
    valor_total = quantidade * preco_unitario

    ''' 3- Imprima uma frase no formato:
        Pedido: 2x Café - Total: R$13.00
        Pedido: 5x Pão - Total: R$6.00
        Pedido: 1x Suco - Total: R$8.00
    '''
    print(f"Pedido: {quantidade} x {produto} - Total: R${valor_total:.2f}")

