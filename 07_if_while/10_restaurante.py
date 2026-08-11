# %%
total = 0
opcao = int(input("""
Menu
1- Hambúrguer = R$ 30,00
2- Batata = R$ 10,00
3- Refri = R$ 9,90
4- Sovete = R$ 4,00
5- Fechar pedido
"""))

while True:
    opcao = int(input("Digite a opção:"))

    if opcao == 1:
        total = total + 30
        opcao = "Hambúrguer"
        print("Você pediu",opcao)
    elif opcao == 2:
            total = total + 10
            opcao = "Batata"
            print("Você pediu",opcao)
    elif opcao == 3:
            total = total + 9.99
            opcao = "Refri"
            print("Você pediu",opcao)
    elif opcao == 4:
            total = total + 4
            opcao = "Sorvete"
            print("Você pediu",opcao)
    elif opcao == 5:  
        if total >= 100:
                desconto = total * 0.10
                desconto = total - desconto  
                troco = float(input(f"""
                Seu pedido foi:{opcao}
                Total:{desconto}
                """))
                if troco < desconto:
                                print("Paque o valor todo.")
                else:
                                desconto = troco - desconto
                                print("Seu troco foi R$",desconto,)
                                break
        else:
                troco = float(input(f"""
                                Seu pedido foi:{opcao}
                                Total:{total}
                                """))
        if troco < total:
                print("Paque o valor todo.")
        else:
                total = troco - total
                print("Seu troco foi R$",total,)
                break


    
