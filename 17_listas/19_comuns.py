# %%

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

comuns = []

for i, enu in enumerate(lista1):
    for j, enu_j in enumerate(lista2):
        if enu == enu_j:
            if enu not in comuns:
                comuns.append(enu)

print(comuns)

# como usar set()

