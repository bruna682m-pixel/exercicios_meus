# %%

lista = [5, 2, 5, 8, 2, 10, 8, 3]
sem_repetir = []

for i in lista:
    if i not in sem_repetir:
        sem_repetir.append(i)

print(sem_repetir)