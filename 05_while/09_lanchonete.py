# %%
print("""
Qual produto voce quer:

1- Hambúrguer - R$ 35,00
2- Batata - R$ 10,00
3- Refrigerente - R$ 7,00
4- Finalizar pedido
""")
conta = 0

while True:
    opcao = input("""
Qual produto voce quer:

1- Hambúrguer - R$ 35,00
2- Batata - R$ 10,00
3- Refrigerente - R$ 7,00
4- Finalizar pedido
""")

    opcao = float(opcao)

    if opcao == 4:
        break

    if opcao == 1:
        conta = conta + 35
        print("voce escolheu: hambúrguer")
    elif opcao == 2:
        conta = conta + 10
        print("voce escolheu: batat")
    elif opcao == 3:
        conta = conta + 7
        print("voce escolheu: refri")

print("Sua conta deu:",conta)   

# %%

total = 0
opcao = "0"

while opcao < "4":
    opcao = input("""
    Qual produto voce quer:
    
    1- Hambúrguer - R$ 35,00
    2- Batata - R$ 10,00
    3- Refrigerente - R$ 7,00
    4- Finalizar pedido
    """)

    if opcao == "1":
        total = 35
        opcao = "Hambúrguer"
    elif opcao == "2":
        total = total = 10
        opcao = "Batata"
    elif opcao == "3":
        total = total + 7
        opcao = "Refri"

print("Sua conta deu:", total, "sua opcoes", opcao)