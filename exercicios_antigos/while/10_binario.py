# Solicitar um número inteiro na base decimal positivo ( consistir ) calcular o binário e mostrar

# %%
quociente = 0
resto = 0
numero = int(input("Digite um número para calcular o binário:"))
binario = ""


while numero < 0:
    numero = int(input("Digite um número para calcular o binário:"))

if numero == 0:
    print("Binário de",numero,"é 0")
else:
    while numero > 0:
        resto = numero % 2
        numero //= 2
        binario = str(resto) + binario

    print("O binário do seu número é:",binario)

    
    
