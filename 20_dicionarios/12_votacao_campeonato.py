# %%
votos = {    "Ana": 0,    "Bruno": 0,    "Carla": 0}
loop = 0
vencedor = 0
chave_vencedor = 0
empate = []

while True:
    opcao = input("Quer registrar um voto? sim ou não?")
    if opcao == "sim":
        voto = input("Digite sua escolha:")
        if voto in votos:
            votos[voto] += 1
        else:
            print("Candidato não está na lista.")
    else:
        print("Você escolheu não votar.")
        break

for chave, valor in votos.items():
    if loop == 0:
        vencedor = valor
        chave_vencedor = chave
    else:
        if valor > vencedor:
            vencedor = valor
            chave_vencedor = chave

    loop += 1
if vencedor == 0:
    print("Nenhum voto registrado.")
else:
    print("vencedor:", chave_vencedor, vencedor)

for chave_empate, valor_empate in votos.items():
    if vencedor == valor_empate:
        empate.append(chave_empate)

if len(empate) == 1:
    print("Sem empate.")
else:
    print("Empate.")

print(f"""
Candidatos: {votos}
""")