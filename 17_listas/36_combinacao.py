# %%

numeros = [10, 50, 20, 80, 30, 70]
maior = 0
menor = 0
segundo_maior = 0
posicao_maior = 0
posicao_menor = 0

for i, enu in enumerate(numeros):
    if i == 0:
        maior = enu
        menor = enu
        segundo_maior = enu
    else:
        if enu > maior:
            segundo_maior = maior
            maior = enu
            posicao_maior = i
        elif enu > segundo_maior:
            segundo_maior = enu

        if enu < menor:
            menor = enu
            posicao_menor = i

print(f"""
Maior = {maior}
Menor = {menor}
Posição do maior = {posicao_maior}
Posição do menor = {posicao_menor}
Segundo maior = {segundo_maior}

""")
