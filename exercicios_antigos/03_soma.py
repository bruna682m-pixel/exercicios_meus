# Mostrar os pares entre 10 e 100 e a somatória dos pares, (após mostrar os pares, mostrar
#a somatória)

# %%
count = 0
total = 0

while count <= 100:
    if count % 2 == 0:
        print("Estamos no número:",count)

    count += 1
    total = total + count

print("a soma dos pares é:", total)
# %%
