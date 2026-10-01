# %%
numeros = [10, 50, 20, 80, 30, 70]
maior = 0
segundo_maior = 0

for i, enu in enumerate(numeros):
    if i == 0:
        maior = enu
        segundo_maior = enu
    else:
        if enu > maior:
            segundo_maior = maior
            maior = enu
        elif enu > segundo_maior:
            segundo_maior = enu
    

print(maior)
print(segundo_maior)
