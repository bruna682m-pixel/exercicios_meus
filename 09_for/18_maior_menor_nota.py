# %%

numero_max = 5
maior = 0
menor = 0

for i in range(1, numero_max+1):
    notas = float(input("Digite sua nota:"))

    if i == 1:
        maior = notas
        menor = notas
    else:
        if notas > maior:
            maior = notas

        if notas < menor:
            menor = notas

print("Maior nota:",maior)
print("Menor nota:",menor)




        