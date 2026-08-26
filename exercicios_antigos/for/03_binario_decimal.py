
# Solicitar um valor inteiro positivo ( consistir) na base decimal e mostrar o binário.

# %%

numero = int(input("Digite um número:"))
resto = 0
binario = ""

for i in range(1, numero+1, 2):

    if numero > 0:
        resto = numero % 2
        numero //= 2
        binario = str(resto) + binario

print(binario)

