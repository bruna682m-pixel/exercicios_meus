# %%
grupo = {    
    "Arin": {"vida": 80, "nivel": 5},    
    "Mira": {"vida": 45, "nivel": 7},    
    "Toren": {"vida": 0, "nivel": 6},    
    "Luna": {"vida": 100, "nivel": 7},    
    "Kael": {"vida": 30, "nivel": 3}
}
sem_vida = []
entre_0_a_50_vida = []
loop = 0
chave_maior = 0
maior = 0
empate = []
soma = 0
media = 0

print(grupo)

restaurar_vida = input("Digite o personagem para restaurar vida:")

for chave, valor in grupo.items():
    if valor["vida"] == 0:
        sem_vida.append(chave)

    if valor["vida"] > 0 and valor["vida"] <= 50:
        entre_0_a_50_vida.append(chave)

    if loop == 0:
        maior = valor["nivel"]
        chave_maior = chave
    else:
        if valor["nivel"] > maior:
            maior = valor["nivel"]
            chave_maior = chave

    loop += 1

    soma = soma + valor["vida"]

media = soma / len(grupo)

for chave_100, valor_100 in grupo.items():
    if valor_100["nivel"] == maior:
            empate.append(chave_100)

if restaurar_vida in grupo:
    if grupo[restaurar_vida]["vida"] < 100:
        grupo[restaurar_vida]["vida"] = 100
    else:
        print("Seu personagem já tem vida maxima")
else:
    print("Seu personagem não existe.")


if len(empate) >= 2:
    print("Há 2 ou mais pessoas com o mesmo nível.",empate)
else:
    print("Há apenas 1 pessoa com o maior nível", chave_maior, maior)


print(f"""
Lista integrantes e atributos: {grupo}
Sem vida: {sem_vida}
Entre 0 e 50 de vida: {entre_0_a_50_vida}
Média: {media}
""")

