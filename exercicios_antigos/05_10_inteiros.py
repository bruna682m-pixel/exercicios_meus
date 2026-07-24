# Ler 10 valores inteiros, um de cada vez, e contar quantos deles estão no intervalo [10,20] e
#quantos deles estão fora do intervalo, ao final mostrar estas informações.

# %%
count = 0

no_intervalo = 0
fora_intervalo = 0

while count <= 10:
    numero = input("Digite um número:")
    print(count)

    numero = float(numero)
    print(numero)

    if numero >= 10 and numero <= 20:
        no_intervalo += 1

    if numero < 10 or numero > 20:
        fora_intervalo += 1

    count += 1

print("""
No intervalo:""", no_intervalo,"""
Fora do intervalo:""", fora_intervalo)
1# %%
