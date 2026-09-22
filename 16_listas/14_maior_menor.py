# %%
lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]
maior = 0
menor = 0
posicao_maior = 0
posicao_menor = 0

for i, enu in enumerate(lista):
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

print("Maior:",maior, "Posição:",posicao_maior)
print("Menor:",menor,"Posição:",posicao_menor)

