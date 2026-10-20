# %%
jogadores = {}
maior = 0
chave_maior = 0
ate_100 = 0
empate = 0

while True:
    opcao = int(input("Digite a opção:"))

    if opcao == 1:
        jogador = input("Digite o nome do jogador:")

        if jogador not in jogadores:
            pontuacao = float(input("Digite sua pontuação:"))
            jogadores[jogador] = pontuacao
        else:
            print("Jogador já existe.")

    elif opcao == 2:
        consultar_jogador = input("Digite o nome do jogador para consultar:")

        if consultar_jogador in jogadores:
            print(jogadores[consultar_jogador])
        else:
            print("Cadastro não encontrado.")

    elif opcao == 3:
        atualizar_pontuacao = input("Digite o nome para atualizar pontuação:")

        if atualizar_pontuacao in jogadores:
            pontuacao_nova = float(input("Digite o nova pontuação:"))
            jogadores[atualizar_pontuacao] = pontuacao_nova
        else:
            print("Cadastro não encontrado.")

    elif opcao == 4:
        loop = 0
        for chave, valor in jogadores.items():
            if loop == 0:
                maior = valor
                chave_maior = chave
            else:
                if valor > maior:
                    maior = valor
                    chave_maior = chave

            loop += 1

        print("Maior pontuação:",chave_maior, maior)

    elif opcao == 5:
        if maior == 0:
            print("Calcule o maior primeiro")
        else:
            for c, v in jogadores.items():
                if v == maior:
                 empate += 1
                else:
                    print("Sem empate.", empate)
 
        print(empate)

    elif opcao == 6:
        for chave_100, valor_100 in jogadores.items():
            if valor_100 <= 100:
                ate_100 += 1

        print("Jogadores com ate 100 pontos:", ate_100)

    elif opcao == 7:
        print("Saindo......")
        break

    else:
        print("Opção invalida.")
