# %%
aux = 0
numeros = [10, 20, 30, 40, 50]

aux = numeros[0]
numeros[0] = numeros[4]
numeros[4] = aux

print(numeros)