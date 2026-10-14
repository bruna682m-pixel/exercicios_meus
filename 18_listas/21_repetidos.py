# %%
lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [2, 4, 6]
sem_repetir = []

for i in lista_a:
    if i not in lista_b:
        sem_repetir.append(i)

print(sem_repetir)
