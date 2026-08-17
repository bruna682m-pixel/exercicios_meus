# %%

numero_max = 5
media = 0
soma = 0

for i in range(1, numero_max+1):
    nota = float(input("Digite as 5 notas:"))

    soma = soma + nota

media = soma / numero_max

if media >= 5:
    print("Aprovado.")
else:
    print("Reprovado.")