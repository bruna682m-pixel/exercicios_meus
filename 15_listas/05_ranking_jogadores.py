# %%

jogadores = []
pontuacoes = []

primeiro = segundo = terceiro = quarto = float('-inf')
nome_1 = nome_2 = nome_3 = nome_4 = "Ninguem"

while True:
    jogador = input("Digite seu nome:")
    pontuacao = input("Digite sua pontuação")

    if jogador == "" and pontuacao == "":
        print("saindo...")
        break
    else:
        pontuacao = int(pontuacao)
        jogadores.append(jogador)
        pontuacoes.append(pontuacao)

for i in range(len(pontuacoes)):
    num = pontuacoes[i]
    nome =  jogadores[i]
    
    if num > primeiro:
        quarto = terceiro
        nome_4 = nome_3

        terceiro = segundo
        nome_3 = nome_2

        segundo = primeiro
        nome_2 = nome_1

        primeiro = num
        nome_1 = jogador
    elif num > segundo:
        quarto = terceiro
        nome_4 = nome_3

        terceiro = segundo
        nome_3 = nome_2

        segundo = num
        nome_2 = jogador
    elif num > terceiro:
        quarto = terceiro
        nome_4 = nome_3

        terceiro = num
        nome_3 = jogador
    elif num > quarto:
        quarto = num
        nome_4 = jogador

     
print(nome_1,"-",primeiro)
print(nome_2,"-",segundo)
print(nome_3,"-",terceiro)
print(nome_4,"-",quarto)

# %%



