# %%
contas = {
    "Ana": 200,
    "Bianca": 300,
    "Carlos": 50,
}

nome = input("Digite seu nome:")

if nome in contas:
    saque = int(input("Digite o valor do saque:"))

    if saque > 0 and saque <= contas[nome]:
        contas[nome] -= saque
        print("Saque realizado. Valor restante:", contas[nome])
    else:
        print("Valor de saque inválido")
else:
    print("Opção inválida.")
