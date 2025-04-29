# Você recebeu um dicionário com informações de uma venda. Crie variáveis separadas e calcule o total da venda:

venda = {
    "produto": "Café",
    "quantidade": 4,
    "preco_unitario": 6.50,
    "cliente_vip": True
}

produto = venda["produto"]
quantidade = venda["quantidade"]
preco_unitario = venda["preco_unitario"]
cliente_vip = venda["cliente_vip"]

# 1- Se cliente_vip for True, aplique 10% de desconto no valor total.
if cliente_vip:
    desconto = 0.10
    valor_total = (quantidade * preco_unitario) * (1 - desconto)
    print(f"Venda realizada: {quantidade} x {produto} por R${preco_unitario}. Total com desconto: R${"{:.2f}".format(valor_total)}")
else:
    desconto = 0.00
    valor_total = (quantidade * preco_unitario)
    print(f"Venda realizada: {quantidade} x {produto} por R${preco_unitario}. Total: R${"{:.2f}".format(valor_total)}") 


