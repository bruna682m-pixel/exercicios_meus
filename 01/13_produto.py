preco = input("qual o preço do produto? ")

preco = int(preco)

dez = preco * 0.10
avista = preco - dez
cinco = preco * 0.05
parcelado = preco + cinco

print("seu produto a vista ficara ", avista , "com 10% de desconto ")
print("seu produto fica ", parcelado, "pago parcelado com 5% de juros ")