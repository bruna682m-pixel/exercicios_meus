# %%

palavra = "programacao"

letras = {}

loop = 0
maior = 0
chave_maior = 0
maior_3 = False
apenas_1_vez = []
empate = []

for letra in palavra:
    if letra not in letras:
        letras[letra] = 1
    else:
        letras[letra] += 1

for chave, valor in letras.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave

    if valor >= 3:
        maior_3 = True

    if valor == 1:
        apenas_1_vez.append(chave)

    loop += 1

for chave_2, valor_2 in letras.items():
    if valor_2 == maior:
        empate.append(chave_2)

qtd_letras = len(letras)   

print(f"""
Qtd letras: {letras}
Letras que mais aparece: {maior} {chave_maior}
Letras diferentes: {qtd_letras}
Letras que aparecem 1 vez: {apenas_1_vez}
3 vezes ou mais: {maior_3}
Empate maior frequencia: {empate}
""")


