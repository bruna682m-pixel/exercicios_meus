# %%
lista = [12, 35, 1, 10, 34, 1, 35]
lista_nova = []
maior = 0
segundo_maior = 0
indice = 0

for i, enu in enumerate(lista):
    if enu not in lista_nova:
        lista_nova.append(enu)

    if i == 0:
        maior = enu
    else:
        if enu > maior:
            maior = enu
            indice = i

lista_nova.pop(indice)
segundo_maior = max(lista_nova)
            
print(f"O segundo maior valor é: {segundo_maior}")

# %%
lista = [12, 35, 1, 10, 34, 1, 35]
maior = 0
segundo_maior = 0

for i, enu in enumerate(lista):
    if i == 0:
        maior = enu
    elif i == 1:
        if enu > maior:
            segundo_maior = maior
            maior = enu
        else:
            segundo_maior = enu
    else:
        if enu > maior:
            segundo_maior = maior
            maior = enu

        if enu > segundo_maior and enu < maior:
            segundo_maior = enu

print(maior)
print(segundo_maior)

# %%

numeros = [10, 50, 20, 80, 30, 70, 75, 75]

maior = 0
segundo_maior = 0

for i, enu in enumerate(numeros):
    if i == 0:
        maior = enu
        segundo_maior = enu
    if enu > maior:
        maior = enu
    else:
        segundo_maior = enu

print(maior)
print("Segundo maior é:",segundo_maior)

# %%

numeros = [10, 50, 20, 80, 30, 70, 75, 75]

maior = 0
segundo_maior = 0

for i, enu in enumerate(numeros):
    if i == 0:
        maior = enu
    elif i == 1:
        if enu > maior:
            segundo_maior = maior
            maior = enu
        else:
            segundo_maior = enu
    else:
        if enu > maior:
            segundo_maior = maior
            maior = enu

        if enu > segundo_maior and enu < maior:
            segundo_maior = enu

print(maior)
print("Segundo maior é:",segundo_maior)

# %%
numeros = [10, 50, 20, 80, 30, 70, 75, 75]

maior = numeros[0]
segundo_maior = numeros[1]

if segundo_maior > maior:
    maior = numeros[1]
    segundo_maior = numeros[0]

for i in range(2, len(numeros)):
    numero = numeros[i]

    if numero > maior:
        segundo_maior = maior
        maior = numero

    elif numero > segundo_maior:
        segundo_maior = numero

print("Maior:", maior)
print("Segundo maior:", segundo_maior)







