# %%

produtos = ["arroz", "feijao", "macarrao"]

while True:
    opcao = int(input("""
1- Mostrar produtos
2- Adicionar produto
3- Remover produto pelo índice
4- Alterar produto pelo índice
5- Mostrar quantidade de produtos
6- Sair
"""))

    if opcao == 1:
        print("Produtos no estoque.")
        print(produtos)

    elif opcao == 2:
        add_produto = input("Digite o produto para adicionar no estoque:")

        produtos.append(add_produto)

        print("O produto", add_produto,"foi adicionado ao estoque.")
        print("Agora você tem",produtos, "no estoque.")


    elif opcao == 3:
        remover_indice = int(input("Digite o índice do produto para remover:"))

        if produtos == []:
            print("A lista está vazia. Não tem o que remover.")

        for i, enu in enumerate(produtos):
            if i == remover_indice:
                print("O produto", enu,"foi removido.")
                produtos.pop(i) 

        if i != remover_indice:
            print("O índice não existe na lista.")

    elif opcao == 4:
        alterar_indice = int(input("Digite qual o índice do produto para alterar:"))

        if produtos == []:
            print("A lista está vazia. Não tem o que alterar.")

        for i, enu in enumerate(produtos):
            if i == alterar_indice:
                produtos[i] = alterar_produto = input("Digite o nome do produto para alterar:")
                print("O produto", enu, "foi alterado para", alterar_produto)
        else:
            print("O índice não existe na lista")

    elif opcao == 5:
        print("A quatidade de produtos no estoque é:", len(produtos))
    
    elif opcao == 6:
        break

    else:
        print("Opção invalida.")
# %%

produtos = ["arroz", "feijao", "macarrao"]

while True:
    opcao = int(input("""
1- Mostrar produtos
2- Adicionar produto
3- Remover produto pelo índice
4- Alterar produto pelo índice
5- Mostrar quantidade de produtos
6- Sair
"""))

    if opcao == 1:
        print("Produtos no estoque.")
        print(produtos)

    elif opcao == 2:
        add_produto = input("Digite o produto para adicionar no estoque:")

        produtos.append(add_produto)

        print("O produto", add_produto,"foi adicionado ao estoque.")
        print("Agora você tem",produtos, "no estoque.")


    elif opcao == 3:
        remover_indice = int(input("Digite o índice do produto para remover:"))


        if produtos == []:
            print("Lista vazia.")
        else:
            if remover_indice >= 0 and remover_indice <= len(produtos) -1:
                produtos.pop(remover_indice)
                print(produtos) 
            else:
                print("índice invalido.")

    elif opcao == 4:
        alterar_indice = int(input("Digite qual o índice do produto para alterar:"))

        if produtos == []:
            print("Lista vazia.")
        else:
            if  alterar_indice >= 0 and alterar_indice <= len(produtos) -1:
                        produtos[alterar_indice] = novo_produto = input("Digite o nome do novo produto:")
                        print(produtos) 
            else:
                print("índice invalido.")

    elif opcao == 5:
        print("A quatidade de produtos no estoque é:", len(produtos))
    
    elif opcao == 6:
        break

    else:
        print("Opção invalida.")

