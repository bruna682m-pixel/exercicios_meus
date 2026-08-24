# %%
saldo = 1000
qtd_depositos = 0
qtd_saques = 0
total_deposito = 0
total_saques = 0
historico = []
saque_max = 3


while True:
    opcao = int(input("""
1- Consultar saldo
2- depositar
3- sacar
4- hístórico de operações
5- estatísticas
6- sair
"""))

    if opcao == 1:
        print("Saldo:",saldo)

    elif opcao == 2:
        valor_deposito = float(input("Digite o valor do deposito:"))

        if valor_deposito <= 0:
            print("O valor do deposito deve ser maior que 0.")
        else:
            saldo = saldo + valor_deposito
            print("Depositou R$",valor_deposito,"reais.")
            print("Saldo: R$",saldo,"reais.")
            qtd_depositos += 1
            total_deposito = total_deposito + valor_deposito
            historico.append(f"Depósito: R$ {valor_deposito}")

    elif opcao == 3:
            if qtd_saques >= saque_max:
                print("Limite de saques.")
            else:
                valor_saque = float(input("Digite o valor do saque:"))

                if valor_saque > saldo:
                    print("Valor do saque maior que o saldo.")
                elif valor_saque <= 0:
                    print("o valor do saque deve ser maior que 0. ")
                else:
                    saldo = saldo - valor_saque
                    print("Saque de R$",valor_saque,"reais feito.")
                    print("Seu saldo é:",saldo)
                    qtd_saques += 1
                    total_saques = total_saques + valor_saque
                    historico.append(f"Saque R$: {valor_saque}")

    elif opcao == 4:
        for operacao in historico:
            print(operacao)

    elif opcao == 5:
        print(f"""
Quantidade de depósitos: {qtd_depositos}
Quantidade de saques: {qtd_saques}
Total debositado: {total_deposito}
Total sacado: {total_saques}
Saldo final: {saldo}

""")


    elif opcao == 6:
        print("saindo...")
        break
    

    
# %%
# %%
saldo = 1000
qtd_depositos = 0
saque_max = 3
qtd_saques = 0
total_deposito = 0
total_saques = 0


while True:
    opcao = int(input("""
1- Consultar saldo
2- depositar
3- sacar
4- hístórico de operações
5- estatísticas
6- sair
"""))

    if opcao == 1:
        print("Saldo:",saldo)

    elif opcao == 2:
        valor_deposito = float(input("Digite o valor do deposito:"))

        if valor_deposito <= 0:
            print("O valor do deposito deve ser maior que 0.")
        else:
            saldo = saldo + valor_deposito
            print("Depositou R$",valor_deposito,"reais.")
            print("Saldo: R$",saldo,"reais.")
            qtd_depositos += 1
            total_deposito = total_deposito + valor_deposito

    elif opcao == 3:

            valor_saque = float(input("Digite o valor do saque:"))

            if valor_saque > saldo:
                print("Valor do saque maior que o saldo.")
            elif valor_saque <= 0:
                print("o valor do saque deve ser maior que 0. ")
            else:
                saldo = saldo - valor_saque
                print("Saque de R$",valor_saque,"reais feito.")
                print("Seu saldo é:",saldo)
                qtd_saques += 1
                total_saques = total_saques + valor_saque

                if qtd_saques >= 3:
                    print("Limite de saques.")

    elif opcao == 4:
        print("a")

    elif opcao == 5:
        print(f"""
Quantidade de depósitos: {qtd_depositos}
Quantidade de saques: {qtd_saques}
Total debositado: {total_deposito}
Total sacado: {total_saques}
Saldo final: {saldo}

""")


    elif opcao == 6:
        print("saindo...")
        break
    

    
# %%
