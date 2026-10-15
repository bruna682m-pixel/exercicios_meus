
# %%
produtos = {
    "Teclado": 200,
    "Meias":  100,
    "Mouse": 60,
    "Uva": 7.99,
    "Mala": 500
    }

loop = 1
total = 0

while loop <= 3:
    produto = input("Digite 3 produtos:")

    if produto not in produtos:
        print("Não temos esse")
    else:
        for chave, valor in produtos.items():
            if chave == produto:
                total += valor
                
    loop += 1

print(produtos)
print(total)

