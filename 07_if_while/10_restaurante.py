# %%
total = 0
pedido = ""
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
        pedido += "Hambúrguer\n"

    elif opcao == 2:
            total = total + 10
            pedido += "Batata\n"

    elif opcao == 3:
            total = total + 9.99
            pedido += "Refri\n"
            
    elif opcao == 4:
            total = total + 4
            pedido += "Sorvete\n"

    elif opcao == 5:  
        if total >= 100:
                desconto = total * 0.10
                desconto = total - desconto  
                troco = float(input(f"""
                Seu pedido foi:{pedido}
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
                                Seu pedido foi:{pedido}
                                Total:{total}
                                """))
                if troco < total:
                        print("Paque o valor todo.")
                else:
                        total = troco - total
                        print("Seu troco foi R$",total,)
                        break


    
