# %%
numero_max = 10

numero = int(input("Digite um número:"))

opcao = int(input("""
Digite uma opção:
1- soma
2- subtração
3- multiplicação
4- divisão
"""))

for i in range(1, numero_max+1):

    if opcao == 1:
        soma = i + numero
        print(i,"+",numero,"=",soma)
    elif opcao == 2:
        subtracao = i - numero
        print(i,"-",numero,"=",subtracao)
    elif opcao == 3:
        multiplicacao = i * numero
        print(i,"x",numero,"=",multiplicacao)
    elif opcao == 4:
        if numero == 0:
            print("Divisão por 0.")
        else:
            divisao = i / numero
            print(i,"/",numero,"=",divisao)
    else:
        print("invalido.")
        break


