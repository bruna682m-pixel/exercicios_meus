# %%
# Receber 3 valores numéricos em 3 variáveis, A, B e C, e trocar os valores entre as variáveis de forma
#que, ao final do algoritmo, a variável A possua o menor valor e a variável C o maior.

a = input("Digite o valor a:")
b = input("Digite o valor b:")
c = input("Digite o valor c:")

a = float(a)
b = float(b)
c = float(c)

maior = 0
menor = 0

print(a,b,c)

if a > b and a > c:
    maior = a
    a = maior
    print("b,c,a")
elif b > a and b > c:
    maior = b
    b = maior
    print("bb")
else:
    maior = c
    c = maior
    print("cc")

if a < b and a < c:
    menor = a
    a= menor
    print("a ")
elif b < a and b < c:
    menor = b
    b = menor
    print("b")
else:
    menor = c
    c = menor
    print("c")




if a > b > c:
    print(a,b,c)
elif a > c > b:
    print(a,c,b)
elif b > a > c:
    print(b,a,c)
elif b > c > a:
    print(b,c,a)
elif c > a > b:
    print(c,a,b)
elif c > b > a:
    print(c,b,a)




print(menor, maior)

