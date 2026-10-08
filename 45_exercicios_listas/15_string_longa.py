# %%
# minha solução
palavras = ["PHP", "Exercises", "Backend", "Python"]
maior = 0
contador = 0
maior_palavra = 0

for i, palavra in enumerate(palavras):
    contador = 0
    for letra in palavra:
        contador += 1

    if i == 0:
        maior = contador
    else:
        if contador > maior:
            maior = contador
            maior_palavra = palavra

print(f"A maior palavra é: {maior_palavra}")



# %%
# Solução recomendada
palavras = ["PHP", "Exercises", "Backend", "Python"]

maior_palavra = max(palavras, key=len)

print(f"Maior palavra: {maior_palavra}")
        