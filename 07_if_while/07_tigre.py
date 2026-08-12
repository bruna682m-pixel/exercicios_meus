# %%
import random

saldo = 100
vezes = 0

while True:
    opcao = int(input("""
1- Apostar
2- Consultar saldo
3- Sair
"""))
    if opcao == 1:
        if saldo <= 0: 
                    print("Sem saldo.")
                    break

        numero = int(input("Escolha um número entre 1 e 6"))
        numero_pc = random.randint(1,6)

        if numero == numero_pc:
            saldo = saldo * 2
            print("Você ganhou a aposta. Seu saldo agora é o dobro.",saldo)
        else:
            saldo = saldo - 10
            print("Você perdeu a aposta. Seu saldo é:",saldo)

        vezes += 1

    elif opcao == 2:
        print("""
Status
Saldo:""",saldo,"""
Vezes jogadas:""",vezes)

    elif opcao == 3:
        print("Saindo...")
        break

    




