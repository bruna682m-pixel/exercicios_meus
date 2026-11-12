# %%
loja = {    
    "vida": {"preco": 30, "estoque": 8},    
    "mana": {"preco": 20, "estoque": 5},    
    "forca": {"preco": 50, "estoque": 3},    
    "velocidade": {"preco": 40, "estoque": 6}
}
valor_compra = 0
vendas = {}

while True:
    print(loja)

    opcao = input("Qual poção você quer comprar ou sair:")

    if opcao == "sair":
        print("Saindo..")
        break

    if opcao in loja:
        quantidade = int(input("Digite a quantidade de poções:"))

        if quantidade > 0:
            if loja[opcao]["estoque"] >= quantidade:
                loja[opcao]["estoque"] -= quantidade
                valor_compra += loja[opcao]["preco"] * quantidade
                if opcao not in vendas:
                    vendas[opcao] = quantidade
                else:
                    vendas[opcao] += quantidade
            else:
                print("Sem estoque suficiente.")

        else:
            print("Digite uma qtd maior que 0.")
    else:
        print("Digite uma poção valida.")


print("Sua compra deu:",valor_compra)
print("Vendas:",vendas)