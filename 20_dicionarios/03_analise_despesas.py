# %%
despesas = {
    "Aluguel": 850,
    "Mercado": 420,
    "Internet": 100,
    "Energia": 160,
    "Transporte": 120,
    "Lazer": 90
}

total = 0
media = 0
mais_cara = 0
menos_cara = 0
mais_cara_chave = 0
menos_cara_chave = 0
acima_media = []
menor_150 = []
loop = 0

for chave, valor in despesas.items():
    if loop == 0:
        mais_cara = valor
        mais_cara_chave = chave

        menos_cara = valor
        menos_cara_chave = chave
    else:
        if valor > mais_cara:
            mais_cara = valor
            mais_cara_chave = chave
        if valor < menos_cara:
            menos_cara = valor
            menos_cara_chave = chave

    loop +=1

    total = total + valor
media = total / len(despesas)

for chave, valor in despesas.items():
    if valor > media:
        acima_media.append(chave)

    if valor < 150:
        menor_150.append(chave)

print(f"""
Total depesas: {total}
Média: {media}
Mais cara: {mais_cara_chave} {mais_cara}
Menos cara: {menos_cara_chave} {menos_cara}
Acima média: {acima_media}
Abaixo de 150: {menor_150}
""")
