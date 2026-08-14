# %%

saldo = 1000 # saldo = 1000
saques = 0 # variavel p_ contar saques

while True: # loop infinito atá o break

# pedindo a opção
    opcao = int(input(""" 
Banco Python

1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Sair

Escolha:
"""))

    if opcao == 1: # se a opção == 1 faz a consulta do saldo
        print("Saldo:", saldo)

    elif opcao == 2: # se a opção for 2 faz a operação de depósito
        deposito = float(input("Valor do depósito: ")) # pedindo valor depósito

        if deposito > 0: # ver se depósito é maior que 0 ai sim ele deposita
            saldo = saldo + deposito
        else:
            print("Valor inválido.") # se não valor invalido

    elif opcao == 3: # se opção for 3 faz a operação de saque

        saque = float(input("Valor do saque: ")) # pedindo valor do saque

        if saques >= 3: # se o total de saque for 3 dá limite atingido antes permitia + que 3
            print("Limite de saques atingido.")

        elif saque > saldo: # se o saque for maior que saldo diz que não é suficiente
            print("Saldo insuficiente.")

        elif saque <= 0: # não permite saque negativo e 0
            print("Valor inválido.")

        else: # se as de cima forem falso deixa fazer o saque, fazendo o calculo, somando a qtd de saque e mostrando
            saldo = saldo - saque
            saques += 1
            print("Saque realizado.")

    elif opcao == 4: # se opção for 4 encerra o programa
        print("Saindo...")
        break

    else: # se opção for diferente de 1 a 4 da opção invalida
        print("Opção inválida.")

# permitia + que 3 saques
# mesmo se o saque posse invalida mostrava saque realizado
# reformulei o if colocando tudo em um único if e colocando elif