# %%

pontos = {    
    "Lia": 150,    
    "Rafa": 200,    
    "Bia": 150,    
    "Gui": 90,    
    "Nina": 250
}

loop = 0
maior = 0
chave_maior = 0
soma = 0
pelo_menos_150 = 0
media = 0
menor_media = []
empate = []

for chave, valor in pontos.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave

    if valor >= 150:
        pelo_menos_150 += 1

    soma = soma + valor

    loop += 1

media = soma / len(pontos)

for chave_media, valor_media in pontos.items():
    if valor_media < media:
        menor_media.append(chave_media)

for chave_2, valor_2 in pontos.items():
    if valor_2 == maior:
        empate.append(chave_2)

if len(empate) > 1:
    print("Tem empate:", empate)
else:
    print("Sem empate.", empate[0], maior)

print(f"""
Maior pontuação: {chave_maior} {maior}
Pelos menos 150: {pelo_menos_150}
Soma: {soma}
Média: {media}
Abaixo média: {menor_media}
""")