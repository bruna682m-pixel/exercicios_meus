# %%
modelo = input("""
Menu
(1) Samsung - R$ 2000
(2) Motorola - R$ 1500
(3) Iphone - R$ 5000
""")
garantia = input("""
Quer garantia estendida? 
Preço da garantia estendida R$ 100.00
1- sim 
2- não
""")

pelicula = input("""
Quer garantia pelicula? 
Preço da pelicula R$ 10.00
1- sim 
2- não
""")

conta = 0
conta = float(conta)

if modelo == "1":
    conta = 2000
    modelo = "Samsung"
elif modelo == "2":
    conta = 1500
    modelo = "Motorola"
elif modelo == "3":
    modelo = "Iphone"
    conta = 5000
else:
    print("Não temos este modelo")

if garantia == "1":
    conta = conta + 100
    garantia = "garantia"
elif garantia == "2":
    conta = conta + 0
    garantia = "sem garantia"
else:
    print("Digite uma das 2 opções se voce quer garantia")

if pelicula == "1":
    conta = conta + 10
    pelicula = " pelicula"
elif pelicula == "2":
    conta = conta + 0
    pelicula = " sem pelicula"
else:
    print("Digite uma das 2 opções")


print("Seu modelo é",modelo, "voce optou por ",garantia, "e optou por ",pelicula, "sua conta deu: R$",conta)



