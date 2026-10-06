# %%

lista = [1, 2, 3, 2, 1]
lista_inversa = []
palindromo = True

lista_inversa = lista[::-1]

for i in lista:
    for j in lista_inversa:
        if i == j:
            palindromo = True
        else:
            palindromo = False

print(f"A lista é um palindromo: {palindromo}")
print(lista_inversa)
