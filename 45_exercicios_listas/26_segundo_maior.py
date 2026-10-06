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


