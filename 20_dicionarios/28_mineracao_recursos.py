# %%
mina = {    
    "madeira": {"quantidade": 10, "valor": 5},    
    "ferro": {"quantidade": 8, "valor": 15},    
    "ouro": {"quantidade": 3, "valor": 50},    
    "cristal": {"quantidade": 5, "valor": 30}
}
registro_coleta = {}
registro_uso = {}
total_recursos = 0
valor_total = 0

while True:
    opcao = int(input("Digite a opção do menu:"))
    print("""
1- Listar recursos
2- Registrar coleta
3- Registrar uso
4- Consultar recurso
5- Valor total dos recursos
6- Maior qunatidade
7- Maior valor unitário
8- Recursos abaixo de 5
9- Sair
""")

    if opcao == 1:
        print("Listando recursos:", mina)

    elif opcao == 2:
        coleta_valida = False

        coleta = input("Qual material você coletou:")
        qtd_coleta = int(input("Digite a quantidade de material que você coletou:"))

        if qtd_coleta <= 0:
            print("A quantidade precisa ser maior que 0.")
        else:
            if coleta not in mina:
                valor_coleta = int(input("Digite o valor de cada item da coleta:"))

                if valor_coleta > 0:
                    mina[coleta] = {
                        "quantidade": qtd_coleta,
                        "valor": valor_coleta
                    }
                    coleta_valida = True
                else:
                    print("O valor da coleta precisa ser maior que 0.") # se digitar material que nao existe da erro eu queria cadastrar o novo material
            else:
                mina[coleta]["quantidade"] += qtd_coleta
                coleta_valida = True

            if coleta_valida:
                if coleta not in registro_coleta:
                    registro_coleta[coleta] = qtd_coleta
                else:
                    registro_coleta[coleta] += qtd_coleta

    elif opcao == 3:
        uso = input("Qual material você quer usar:")

        if uso in mina:
            qtd_uso = int(input("Digite a quantidade de material para usar:"))
            if qtd_uso <= 0:
                print("A quantidade precisa ser maior que 0.")
            else:
                if qtd_uso <= mina[uso]["quantidade"]:
                    mina[uso]["quantidade"] -= qtd_uso
                    if uso not in registro_uso:
                        registro_uso[uso] = qtd_uso
                    else:
                        registro_uso[uso] += qtd_uso
                else:
                    print("Não temos tudo isso no estoque.")
        else:
            print("Este recurso não está na lista.")

    elif opcao == 4:
        consulta_nome = input("Digite o nome do material para consultar:")
        
        if consulta_nome in mina:
            print("Dados do material que você pesquisou:",mina[consulta_nome])
        else:
            print("Você não coletou este item.")

    elif opcao == 5:
        total_recursos = 0
        valor_total = 0

        for chave, valor in mina.items():
            total_recursos = total_recursos + valor["quantidade"]

            valor_total = valor_total + valor["valor"] * valor["quantidade"]

        print(f"""
        Total recursos: {total_recursos}
        Total valor: {valor_total}
        """)

    elif opcao == 6:
        loop_qtd = 0
        maior_qtd = 0
        chave_qtd = 0

        for chave_q, valor_qtd in mina.items():
            if loop_qtd == 0:
                maior_qtd = valor_qtd["quantidade"]
                chave_qtd = chave_q
            else:
                if valor_qtd["quantidade"] > maior_qtd:
                    maior_qtd = valor_qtd["quantidade"]
                    chave_qtd = chave_q
            loop_qtd += 1

        print(f"Maior quantidade: {chave_qtd} {maior_qtd}")

    elif opcao == 7:
        loop_valor = 0
        maior_valor = 0
        maior_chave_valor = 0

        for chave_valor, valor_valor in mina.items():
            if loop_valor == 0:
                maior_valor = valor_valor["valor"]
                maior_chave_valor = chave_valor
            else:
                if valor_valor["valor"] > maior_valor:
                    maior_chave_valor = chave_valor
                    maior_valor = valor_valor["valor"]
            loop_valor += 1

        print(f"Maior preço: {maior_chave_valor} {maior_valor}")

    elif opcao == 8:
        abaixo_5 = []
        for chave, valor in mina.items():
            if valor["quantidade"] < 5:
                abaixo_5.append(chave)

        print("Itens abaixo de 5: ", abaixo_5)

    elif opcao == 9:
        print("Saindo...")
        break

    else:
        print("Opção invalida.")




