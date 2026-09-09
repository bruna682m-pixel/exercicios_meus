# %%

numeros = [5, 8, 5, 2, 9, 5, 7, 5]
encontrado = False

numero_remover = int(input("Digite um número para procurar? "))

for i, enu in enumerate(numeros):
    if enu == numero_remover:
        encontrado = True
        print("Encontrado na posição",i)
