# %%
# Receber valores de base e altura de um triângulo e verificar se são valores válidos (positivos maiores
#que zero). Em caso afirmativo, calcular a área do triângulo.

base = input("Digite a base do triangulo:")
altura = input("Digite a altura do triangulo:")

base = float(base)
altura = float(altura)


if base > 0 and altura > 0:
    area = base * altura / 2
    print("A área do triangulo é",area)
else:
    print("Digite números positivos maiores que 0")
# %%
