# %%

numero_max = 10
soma = 0

for i in range(0, numero_max+1):
    numero = int(input("Digite os números:"))

    if numero % 2 == 0:
        soma = soma + numero
        print(numero)


print("A soma é:",soma)