# %%
numero = 0
positivo = 0
negativo = 0
zeros = 0

for i in range(1, 6):
    numero = int(input("Digite 5 números:"))

    if numero < 0:
        negativo += 1
    elif numero == 0:
        zeros += 1
    else:
        positivo += 1

print("Positivos:",positivo)
print("Negativos:",negativo)
print("Zeros:",zeros)
    