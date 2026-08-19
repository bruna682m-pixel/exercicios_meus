# %%

numero_max = 4
maior = 0
menor = 0
soma = 0

for i in range(1, numero_max+1):
    numero = float(input("Digite sua nota:"))

    soma = soma + numero

    if i == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print("Soma:",soma)
print("Menor número:",menor)
print("Maior número:",maior)
