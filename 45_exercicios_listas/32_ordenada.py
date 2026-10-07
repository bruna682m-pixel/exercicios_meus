# %%
lista = [10, 20, 30, 25, 40]
ordenada = True
tamanho = len(lista)

for i in range(tamanho):
    for j in range(0, tamanho - i -1):
        if  lista[j] > lista[j + 1]:
            ordenada = False
        

print(f"A Lista está ordenada: {ordenada}")

# %%
lista = [10, 20, 30]
ordenada = True

for i in lista:
    for j in lista:
        if  i > j:
            ordenada = False
            break
        else:
            ordenada = True

print(f"A Lista está ordenada: {ordenada}")

