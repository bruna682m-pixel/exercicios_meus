# %%
cardapio = {    
    "hamburguer": 18.00,    
    "batata": 9.00,    
    "suco": 6.00,    
    "sanduiche": 12.00
}

pedido = {}
total = 0

print("Mostrando cardápio:",cardapio)

while True:
    nome_produto = input("Digite o nome do produto ou digite sair para encerrar:")

    if nome_produto == "sair":
        print("Saindo....")
        break

    if nome_produto in cardapio:
        qtd_produto = int(input("Digite a qtd do produto:"))
        if nome_produto in pedido:
            pedido[nome_produto] = pedido[nome_produto] + qtd_produto
        else:
            pedido[nome_produto] = qtd_produto
    else:
        print("Seu produto não está no cardápio.")

for nome_produto, qtd_produto in pedido.items():
    total += cardapio[nome_produto] * qtd_produto


print(total)
print(pedido)


# %%
