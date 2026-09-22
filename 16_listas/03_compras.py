# %%

produtos = []
loop = 1
indice_encontrado = 0
encontrado = False

while loop <= 5:
    entrada_produto = input("Digite 5 produtos:")

    produtos.append(entrada_produto)

    loop += 1

procurar = input("Digite o produto que você quer procurar:")

for i, enu in enumerate(produtos):
    if enu == procurar:
        encontrado = True
        indice_encontrado = i


if encontrado == True:
    print("Seu produto foi encontrado. E está no índice:",indice_encontrado)
else:
    print("Seu produto não foi encontrado.")

            

# %%
