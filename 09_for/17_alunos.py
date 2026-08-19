# %%

numero_max = 5
aprovado = 0
reprovado = 0

for i in range(1, numero_max+1):
    nome = input("Digite seu nome:")
    nota = float(input("Digite sua nota:"))

    if nota >= 5:
        aprovado += 1
        print(nome, "Aprovado.")
    else:
        reprovado += 1
        print(nome, "Reprovado.")
