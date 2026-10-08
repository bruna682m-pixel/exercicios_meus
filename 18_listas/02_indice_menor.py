# %%
lista = [40, 15, 70, 8, 25]
menor = 0
indice_menor = 0

for i, enu in enumerate(lista):
    if i == 0:
        menor = enu
    else:
        if enu < menor:
            menor = enu
            indice_menor = i


print(menor)
print(indice_menor)