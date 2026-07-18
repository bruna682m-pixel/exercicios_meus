# %%
texto = """Escolha algum produto de nossa padaria e a quantidade
(1) Pão Frances - R$5,00
(2) Pão de queijo - R$2.99
(3) Sonho - R$5.98
(4) Café - R$2.50
"""
print(texto)
texto = input("Qual produto voce quer? ")
qtd = input("Digite a quantidade: ")


qtd = float(qtd)

if texto == "1":
    conta = 5 * qtd
    texto = "Pão Frances"
elif texto == "2":
    conta = qtd * 2.99
    texto = "Pão de Queijo"
elif texto == "3":
    conta = qtd * 5.98
    texto = " Sonho"
elif texto == "4":
    conta = qtd * 2.50
    texto = "Café"
else:
    print("Digite umas das opções de produto.")

print("O seu pedido foi:" ,texto, "com ", qtd , "unidades e sua conta deu:" , conta)


