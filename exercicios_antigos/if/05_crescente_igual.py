# %%
# Solicitar dois valores inteiros, e mostrá-los na ordem crescente e decrescente.( prever para quando os
#valores forem iguais.

numero1 = input("Digite um número:")
numero2 = input("Digite outro número:")

numero1 = float(numero1)
numero2 = float(numero2)

maior = 0
menor = 0

if numero1 == numero2:
    print("Seus números são iguais")
elif numero1 < numero2:
    maior = numero2
    print("Seus números em ordem ficam", numero1,"e", maior)
    print("Seus números em ordem ficam", maior,"e", numero1)
elif numero1 > numero2:
    menor = numero2
    print("Seus números em ordem ficam", menor,"e", numero1)
    print("Seus números em ordem ficam", numero1,"e", menor)


    
# %%
# %%
# 3)Solicitar dois valores inteiros, e mostrá-los na ordem crescente e decrescente.

numero1 = input("Digite um número:")
numero2 = input("Digite outro número:")

numero1 = int(numero1)
numero2 = int(numero2)

if numero1 == numero2:
    print("Seus números são iguais")
elif numero1 < numero2:
    print("Seus números em ordem crescente ficam", numero1,"e", numero2)
    print("Seus números em ordem decrescente ficam", numero2,"e", numero1)
else:
    print("Seus números em ordem crescente ficam", numero2,"e", numero1)
    print("Seus números em ordem decrescente ficam", numero1,"e", numero2)
