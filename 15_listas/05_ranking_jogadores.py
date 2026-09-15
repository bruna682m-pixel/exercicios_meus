# %%

jogadores = []
pontuacoes = []
numero_1 = 0
pontuacao_1 = 0
numero_2 = 0
pontuacao_2 = 0
numero_3 = 0
pontuacao_3 = 0
volta = 0

while True:
    jogador = input("Digite seu nome:")
    pontuacao = input("Digite sua pontuação")

    if jogador == "" and pontuacao == "":
        print("saindo...")
        break
    else:
        pontuacao = int(pontuacao)
        jogadores.append(jogador)
        pontuacoes.append(pontuacao)

    if volta == 0:
        numero_1 = jogador
        pontuacao_1 = pontuacao
        numero_2 = jogador
        pontuacao_2 = pontuacao
        numero_3 = jogador
        pontuacao_3 = pontuacao
    else:
        if pontuacao > pontuacao_1:
            pontuacao_1 = pontuacao
        else:
            if pontuacao_1 >= pontuacao:
                pontuacao_2 = pontuacao_1
            else:
                pontuacao_2 <= pontuacao
                pontuacao_3 = pontuacao_2
        
    volta += 1
print(pontuacao_1)
print(pontuacao_2)
print(pontuacao_3)
