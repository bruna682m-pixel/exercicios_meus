# %%

numeros = [10, 20, 30, 40, 50, 60]

invertida = []

for i in (range(len(numeros) -1, -1, -1)):
    invertida.append(numeros[i])

print(invertida)