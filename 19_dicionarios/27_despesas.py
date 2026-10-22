# %%
despesas = {
    "Mercado": 120.50,
    "Transporte": 45.00,
    "Internet": 99.90,
    "Lanche": 25.00,
    "Farmacia": 60.00
}

soma = 0
media = 0
maior = 0
acima_50 = 0
ate_50 = []
acima_100 = []
loop = 0
chave_maior = 0
sobra = 0

for chave, valor in despesas.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave
    loop += 1

    if valor > 50:
        acima_50 += 1

    if valor > 100:
        acima_100.append(chave)
   
    if valor <= 50:
        ate_50.append(chave)

    soma = soma + valor
media = soma / len(despesas)
sobra = 500 - soma

print(f"""
Soma: {soma}
Maior: {chave_maior} {maior}
Acima de 50: {acima_50}
Média: {media}
Até 50: {ate_50}
Acima 100: {acima_100}
Sobra: {sobra}
""")
