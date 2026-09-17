# %%

nomes = []
telefones = []

while True:
    opcao = int(input("""
1- Adicionar contato
2- Mostrar contatos
3- Procurar contato
4- Alterar contato
5- Remover contato
6- Sair

"""))

    if opcao == 1:
        add_nome = input("Digite o nome do contato:")
        add_telefone = input("Digite o número do contato:")

        nomes.append(add_nome)
        telefones.append(add_telefone)

        print("Telefone",add_telefone,"adicionado com o nome",add_nome)

    elif opcao == 2:
        print("Mostrando contatos:")
        print(nomes)
        print(telefones)

    elif opcao == 3:
        procurar_telefone = int(input("Digite o índice do contato:"))

        if nomes == [] and telefones == []:
            print("Lista vazia.")
        elif procurar_telefone >= 0 and procurar_telefone <= len(nomes) -1:
            nome_achado = nomes[procurar_telefone]
            telefone_achado = telefones[procurar_telefone]

            print("Contato encontrado:",nome_achado,telefone_achado)
        else:
            print("índice invalido.")

    elif opcao == 4:
        alterar_indice = int(input("Digite o índice do contato:"))

        if nomes == [] and telefones == []:
            print("Lista vazia.")
        elif alterar_indice >= 0 and alterar_indice <= len(nomes) -1:
            nomes[alterar_indice] = novo_nome = input("Digite o novo nome:")
            telefones[alterar_indice] = novo_telefone = input("Digite o novo telefone")

            print("Contato alterado para:", novo_nome, novo_telefone)
        else:
            print("índice invalido.")

    elif opcao == 5:
        remover_indice = int(input("Digite o índice do contato:"))

        if nomes == [] and telefones == []:
            print("Lista vazia.")
        elif remover_indice >= 0 and remover_indice <= len(nomes) -1:
            nomes.pop(remover_indice)
            telefones.pop(remover_indice)

            print("Contato removido.")
        else:
            print("índice invalido.")

    elif opcao == 6:
        print("Saindo..")
        break
    else:
        print("Opção errada.")