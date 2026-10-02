# %%

numeros = [10, 21, 4, 45, 66, 93, 11]
pares = 0
impares = 0

for i in numeros:
    if i % 2 != 0:
        impares += 1
    else:
        pares += 1

print("Números pares:", pares)
print("Números impares:", impares)
