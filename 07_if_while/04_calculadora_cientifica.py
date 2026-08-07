# %%
numero_atual = numero1
opcao = int(input("""

1- Soma
2- Subtração
3- Multiplicação
4- Divisão
5- Fatorial
6- Primo
7- Decimal = Binário
8- Bhaskara
9- Triângulo
10- Ordernar 3 números
11- Tipo de triângulo
12- Conversão de segundos
13- Sair

"""))


while opcao <= 12:
    opcao = int(input("Digite uma opção"))

    if opcao == 1:
        numero1 = float(input("Digite um número para somar:"))
        numero2 = float(input("Digite outro número para somar:"))

        total = numero1 + numero2

        print("Sua soma deu:",total)

    elif opcao == 2:
        numero1 = float(input("Digite um número para subtrair:"))
        numero2 = float(input("Digite outro número para subtrair:"))

        total = numero1 - numero2

        print("Sua subtração deu:",total)

    elif opcao == 3:
        numero1 = float(input("Digite um número para multiplicar:"))
        numero2 = float(input("Digite outro número para multiplicar:"))

        total = numero1 * numero2

        print("Sua multiplicação deu:",total)

    elif opcao == 4:
        numero1 = float(input("Digite um número para dividir:"))
        numero2 = float(input("Digite outro número para dividir:"))

        total = numero1 / numero2

        print("Sua divisão deu:",total)

    elif opcao == 5:
        numero1 = int(input("Digite um número para calcular o fatorial:"))
        total = 1
        numero_atual = numero1
    if numero1 > 0:
        while numero1 >= 1:
            total = total * numero1
            numero1 -= 1
    elif numero1 == 0:
        print("O fatorial de",numero_atual,"é igual a 1")
    else:
        print("O número deve ser positivo")

    print("O fatorial de",numero_atual,"é igual a",total)

print("sai")

# %%
