# %%

preco = input("Digite o preço dos produtos:")
vip = input("Voce é cliente vip? 1- sim e 2- não")
preco = float(preco)
desconto = 0
desconto = float(desconto)


if vip == "1":
    desconto = preco * 0.10
    desconto = preco - desconto
    print("Obrigado por ser vip! Seu valor total ficou:" ,desconto)
else:
    print("Seu valor total é:", preco)
 

