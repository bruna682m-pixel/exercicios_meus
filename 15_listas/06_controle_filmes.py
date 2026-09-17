# %%

filmes = []
assistidos = []

while True:
    opcao = int(input("""
1- Adicionar filme
2- Mostrar filme
3- Remover filme
4- Alterar filme
5- Procurar filme
6- Mostrar primeiro filme
7- Mostrar último filme
8- Mostrar quantidade
9- Marcar como assistido
10- Sair
"""))

    if opcao == 1:
        add_filme = input("Digite o filme que você quer adicionar:")
        filmes.append(add_filme)
        print("Filme",add_filme,"adicionada a lista.")

    elif opcao == 2:
        print("Sua lista:")
        print(filmes)

    elif opcao == 3:
        remover_filme = int(input("Digite o índice do filme que você quer remover:"))

        if filmes == []:
            print("Lista vazia.")
        elif remover_filme >= 0 and remover_filme <= len(filmes) -1:
            print("Filme",remover_filme,"removido da lista.")
            filmes.pop(remover_filme)
        else:
            print("ìndice invalido.")

    elif opcao == 4:
        alterar_filme = int(input("Digite o índice do filme que você quer alterar:"))
        novo_titulo_filme = input("Digite novo titulo:")
        
        if filmes == []:
            print("Lista vazia.")
        elif alterar_filme >= 0 and alterar_filme <= len(filmes) -1:
            filmes[alterar_filme] = novo_titulo_filme
            print("Filme",novo_titulo_filme,"alterado na lista.")
           
        else:
            print("ìndice invalido.")

    elif opcao == 5:
        procurar_filme = int(input("Digite o índice do filme para procurar:"))

        if filmes == []:
            print("A lista está vazia.")
        elif procurar_filme >= 0 and procurar_filme <= len(filmes) -1:
            print(filmes[procurar_filme])
            print("Filme",procurar_filme,"encontrado.")
        else:
            print("Filme não encontrado.")

    elif opcao == 6:
        primeiro_filme = filmes[0]
        print("Primeiro filme da lista é",primeiro_filme)

    elif opcao == 7:
        ultimo_filme = filmes[-1]
        print("O último filme foi:",ultimo_filme)

    elif opcao == 8:
        qtd_filmes = len(filmes)
        print("A quantidade de filmes é:",qtd_filmes)

    elif opcao == 9:
        marcar_assistido = int(input("Digite o índice do filme para marcar com assistido:"))

        if filmes == []:
            print("Lista vazia.") 
        elif marcar_assistido >= 0 and marcar_assistido <= len(filmes) -1:
            assistidos.append(filmes[marcar_assistido])
            filmes.pop(marcar_assistido)
            print("Filme",marcar_assistido,"marcado com assistido.")
        else:
            print("índice não encontrado.")

        print(assistidos)
                
    elif opcao == 10:
        print("Saindo...")
        break
    else:
        print("Opção invalida.")