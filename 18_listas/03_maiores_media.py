# %%
lista = [10, 20, 30, 40, 50]
soma = 0
media = 0
contador = 0

soma = sum(lista)
media = soma / len(lista)

print(media)
print(soma)

for i in lista:
    if i > media:
        contador += 1

print(contador)
