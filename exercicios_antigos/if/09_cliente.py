# %%

# Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente. O algoritmo
#deve receber o código de um produto e a quantidade comprada e calcular o preço total, usando a tabela
#abaixo:
#Código do produto Preço unitário
#1 R$ 32,00
#2 R$ 45,00
#3 R$ 37,00
#4 R$ 33,00

print("""
Código do produto               Preço
      1                         R$ 32,00
      2                         R$ 45,00
      3                         R$ 37,00
      4                         R$ 33,00
""")

total = 0

codigo = input("Digite o códico do produto:")
codigo = int(codigo)
    
qtd = input("Digite a quantidade do produto:")
qtd = int(qtd)

if codigo == 1:
    total = 32 * qtd
elif codigo == 2:
    total = 45 * qtd
elif codigo == 3:
    total = 37 * qtd
elif codigo == 4:
    total = 33 * qtd
else:
    print("Digite um código invalido.")

print("Sua compra deu: R$", total)