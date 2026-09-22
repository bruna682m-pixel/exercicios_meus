# %%
tarefas = []
indice = 0

while True:
    add_tarefa = input("Digite a tarefa ou fim para encerrar:")

    if add_tarefa == "fim":
        print("Saindo....")
        break
    else:
        tarefas.append(add_tarefa)

    for i, enu in enumerate(tarefas):
        indice = i + 1

    print("Tarefas cadastradas:")
    print(indice,"-", tarefas)