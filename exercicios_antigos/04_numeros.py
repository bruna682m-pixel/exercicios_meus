#  Ler dois valores inteiros negativos ( consistir se é negativo), multiplicar e mostrar o resultado
# %%

count = 0
multiplicacao = 0

while True:
    numero1 = input("Digite um numero:")
    numero2 = input("Digite outro numero:")

    numero1 = float(numero1)
    numero2 = float(numero2)

    if numero1 <= 0 and numero2 <= 0:
        break

    multiplicacao = numero1 * numero2

print("A Multiplicacao deu:", multiplicacao)

    