# %%
saldo = 1000
operacao = 0
total = 0

while True:
    operacao = input("""
        1- Depositar
        2- Sacar
        3- Consultar saldo
        4- sair
""")
    operacao = int(operacao)

    if operacao == 1:
        total = input("Quanto voce quer depositar?")
        total = float(total)
        saldo = saldo + total
        print("Deposito realizado com sucesso. Seu saldo é:",saldo)
    elif operacao == 2:
        total = input("Quanto voce quer sacar?")
        total = float(total)
        saldo = saldo - total
        print("Saque realizado com sucesso. Seu saldo é:",saldo)
    elif operacao == 3:
        print("Seu saldo é de:",saldo)
    else:
        break


print("Seu saldo é:",saldo)
# %%
saldo = 1000
operacao = 0
total = 0

while True:
    operacao = input("""
        1- Depositar
        2- Sacar
        3- Consultar saldo
        4- sair
""")
    operacao = int(operacao)

    if operacao == 1:
        total = input("Quanto voce quer depositar?")
        total = float(total)
        saldo = saldo + total
        print("Deposito realizado com sucesso. Seu saldo é:",saldo)
    elif operacao == 2:
        total = input("Quanto voce quer sacar?")
        total = float(total)
        print(saldo)
        print(total)
        if total > saldo:
            print("Voce não tem saldo suficiente para sacar.")
        else:
            saldo = saldo - total
            print("Saque realizado com sucesso. Seu saldo é:",saldo)
    elif operacao == 3:
        print("Seu saldo é de:",saldo)
    else:
        break
    

# %%
