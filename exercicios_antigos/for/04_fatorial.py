# %%
# Fatorial de um valor informado ( consistir para maior que zero e menor que 14
fatorial = 1

numero = int(input("Digite um número para calcular o fatorial:"))

if numero > 0 and numero < 14:
    for i in range(1, numero+1):
        fatorial = fatorial * i
        print(i)
else:
    print("Seu número deve ser entre 0 e 14.")

print("o fatorial de",numero,"é:",fatorial)

