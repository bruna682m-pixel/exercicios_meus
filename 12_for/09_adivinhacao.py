# %%
import random
numero_pc = random.randint(1,10)

while True:
    opcao_dificuldade = int(input("""
Escolha a dificuldade:
1- Fácil
2- Médio
3- Difícil
"""))

    if opcao_dificuldade == 1:
        numero_pc = random.randint(1,10)

        for i in range(1, 6):
            palpite = int(input("Digite seu palpite:"))

            if palpite == numero_pc:
                print("Acertou.")
                break
        else:
            print("Acabou suas tentativas.")

    elif opcao_dificuldade == 2:
        numero_pc = random.randint(1,50)

        for i in range(1, 8):
            palpite = int(input("Digite seu palpite:"))

            if palpite == numero_pc:
                print("Acertou.")
                break
        else:
            print("Acabou suas tentativas.")

    elif opcao_dificuldade == 3:
        numero_pc = random.randint(1 , 100)

        for i in range(1, 6):
            palpite = int(input("Digite sua palpite:"))

            if palpite == numero_pc:
                print("Acertou.")
                break
        else:
            print("Acabou suas tentativas.")

    else:
        print("Opção invalida.")

    novamente = int(input("""
Jogar novamente:
1- Sim 
2- Não
"""))

    if novamente == 1:
        print("voltando.")
    else:
        print("Saindo...")
        break