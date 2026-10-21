# %%
mochila = {
    "Lapis": 3,
    "Caneta": 2,
    "Caderno": 1,
    "Borracha": 0
}

qtd_soma = 0
esgotados = []
tipos_soma = 0
maior = 0
pelo_menos_2 = []
loop = 0
chave_maior = 0

for chave, valor in mochila.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave

    loop += 1

    if valor >= 2:
        pelo_menos_2.append(chave)

    tipos_soma = len(mochila)
    qtd_soma = qtd_soma + valor

    if valor == 0:
        esgotados.append(chave)

print(f"""
Maior: {maior} {chave_maior}
Soma tipos de objeto: {tipos_soma}
Soma total: {qtd_soma}
Pelo menos 2: {pelo_menos_2}
Esgotados: {esgotados}
""")
