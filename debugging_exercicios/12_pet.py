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

        if energia < 0:
            energia = 0

        print("Você alimentou o pet.")

    elif opcao == 2:

        energia += 20
        fome += 10

        if energia > 100:
            energia = 100

        if fome > 100:
            fome = 100

        print("Você dormiu.")

    elif opcao == 3:

        if energia < 20:
            print("Você está cansado.")

        felicidade += 30
        energia -= 20
        fome += 10

        if felicidade > 100:
            felicidade = 100

    elif opcao == 4:

        if energia < 30:
            print("Você está cansado.")

        dinheiro += 50
        energia -= 30
        fome += 20
        felicidade -= 10

    elif opcao == 5:

        print("Fome:", fome)
        print("Energia:", energia)
        print("Felicidade:", felicidade)
        print("Dinheiro:", dinheiro)

    elif opcao == 6:

        print("Saindo...")
        break