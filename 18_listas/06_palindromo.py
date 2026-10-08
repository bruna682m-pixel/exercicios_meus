# %%
lista = [1, 2, 3, 2, 1]
lista_inversa = lista[::-1]
palindromo = True


for i, enu in enumerate(lista):
    if lista[i] != lista_inversa[i]:
        palindromo = False
        break

print(palindromo)


