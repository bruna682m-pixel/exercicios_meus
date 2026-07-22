# %%

total_compra = 0
total_qtd_produtos = 0

while True:
    produtos = input("Digite os preços dos produtos:")
    qtd_produto = input("Digite a quantidade dos produtos:")

    if produtos == "":
        break

    produtos = float(produtos)  
    qtd_produto = float(qtd_produto)  
    total_qtd_produtos = total_qtd_produtos + qtd_produto
    total_compra = total_compra + produtos
    
print("A soma total dos produtos deu:", total_compra, "A quantidade dos produtos deu: ", total_qtd_produtos)

# %%

total_compra = 0
total_produtos = 0

while True:
    produto = input("Digite o valor do produto:")
    qtd_produto = input("Digite a quantidade do produto:")

    if produto == "":
        break

    produto = float(produto)
    qtd_produto = int(qtd_produto)
    total_produtos = total_produtos + qtd_produto
    produto = produto * qtd_produto
    total_compra = total_compra + produto 

print("O total dos produtos deram:",total_compra, "Voce comprou", total_produtos, "produtos")
