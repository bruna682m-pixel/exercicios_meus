# %%
import random


tentativa = 1
numero_usuario = int(input("Digite um número:"))

opcao = int(input("""
Escolha a dificuldade

1- Fácil
2- Médio
3- Dificil
"""))

if opcao == 1:
    numero_pc = random.randint(1,10)
    print("10")
elif opcao == 2:
    numero_pc = random.randint(1,50)
    print("50")
else:
    numero_pc = random.randint(1,100)
    print("100")

while True:
    numero_usuario = int(input("Digite um número:"))
    if numero_pc > numero_usuario:
        print("maior")
    elif numero_pc < numero_usuario:
        print("menor")
    else:
        print("acertou")
        break
    tentativa += 1

    if tentativa > 10:
        print("Acabou as tentativas")
        break

if tentativa == 1:
    print("Mestre dos números")
elif tentativa <= 2:
    print("Detetive")
elif tentativa <= 5:
    print("Investigador")
elif tentativa <= 8:
    print("Aprendiz")
elif tentativa == 9:
    print("Persistente")

print("Voce tentou",tentativa,"vezes")

# %%
numero_pc = 3
tentativa = 1
numero_usuario = int(input("Digite um número:"))
pontuacao = 100

while True:
    numero_usuario = int(input("Digite um número:"))
    if numero_pc > numero_usuario:
        print("maior")
    elif numero_pc < numero_usuario:
        print("menor")
    else:
        print("acertou")
        break
    tentativa += 1

    while pontuacao > 100:
        print("Voce tentou",tentativa,"vezes")

    if pontuacao > 100:
        pontuacao = pontuacao - 10
        print("-10")
    elif tentativa > 10:
        print("Acabou as tentativas")
        break

    


print("Voce tentou",tentativa,"vezes")
