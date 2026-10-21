# %%

temperaturas = {
    "Segunda": 23,
    "Terca": 28,
    "Quarta": 25,
    "Quinta": 19,
    "Sexta": 30
}

maior = 0
dia_maior = 0
menor = 0
dia_menor = 0
media = 0
soma = 0
acima_25 = 0
loop = 0

for chave, valor in temperaturas.items():
    if loop == 0:
        maior = valor
        dia_maior = chave

        menor = valor
        dia_menor = chave
    else:
        if valor > maior:
            maior = valor
            dia_maior = chave
        if valor < menor:
            menor = valor
            dia_menor = chave
    loop += 1

    soma = soma + valor

    if valor > 25:
        acima_25 += 1

media = soma / len(temperaturas)

print(f"""
Maior: {maior} {dia_maior}
Menor: {menor} {dia_menor}
Média: {media}
Temp acima de 25: {acima_25}
""")


