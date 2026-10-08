# %%
lista = [10, 20, 15, 40, 50]
ordenada = True
tamanho = len(lista)

for i in range(tamanho):
    for j in range(0, tamanho - i -1):
        if lista[j] < lista[j + 1]:
            ordenada = False

print(ordenada)

# %%
