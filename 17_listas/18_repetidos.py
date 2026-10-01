# %%

numeros = [2, 5, 2, 8, 5, 2, 10]
sem_repetir = []

for i, enu in enumerate(numeros):
    if enu not in sem_repetir:
        sem_repetir.append(enu)

print(sem_repetir)