# Solicitar um número inteiro na base decimal positivo ( consistir ) calcular o binário e mostrar
# %%
quociente = 0
resto = 0
numero = int(input("Digite um número para calcular o binário:"))

while numero < 0:
    numero = int(input("Digite um número para calcular o binário:"))


if numero > 0:
    quociente = numero // 2
    print("sai",numero, quociente)

if numero > 0:
    resto = numero % 2
    print("resto",numero,resto)

    if quociente > 0:
    resto = quociente % 2
    print("resto",numero,resto)

print("sai")
# %%
quociente = 0
resto = 0
numero = int(input("Digite um número para calcular o binário:"))

while numero < 0:
    numero = int(input("Digite um número para calcular o binário:"))

while numero > 0:
    resto = numero % 2
    quociente = numero // 2
    print("sai1",numero,quociente,resto)
    numero //= 2

print("sai2")

while quociente > 0:
    resto = quociente % 2
    print("resto",numero,resto)


print("sai3")

# %%
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

    
    
# %%
# %%
quociente = 0
resto = 0
numero = int(input("Digite um número para calcular o binário:"))
binario = ""

while numero < 0:
    numero = int(input("Digite um número para calcular o binário:"))

while numero > 0:
    resto = numero % 2
    quociente = numero // 2
    print("sai1",numero,quociente,resto)
    numero //= 2
    binario = str(resto) + binario
    print(type(resto))
    print(type(binario))
    print("b", resto,binario)
    
    

print("sai3")
