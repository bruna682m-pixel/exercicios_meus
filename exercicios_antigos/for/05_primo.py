# %%
# Mostrar se um número é ou não primo ( consistir )

numero = int(input("Digite um número:"))

if numero <= 1:
    print("Não é primo.")
else:

    for i in range(2, numero):
        if numero % i == 0:
            print("não primo.")
            break

    else:
        print("primo")

    



