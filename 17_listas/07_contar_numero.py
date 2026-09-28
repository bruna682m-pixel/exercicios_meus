# %%

numeros = [4, 7, 4, 2, 4, 9, 7, 1]
encontrado = 0

opcao = int(input("Digite um número:"))

for i in numeros:
    if i == opcao:
        encontrado += 1

print("Seu número foi encontrado:",encontrado,"vezes.")




