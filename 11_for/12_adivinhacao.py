# %%
import random

numero_max = 7

while True:
    numero_pc = random.randint(1, 100)

    for i in range(1, numero_max+1):
        print("Tentativa",i,"de",numero_max)
        palpite = int(input("Digite seu palpite:"))

        if palpite > numero_pc:
            print("Palpite alto!")
        elif palpite < numero_pc:
            print("Palpite baixo!")
        else:
            print("Você acertou!")
            print("Tentativas utilizadas:",i)
            break

    else:
        print("Você perdeu.")
        print("O número era",numero_pc)

    opcao = int(input("Deseja jogar novamente? 1- sim 2- não."))
    if opcao == 2:
        break



# %%
