# %%
nome_produto = ""
preco = 0
qtd_produto = 0
desconto = 0
count = 1
valor_pago =0
total = 0

opcao = int(input("""
Deseja adicionar um produto?

1- sim
2- não

"""))

while opcao == 1:
    opcao = int(input("""
Deseja adicionar um produto?

1- sim
2- não
2
"""))
    if opcao == 1:
        nome_produto = input("Digite o nome do produto.")
        preco = float(input("Digite o preço do produto."))
        qtd_produto = int(input("Digite a quantidade do produto."))

        print("Voce adicionou no carrinho",nome_produto,total)

        if count == 1:
            total = preco * qtd_produto
            print("2",total,count)
        else:
            total = total + (preco * qtd_produto)
            print("1",total,count)
    else:
        break
    count += 1


if total > 200:
        desconto = total * 0.10
        desconto = total - desconto
        print("Quantidade de produto:""",qtd_produto,)
        print("Voce recebeu R$ 10,00 de desconto. O total deu R$",desconto)   

valor_pago = float(input("Digite o valor pago."))

while valor_pago > total:
    if valor_pago > total:
        troco = valor_pago - total
        print("""
        Quantidade de produto:""",qtd_produto,"""
        Total compra R$""",total)
        print("Voce pagou R$",total,"Seu troco foi de R$",troco)
        break
    
    else:
        print("Valor insuficiente.")
        break


print("sai")

# %%
nome_produto = input("Digite o nome do produto.")
preco = float(input("Digite o preço do produto."))
qtd_produto = int(input("Digite a quantidade do produto."))

total = preco * qtd_produto

opcao = int(input("""
Deseja adicionar mais outro produto?

1- sim
2- não

"""))

while opcao == 1:
    opcao = int(input("""
Deseja adicionar mais outro produto?

1- sim
2- não
2
"""))
    if opcao == 1:
        nome_produto = input("Digite o nome do produto.")
        preco = float(input("Digite o preço do produto."))
        qtd_produto = int(input("Digite a quantidade do produto."))

        total = preco * qtd_produto
    else:
        break


print("sai")

if total > 200:
        desconto = total * 0.10
        desconto = preco - desconto
        print("Quantidade de produto:""",qtd_produto,)
        print("Voce recebeu R$ 10,00 de desconto. O total deu R$",desconto)   