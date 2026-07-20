# %%
tipo = input("""
Escolha seu Hamburguer:
             1- X-Burguer - R$20.00
             2- X-Salada - R$25.00
             3- X-Bacon - R$30.00
""")

carne = input("""
Escolha o tipo de carne:
              1- Bovina - R$ 0.00
              2- Frango - R$ 2.00
              3- Costela - R$ 5.00
""")

queijo = input("""
Escolha o tipo de queijo:
               1- Mussarela - R$ 3.00
               2- Cheddar - R$ 5.00
               3- Prato - R$ 4.00
""")

bebida = input("""
Escolha a bebida:
               1- Refri - R$ 8.00
               2- Suco - R$ 7.00
               3- Agua - R$ 4.00

""")

batata = input("""
Escolha a batata:
               1- Pequena - R$ 8.00
               2- Média - R$ 12.00
               3- Grande - R$ 16.00
""")

sobremesa = input("""
Escolha a sobremesa:
                  1- Sorvete - R$ 10.00
                  2- Brownie - R$ 12.00
                  3- Não quero - R$ 0.00
""")

conta = 0

if tipo == "1":
    tipo = "X-Burger"
    conta = 20
elif tipo == "2":
    tipo = "X-Salada"
    conta = 25
elif tipo == "3":
    tipo = "X-Bacon"
    conta = 30
else:
    print("Digite alguma opção.")

if carne == "1":
    carne = "Bovina"
    conta = conta + 0
elif carne == "2":
    carne = "Frango"
    conta = conta + 2
elif carne == "3":
    carne = "Costela"
    conta = conta + 5
else:
    print("Digite alguma opção.")

if queijo == "1":
    queijo = "Mussarela"
    conta = conta + 3
elif queijo == "2":
    queijo = "Cheddar"
    conta = conta + 5
elif queijo == "3":
    queijo = "Prato"
    conta = conta + 4
else:
    print("Digite alguma opção.")

if bebida == "1":
    bebida = "Refri"
    conta = conta + 8
elif bebida == "2":
    bebida= "Suco"
    conta = conta + 7
elif bebida == "3":
    bebida = "Agua"
    conta = conta + 4
else:
    print("Digite alguma opção.")

if batata == "1":
    batata = "Pequena"
    conta = conta + 8
elif batata == "2":
    batata = "Média"
    conta = conta + 12
elif batata == "3":
    batata = "Grande"
    conta = conta + 16
else:
    print("Digite alguma opção.")

if sobremesa == "1":
    sobremesa = "Sorvete"
    conta = conta + 10
elif sobremesa == "2":
    sobremesa = "Brownie"
    conta = conta + 12
elif sobremesa == "3":
    sobremesa = "Não quero"
    conta = conta + 0
else:
    print("Digite alguma opção.")

print("""
Resumo do pedidos
      
Hamburguer:""" , tipo,
"""
Carne:""", carne,
"""
Queijo:""", queijo,
"""
Bebida:""", bebida, 
"""
Batata:""", batata,
"""
Sobremesa:""", sobremesa,
"""
Total: """, conta)