# list - coleção ordenada, mutável e indexada. Permite duplicatas.
produtos = ["Café", "Pão", "Suco"]

# dict - coleção de pares chave-valor. Não é ordenada, mutável e não permite duplicatas.
produto = {"nome": "Café", "preco": 6.50}

# É possível combinar listas e dicionários para criar estruturas mais complexas. Por exemplo, podemos ter uma lista de dicionários, onde cada dicionário representa um produto com suas infos:
produtos = [
    {"nome": "Café", "preco": 6.50, "estoque": 20},
    {"nome": "Pão", "preco": 1.20, "estoque": 50},
    {"nome": "Suco", "preco": 8.00, "estoque": 15}
]

# Você recebeu a lista de produtos cadastrados no sistema acima.

# 1- Percorra a lista com um for.
for p in produtos:
    # 2- Imprima uma frase no formato:
    #Produto: Café | Preço: R$6.50 | Estoque: 20 unidades
    produto, preco, estoque = p["nome"], p["preco"], p["estoque"]
    print(f"Produto: {produto} | Preço: R${preco:.2f} | Estoque: {estoque} unidades")

