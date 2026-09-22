# %%
produtos = []

while True:
    add_produto = input("Digite o nome do produto ou fim para encerrar:")

    if add_produto == "fim":
        print("Saindo...")
        break
    else:
        produtos.append(add_produto)

print("Carrinho:",produtos)
print("Quantidade:",len(produtos))