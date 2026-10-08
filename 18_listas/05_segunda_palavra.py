palavras = ["PHP", "Exercises", "Backend", "Python", "Java"]

contador = 0
maior_contador = 0
maior_palavra = ""
segunda_maior = ""
segunda_maior_contador = 0

for i, palavra in enumerate(palavras):
    contador = 0

    for letra in palavra:
        contador += 1

    if i == 0:
        maior_contador = contador
        maior_palavra = palavra

    else:
        if contador > maior_contador:
            segunda_maior_contador = maior_contador
            segunda_maior = maior_palavra

            maior_contador = contador
            maior_palavra = palavra

        elif contador > segunda_maior_contador:
            segunda_maior_contador = contador
            segunda_maior = palavra

print("Maior palavra:", maior_palavra)
print("Segunda maior palavra:", segunda_maior)