# %%


nome = ""
idade = 0
telefone = 0
cidade = ""

while True:
    opcao = int(input("""
1- Cadastrar
2- Consultar
3- Alterar
4- Excluir
5- Sair
"""))

    if opcao == 1:
        print("Digite seus dados:")
        nome = input("Digite seu nome:")
        idade = int(input("Digite sua idade:"))
        telefone = input("Digite seu telefone:")
        cidade = input("Digite sua cidade:")

        print(f"""
Cadastro feito:
Nome:{nome}
Idade:{idade}
Telefone:{telefone}
Cidade:{cidade}
""")

    elif opcao == 2:
        print(f"""
Cadastro atual:
Nome:{nome}
Idade:{idade}
Telefone:{telefone}
Cidade:{cidade}
""")

    elif opcao == 3:
        print("Digite seus novos dados:")
        nome = input("Digite seu nome:")
        idade = int(input("Digite sua idade:"))
        telefone = input("Digite seu telefone:")
        cidade = input("Digite sua cidade:")
        
        print(f"""
Atualização de cadastro feita:
Nome:{nome}
Idade:{idade}
Telefone:{telefone}
Cidade:{cidade}
""")

    elif opcao == 4:
        opcao_excluir = int(input("Você que mesmo excluir? 1- sim 2- não"))

        if opcao_excluir == 1:
            print("Excluindo seus dados.")  
            nome = ""
            idade = 0
            telefone = 0
            cidade = ""
        else:
            print("Operação cancelada.")

    elif opcao == 5:
        print("Saindo...")
        break
