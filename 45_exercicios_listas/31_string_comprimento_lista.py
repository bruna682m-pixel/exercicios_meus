# %%

lista = ["apple", "pie", "banana", "kiwi", "pear"]
caracteres = 0
lista_filtrada = []

for i, palavra in enumerate(lista):
    caracteres = 0
    for letra in palavra:
        caracteres += 1

    if caracteres >= 5:
        lista_filtrada.append(palavra)


print(f"Lista filtrada: {lista_filtrada}")

# %%

lista = ["apple", "pie", "banana", "kiwi", "pear"]

lista_filtrada = [palavra for palavra in lista  if len(palavra) >= 5]

print(f"Lista filtrada: {lista_filtrada}")
