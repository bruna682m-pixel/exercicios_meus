# %%

lista = [10, 20, 30, 40, 50]
aux = 0

aux = lista[4]
lista[4] = lista[0]
lista[0] = lista[1]
lista[1] = lista[2]
lista[2] = lista[3]
lista[3] = aux

print(lista)
