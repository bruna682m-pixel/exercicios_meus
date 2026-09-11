# %%
lista_frase =[]
qtd_espacos = 0
qtd_letras = 0
qtd_numeros = 0

frase = input("Digite uma frase:")


for i in frase:
    lista_frase.append(i)

    if i == " ":
        qtd_espacos += 1

    if i.isalpha():
        qtd_letras += 1

    if i.isdigit():
        qtd_numeros += 1

ultima_posicao = (lista_frase[-1])
primeira_posicao = (lista_frase[0])
qtd_caracteres = len(lista_frase)


print(f"""
Quantidade de caracteres: {qtd_caracteres}
Quantidade de espaços: {qtd_espacos}
Quantidade de números: {qtd_numeros}
Quantidade de letra: {qtd_letras}
primeira posição: {primeira_posicao}
última posição: {ultima_posicao}
""")
