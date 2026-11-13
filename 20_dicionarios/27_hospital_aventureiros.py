# %%
hospital = {    
    "Arin": {"vida": 35, "ferimentos": 2, "tratamento": "pendente"},    
    "Mira": {"vida": 70, "ferimentos": 1, "tratamento": "concluido"},    
    "Toren": {"vida": 10, "ferimentos": 4, "tratamento": "pendente"},    
    "Luna": {"vida": 90, "ferimentos": 0, "tratamento": "concluido"},    
    "Kael": {"vida": 45, "ferimentos": 3, "tratamento": "pendente"}
}
pendente = 0
concluido = 0
pendente_lista = []
menor = 0
chave_menor = 0
loop = 0
soma = 0
media = 0

print(hospital)

nome = input("Digite o nome do paciente para pesquisar:")
escolha_paciente = input("Digite um paciente para aumentar 20 de vida:")

if escolha_paciente in hospital:
    if hospital[escolha_paciente]["tratamento"] == "pendente":
        if hospital[escolha_paciente]["vida"] + 20 > 100:
            hospital[escolha_paciente]["vida"] = 100
            print(escolha_paciente,"recebeu +20 de vida")
            hospital[escolha_paciente]["tratamento"] = "concluido"
        else:
            hospital[escolha_paciente]["vida"] += 20
            hospital[escolha_paciente]["tratamento"] = "concluido"
    else:
        print("O status do tratamento deve ser pendente.")
else:
    print("O paciente não foi encontrado.")

if nome in hospital:
    print("O paciente foi encontrado:", hospital[nome])

    opcao = input("Deseja atualizar o tratamento de um paciente?")

    if opcao == "sim":
        status = input("Digite o tratamento do cliente:")
        if status == "pendente" or status == "concluido":
            hospital[nome]["tratamento"] = status
        else:
            print("Digite um status valido pendente ou concluido.")
    else:
        print("Você não atualizou nenhum cadastro.")
else:
    print("O paciente não foi encontrado.")


for chave, valor in hospital.items():
    if valor["tratamento"] == "pendente":
        pendente_lista.append(chave)
        pendente += 1
    else:
        concluido += 1

    if loop == 0:
        menor = valor["vida"]
        chave_menor =  chave
    else:
        if valor["vida"] < menor:
            menor = valor["vida"]
            chave_menor = chave
    loop += 1

    soma = soma + valor["vida"]

media = soma / len(hospital)



print(f"""
Menor: {chave_menor} {menor}
Média: {media}
Pendente lista: {pendente_lista}
Número de pendentes: {pendente}
Número de concluídos: {concluido}
Lista atualizada: {hospital}
""")
        
