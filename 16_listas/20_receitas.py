# %%

receitas = []
receitas_mais_feitas = []

while True:
    opcao = int(input("""Digite a opção:
    1- Adicionar receitas
    2- Mostrar receitas
    3- Remover receita
    4- Alterar receita
    5- Procurar receita
    6- Mostrar primeira receita
    7- Mostrar última receita
    8- Quantidade de receita
    9- Mostrar receitas invertida
    10- Marcas receitas mais feitas
    11- Sair
    """))

    if opcao == 1:
        add_receita = input("Digite a receita:")

        receitas.append(add_receita)

        print("Receita adicionada.")

    elif opcao == 2:
        print("Suas receitas são:",receitas)

    elif opcao == 3:
        indice = int(input("Digite o índice para remover:"))

        if receitas == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(receitas) -1:
            receitas.pop(indice)
            print("Receita removida.")
        else:
            print("índice inválido.")

    elif opcao == 4:
        indice = int(input("Digite o índice para alterar:"))

        if receitas == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(receitas) -1:
            alterar_receita = input("Digite a nova receita:")
            receitas[indice] = alterar_receita
        else:
            print("índice inválido.")

    elif opcao == 5:
        indice = int(input("Digite o índice para procurar:"))

        if receitas == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(receitas) -1:
            print("Receita encontrada:",receitas[indice])
        else:
            print("índice invalido.")

    elif opcao == 6:
        print("A primeira receita é:",receitas[0])

    elif opcao == 7:
        print("A última receita é:",receitas[-1])

    elif opcao == 8:
        print("Você tem",len(receitas),"receitas.")

    elif opcao == 9:
        invertida = []

        for i in range(len(receitas)-1, -1, -1):
            invertida.append(receitas[i])

        print("Mostrando receitas invertidas.",invertida)

    elif opcao == 10:
        indice = int(input("Digite o índice da receira para adicionar as mais feitas:"))

        if receitas == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(receitas) -1:
            receitas_mais_feitas.append(receitas[indice])
            print("Adicionado a lista de receitas mais feitas",receitas_mais_feitas)
        else:
            print("índice invalido.")

    elif opcao == 11:
        print("Saindo...")
        break

    else:
        print("opção invalida.")