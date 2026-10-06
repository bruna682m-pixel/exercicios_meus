# %%

lista = [1, 2, 4, 5, 6, 7, 8, 9, 10]
lista_pares = []

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)

print("Os números pares são:",lista_pares)

# %%
lista = [1, 2, 4, 5, 6, 7, 8, 9, 10]

lista_pares = [i for i in lista if i % 2 == 0]

print(f"Lista de pares: {lista_pares}")
