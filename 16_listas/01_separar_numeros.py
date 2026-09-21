# %%

numeros = [10, -5, 8, -2, 0, 15, -7]
positivos = []
negativos = []

for i in numeros:
    if i < 0:
        negativos.append(i)
    else:
        positivos.append(i)

print("Positivos", positivos)
print("Negativos", negativos)