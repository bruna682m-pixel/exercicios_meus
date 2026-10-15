# %%
nova_qtd = 0
estoque = {
    "Meias": 10,
    "Balas": 300,
    "Lapis": 2,
    "Monitor": 30
}

nome = input("Digite o nome do produto:")

if nome in estoque:
    print(estoque[nome])

    opcao = input("Deseja informar a qtd do produto?")

    if opcao == "sim":
        nova_qtd = int(input("Digite a nova qtd:"))
        if nova_qtd < 0:
            print("Digite uma qtd valida.")
        else:
            estoque[nome] = nova_qtd
    elif opcao == "não":
        print("Tudo igual.")
    else:
        print("Opção invalida.")
else: 
    print("Não temos esse.")

print(estoque)