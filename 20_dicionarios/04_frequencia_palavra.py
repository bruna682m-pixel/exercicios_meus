# %%

frase = "gato cachorro gato peixe cachorro gato "
palavra_atual = ""
frequencia = {}
loop = 0
maior = 0
empate = 0
chave_maior = 0
apenas_1_vez = []
empate = []
qtd_palavra = 0

for i in frase:
    if i != " ":
        palavra_atual += i
    else:
        if palavra_atual:
            if palavra_atual not in frequencia:
                frequencia[palavra_atual] = 1
            else:
                frequencia[palavra_atual] += 1

        palavra_atual = ""

for chave, valor in frequencia.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave
    loop += 1

    if valor == 1:
        apenas_1_vez.append(chave)

for chave_empate, valor_empate in frequencia.items():
    if maior == valor_empate:
        empate.append(chave_empate)
    
qtd_palavra = len(frequencia)


print(f"""
Frequências: {frequencia}
Maior: {chave_maior} {maior}
Apenas 1 vez: {apenas_1_vez}
Empate: {empate}
Qtd de palavras: {qtd_palavra}
""")

               