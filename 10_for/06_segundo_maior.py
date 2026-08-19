# %%

numero_max = 5
maior = 0
segundo_maior = 0

for i in range(1, numero_max+1):
    numero = float(input("Digite 5 números:"))

    if i == 1:
        maior = 0
        segundo_maior = 0
    else:
        if numero > maior:
            maior = numero

        if numero > maior and maior < segundo_maior:
            segundo_maior = maior

print(maior)
print(segundo_maior)

        