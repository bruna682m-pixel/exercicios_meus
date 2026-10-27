# %%

vendas = {
    "Caderno": 12,
    "Caneta": 30,
    "Mochila": 5,
    "Borracha": 18,
    "Estojo": 8
}

qtd_total = 0
pelo_menos_10 = []
maior_10 = []
loop = 0
maior = 0
chave_maior = 0
pelo_menos_10_qtd = 0

for chave, valor in vendas.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave

    if valor >= 10:
        maior_10.append(chave)
    else:
        pelo_menos_10.append(chave)

    qtd_total = qtd_total + valor
pelo_menos_10_qtd = len(pelo_menos_10)

print(f"""
Qtd total: {qtd_total}
Pelo menos 10: {pelo_menos_10_qtd}
Mais de 10: {maior_10}
Maior venda: {chave_maior} {maior}
""")
