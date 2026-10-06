# %%

lista = [10, 20, 30, 40, 50]

for i, enu in enumerate(lista):
    if enu == 30:
        lista.insert(i + 1, 35)

print(lista)

# %%

lista = [10, 20, 30, 40, 50]
alvo = 30
novo_valor = 35

index = lista.index(alvo)

lista.insert(index + 1, novo_valor)

print(f"Lista atualizada: {lista} ")

