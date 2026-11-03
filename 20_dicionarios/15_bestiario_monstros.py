# %%

bestiario = {
    "slime": 12,
    "esqueleto": 25,
    "morcego": 0,
    "zumbi": 20,
    "ender dragon": 200,
    "creeper": 30
}
experiancia_maior_25 = []
experiancia_menor_20 = 0
loop = 0
maior = 0
chave_maior = 0

monstro = input("Digite o nome do monstro para descobrir quanto de experiência dá:")
opcao = input("Deseja cadastrar um novo mosntro?")

if opcao == "sim":
    chave_monstro = input("Digite o nome do monstro:")

    if chave_monstro not in bestiario:
        valor_experiencia = int(input("Digite o valor da experiência do monstro:"))
        bestiario[chave_monstro] = valor_experiencia
    else:
        print("Você já encontrou esta monstro.")
else:
    print("Você não cadastrou nenhum monstro novo.")

if monstro in bestiario:
    print(f"O monstro {monstro} dà", bestiario[monstro], "de experiência.")
else:
    print("Você não encontrou este monstro.")

for chave, valor in bestiario.items():
    if valor >= 25:
        experiancia_maior_25.append(chave)

    if valor < 20:
        experiancia_menor_20 += 1

    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave
    loop += 1

    


print(f"""
Bestiário: {bestiario}
Mais de 25 de experiência: {experiancia_maior_25}
Menor de 20 de experiência: {experiancia_menor_20}
Maior experiência: {chave_maior} {maior}


""")