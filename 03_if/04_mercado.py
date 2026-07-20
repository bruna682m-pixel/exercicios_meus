# %%
produto = input("""
Digite o produto que voce quer:
               1- Arroz - R$ 28.90
               2- Feijão - R$ 9.50
               3- Macarraão - R$ 6.80 
               4- Leite - R$ 5.90
               5- Café - R$ 19.90
""")

qtd = input("qual a quantidade de produto voce quer?")

fidelidade = input(""" 
Cartão fidelidade?
                   1- sim 5% de desconto
                   2- não
""")

pagamento = input("""
Qual o tipo de pagamento?
                  1 - Pix 3% de desconto
                  2- Cartão sem desconto
                  3- Dinheiro 2% de desconto

""")

qtd = float(qtd)
conta = 0
desconto = 0

if produto == "1":
    produto = "Arroz"
    conta = 28.90 * qtd
elif produto == "2":
    produto = "Feijão"
    conta = 9.50 * qtd
elif produto == "3":
    produto = "Macarraão"
    conta = 6.80 * qtd
elif produto == "4":
    produto = "Leite"
    conta = 5.90 * qtd
elif produto == "5":
    produto = "Café"
    conta = 19.90 * qtd
else:
    print("Escolha uma das opções.")

if fidelidade == "1":
    fidelidade = "com fidelidade"
    desconto = conta * 0.05 
    conta = conta - desconto
elif fidelidade == "2":
    fidelidade = "sem fidelidade"
    conta = conta - 0
else:
    print("Digite uma das opções")

if pagamento == "1":
    pagamento = "Pix"
    desconto = conta * 0.03 
    conta = conta - desconto
elif pagamento == "2":
    pagamento = "Cartão"
    conta = conta - 0
elif pagamento == "3":
    pagamento = "Dinheiro"
    desconto = conta * 0.02
    conta = conta - desconto
else:
    print("Digite uma das opções")

    
print("voce comprou o:", produto, "com", qtd, "quantidade", "voce escolheu, ", fidelidade, "e pagou com", pagamento, "Sua conta deu: ",conta )
# %%
