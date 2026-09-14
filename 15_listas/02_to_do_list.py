# %%

tarefas = []
tarefas_feitas = []
while True:
    opcao = int(input("""
===== Lista de tarefas =====

    Escolha uma opção
1- Adicionar tarefa
2- Mostrar tarefa
3- Concluir tarefa
4- Remover tarefa
5- Alterar tarefa
6- Quantidade de tarefas
7- Sair
"""))

    if opcao == 1:
        add_tarefa = input("Digite a terefa:")

        tarefas.append(add_tarefa)

        print(add_tarefa,"adicionado a to-do-list.")

    elif opcao == 2:
        print("To-do-List:")
        print(tarefas)

    elif opcao == 3:
        add_tarefa_feita = int(input("Digite o índice da tarefa para concluir:"))

        if tarefas == []:
            print("Sem tarefas para concluir.")
        else:
            if add_tarefa_feita >= 0 and add_tarefa_feita <= len(tarefas) -1:
                for i, enu in enumerate(tarefas):
                    if add_tarefa_feita == i:
                        tarefas_feitas.append(enu)
                        print("A tarefa",enu,"foi concluida.")
                        print(tarefas_feitas)

                        tarefas.pop(add_tarefa_feita)
            else:
                print("índice invalido.")

    elif opcao == 4:
        remover_tarefa = int(input("Digite o índice da tarefa para remover:"))

        if tarefas == []:
            print("Sem tarefas para remover.")
        else:
            if remover_tarefa >= 0 and remover_tarefa <= len(tarefas) -1:
                tarefas.pop(remover_tarefa)
                print("Tarefa",remover_tarefa,"foi removida.")
            else:
                print("índice invalido.")

    elif opcao == 5:
        alterar_tarefa = int(input("Digite o índice da tarefas para alterar:"))

        if tarefas == []:
            print("Sem tarefas para alterar.")
        else:
            if alterar_tarefa >= 0 and alterar_tarefa <= len(tarefas) -1:
                tarefas[alterar_tarefa] = tarefa_alterada = input("Digite a tarefa modificada:")
                print("Tarefa",alterar_tarefa,"foi alterada para", tarefa_alterada)
            else:
                print("índice invalido.")

    elif opcao == 6:
        print("A quantidade de tarefas é:",len(tarefas))

    elif opcao == 7:
        print("Saindo...")
        break

    else:
        print("Opção invalida")