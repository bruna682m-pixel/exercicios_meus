# %%

palavras = ["sol", "computador", "livro", "mar", "python", "teclado", "ana"]
curtas = []
longas = []


for palavra in palavras:
    contador = 0
    for letras in palavra:
        contador += 1

    if palavra not in curtas:
        if contador < 5:
            curtas.append(palavra)

    if palavra not in longas:
        if contador > 5:
            longas.append(palavra)

print(curtas)
print(longas)