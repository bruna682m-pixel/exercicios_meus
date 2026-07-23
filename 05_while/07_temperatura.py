# %%
count = 0
media  = 0
maior = 0
menor = 0
soma = 0

while True:
    temperatura = input("Digite as temperaturas:")

    if temperatura == "999":
        break

    temperatura = float(temperatura)

    if count == 0:
        maior = temperatura
        menor = temperatura

    if maior < temperatura:
        maior = temperatura

    if menor > temperatura:
        menor = temperatura

    count += 1

    soma = soma + temperatura

media = soma / count

print("""
Média:""", media, 
"""
Maior valor:""", maior,
"""
Menor valor:""", menor
)
