# %%
media = 0
maior = 0
menor = 0
count = 1
soma = 0

maior = float(maior)
menor = float(menor)
media = float(media)
soma = float(soma)

while True:
    notas = input("Digite suas notas:")

    if notas == "":
        break

    if count == 1:
        notas = float(notas)
        maior = notas
        menor = notas
    else:
        notas = float(notas)
        if notas > maior:
            maior = notas
        elif notas < menor:
            menor = notas
              
    count += 1

soma = soma + notas
media = soma / count
print("""
Média =""", media,"""
Maior nota:""", maior, """
Menor nota:""", menor)