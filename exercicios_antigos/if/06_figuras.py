# %%
#resolver
# Receber 3 valores numéricos, X, Y e Z, e verificar se esses valores podem corresponder aos lados de
# um triângulo. Em caso afirmativo, informar ao usuário se o triângulo é equilátero, isóscelos ou escaleno.

x = input("Digite um valor para x:")
y = input("Digite um valor para y:")
z = input("Digite um valor para z:")

x = float(x)
y = float(y)
z = float(z)

if x + y > z and x + z > y and y + z > x:
    print("Suas medidas formam um triângulo.")
    if x == y and y == z:
        print("Seu triãngulo é equilátero")
    elif x == y or x == z or y == z:
        print("Seu triãngulo é isóseles")
    elif x != y and y != z:
        print("Seu triãngulo é escaleno")
    else:
        print("Suas medidas não formam um triângulo.")







