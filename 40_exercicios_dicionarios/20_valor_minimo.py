# %%
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}

loop = 0
menor = 0
chave_menor = 0

for chave, valor in stock.items():
    if loop == 0:
        menor = valor
        chave_menor = chave
    else:
        if valor < menor:
            menor = valor
            chave_menor = chave
    loop += 1

print("Produto com estoque mais baixo:", chave_menor)

# %%
stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}

lowest = min(stock, key=stock.get)
print("Baixo:", lowest)
