# %%

numeros = [5, -2, 0, 8, -10, 0, 3, -1]
negativos = 0
positivos = 0
zeros = 0

for i in numeros:
    if i < 0:
        negativos += 1
    elif i == 0:
        zeros += 1
    else:
        positivos += 1

print("Positivos:",positivos)
print("Negativos:",negativos)
print("Zeros:", zeros)