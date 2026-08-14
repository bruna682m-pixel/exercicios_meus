# %%
total = 0 # variavel total = 0

while True: # loop infinito atá digitar 0 que vai para o break
    preco = float(input("Digite o preço do produto ou 0 para finalizar: ")) # pedindo o preço dos produtos

    if preco == 0: # se digitar 0 sai do programa
        break

    total = total + preco # estava colocando o valor de preço dentro do total

print("Total da compra:", total) # mostra o preço total

# erro estava colocando o valor de preço dentro do total
# somei o valor de preço a cada volta do loop total + preco e coloquei o resultado em total