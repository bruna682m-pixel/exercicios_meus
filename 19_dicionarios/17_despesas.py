# %%

despesas = {}
opcao = 0
soma = 0
maior = 0
chave_maior = 0

while True:
    opcao = int(input("Digite uma opção:"))

    if opcao == 1:
        cadastro = input("Digite uma despesa:")

        if cadastro not in despesas:
            preco = float(input("Digite o preço da despesa:"))
            if preco > 0:
                despesas[cadastro] = preco
            else:
                print("Preço negativo.")
        else:
            print("Despesa já existe.")

    elif opcao == 2:
        consulta = input("Digite uma despesa para consultar:")

        if consulta in despesas:
            print(despesas[consulta])
        else:
            print("Despesa não existe.")

    elif opcao ==  3:
        atualizar = input("Digite uma despesa para atualizar:")

        if atualizar in despesas:
            preco = float(input("Digite o preço para atualizar:"))

            if preco > 0:
                despesas[atualizar] = preco
            else:
                print("Preço negativo.")
        else:
            print("Despesa não existe.")

    elif opcao == 4:
        soma = 0
        for chave, valor in despesas.items():
            soma += valor

        print(soma)

    elif opcao == 5:
        if not despesas:
            print("Dicionário vazio.")
        else:
            loop = 0
            for chave, valor in despesas.items():
                if loop == 0:
                    maior = valor
                    chave_maior = chave
                else:
                    if valor > maior:
                        maior = valor
                        chave_maior = chave

                loop += 1

            print(chave_maior, maior)

    elif opcao == 6:
        print("Saindo....")
        break

    else:
        print("Opção invalida.")