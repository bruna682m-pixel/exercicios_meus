# %%

lista = [1, 3, 3, 2, 1, 1, 4, 3, 3]
lista_modificada = []

for i, enu in enumerate(lista):
    for j, enuj in enumerate(lista):
        if i == j:
            if enu not in lista_modificada:
                lista_modificada.append(enu)

print(lista_modificada)