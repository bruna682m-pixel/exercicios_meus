# %%

numeros = []
maior = 0
menor = 0
posicao_maior = 0
posicao_menor = 0
loop = 1

while loop <= 5:
    entrada_numero = int(input("Digite 5 números:"))

    numeros.append(entrada_numero)

    for i, enu in enumerate(numeros):
        if i == 0:
            maior = enu
            menor = enu
        else:
            if enu > maior:
                maior = enu
                posicao_maior = i
            if enu < menor:
                menor = enu
                posicao_menor = i

    loop += 1

maior_max = max(numeros)
menor_min =  min(numeros)
posicao_maior 

print(f"""
Maior: {maior}
Menor: {menor}
Maior Max: {maior_max}
Menor Min: {menor_min}
Posição maior: {posicao_maior}
Posição menor: {posicao_menor}
""")
