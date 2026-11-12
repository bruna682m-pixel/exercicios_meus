# %%

guilda = {    
    "Arin": {"classe": "guerreiro", "nivel": 8, "missoes": 5},    
    "Mira": {"classe": "mago", "nivel": 12, "missoes": 9},    
    "Toren": {"classe": "guerreiro", "nivel": 6, "missoes": 3},    
    "Luna": {"classe": "arqueira", "nivel": 12, "missoes": 7},    
    "Kael": {"classe": "mago", "nivel": 4, "missoes": 2}
}
classes = {}
maior = 0
chave_maior = 0
loop = 0
empate = []
soma = 0
media = 0
pelo_menos_5 = []

print(guilda)

nome = input("Digite o nome para pesquisar:")

if nome in guilda:
    print("As informações do nome pesquisado é:",guilda[nome])
else:
    print("O integrante não está na lista.")

cadastro = input("Digite o nome do integrante para cadastrar:")

if cadastro not in guilda:
    classe_cadastro = input("Digite a classe do novo integrante:")
    nivel = input("Digite o nivel do novo integrante:")
    missoes_cadastro = int(input("Digite a missão do novo integrante:"))

    guilda[cadastro] = {
        "classe": classe_cadastro,
        "nivel": int(nivel),
        "missoes": missoes_cadastro
    }
else:
    print("O integrante já está cadastrado.")

for chave, valor in guilda.items():
    if valor["classe"] not in classes:
        classes[valor["classe"]] = 1
    else:
        classes[valor["classe"]] += 1

    if loop == 0:
        maior = valor["nivel"]
        chave_maior = chave
    else:
        if valor["nivel"] > maior:
            maior = valor["nivel"]
            chave_maior = chave
    loop += 1

    if valor["missoes"] >= 5:
        pelo_menos_5.append(chave)


    soma = soma + valor["missoes"]

media = soma / len(guilda)

for chave_empate, valor_empate in guilda.items():
    if valor_empate["nivel"] == maior:
        empate.append(chave_empate)

if len(empate) >= 2:
    print("Houve empate.",empate)
else:
    print("Sem empate:",chave_maior,maior)

print(f"""
Classes: {classes}
Média: {media}
Pelos menos 5 missões: {pelo_menos_5}
Lista completa: {guilda}
""")

