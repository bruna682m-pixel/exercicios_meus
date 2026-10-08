# %%
lista = [5, 6, 7, 10, 11, 20, 21, 22, 23]
sequencia = 1
maior_sequencia = 1
ultimo = len(lista) -1

for i, enu in enumerate(lista):
    if i < ultimo:
        if enu + 1 == lista[i + 1]:
            sequencia += 1
        else:
            sequencia = 1

        if sequencia > maior_sequencia:
            maior_sequencia = sequencia

print(maior_sequencia)
