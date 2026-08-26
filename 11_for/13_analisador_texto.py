# %%

qtd_caracteres = 0
qtd_espacos = 0
qtd_vogais = 0
qtd_numeros = 0
qtd_letras = 0
qtd_a = 0

frase = input("Digite uma frase:")

for i in frase:

    if i == "a":
        qtd_a +=1

    if i in "aeiou":
        qtd_vogais += 1

    if i == " ":
        qtd_espacos += 1

    if i.isdigit():
        qtd_numeros += 1

    if i.isalpha():
        qtd_letras += 1

qtd_caracteres = len(frase)

print(f"""
Qtd de caracteres: {qtd_caracteres}
Qtd de espaços: {qtd_espacos}
Qtd de vogais: {qtd_vogais}
Qtd de números: {qtd_numeros}
Qtd de letras: {qtd_letras}
Qtd de 'a': {qtd_a}

""")



# %%
