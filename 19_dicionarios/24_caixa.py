# %%

caixa = {
    "Venda de bolsa": 80,
    "Compra de materiais": -25,
    "Venda de porta-copos": 30,
    "Embalagens": -10
}
total_recebido = 0
total_gasto = 0
movimentacoes = 0
loop = 0
maior = 0
qtd_movimentacoes = 0

for chave, valor in caixa.items():
    if valor >= 0:
        total_recebido = total_recebido + valor
    else:
        total_gasto = total_gasto + valor

    if valor >= 0:
        if loop == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    loop += 1

    movimentacoes += valor
qtd_movimentacoes = len(caixa)

print(f"""
Total movimentações: {movimentacoes}
Total recebido: {total_recebido}
Total gasto: {total_gasto}
Maior: {maior}
Qtd movimentações: {qtd_movimentacoes}
""")
