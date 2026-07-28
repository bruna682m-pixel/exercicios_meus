# %%
# Solicitar um valor inteiro positivo ( consistir ) e mostrar se esse número é par ou não par

numero = input("Digite um número inteiro:")

numero = int(numero)

if numero > 0:
    if numero % 2 == 0:
        print("Número par")
    elif numero % 2 != 0:
        print("Número impar")
else:
    print("Digite um número inteiro positivo")

    
# %%
numero = input("Digite um número inteiro:")

numero = int(numero)

if numero > 0:
    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número impar")
else:
    print("Digite um número inteiro positivo")
