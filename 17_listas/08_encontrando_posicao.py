# %%

numeros = [4, 7, 4, 2, 4, 9, 7, 1]

opcao = int(input("Digite um número:"))

print("O número aparece nas posições:")

for i, enu in enumerate(numeros):
    if enu == opcao:
        print(i)
