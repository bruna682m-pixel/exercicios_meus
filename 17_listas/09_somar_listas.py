# %%

lista1 = [10, 20, 30, 40]
lista2 = [1, 2, 3, 4]
soma = 0
resultado = []

for i, enu in enumerate(lista1):
    for j, enu2 in enumerate(lista2):
        if i == j:
            soma = enu + enu2
            resultado.append(soma)

print(resultado)



