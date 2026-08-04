# %%
# Receber 3 valores numéricos em 3 variáveis, A, B e C, e trocar os valores entre as variáveis de forma
#que, ao final do algoritmo, a variável A possua o menor valor e a variável C o maior.

a = input("Digite o valor a:")
b = input("Digite o valor b:")
c = input("Digite o valor c:")

a = float(a)
b = float(b)
c = float(c)

if a > b:
    aux = a
    a = b
    b = aux

if b > c:
    aux = b
    b = c
    c = aux

if a > b:
    aux = a
    a = b
    b = aux

print("Os números em ordem crescente ficaram:", a, b, c)
print("Os números em ordem decrescente ficaram:", c, b, a)
