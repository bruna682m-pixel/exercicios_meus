# %%

lista = [12, 35, 8, 42, 19, 42, 7]
maior = 0
segundo_maior = 0
segundo_maior_indice = 0

for i, enu in enumerate(lista):
    if i == 0:
        maior = enu
        segundo_maior = enu
        segundo_maior_indice = i

    else:
        if enu > maior:
            segundo_maior = maior
            segundo_maior_indice = i
            maior = enu

print(segundo_maior)