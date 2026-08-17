# %%

numero_max = 4
soma = 0
maior = 0
menor = 0

for i in range(1, numero_max+1):
    numero = int(input("Digite 4 números:"))

    print(i)

    if i == 1:
        maior = numero
        menor = numero

    if numero < menor:
        menor = numero
    elif numero > menor:
        maior = numero
    elif numero < maior:
        menor = numero
    elif numero > maior:
        maior = numero


    soma = soma + numero


print("soma",soma)
print("este menor",menor)
print("este maior",maior)
# %%
