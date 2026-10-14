# %%
lista = [120, 80, 200, 150, 50, 100]

acima_media = 0
media = 0
soma = 0
elementos = len(lista)

for i in lista:
    soma = soma + i

for j in lista:
    media = soma / elementos

    if j > media:
        acima_media += 1

print(acima_media)
print(media)





