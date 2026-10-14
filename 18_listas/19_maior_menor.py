# %%

lista = [17, 4, 29, 11, 29, 2]
maior = 0
menor = 0
indice_maior = 0
indice_menor = 0

for i, enu in enumerate(lista):
    if i == 0:
        maior = enu
        indice_maior = i

        menor = enu
        indice_menor = i
    else:
        if enu > maior:
            maior = enu
            indice_maior = i

        if enu < menor:
            menor = enu
            indice_menor = i

print(maior , indice_maior)
print(menor,  indice_menor)
