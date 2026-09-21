# %%

numeros = [2, 5, 2, 8, 5, 2, 10]
repetidos = []

for i in numeros:
    for outro_i in numeros:
        if outro_i == i:
            repetidos.append(i)

print(repetidos)