# %%

clientes = []
pedidos = []
status = []
indice = 0

while True:
    opcao = int(input("""Digite a opção:
    1- Cadastrar pedido
    2- Mostrar pedido
    3- Procurar pedido
    4- Remover pedido
    5- Alterar pedido
    6- Quantidade de pedidos
    7- Sair
    """))

    if opcao == 1:
        add_pedido = int(input("Digite o número do pedido:"))
        add_cliente = input("Digite o nome do cliente:")
        add_status = input("Digite o status do pedido:")

        pedidos.append(add_pedido)
        clientes.append(add_cliente)
        status.append(add_status)

        print("O pedido foi adicionado.")
        print("O cliente foi adicionado.")
        print("O status foi adicionado.")

    elif opcao == 2:
        print("Pedidos:", pedidos)
        print("Clientes:",clientes)
        print("Status:",status)

    elif opcao == 3:
        indice = int(input("Digite o índice para procurar:"))

        if pedidos == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(pedidos) -1:
            print("Pedido encontrado", pedidos[indice], clientes[indice], status[indice]) 
            
        else:
            print("índice invalido.")

    elif opcao == 4:
        indice = int(input("Digite o índice para remover:"))

        if pedidos == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(pedidos) -1:
            pedidos.pop(indice)
            clientes.pop(indice)
            status.pop(indice)
            print("Pedido removido.")
        else:
            print("índice invalido.")

    elif opcao == 5:
        indice = int(input("Digite o índice para alterar:"))

        if pedidos == []:
            print("Lista vazia.")
        elif indice >= 0 and indice <= len(pedidos) -1:
            pedidos[indice] = alterar_pedido = int(input("Digite o número do pedido:"))
            clientes[indice] = alterar_cliente = input("Digite o nome do cliente:")
            status[indice] = alterar_status = input("Digite o status do pedido:")
            print("Dados alterados.")
        else:
            print("índice invalido.")

    elif opcao == 6:
        print("Quantidade de pedidos:")
        print(len(pedidos))

    elif opcao == 7:
        print("Saindo......")
        break

    else:
        print("Opção invalida.")