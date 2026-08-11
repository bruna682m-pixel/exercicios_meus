
# %%

fome = 50
sono = 50
energia = 50
felicidade = 50
dinheiro = 0

opcao = (input("""
Digite a opção:

1- Alimentar
2- Dormir
3- Brincar
4- Trabalhar
5- Status
6- Sair
"""))

while True:
    opcao = int(input("""
Digite a opção:

1- Alimentar
2- Dormir
3- Brincar
4- Trabalhar
5- Status
6- Sair
"""))
    if opcao == 1:
        fome -= 30
        energia -= 10
        if fome < 0:
            fome = 0
            print("Você esta cheio.")

        if energia < 0:
            energia = 0
            print("Você está sem energia. Vá dormir")

        print("Você alimentou seu pet.")
        print("Fome:",fome)
        print("Energia:",energia)

    elif opcao == 2:
        energia += 20
        fome += 10
        if energia > 100:
            energia = 100
            print("Você está cheio de energia")

        if fome >= 100:
            fome = 100
            print("Seu pet morreu de fome.")
            break

        print("Você dormiu.")
        print("Energia:",energia)
        print("Fome:",fome)

    elif opcao == 3:
        if energia < 20:
            print("Você está muito cansado para brincar.")
        else:
            felicidade += 30
            energia -= 20
            fome += 10

        if felicidade > 100:
            felicidade = 100
            print("Você está muito feliz.")

        if energia < 0:
            energia = 0
            print("Você está sem energia.")

        if fome > 100:
            fome = 0
            print("Seu pet morreu de fome.")

        print("Você brincou. Sua felicidade é:",felicidade)
        print("Energia:",energia)
        print("Fome:",fome)

    elif opcao == 4:
        if energia < 30:
            print("Você está muito cansado para trabalhar.")
        else:
            dinheiro += 50
            energia -= 30
            fome += 20
            felicidade -= 10

        if felicidade < 0:
            felicidade = 0
            print("Você está muito infeliz.")
        
        if energia < 0:
            energia = 0
            print("Você está sem energia.")
        
        if fome > 100:
            fome = 0
            print("Seu pet morreu de fome.")
        
        print("Você trabalhou. Sua conta está com:",dinheiro)
        print("Energia:",energia)
        print("Fome:",fome)
        print("Felicidade:",felicidade)

    elif opcao == 5:
        print("""
Seu status é:
Fome:""",fome,"""
Energia:""",energia,"""
Sono:""",sono,"""
Felicidade:""",felicidade,"""
Dinheiro:""",dinheiro)
        
    elif opcao == 6:
        print("Saindo...")
        break

        
