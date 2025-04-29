'''Cenário:
Você recebeu uma lista com vários pedidos de venda, contendo:
    - Produto
    - Quantidade
    - Preço unitário
    - Flag se o cliente é VIP
    - Data da compra (em formato 'dd/mm/aaaa')
'''

'''
TAREFA:
1- Calcular o valor total do pedido (quantidade * preco_unitario).
2- Aplicar 10% de desconto para clientes VIP.
3- Salvar o valor final em cada dicionário, como "valor_final".
4- Arredonde os valores para duas casas decimais.
5- Mostrar um relatório resumido de cada pedido com
[Data] Produto: [produto] | Qtde: [quantidade] | VIP: [Sim/Não] | Total: R$[valor_final]

6 - Ao final, exiba as seguintes métricas gerais:
- Total de pedidos
- Total de vendas em reais
- Total de vendas feitas para clientes VIP
- Valor médio por pedido
- Produto mais vendido (em quantidade total somada)
'''

pedidos = [
    {"produto": "Café", "quantidade": 3, "preco_unitario": 6.50, "cliente_vip": True, "data": "01/04/2025"},
    {"produto": "Pão", "quantidade": 5, "preco_unitario": 1.20, "cliente_vip": False, "data": "02/04/2025"},
    {"produto": "Suco", "quantidade": 2, "preco_unitario": 8.00, "cliente_vip": True, "data": "02/04/2025"},
    {"produto": "Café", "quantidade": 1, "preco_unitario": 6.50, "cliente_vip": False, "data": "03/04/2025"},
    {"produto": "Bolo", "quantidade": 1, "preco_unitario": 15.00, "cliente_vip": False, "data": "03/04/2025"},
    {"produto": "Café", "quantidade": 2, "preco_unitario": 6.50, "cliente_vip": True, "data": "04/04/2025"}
]

vendas_por_produto = {}

for pedido in pedidos:
    produto, quantidade, preco_unitario, cliente_vip, data = pedido["produto"], pedido["quantidade"], pedido["preco_unitario"], pedido["cliente_vip"], pedido["data"]

    valor_total = quantidade * preco_unitario
    if cliente_vip:
        valor_total *= 0.9

    pedido["valor_final"] = round(valor_total, 2)

    vendas_por_produto[produto] = vendas_por_produto.get(produto, 0) + quantidade

    print(f"[{data}] Produto: {produto} | Qtde: {quantidade} | VIP: {'Sim' if cliente_vip else 'Não'} | Total: R${pedido['valor_final']:.2f}")

print("\nRelatório Final:")
total_pedidos = len(pedidos)
total_vendas = sum(pedido["valor_final"] for pedido in pedidos)
total_vendas_vip = sum(pedido["valor_final"] for pedido in pedidos if pedido["cliente_vip"])
valor_medio_pedido = total_vendas / total_pedidos
produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)

print(f"Total de pedidos: {total_pedidos}")
print(f"Total de vendas em reais: R${total_vendas:.2f}")
print(f"Total de vendas feitas para clientes VIP: R${total_vendas_vip:.2f}")
print(f"Valor médio por pedido: R${valor_medio_pedido:.2f}")
print(f"Produto mais vendido: {produto_mais_vendido} ({vendas_por_produto[produto_mais_vendido]} unidades)")