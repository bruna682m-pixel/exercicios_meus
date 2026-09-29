# %%

numeros = [10, 20, 30, 40, 50]
aux = 0
aux2 = 0

aux = numeros[0]
numeros[0] = numeros[-1]
numeros[-1] = aux

print(aux)
print(numeros)

# %%
numeros = [10, 20, 30, 40, 50]
aux = 0
aux2 = 0
indice = len(numeros) -1

for i, numeros in enumerate(numeros):
    if i == 0:
        aux = numeros
        numeros[0] = aux2

    if i == indice:
            aux2 = numeros
            numeros[-1] = aux
    
print(aux)
print(aux2)
print(numeros)





    

    
