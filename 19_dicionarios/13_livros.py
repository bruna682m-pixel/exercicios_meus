# %%
livros = {}
loop = 1
pesquisa_titulo = 0

while True:
    opcao = int(input("Digite uma opção:"))
    if opcao == 1:
        if loop <= 2:
            titulo = input("Digite o titulo do livro:")
            autor = input("Digite o autor do livro:")
            if titulo not in livros:
                livros[titulo] = autor

                loop += 1
            else:
                print("Titulo repertido.")
        else:
            print("Limite de cadastro atingido.")

    elif opcao == 2:
        pesquisa_titulo = input("Digite o titulo de um livro:")

        if pesquisa_titulo in livros:
            print(livros[pesquisa_titulo])
        else:
            print("titulo não está cadastrado.")


    elif opcao == 3:
        print("saindo....")
        break

    else:
        print("opção inválida.")

