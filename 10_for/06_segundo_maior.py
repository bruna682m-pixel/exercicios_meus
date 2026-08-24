# %%

numero_max = 5
maior = 0
segundo_maior = 0

for i in range(1, numero_max+1):
    numero = float(input("Digite 5 números:"))

    if i == 1:
        maior = numero
    elif i == 2:
        if numero > maior:
            segundo_maior = maior
            maior = numero
        else:
            segundo_maior = numero
    else:
        if numero > maior:
            segundo_maior = maior
            maior = numero

        if numero > segundo_maior and numero < maior:
            segundo_maior = numero


print(maior)
print(segundo_maior)

# %%
# sem valor definido none
numero_max = 5

maior = None
segundo_maior = None

for i in range(1, numero_max + 1):
    numero = float(input("Digite 5 números: "))

    if maior is None:
        maior = numero

    elif numero >= maior:
        segundo_maior = maior
        maior = numero

    elif segundo_maior is None or numero > segundo_maior:
        segundo_maior = numero

print("Maior:", maior)
print("Segundo maior:", segundo_maior)

# segundo maior e maior iguais
numero_max = 5

maior = None
segundo_maior = None

for i in range(1, numero_max + 1):
    numero = float(input("Digite 5 números: "))

    if maior is None:
        maior = numero

    elif numero >= maior:
        segundo_maior = maior
        maior = numero

    elif segundo_maior is None or numero > segundo_maior:
        segundo_maior = numero

print("Maior:", maior)
print("Segundo maior:", segundo_maior)


        