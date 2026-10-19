# %%

tarefas = {}
opcao = 0

while True:
    opcao = int(input("Digite uma opção:"))

    if opcao == 1:
        nome_tarefa = input("Digite o nome da tarefa:")

        if nome_tarefa not in tarefas:
            tarefas[nome_tarefa] = "pendente"
        else:
            print("Tarefa já existe.")

    elif opcao == 2:
        consulta_tarefa = input("Digite o nome da tarefa para consultar:")

        if consulta_tarefa in tarefas:
            print(tarefas[consulta_tarefa])
        else:
            print("Tarefa não existe.")

    elif opcao == 3:
        concluido_tarefa = input("Digite o nome da tarefa para atualizar:")

        if concluido_tarefa in tarefas:
            tarefas[concluido_tarefa] = "concluida"
        else:
            print("Tarefa não existe.")

    elif opcao == 4:
        print(tarefas)

    elif opcao == 5:
        print("Saindo..")
        break

    else:
        print("Opção invalida.")
