# %%
print("""
Escolha as opções de sua pizza:

Tamanho
1- Pequena - R$ 30.00
2- Média - R$ 45.00
3- Grande - R$ 60.00

Sabor
1- Calabresa - R$ 0.00
2- Frango - R$ 3.00
3- Portuguesa - R$ 5.00
4- Marguerita -  R$ 4.00

Borda
1- Catupiry - R$ 8.00
2- Cheddar - R$ 8.00
3- Sem borda - R$ 0.00
              
Refrigerante
1- Coca-cola 2l - R$ 12.00
2- Guaraná 2l - R$ 10.00
3- Não quero - RS 0.00              

Sobremesa
1- Pudim - R$ 10.00
2- Mousse - R$ 9.00
3- Não quero R$ 0.00                          

""")

tamanho = input("Digite a opção de tamanho:")
sabor = input("Digite a opção de sabor:")
borda = input("Digite a opção de borda:")
refri = input("Digite a sua opção de refri:")
sobremesa = input("Digite a sua opção de sobremesa:")

conta = 0

if tamanho == "1":
    tamanho = "Pequeno"
    conta = 30
elif tamanho == "2":
    tamanho = "Médio"
    conta = 45
elif tamanho == "3":
    tamanho = "Grande"
    conta = 60
else:
    print("Digite uma opção de tamanho")

if sabor == "1":
    sabor = "Calabresa"
    conta = conta + 0
elif sabor == "2":
    sabor = "Frango"
    conta = conta + 3
elif sabor == "3":
    sabor = "Portuguesa"
    conta = conta + 5
elif sabor == "4":
    sabor = "Marguerita"
    conta = conta + 4
else:
    print("Digite uma opção de sabor")

if borda == "1":
    borda = "Catupiry"
    conta = conta + 8
elif borda == "2":
    borda = "Cheddar"
    conta = conta + 8
elif borda == "3":
    borda = "Sem borda"
    conta = conta + 0
else:
    print("Digite uma opção de borda")

if refri == "1":
    refri = "Coca-cola"
    conta = conta + 12
elif refri == "2":
    refri = "Guaraná"
    conta = conta + 10
elif refri == "3":
    refri = "Sem refri"
    conta = conta + 0
else:
    print("Digite uma opção de bebida")

if sobremesa == "1":
    sobremesa = "Pudim"
    conta = conta + 10
elif sobremesa == "2":
    sobremesa = "Mousse"
    conta = conta + 9
elif sobremesa == "3":
    sobremesa = "Não quero"
    conta = conta + 0
else:
    print("Digite uma opção de sobremesa")

print("Seu pedidos foi: tamanho", tamanho, "Com sabor de",sabor, "Com opção de borda",borda, "a sua opção de bebida foi: ", refri, "com opção de sobremesa", sobremesa, "Sua conta deu:",conta )
# %%
