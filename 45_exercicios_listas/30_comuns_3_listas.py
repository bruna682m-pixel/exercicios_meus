# %%

lista_a = [1, 5, 10, 20]
lista_b = [6, 7, 20, 80, 100]
lista_c = [3, 4, 15, 20, 30, 70, 80]

for i in lista_a:
    if i in lista_b and i in lista_c:
        print(f"O número igual nas 3 listas é: {i}")

# %%
lista_a = [1, 5, 10, 20]
lista_b = [6, 7, 20, 80, 100]
lista_c = [3, 4, 15, 20, 30, 70, 80]

numero_repetido = list(set(lista_a) & set(lista_b) & set(lista_c))

print(numero_repetido)
