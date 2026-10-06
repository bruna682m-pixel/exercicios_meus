# %%

lista1 = ["Py", "is", "awes"]
lista2 = ["thon", "", "ome"]

resultado = []

for i, enu in enumerate(lista1):
    resultado.append(enu + str(lista2[i]))

print(resultado)

# %%
lista1 = ["Py", "is", "awes"]
lista2 = ["thon", "", "ome"]

resultado =  [i + str(j) for i, j  in zip(lista1, lista2)]

print(resultado)
