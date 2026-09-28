# %%

lista1 = [10, 50, 20, 80]
lista2 = [30, 40, 70, 60]
maior_posicao = []


for i, enu in enumerate(lista1):
    for j, enu2 in enumerate(lista2):
        if i == j:
            if enu > enu2:
                maior_posicao.append(enu)
            elif enu2 > enu:
                maior_posicao.append(enu2)


print(maior_posicao)
