# %%

numeros = [2, 5, 2, 8, 5, 2, 10]
repetidos = []

for i, enu in enumerate(numeros):
    for j, outro_enu in enumerate(numeros):
        if numeros == outro_enu and i != j:
            if enu not in repetidos:
                repetidos.append(enu)

print(repetidos)