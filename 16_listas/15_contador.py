# %%

numeros = []
contar_numero = 0
numero_encontrado = 0

while True:
    add_numero = input("Digite os números para a lista ou fim para encerrar:")

    if add_numero == "fim":
        print("Saindo....")
        break
    else:
        add_numero = int(add_numero)
        numeros.append(add_numero)

contar_numero = int(input("Digite qual número contar:"))

for i in numeros:
    if i == contar_numero:
        numero_encontrado += 1

print("O número", contar_numero, "foi encontrado", numero_encontrado, "vezes.")



