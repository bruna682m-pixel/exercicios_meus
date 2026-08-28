# %%
numero_max = 5
resto = 0
numero = 0
divisiveis = 0
qtd_divisores = 0

for i in range(1, numero_max+1):
    numero = int(input("Digite um número:"))
    qtd_divisores = 0

    for i in range(1, numero+1):
        resto = numero % i
       
        if resto == 0:
            qtd_divisores += 1

    if qtd_divisores == 2:
        print("Seu número é primo")
    else:
        print("Seu número não é primo")


