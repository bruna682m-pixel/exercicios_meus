# %%

produtos = {
    "Teclado": 200,
    "Meias":  100,
    "Mouse": 60,
    "Uva": 7.99,
    "Mala": 500
    }

loop = 0
maior = 0
nome = 0

for chave, valor in produtos.items():
    if loop == 0:
        maior = valor
        nome = chave
    else:
        if valor > maior:
            maior = valor
            nome =  chave

    loop +=1

print("Maior:",maior, nome)

