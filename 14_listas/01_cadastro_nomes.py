# %%

nomes = []

while True:
    nome = input("Digite nomes:")

    if nome == "":
        break

    nomes.append(nome)

print(nomes)
print("Qtd de pessoas:", len(nomes))
print("ultimo nome:", nomes[-1])
print("primeiro nome:", nomes[0])
