# %%

nomes = ["Ana", "Bianca", "Carlos", "Daniel"]
notas = [8, 5, 10, 6]

for i, enu in enumerate(notas):
    for j, enu2 in enumerate(nomes):
        if i == j:
            if enu >= 7:
                print(enu2, "-", enu)