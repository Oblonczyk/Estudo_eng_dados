'''Cenário:
Você recebeu uma lista de pedidos realizados em um marketplace.
Cada pedido contém:
    - Produto comprado
    - Quantidade
    - Preço unitário
    - Flag se o cliente é VIP
'''

'''
TAREFA:
1- Percorrer toda a lista de pedidos.
2- Para cada pedido:
- Calcular o valor total sem desconto (quantidade * preco_unitario).
- Se o cliente for VIP, aplicar 10% de desconto no valor total.
- Salvar o valor final (com ou sem desconto) em uma nova chave no dicionário, chamada "valor_final".
3- Imprimir para cada pedido uma frase no formato:
Produto: [produto] | Quantidade: [quantidade] | Preço Unitário: [preco_unitario] | Cliente VIP: [Sim/Não] | Valor Final: R$[valor_final]
'''

pedidos = [
    {"produto": "Café", "quantidade": 3, "preco_unitario": 6.50, "cliente_vip": True},
    {"produto": "Pão", "quantidade": 5, "preco_unitario": 1.20, "cliente_vip": False},
    {"produto": "Suco", "quantidade": 2, "preco_unitario": 8.00, "cliente_vip": True},
    {"produto": "Bolo", "quantidade": 1, "preco_unitario": 15.00, "cliente_vip": False}
]

contador = 0

for pedido in pedidos:
    produto, quantidade, preco_unitario, cliente_vip = pedidos[contador]["produto"], pedidos[contador]["quantidade"], pedidos[contador]["preco_unitario"], pedidos[contador]["cliente_vip"]
    valor_total = quantidade * preco_unitario
    if cliente_vip:
        valor_total *= 0.9
    pedidos[contador]["valor_final"]= F"{valor_total:.2f}"

    print(f"Produto: {produto} | Quantidade: {quantidade} | Preço Unitário: R${preco_unitario:.2f} | Cliente VIP: {'Sim' if cliente_vip else 'Não'} | Valor Final: R${valor_total:.2f}")

    contador += 1
    