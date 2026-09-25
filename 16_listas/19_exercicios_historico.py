# %%
exercicios = []

while True:
    opcao = int(input("""Digite uma opção:
    1- Adicionar exercício
    2- Mostrar exercício
    3- Remover exercício
    4- Alterar exercício
    5- Procurar exercício
    6- Mostrar primeiro exercício
    7- Mostrar último exercício
    8- Quantidade de exercícios
    9- Sair
    """))

    if opcao == 1:
        add_exercicio = input("Digite o exercício para adicionar na lista:")

        exercicios.append(add_exercicio)

        print("Exercício adicionado a lista.")

    elif opcao == 2:
        print("Seu exercícios:",exercicios)

    elif opcao == 3:
        indice =  int(input("Digite o índice para remover:"))

        if exercicios == []:
            print("Lista vazia")
        elif indice >= 0 and indice <= len(exercicios) -1:
            exercicios.pop(indice)
            print("Exercício removido.")
        else:
            print("índice inválido.")

    elif opcao == 4:
        indice = int(input("Digite o índice para alterar:"))

        if exercicios == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(exercicios) -1:
            alterar_exercicio = input("Digite o novo exercício:")
            exercicios[indice] = alterar_exercicio
            print("Exercício alterado.")
        else:
            print("índice inválido.")

    elif opcao == 5:
        indice = int(input("Digite o índice para procurar:"))

        if exercicios == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(exercicios) -1:
            print("Exercício encontrado:",exercicios[indice])
        else:
            print("índice inválido.")

    elif opcao == 6:
        print("O primeiro exercício é:",exercicios[0])

    elif opcao == 7:
        print("O último exercício é:",exercicios[-1])

    elif opcao == 8:
        print("Quantidade de exercícios é",len(exercicios))

    elif opcao == 9:
        print("Saindo...")
        break

    else:
        print("Opção invalida.")
