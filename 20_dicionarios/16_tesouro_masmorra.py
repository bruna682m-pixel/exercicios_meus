# %%

tesouros = {
    "anel": 80,
    "gema": 250,
    "coroa": 500,
    "amuleto": 180,
    "moeda_antiga": 80
}
total = 0
mais_valioso = 0
chave_mais_valioso = 0
loop = 0
menor_200 = []
valor_igual = []

novo_tesouro = input("Digite novos tesouros achados:")

if novo_tesouro not in tesouros:
    valor_novo_tesouro = int(input("Digite o valor do novo tesouro."))
    tesouros[novo_tesouro] = valor_novo_tesouro
else:
    print("Este tesouro já foi encontrado.")

for chave, valor in tesouros.items():
    total = total + valor

    if loop == 0:
        mais_valioso = valor
        chave_mais_valioso = chave
    else:
        if valor > mais_valioso:
            mais_valioso = valor
            chave_mais_valioso = chave

    loop += 1

    if valor < 200:
     menor_200.append(chave)

for chave_repetido, valor_repetido in tesouros.items():
    for repetido_chave, repetido_valor in tesouros.items():
        if chave_repetido != repetido_chave and valor_repetido == repetido_valor:
            if chave_repetido not in valor_igual:
                valor_igual.append(chave_repetido)

if len(valor_igual) >= 2:
    print(f"Tem valores iguais. {valor_igual}")
else:
    print(f"Sem valores iguais. {chave_mais_valioso} {mais_valioso}")
    

print(f"""
Tesouros: {tesouros}
Soma tesouros: {total}
Tesouro inferior a 200: {menor_200}
""")