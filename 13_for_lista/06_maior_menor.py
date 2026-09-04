# %%

numeros = [15, 3, 87, 42, 9, 61, 28]
maior = 0
menor = 0

for i, numero_lista in enumerate(numeros):

    if i == 0:
        maior = numero_lista
        menor = numero_lista
    else:
        if numero_lista > maior:
            maior = numero_lista
        elif numero_lista < menor:
            menor = numero_lista

print(maior)
print(menor)