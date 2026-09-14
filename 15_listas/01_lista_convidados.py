# %%

convidados = []
volta = 0

while True:
    opcao = int(input("""
1- Adicionar convidado
2- Mostrar convidados
3- Remover convidados
4- Alterar convidado
5- Procurar convidado
6- Mostrar quantidade
7- Sair
"""))

    if opcao == 1:
        if volta == 0:
            add_convidado = input("Digite o nome do convidado:")
            convidados.append(add_convidado)
        else:
            add_convidado = input("Digite o nome do convidado:")
            for i, enu in enumerate(convidados):
                if enu == add_convidado:
                    print("Convidado já cadastrado.")
                if enu != add_convidado: 
                    convidados.append(add_convidado)
                    print(add_convidado, "foi adicionado a lista de convidados.")

        volta += 1
            
    elif opcao == 2:

        print("Os convidados são:",convidados)

    elif opcao == 3:
        remover = int(input("Digite o índice do convidado para excluir:"))

        if convidados == []:
            print("Lista está vazia.")
        else:
            if remover >= 0 and remover <= len(convidados) -1:
                convidados.pop(remover)
                print("Convidado",remover, "removido.")
            else:
                print("índice invalido.")

    elif opcao == 4:
        alterar = int(input("Digite o índice do convidado para alterar:"))

        if convidados == []:
            print("Lista está vazia.")
        else:
            if alterar >= 0 and alterar <= len(convidados) -1:
                convidados[alterar] = alteracao_convidado = input("Digite o convidado alterado:")
                print("Convidado", alterar, "alterado.")

    elif opcao == 5:
        procurando = input("Digite o nome do convidado:")

        for i, enu in enumerate(convidados):
            if enu == procurando:
                print("O convidado",enu,"foi encontrado no ídice:",i)
            else:
                print("Convidado não encontrado.")

        add_convidado = input("Digite o nome do convidado:")

        for i, enu in enumerate(convidados):
            if enu == add_convidado:
                print("Convidado já cadastrado.")
            else:
                convidados.append(add_convidado)
                print(add_convidado, "foi adicionado a lista de convidados.")

    elif opcao == 6:
        print("A quantidade de convidados é:", len(convidados))

    elif opcao == 7:
        print("Saindo....")
        break

    else:
        print("Opção invalida.")