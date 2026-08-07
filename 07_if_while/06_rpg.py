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
        print("loja")          # parei na loja 

    elif opcao_menu == 6:
        print("Saindo...")  
        break      

# %%
# %%
import random
floresta = random.randint(1,4)
vida = 100
ataque = 10
moedas = 0
defesa = 0
pocoes = 0
espada = 0
armadura = 0
dragao = 0

opcao = int(input("Digite a opção:"))

while True:
    opcao = int(input("""
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

    if opcao == 1:
        opcao = int(input("""
        Você encontrou o Fachada um Goblin:

        1- Atacar
        2- Fugir
"""))
        if floresta == 1:

            if opcao == 1:
                vida -= 15
                moedas += 20
                print("""
Você derrotou Fachada o Goblin. 
E recebeu 15 de dano ficando com""",vida,"""vidas. 
E recebeu 20 moedas ficando com""",moedas,)
            elif opcao == 2:
                print("Você conseguiu fugir. Não recebeu nenhum dano.",vida)
            else:
                print("Digite uma opção valida.")
    

    if opcao == 6:
        print("Saindo...")  
        break      


