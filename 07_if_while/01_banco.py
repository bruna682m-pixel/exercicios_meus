# %%
print("""
Banco Python

1- Consultar saldo
2- Depositar
3- Sacar
4- Sair

""")
opcao = 0
saldo = 1000
qtd_saque = 0
total_deposito = 0
total_saque = 0


while opcao <= 3:
    opcao= int(input("Digite a opção voce quer fazer:"))

    if opcao == 1:
        print("Seu saldo atual é: R$",saldo)
        print("Voce fez",qtd_saque,"saques.")
        print("Voce sacou R$",total_saque,"reais.")
        print("Voce depósitou R$",total_deposito,"reais")

    if opcao == 2:
        deposito = float(input("Digite o valor do depósito"))

        if deposito < 0:
            print("Depósito não pode ser negativo.")
        elif deposito == 0:
            print("Depósito igual a zero não é permitido.")
        else: 
            saldo = saldo + deposito
            print("Depósito realizado. Seu saldo atual é: R$",saldo)
            total_deposito = total_deposito + deposito


    if opcao == 3:
        saque = float(input("Digite o valor do saque:"))

        if qtd_saque > 2  :
                    print("Máximo de 3 saques por dia.")
                    break

        if saque > saldo:
            print("Voce não tem saldo suficiente.")
        elif saque < 0:
            print("Saque não pode ser negativo.")
        elif saque == 0:
            print("Saque igual a 0 não é permitido")
        else:
            saldo = saldo - saque
            print("Voce sacou",saque, "Agora seu saldo é R$",saldo)
            total_saque = total_saque + saque
            qtd_saque += 1

        
            


