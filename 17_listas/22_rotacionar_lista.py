# %%

numeros = [10, 20, 30, 40, 50]
aux = 0

aux = numeros[0]
numeros[0] = numeros[-1]
numeros[-1] = aux
numeros[-1] = numeros[0]
numeros[0] = numeros[1]
numeros.pop(1)
numeros.append(aux)

print(aux)
print(numeros)
    
# %%
