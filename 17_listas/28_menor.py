# %%

numeros = [8, 3, 15, 6, 2]
menor = 0

for i, enu in enumerate(numeros):
    if i == 0:
        menor = enu
    else:
        if enu < menor:
            menor = enu

print(menor)