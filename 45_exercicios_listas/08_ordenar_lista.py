# %%

nao_ordenada = [56, 12, 86, 3, 22]
ordenada = []

nao_ordenada.sort() 
ordenada = sorted(nao_ordenada)

print(ordenada)
print(nao_ordenada)

# %%
nao_ordenada = [56, 12, 86, 3, 22]
ordenada = []
menor = 0

for i, enu in enumerate(nao_ordenada):
    if enu not in ordenada:
        if i == 0:
            menor = enu
        else:
            if enu < menor:
                menor = enu
            else:
                if enu not in ordenada:
                    ordenada.append(enu)
print(menor)
print(ordenada)
