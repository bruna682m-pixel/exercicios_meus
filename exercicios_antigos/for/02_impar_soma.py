# %%
# Mostrar os impares entre 10 e 80 o a somatória deles.

numero_max = 80
soma = 0

for i in range(10, numero_max+1):
    if i % 2 != 0:
        print(i)

        soma = soma + i

print("A soma dos impares deu:",soma)

