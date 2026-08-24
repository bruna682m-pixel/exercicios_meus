
# %%
acertos = 0
erros = 0
pontuacao = 0
numero_max = 5

for i in range(1, numero_max+1):
    if i  == 1:
        resposta1 = int(input("""
Qual é a capital do Brasil?
1- São Paulo
2- Brasília
3- Rio de Janeiro
4- Salvador
"""))
        if resposta1 == 2:
                    acertos += 1
                    print("Acertou.")
                    pontuacao += 20
        else:
                    erros += 1
                    print("Errou.")

    elif i == 2:
        resposta2 = int(input("""
Qual a linguagem padrão usada em bancos de dados relacionais?
1- Oracle
2- Python
3- MySql
4- SQL
"""))
        if resposta2 == 4:
                    acertos += 1
                    print("Acertou.")
                    pontuacao += 20
        else:
                    erros += 1
                    print("Errou.")

    elif i == 3:
        resposta3 = int(input("""
Qual é o tipo de variavel de um texto?
1- String
2- Boleano
3- Int
4- Or
"""))
        if resposta3 == 1:
                    acertos += 1
                    print("Acertou.")
                    pontuacao += 20
        else:
                    erros += 1
                    print("Errou.")

    elif i == 4:
        resposta4 = int(input("""
Qual das cores é uma cor primaria?
1- Laranja
2- Azul
3- Roxo
4- Verde
"""))
        if resposta4 == 2:
                    acertos += 1
                    print("Acertou")
                    pontuacao += 20
        else:
                    erros += 1
                    print("Errou.")

    elif i == 5:
        resposta5 = int(input("""
O que faz o atalho Windows + shift + s?
1- Abre as configurações
2- Bloqueia o computador
3- Abre o cmd
4- Tira um print
"""))
        if resposta5 == 4:
                    acertos += 1
                    print("Acertou.")
                    pontuacao += 20
        else:
                    erros += 1
                    print("Errou.")
    
else:
    print(f"""
Resultado
Acertos: {acertos}
Erros: {erros}
Pontuação: {pontuacao} %
""")
