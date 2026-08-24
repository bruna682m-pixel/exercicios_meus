# %%

media = 0
soma = 0
nota = 0


for i in range(1, 6):
    nota = float(input("Digite suas notas:"))
    soma = soma + nota

media = soma / 5

print(soma)
print(media)