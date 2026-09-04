# %%

numeros = [12, -5, 8, 20, 0, -3, 15, 8, 7, -10]
soma = 0
media = 0
maior = 0
menor = 0
positivos = 0
negativos = 0
zeros = 0
pares = 0
impares = 0

for i, numero_lista in enumerate(numeros):
   soma = soma + numero_lista

   if i == 0:
        maior = numero_lista
        menor = numero_lista
   else:
        if numero_lista > maior:
            maior = numero_lista
        elif numero_lista < menor:
            menor = numero_lista

   if numero_lista < 0:
       negativos += 1
   elif numero_lista > 0:
       positivos += 1
   else:
       zeros += 1

   if numero_lista % 2 == 0:
       pares += 1
   else:
       impares += 1

media = soma / len(numeros)

print(f"""
Maíor: {maior}
Menor: {menor}
Soma: {soma}
Média: {media}
Posítivos: {positivos}
Negatívos: {negativos}
Zeros: {zeros}
Pares: {pares}
ímpares: {impares}

""")