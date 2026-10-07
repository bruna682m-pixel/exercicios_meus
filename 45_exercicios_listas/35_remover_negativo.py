# %%
lista = [10, -5, 20, -1, 0, -8]


for i in range(len(lista) -1, -1, -1):
    if lista[i] < 0:
        del lista[i]

print(lista)