# %%

qtd_livro = 0
opcao = 0
qtd_total_livros = 10
qtd_emprestimo = 0

opcao = int(input("opcao"))

while True:
    opcao = int(input("""
Digite a opção do menu:
1- Cadastrar
2- Emprestar
3- Devolver
4- Mostrar quantidade
5- Sair
"""))

    if opcao == 1:
        qtd_livro = int(input("Quantos livros você quer cadastrar?"))

        if qtd_livro > 0:
            qtd_total_livros = qtd_total_livros + qtd_livro
            print("Você cadastrou",qtd_livro,"livros.")
        else:
            print("Digite uma quantidade valida de livros para cadastrar.")

    elif opcao == 2:
        qtd_livro = int(input("quantos livros você quer emprestar?"))

        if qtd_livro > qtd_total_livros:
            print("Não temos tudo isso de livros.")
        elif qtd_livro <= 0:
            print("Digite uma quantidade valida de livros para emprestrar.")
        else:
            qtd_total_livros = qtd_total_livros - qtd_livro
            print("Você emprestou",qtd_livro,"livros.")

    elif opcao == 3:
        qtd_livro = int(input("Digite a quantidade que você quer devolver?"))

        if qtd_livro > 0:
            qtd_total_livros = qtd_total_livros + qtd_livro
            print("Você devolveu",qtd_livro,"livros",qtd_total_livros)
        else:
            print("Digite uma quantidade valida de livros para devolver.")

    elif opcao == 4:
        print("A quantidade de livros no sistema é",qtd_total_livros,"livros.")

    elif opcao == 5:
        print("Saindo...")
        break

# %%
# %%

qtd_livro = 0
opcao = 0
qtd_total_livros = 10
qtd_emprestimo = 0

while True:
    opcao = int(input("""
Digite a opção do menu:
1- Cadastrar
2- Emprestar
3- Devolver
4- Mostrar quantidade
5- Sair
"""))

    if opcao == 1:
        qtd_livro = int(input("Quantos livros você quer cadastrar?"))

        if qtd_livro > 0:
            qtd_total_livros = qtd_total_livros + qtd_livro
            print("Você cadastrou",qtd_livro,"livros.")
        else:
            print("Digite uma quantidade valida de livros para cadastrar.")

    elif opcao == 2:
        qtd_emprestimo_novo = int(input("quantos livros você quer emprestar?"))

        if qtd_emprestimo_novo > qtd_total_livros:
            print("Não temos tudo isso de livros.")
        elif qtd_emprestimo_novo <= 0:
            print("Digite uma quantidade valida de livros para emprestrar.")
        else:
            qtd_emprestimo = qtd_emprestimo + qtd_emprestimo_novo
            qtd_total_livros = qtd_total_livros - qtd_emprestimo_novo
            print("Você emprestou",qtd_emprestimo_novo,"livros.")

    elif opcao == 3:
        qtd_livro = int(input("Digite a quantidade que você quer devolver?"))

        if qtd_livro > 0:
            if qtd_emprestimo > qtd_livro:
                qtd_total_livros = qtd_total_livros + qtd_livro
                qtd_emprestimo = qtd_emprestimo - qtd_livro
                print("Você ainda tem",qtd_emprestimo,"livros para devolver." )
            
            elif qtd_emprestimo == qtd_livro:
                qtd_emprestimo = qtd_emprestimo - qtd_livro
                qtd_total_livros = qtd_total_livros + qtd_livro
                print("Você devolveu todos os livros.")
            
            elif qtd_emprestimo < qtd_livro:
                print("Você está devolvendo mais livros que emprestou")

        else:
            print("Digite uma quantidade valida de livros para devolver.")

    elif opcao == 4:
        print("A quantidade de livros no sistema é",qtd_total_livros,"livros.")

    elif opcao == 5:
        print("Saindo...")
        break