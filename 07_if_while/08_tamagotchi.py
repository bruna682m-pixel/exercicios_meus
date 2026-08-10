# %%

fome = 50
sono = 50
energia = 50
felicidade = 50

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
        if fome > 0 and fome < 100:
            fome += 30
            energia -= 10
            print("Você comeu e ficou com",fome,"de fome")
        elif fome <= 0:
            print("Print seu pet morreu de fome.",fome)
            break
        elif fome > 100:
            print("Print está cheio.")
    elif opcao == 2:
        if energia > 0 and energia < 100:
            energia += 20
            fome -= 10
            print("Você dormiu. Recuperu 20 de energia:",energia,"E perdeu 10 de fome:",fome)
        elif energia <= 0:
            print("Você está sem energia. Dorma rápido.")
        elif energia > 100:
            print("Você está descansado")
    elif opcao == 3:
        if felicidade > 0 and felicidade < 100:
            felicidade += 30
            energia -= 20
            fome -= 10
        elif felicidade <= 0:
            print("Sua felicidade está no minimo. Vá brincar um pouco.",felicidade)
        elif felicidade > 100:
            print("Sua felicidade está no máximo",felicidade)