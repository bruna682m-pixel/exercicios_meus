# %%

musicas = []
favoritas = []

while True:
    opcao = int(input("""Digite a opação:
    1- Adicionar música
    2- Mostrar playlist
    3- Remover música
    4- Alterar música
    5- Procurar música
    6- Mostrar primeira música
    7- Mostrar última música
    8- Quantidade de música
    9- Mostrar playlist invertida
    10- Marcas favoritas
    11- Sair
    
    """))

    if opcao == 1:
        add_musica = input("Digite o nome da música:")

        musicas.append(add_musica)

        print("Música adicionada.")

    elif opcao == 2:
        print("Suas músicas:")
        print(musicas)

        print("Suas músicas favoritas:")
        print(favoritas)

    elif opcao == 3:
        indice = int(input("Digite o índice da música para remover:"))

        if musicas == []:
            print("Playlist vazia.")
        elif indice >= 0 and indice <= len(musicas) -1:
            musicas.pop(indice)
            print("Música removida.")
        else:
            print("índice inválido.")

    elif opcao == 4:
        indice = int(input("Digite o índice da música para alterar:"))

        if musicas == []:
            print("Playlist vazia.")
        elif indice >= 0 and indice <= len(musicas) -1:
            alterar_musica = input("Digite a nova música:")
            musicas[indice] = alterar_musica 
            print("Música alterada.")
        else:
            print("índice inválido.")

    elif opcao == 5:
        indice = int(input("Digite o índice da música para procurar:"))

        if musicas == []:
            print("Playlist vazia.")
        elif indice >= 0 and indice <= len(musicas) -1:
            print("Playlist encontrado:",musicas[indice])
        else:
            print("índice inválido.")

    elif opcao == 6:
        print("A primeira música da playlist é:",musicas[0])

    elif opcao == 7:
        print("A última música da playlist é:",musicas[-1])

    elif opcao == 8:
        print("A playlist tem:", len(musicas), "músicas.")

    elif opcao == 9:
        print("Playlist invertida.",musicas[::-1])

    elif opcao == 10:
        indice = int(input("Digite o índice da música para favoritar:"))

        if musicas == []:
            print("Playlist vazia.")
        elif indice >= 0 and indice <= len(musicas) -1:
            favoritas.append(musicas[indice])
            print("Música adicionada a favoritas.")
        else:
            print("índice inválido.")

    elif opcao == 11:
        print("Saindo...")
        break

    else:
        print("índice invalido.")

