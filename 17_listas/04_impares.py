# %%

numeros = [3, 8, 11, 20, 25, 30, 41]
impares = []

for i in numeros:
    if i % 2 == 1:
        impares.append(i)

print(impares)

# %%

numeros = [3, 8, 11, 20, 25, 30, 41]
impares = []

for i in numeros:
    if i % 2 != 0:
        impares.append(i)

print(impares)

