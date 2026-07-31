#  Ler dois valores inteiros negativos ( consistir se é negativo), multiplicar e mostrar o resultado
# %%

multiplicacao = 0
numero1 = 0
numero2 = 0

while numero1 >= 0 or numero2 >= 0:
    numero1 = input("Digite um numero:")
    numero2 = input("Digite outro numero:")

    numero1 = float(numero1)
    numero2 = float(numero2)

    multiplicacao = numero1 * numero2

print("A Multiplicacao deu:", multiplicacao)

    