# %%

numeros = [2, 7, 10, 3, 8, 15, 20, 11]
soma_par = 0
soma_impar = 0

for i in numeros:
    if i % 2 == 0:
        soma_par = soma_par + i
    else:
        soma_impar = soma_impar + i

print(f"""
pares: {soma_par}
ìmpares: {soma_impar}
""")
