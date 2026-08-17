# %%

numero_max = 5
aprovado = 0
reprovado = 0

for i in range(1, numero_max+1):
    nota = float(input("Digite a nota:"))

    if nota >= 5:
        aprovado += 1
    else:
        reprovado += 1

print("Aprovados:.",aprovado)
print("Reprovados:.",reprovado)