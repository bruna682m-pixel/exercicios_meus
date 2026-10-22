# %%

notas = {
    "Ana": 8.5,
    "Bruno": 5.0,
    "Caio": 7.0,
    "Duda": 9.5,
    "Eva": 4.0
}
aprovados = 0
reprovados = 0
abaixo_media = []
loop = 0
maior = 0
chave_maior = 0
soma =0
for chave, valor in notas.items():
    if valor >= 7:
        aprovados += 1
    else:
        reprovados += 1

    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave

    loop += 1

    soma = soma + valor

media = soma / len(notas)

for chave_media, valor_media in notas.items():
    if valor_media < media:
        abaixo_media.append(chave_media)

for chave_2, valor_2 in notas.items():
    for chave_comparada, valor_comparado in notas.items():
        if chave_2 != chave_comparada:
            if chave_2 < chave_comparada:
                if valor_2 == valor_comparado:
                    print(chave_2, "e", chave_comparada, "têm a mesma nota")

print(f"""
Notas: {notas}
Média: {media}
Aprovados: {aprovados}
Reprovados: {reprovados}
Maior: {maior}
Abaixo média da turma: {abaixo_media}
""")

