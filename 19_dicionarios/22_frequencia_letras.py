# %%

letras = {}

palavra = input("Digite uma palavra:")

for i in palavra:
    if i not in letras:
        letras[i] = 1
    else:
        letras[i] += 1


print(letras) 