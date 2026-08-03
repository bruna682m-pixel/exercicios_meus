#%%
# Solicitar um número inteiro positivo ( consistir ), calcular o fatorial e mostrar

total = 1

numero = input("Digite um número para calcular o fatorial:")
numero = int(numero)

copia_numero = numero

if numero > 0:
    while numero >= 1:
        total = total * numero
        numero -= 1

    print("O fatorial de", copia_numero, "é igual a:", total)

elif numero == 0:
    print("O fatorial de", copia_numero, "é igual a: 1")

else:
    print("Digite um número positivo")