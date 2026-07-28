# %%
# resolver
# Receber 3 valores numéricos em 3 variáveis, A, B e C, e trocar os valores entre as variáveis de forma
#que, ao final do algoritmo, a variável A possua o menor valor e a variável C o maior.

a = input("Digite o valor a:")
b = input("Digite o valor b:")
c = input("Digite o valor c:")

a = float(a)
b = float(b)
c = float(c)

if a < b:
    print("b maior")
    print("a menor")
    print( a, b,c,"a") # 1 3 2
    if b > c:
        print("c maior")
        print(a,b,c,"b") #
# %%


elif a > b:
    print(a,b,c)
    if a < c:
        print("c maior")
        print(b,a,c,"c")





# %%
if numero1 == numero2:
    print("Seus números são iguais")
elif numero1 < numero2:
    maior = numero2
    print("Seus números em ordem ficam", numero1,"e", maior)
elif numero1 > numero2:
    menor = numero2
    print("Seus números em ordem ficam", menor,"e", numero1)
