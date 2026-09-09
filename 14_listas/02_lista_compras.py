# %%

compras = ["arroz", "feijao", "macarrao", "leite", "cafe"]

print(compras)

while True:
    item = input("Digite um item da lista de compras:")

    if item == "":
        break

    compras.append(item)

print(compras)

indice = int(input("Digite o indice para remover da lista:"))

compras.pop(indice)

print(compras)
