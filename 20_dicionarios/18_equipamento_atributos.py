# %%
equipamentos = {    
    "elmo": {"tipo": "defesa", "bonus": 8},    
    "botas": {"tipo": "velocidade", "bonus": 5},    
    "escudo": {"tipo": "defesa", "bonus": 15},    
    "anel": {"tipo": "magia", "bonus": 12},    
    "luvas": {"tipo": "velocidade", "bonus": 3},
    "touca": {"tipo": "defesa", "bonus": 15}
    }

pesquisa = []
soma_bonus = 0
loop = 0
maior = 0
chave_maior = 0
defesa = 0
velocidade = 0
magia = 0
bonus_igual = []

tipo = input("Digite um tipo de equipamento:")
nome_equipamento = input("Digite o nome do equipamento:")

for chave, dados in equipamentos.items():
    print(chave, dados["tipo"], dados["bonus"])

    if dados["tipo"] == tipo:
        pesquisa.append(chave) 

    if loop == 0:
        maior = dados["bonus"]
        chave_maior = chave
    else:
        if dados["bonus"] > maior:
            maior = dados["bonus"]
            chave_maior = chave

    loop += 1

    if dados["tipo"] == "defesa":
        defesa += 1
        soma_bonus = soma_bonus + dados["bonus"]
    elif dados["tipo"] == "velocidade":
        velocidade +=1
    else:
        magia += 1


for chave_empate, dados_empate in equipamentos.items():
    if dados_empate["bonus"] == maior:
        bonus_igual.append(chave_empate)

if nome_equipamento in equipamentos:
        print("Atributos:", equipamentos[nome_equipamento])
else:
    print("O equipamento não existe.")

if len(bonus_igual) >= 2:
    print(f"Tem valores iguais. {bonus_igual}")
else:
    print(f"Sem valores iguais. {chave_maior} {maior}")

if pesquisa == []:
        print("Nehum item encontrado.")
else:
        print("Pesquisa por tipo:",pesquisa)


print(f"""
Soma bonus: {soma_bonus}
Maior bonus: {chave_maior} {maior}
Defesa: {defesa}
Velocidade: {velocidade}
Magia: {magia}

""")