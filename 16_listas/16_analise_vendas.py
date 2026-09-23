# %%

vendas = []
total = 0
media = 0
maior = 0
menor = 0
maior_max = 0
menor_min = 0
qtd_vendas = 0
venda_acima_100 = 0
loop = 0
indice_maior_venda = 0

while True:
    add_venda = input("Digite os valores das vendas ou enter para encerrar")

    if add_venda == "":
        print("Saindo.....")
        break
    else:
        add_venda = int(add_venda)
        vendas.append(add_venda)
        print(vendas)

    if add_venda > 100:
        venda_acima_100 += 1

    for i, enu in enumerate(vendas):
        if i == 0:
            maior = enu
            menor = enu
        else:
            if enu > maior:
                maior = enu
                indice_maior_venda = i
            if enu < menor:
                menor = enu

total = sum(vendas)
maior_max = max(vendas)
menor_min = min(vendas)
qtd_vendas = len(vendas)
media = total / qtd_vendas

print(f"""
{vendas}

Total vendido: {total}
Média das vendas: {media}
Maior venda: {maior}
Menor venda: {menor}
Maior venda max: {maior_max}
Menor venda min: {menor_min}
Quantidade de venda: {qtd_vendas}
Vendas acima de 100: {venda_acima_100}
índice maior venda: {indice_maior_venda}

""")



    

