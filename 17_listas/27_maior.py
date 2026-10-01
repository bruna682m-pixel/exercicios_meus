# %%

numeros = [8, 8, 15, 6, 2]
maior = 0

for i, enu in enumerate(numeros):
    if i == 0:
        maior = enu
    else:
        if enu > maior:
            maior = enu

print(maior)

