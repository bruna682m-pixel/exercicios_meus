# %%

precos = []
loop = 1
maior = 0
menor = 0
maior_max = 0
menor_min = 0
total_sum = 0
media_sum = 0
maior_10 =0 

while loop <= 5:

    entrada_preco = float(input("Digite os preços:"))

    precos.append(entrada_preco)

    if i > 10:
        maior_10 += 1

    for i in precos:
        if loop == 1:
            maior = i
            menor = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i

    total_sum = sum(precos)

    media_sum =  total_sum / len(precos)

    maior_max = max(precos)
    menor_min =  min(precos)


    loop += 1

print(f"""
Total Sum: {total_sum}
Média Sum: {media_sum}
Maior preço: {maior}
Menor preço: {menor}
Maior preço Max: {maior_max}
Menor preço Min: {menor_min}
Qtd maior que 10: {maior_10}
""")

