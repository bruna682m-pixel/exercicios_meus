# %%
prato = input("""
(1) Prato executivo - R$ 15.99
(2) Lasanha R$ 29.50
(3) Hambúrguer - R$ 35.75
""")


bebida = input( """
Qual bebida refri ou suco ?
(1) Refri - R$ 5.99
(2) Suco - R$ 2.30
""")



sobremesa = input("""
Quer sobremesa?
(1) sim - R$ 15.00
(2) não - R$ 0
""")



conta = 0
conta = float(conta)

if prato == "1":
    conta = 15.99
    prato = "Executivo"
elif prato == "2":
    conta = 29.50
    prato = "Lasanha"
elif prato == "3":
    prato = "35.75"
else:
    print("Digite uma prato")

if bebida == "1":
    conta = conta + 5.99
    bebida = "Refri"
elif bebida == "2":
    conta = conta + 2.30
    bebida = "Suco"
else: 
    print("Digite uma bebida")

if sobremesa == "1":
    conta = conta + 15
    sobremesa = "com sobremesa"
elif sobremesa == "2":
    conta = conta + 0
    sobremesa = "sem sobremesa"
else:
    print("Digite uma sobremesa.")

print ("Seu pedido foi",prato, "com",bebida, "e optou por", sobremesa, "Sua conta deu:", conta)




