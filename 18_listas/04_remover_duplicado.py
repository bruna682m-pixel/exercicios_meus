# %%

lista = [5, 2, 5, 8, 2, 10, 8, 3]
lista_sem_repetir = []

for i, enu in enumerate(lista):
    if enu not in lista_sem_repetir:
        lista_sem_repetir.append(enu)

print(lista_sem_repetir)
  
