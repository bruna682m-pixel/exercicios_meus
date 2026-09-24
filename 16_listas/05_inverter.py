# %%

numeros = [10, 20, 30, 40, 50]
invertida = [0] * len(numeros)

for i, eun in enumerate(numeros):
       invertida[len(numeros) -1 -i] = eun

print(invertida)
