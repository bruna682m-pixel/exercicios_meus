# %%
numero_max = 5
aprovado = 0
soma = 0
media = 0

for i in range(1, numero_max+1):
    nota = float(input("Digite sua nota:"))

    if nota >= 5:
        aprovado += 1
        soma = soma + nota

if aprovado > 0:
    media = soma / aprovado
else:
    media = 0

print("Quantidade aprovados:",aprovado)
print("A media dos aprovados é:",media)

