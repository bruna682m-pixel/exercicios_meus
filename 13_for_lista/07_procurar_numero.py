# %%

numeros = [10, 25, 7, 42, 18, 30]
numero_usuario = int(input("Digite um número:"))
encontrou = False

for i in numeros:
    if i == numero_usuario:
        encontrou = True

if encontrou:
    print("Número encontrado!")
else:
    print("Número não encontrado!")

