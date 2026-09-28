# %%

lista1 = [10, 20, 30, 40]
lista2 = [10, 25, 30, 50]

for i, enu in enumerate(lista1):
    for j, enu2 in enumerate(lista2):
        if i == j:
            if enu ==  enu2:
                print("Posição:",i,"iguais.")
            elif enu != enu2:
                print("Posição:",i,"diferentes.")