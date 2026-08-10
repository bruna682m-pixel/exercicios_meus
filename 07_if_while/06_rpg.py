# %%
import random
floresta_random = random.randint(1,4)
vida = 100
ataque = 10
moedas = 100
defesa = 0
pocoes = 0
espada = 0
armadura = 0
dragao = 100
ataque_dragao = 20

opcao_ataque_recusa = 0
opcao_menu = int(input("Digite a opção:"))

while True:
    opcao_menu = int(input("""
Rpg de texto

Vida: 100
Ataque: 10
Defesa: 0
Moedas: 0
Poções: 0

1- Explorar floresta
2- Loja
3- Descansar
4- Ver status
5- Enfretar dragão
6- Sair

"""))

    if opcao_menu == 1:
        if floresta_random == 1:
            opcao_ataque_recusa = int(input("""
Você encontrou o Fachada um Goblin:
            
1- Atacar
2- Fugir
"""))
            if opcao_ataque_recusa == 1:
                vida -= 15
                moedas += 20
                print("""
Você derrotou Fachada o Goblin. 
E recebeu 15 de dano ficando com""",vida,"""vidas. 
E recebeu 20 moedas ficando com""",moedas,)
            elif opcao_ataque_recusa == 2:
                print("Você conseguiu fugir. Não recebeu nenhum dano.",vida)
            else:
                print("Digite uma opção valida.")
        elif floresta_random == 2:
            opcao_ataque_recusa = int(input("""
Você encontrou o Tris o Lobo:
                    
1- Atacar
2- Fugir
"""))
            if opcao_ataque_recusa == 1:
                vida -= 10
                moedas += 10
                print("""
Você derrotou Tris o Lobo. 
E recebeu 10 de dano ficando com""",vida,"""vidas. 
E recebeu 10 moedas ficando com""",moedas,)
            elif opcao_ataque_recusa == 2:
                print("Você conseguiu fugir. Não recebeu nenhum dano.",vida)
            else:
                print("Digite uma opção valida.")

        elif floresta_random == 3:
            moedas += 30
            print("""
Você encontrou um baú:
dentro havia:
+ 30 moedas. Ficando com
""",moedas,"Moedas")
        elif floresta_random == 4:
                    vida -= 20
                    print("""
        Você caiu em uma armadilha e Ficou com
        """,vida,"vidas.")   

    elif opcao_menu == 2:

        opcao_menu = int(input(f"""
Loja
Moedas: {moedas}
1- Espada (50)
2- Armadura (80)
3- Poção (25)
4- Voltar
"""))        
        if opcao_menu == 1 and moedas >= 50:
             ataque = ataque + 10
             moedas = moedas - 50
             espada = True
             print("Espada comprada. Você ficou com:",ataque,"ataque e com",moedas,"moedas")
        elif opcao_menu == 2 and moedas >= 80:
             defesa = defesa + 10
             moedas = moedas - 80
             armadura = True
             print("Armadura comprada. Você ficou com:",defesa,"defesa e com",moedas,"moedas")
        elif opcao_menu == 3 and moedas >= 25:
             pocoes = pocoes + 1
             moedas = moedas - 25
             print("Poção comprada. Você ficou com +",pocoes,"poção e com",moedas,"moedas")
        elif opcao_menu == 4:
             print("Voltando ao menu.")
        else:
             print("Selecione uma opção valida ou você não tem dinheiro.")

    elif opcao_menu == 3:
        if vida < 100:
            vida = vida + 20
            print("Você descansou. Sua vida atual é:",vida)
        else:
            print("Sua vida já esta cheia.")

    elif opcao_menu == 4:
        if espada == True:
            espada = "sim"
        else:
             espada = "não"

        if armadura == True:
            armadura = "sim"
        else:
            armadura = "não"
        
         
        print("""
Status:
Vida:""",vida,"""
Ataque:""",ataque,"""
Defesa:""",defesa,"""
Moedas:""",moedas,"""
Poções:""",pocoes,"""
Armadura:""",armadura,"""
Espada:""",espada)

    elif opcao_menu == 5:
         print("HOPE O Dragão APARECEU")

         opcao_menu = int(input("""
1- Atacar
2- Usar poção
3- Fugir
"""))
         if opcao_menu == 1:
            if vida <= 0:
                print("GAME OVER")
                break
            else:
                if dragao <= 100 and dragao > 0:
                    print("Hope ainda tem",dragao,"vidas")
                    ataque_dragao = 0
                    vida = vida - 20
                    if espada == True:
                        ataque = 20
                        dragao = dragao - 20
                        print("drag",dragao)
                    else:
                        ataque = 10
                        dragao = dragao - 10
                        print("drag",dragao)
                else:
                    print("Você derrotou o dragão. Paranéns!")
                    print("Você venceu o jogo")
         elif opcao_menu == 2:
             if pocoes > 0 and vida < 100:
                 vida = vida + 30
                 pocoes = pocoes - 1
             else:
                print("Você não tem poção ou sua vida está cheia")

    elif opcao_menu == 6:
        print("Saindo...")  
        break      


# %%
# %%
import random
floresta_random = random.randint(4,4)
vida = 100
ataque = 10
moedas = 0
defesa = 0
pocoes = 0
espada = 0
armadura = 0
dragao = 0

opcao_ataque_recusa = 0
opcao_menu = int(input("Digite a opção:"))

while True:
    opcao_menu = int(input("""
Rpg de texto

Vida: 100
Ataque: 10
Defesa: 0
Moedas: 0
Poções: 0

1- Explorar floresta
2- Loja
3- Descansar
4- Ver status
5- Enfretar dragão
6- Sair

"""))

    if opcao_menu == 1:
        if floresta_random == 1:
            opcao_ataque_recusa = int(input("""
Você encontrou o Fachada um Goblin:
            
1- Atacar
2- Fugir
"""))
            if opcao_ataque_recusa == 1:
                vida -= 15
                moedas += 20
                print("""
Você derrotou Fachada o Goblin. 
E recebeu 15 de dano ficando com""",vida,"""vidas. 
E recebeu 20 moedas ficando com""",moedas,)
            elif opcao_ataque_recusa == 2:
                print("Você conseguiu fugir. Não recebeu nenhum dano.",vida)
            else:
                print("Digite uma opção valida.")
        elif floresta_random == 2:
            opcao_ataque_recusa = int(input("""
Você encontrou o Tris o Lobo:
                    
1- Atacar
2- Fugir
"""))
            if opcao_ataque_recusa == 1:
                vida -= 10
                moedas += 10
                print("""
Você derrotou Tris o Lobo. 
E recebeu 10 de dano ficando com""",vida,"""vidas. 
E recebeu 10 moedas ficando com""",moedas,)
            elif opcao_ataque_recusa == 2:
                print("Você conseguiu fugir. Não recebeu nenhum dano.",vida)
            else:
                print("Digite uma opção valida.")

        elif floresta_random == 3:
            moedas += 30
            print("""
Você encontrou um baú:
dentro havia:
+ 30 moedas. Ficando com
""",moedas,"Moedas")
        elif floresta_random == 4:
                    vida -= 20
                    print("""
        Você caiu em uma armadilha e Ficou com
        """,vida,"vidas.")   

    elif opcao_menu == 2:
        opcao_menu = int(input("""
Loja
Moedas:""",moedas,"""
1- Espada (50)
2- Armadura (80)
3- Poção (25)
4- Voltar
"""))        
        if moedas > 0:
            if opcao_menu == 1:
                print("espada")

    elif opcao_menu == 6:
        print("Saindo...")  
        break      
