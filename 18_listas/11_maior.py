# %%

numeros = [12, 35, 8, 42, 19, 42, 7]
maior = 0
indice_maior = 0

segundo_maior = 0
indice_segundo_maior = 0

for i, enu in enumerate(numeros):
    if i == 0:
        maior = enu
        indice_maior = i
    else:
        if enu > maior:
            segundo_maior = maior
            indice_segundo_maior = indice_maior

            maior = enu
            indice_maior = i

        if enu > segundo_maior and enu < maior:
            segundo_maior = enu
            indice_segundo_maior = i

print(maior)
print(indice_maior)

print(segundo_maior)
print(indice_segundo_maior)
