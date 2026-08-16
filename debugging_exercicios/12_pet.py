# %%
fome = 50
energia = 50
felicidade = 50
dinheiro = 0

while True:

    opcao = int(input("""
1 - Alimentar
2 - Dormir
3 - Brincar
4 - Trabalhar
5 - Status
6 - Sair

Escolha:
"""))

    if opcao == 1:

        fome -= 30
        energia -= 10

        if fome < 0:
            fome = 0

        if fome == 0:
            print("Você está cheio.")
        else:
            print("Você alimentou o pet.")

        if energia <= 0:
            energia = 0
            print("Você está muito cansado")

    elif opcao == 2:

        energia += 20
        fome += 10

        if energia > 100:
            energia = 100
            print("Você está com máxima energia.")
       
        print("Você dormiu.")

        if fome > 100:
            fome = 100
            print("Você está com muita fome. Game over.")
            break
        elif fome > 90:
            print("Cuidado com a fome. Você está com",fome,"de fome.")

    elif opcao == 3:

        if energia < 20:
            print("Você está cansado para brincar.")
        else:
            print("Você brincou.")
            felicidade += 30
            energia -= 20
            fome += 10

            if felicidade > 100:
                felicidade = 100
                print("Felicidade máxima.")
            elif felicidade < 0:
                felicidade = 0
                print("Você está infeliz")

        if fome > 100:
            fome = 100
            print("Você está com muita fome. Game over.")
            break
        elif fome > 90:
            print("Cuidado com a fome. Você está com",fome,"de fome.")

    elif opcao == 4:

        if energia < 30:
            print("Você está cansado para trabalhar.")
        else:
            print("Você trabalhou.")
            dinheiro += 50
            energia -= 30
            fome += 20
            felicidade -= 10

            if fome > 100:
                fome = 100
                print("Você está com muita fome. Game over.")
                break
            elif fome > 90:
                print("Cuidado com a fome. Você está com",fome,"de fome.")

            if felicidade > 100:
                felicidade = 100
                print("Felicidade máxima.")
            elif felicidade < 0:
                felicidade = 0
                print("Você está infeliz")
        

    elif opcao == 5:

        print("Fome:", fome)
        print("Energia:", energia)
        print("Felicidade:", felicidade)
        print("Dinheiro:", dinheiro)

    elif opcao == 6:

        print("Saindo...")
        break

    else:
        print("Opção inválida.")