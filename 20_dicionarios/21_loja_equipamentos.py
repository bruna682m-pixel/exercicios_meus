# %%
loja = {
    "espada": {"preco": 150, "estoque": 5},
    "escudo": {"preco": 100, "estoque": 3},
    "pocao": {"preco": 25, "estoque": 10},
    "armadura": {"preco": 250, "estoque": 2}
}
total = 0

while True:
    print(loja)

    produto_comprar = input("Qual produto você quer comprar ou digite sair para encerrar:")

    if produto_comprar == "sair":
        print("Saindo...")
        break

    if produto_comprar in loja:
        unidades = int(input("Quantas unidades do produto você quer comprar:"))

        if unidades > 0:
            if loja[produto_comprar]["estoque"] >= unidades:
                loja[produto_comprar]["estoque"] -= unidades
                total +=  loja[produto_comprar]["preco"] * unidades
                print("Você comprou:",produto_comprar, "com", unidades,"unidades")
            else:
                print("Não temos estoque suficiente")
        else:
            print("A quantidade deve ser maior que 0.")
    else:
        print("O produto não existe.")

print(f"""
Total: {total}
""")