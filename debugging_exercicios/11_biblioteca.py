# %%
livros_disponiveis = 10 # tem 10 livros no sistema
livros_emprestados = 0 # qtd de emprestados

while True: # loop infinito até o break

# digitar a opção
    opcao = int(input("""
1 - Cadastrar
2 - Emprestar
3 - Devolver
4 - Status
5 - Sair

Escolha:
"""))

# se opção for 1 cadastrat
    if opcao == 1:

        quantidade = int(input("Quantos livros cadastrar? ")) # pedindo qtd de livros p/ cadastrar

        if quantidade > 0: # não aceita negativo e 0
            livros_disponiveis += quantidade # soma os 10 com os os cadastrados

    elif opcao == 2: # se opção for 2 emprestrar

        quantidade = int(input("Quantos livros emprestar? ")) # pede qtd que quer emprestar 

        if quantidade <= livros_disponiveis: # verifica se qtd é menor que os livros que quer emprestar
            livros_emprestados += quantidade # soma os livros já emprestados com a qtd que vai emprestat
            livros_disponiveis -= quantidade # erro aqui estava diminuindo de livros_emprestados o certo é diminuir de quantidade . diminui os livros disponiveis da qtd emprestada

            print("Empréstimo realizado.") # emprestimo feito

    elif opcao == 3: # opção = 3 é para devolver

        quantidade = int(input("Quantos livros devolver? ")) # qtd devolver

        if quantidade <= livros_emprestados: # ver se qtd é menor á devolver é menor dos que foram emprestados se for não faz devolução
            livros_emprestados -= quantidade # diminui qtd á devolver da emprestada
            livros_disponiveis += quantidade # soma os devolvidos aos disponiveis

    elif opcao == 4: # mostra status

        print("Disponíveis:", livros_disponiveis)
        print("Emprestados:", livros_emprestados)

    elif opcao == 5: # para sair
        break