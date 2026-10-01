# %%

numeros = [1, 2, 3, 8, 9, 10, 4, 5]
sequencia_atual = 1
maior_sequencia = 1
ultimo = len(numeros) -1

for i, enu in enumerate(numeros):
    if i < ultimo:
        if enu + 1 == numeros[i + 1]:
            sequencia_atual += 1
        else:
            sequencia_atual = 1

        if sequencia_atual > maior_sequencia:
            maior_sequencia = sequencia_atual

print(maior_sequencia)


