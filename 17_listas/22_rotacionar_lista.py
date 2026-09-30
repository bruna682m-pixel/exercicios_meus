# %%

numeros = [10, 20, 30, 40, 50]
aux = 0

for i, enu in enumerate(numeros):
    if i == 0:
        aux = enu

numeros.append(aux)
numeros[0] = numeros[1]
numeros[1] = numeros[2]
numeros[2] = numeros[3]
numeros[3] = numeros[4]
numeros.pop(4)

print(aux)
print(numeros)
    
# %%
numeros = [10, 20, 30, 40, 50]
aux = 0

for i, enu in enumerate(numeros):
    if i == len(numeros) - 1:
        aux = enu

numeros[4] = numeros[3]
numeros[3] = numeros[2]
numeros[2] = numeros[1]
numeros[1] = numeros[0]
numeros[0] = aux

print(aux)
print(numeros)
