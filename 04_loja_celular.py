# %%
modelo = input("""
Menu
(1) Samsung
(2) Motorola
(3) Iphone
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
    modelo = "Samsung"
elif modelo == "2":
    modelo = "Motorola"
elif modelo == "3":
    modelo = "Iphone"
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



