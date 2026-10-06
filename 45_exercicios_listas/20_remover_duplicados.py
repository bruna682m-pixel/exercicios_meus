# %%
lista = [10, 20, 10, 30, 40, 40, 20, 50]
lista_nova = []

for i, enu in enumerate(lista):
    if enu not in lista_nova:
        lista_nova.append(enu)

print(lista_nova)

# %%
lista = [10, 20, 10, 30, 40, 40, 20, 50]

lista_unica = list(dict.fromkeys(lista))

print(f"Lista limpa: {lista_unica}")