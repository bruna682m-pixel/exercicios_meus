# %%

palavras = {}

frase = input("Digite uma frase:")

palavra_atual = ""

for letras in frase:
    if letras != " ":
        palavra_atual += letras
    else:
        if palavra_atual:
            if palavra_atual not in palavras:
                palavras[palavra_atual] = 1
            else:
                palavras[palavra_atual] += 1

        palavra_atual = ""

if palavra_atual:
    print(palavra_atual)

print(palavras)

# %%
palavras = {}

frase = input("Digite uma frase:")

for palavra in frase.split():
    if palavra not in palavras:
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1

print(palavras)


