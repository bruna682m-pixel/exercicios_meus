# %%

notas = []
qtd = 0
maior = 0
menor = 0
media = 0
acima = []
abaixo = []
aprovadas = 0
reprovadas = 0
maior_posicao = 0
menor_posicao = 0

while True:
    add_notas = input("Digite notas ou enter para fechar:")

    if add_notas == "":
        print("Saindo...")
        break
    else:
        add_notas = int(add_notas)
        notas.append(add_notas)

qtd = len(notas)
maior = max(notas)
menor = min(notas)
media = sum(notas) / qtd

for j, enu2 in enumerate(notas):
    if enu2 >= 7:
        aprovadas += 1
    else:
        reprovadas += 1

    if enu2 >= media:
        acima.append(enu2)
    elif enu2 < media:
        abaixo.append(enu2)

for i, enu in enumerate(notas):
    if i == 0:
        maior = enu
        menor = enu
    else:
        if enu > maior:
            maior = enu
            maior_posicao = i
        if enu < menor:
            menor = enu
            menor_posicao = i
       
print(f"""
Notas: {notas}
Quantidade: {qtd}
Maior: {maior}
Menor: {menor}
Média: {media}
Acima da média: {acima}
Abaixo da média: {abaixo}
Aprovadas: {aprovadas}
Reprovadas: {reprovadas}
Posição maior {maior_posicao}
Posição menor {menor_posicao}

""")