# %%

numeros = [10, 20, 30, 40, 50]
invertida = [0] * len(numeros)

for i, eun in enumerate(numeros):
       invertida[len(numeros) -1 -i] = eun

print(invertida)

# %%

numeros = [10, 20, 30, 40, 50]
invertida = []

for i in range(len(numeros)-1, -1, -1):
       invertida.append(numeros[i])

print(invertida)

 