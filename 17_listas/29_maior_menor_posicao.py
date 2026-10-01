# %%

numeros = [8, 8, 15, 6, 2]
maior = 0
menor = 0
posicao_menor = 0
posicao_maior = 0

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

print("Número menor:", menor, "posição:",posicao_menor)
print("Número maior:",maior, "posição:",posicao_maior)
