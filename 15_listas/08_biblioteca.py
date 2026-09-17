# %%

livros = ["Dom Casmurro", "O Hobbit", "Harry Potter"]
emprestados = []

while True:
    opcao =  int(input("""
1 - Mostrar livros
2 - Cadastrar livro
3 - Remover livro
4 - Alterar livro
5 - Procurar livro
6 - Emprestar livro
7 - Devolver livro
8 - Mostrar quantidade
9 - Mostrar emprestados
10- Sair
"""))

    if opcao == 1:
        print("Livros:")
        print(livros)

    elif opcao == 2:
        add_livro = input("Digite o nome do livro:")

        livros.append(add_livro)

        print("Livro",add_livro,"adicionado.")

    elif opcao == 3:
        remover_indice = int(input("Digite o índice do livro:"))

        if livros == []:
            print("Lista vazia.")
        elif remover_indice >= 0 and remover_indice <= len(livros) -1:
            livros.pop(remover_indice)

            print("Livro removido.")

    elif opcao == 4:
        alterar_indice = int(input("Digite o índice do livro:"))

        if livros == []:
            print("Lista vazia.")
        elif alterar_indice >= 0 and alterar_indice <= len(livros) -1:
            livros[alterar_indice] = novo_livro = input("Digite o novo nome do livro:")

            print("Livro alterado para:",novo_livro)

    elif opcao == 5:
        procurar_indice = int(input("Digite o índice do livro:"))

        if livros == []:
            print("Lista vazia.")
        elif procurar_indice >= 0 and procurar_indice <= len(livros) -1:
            print("Livro encontrado",livros[procurar_indice])

    elif opcao == 6:
        emprestar_indice = int(input("Digite o índice do livro:"))

        if livros == []:
            print("Lista vazia.")
        elif emprestar_indice >= 0 and emprestar_indice <= len(livros) -1:
           emprestados.append(livros[emprestar_indice])
           livros.pop(emprestar_indice)
           print("Livro",emprestar_indice,"emprestado.")
           print(emprestados)

    elif opcao == 7:
        devolver_indice = int(input("Digite o índice do livro:"))

        if emprestados == []:
            print("Lista vazia.")
        elif devolver_indice >= 0 and devolver_indice <= len(emprestados) -1:
            livros.append(emprestados[devolver_indice])
            emprestados.pop(devolver_indice)
            print("Livro",devolver_indice,"devolvido.")
            print(emprestados)

    elif opcao == 8:
        print("Livros:",len(livros))
        print("Emprestados:",len(emprestados))

    elif opcao == 9:
            print("Emprestados:")
            print(emprestados)

    elif opcao == 10:
        print("Saindo....")
        break

    else:
        print("índice invalido....")

    