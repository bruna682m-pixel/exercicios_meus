# %%

numero = int(input("Digite um número:"))
resto = 0
soma = 0

for i in range(1, numero):
    resto = numero % i

    if resto == 0:
        soma = soma + i
    
if soma == numero:
    print("Número perfeito.")
else: 
    print("Número não perfeito.")


