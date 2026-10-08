# %%
lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [2, 4, 6]
lista_diferenca = []

for i, enu in enumerate(lista_a):
    if enu not in lista_b:
        lista_diferenca.append(enu)

print(lista_diferenca)