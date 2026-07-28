# %%
vida = 100
pergunta = 0
total = 0

while True:
    pergunta = input("""
    O que voce quer fazer?
    1- Receber dano = - 5 de dano
    2- Tomar poção = + 3 de vida
    3- Ver vida
    4- Sair
    """)

    pergunta = int(pergunta)

    if pergunta == 1:
        if vida == 0:
            print("Voce perdeu todas as suas vidas.")
            break
        vida = vida - 5
        print("Voce tomou 5 de dano. Sua vida é de:", vida)
    if pergunta == 2:
        if vida >= 100:
            print("Voce já tem vida maxima.")
        else:
            vida = vida + 3
            print("Voce ganhou 3 vidas. Sua vida é de:", vida)
    if pergunta == 3:
        print("Sua vida é:",vida)
    if pergunta == 4:
        break

print("Sua vida é:",vida)


# %%
