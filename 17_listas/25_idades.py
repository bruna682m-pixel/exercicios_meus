# %%

idades = [5, 12, 18, 25, 67, 10, 35, 70]
criancas = []
adultos = []
idosos = []

for i in idades:
    if i < 18:
        criancas.append(i)
    elif i >= 18 and i <= 59:
        adultos.append(i)
    else:
        idosos.append(i)

print(criancas)
print(adultos)
print(idosos)