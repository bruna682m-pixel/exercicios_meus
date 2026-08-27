# %%
# se o resto da divisão for 0 é divisível

numero = int(input("Digite um número:"))
resto = 0
qtd_divisores = 0

for i in range(1, numero+1):
    resto = numero % i

    if resto == 0:
        qtd_divisores += 1
        print("divisiveis de:",numero,"são:",i) 

print(numero,"tem",qtd_divisores,"divisores")



