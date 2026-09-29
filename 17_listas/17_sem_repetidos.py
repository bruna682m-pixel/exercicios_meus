# %%

numeros = [2, 5, 2, 8, 5, 2, 10]
sem_repetir = []

for i, enu in enumerate(numeros):
    for j, enu_j in enumerate(numeros):
        if enu != enu_j and i != j:
            if enu not in sem_repetir:
                sem_repetir.append(enu)

print(sem_repetir)
