# %%
missoes = {    
    "coletar madeira": {"recompensa": 50, "status": "pendente"},    
    "derrotar orc": {"recompensa": 100, "status": "pendente"},    
    "encontrar tesouro": {"recompensa": 200, "status": "concluida"},    
    "salvar aldeao": {"recompensa": 150, "status": "em andamento"}
}
pendente = 0
concluida = 0
em_andamento = 0
maior = 0
chave_maior = 0
loop = 0

while True:
    opcao_menu = int(input("Digite a opção:"))

    if opcao_menu == 1:
        print("Listando missões:")
        print(missoes)

    elif opcao_menu == 2:
        nome_missao = input("Digite o nome da missão:")

        if nome_missao in missoes:
            alterar_status = input("Digite o novo status:")
            if alterar_status == "pendente" or alterar_status == "em andamento" or alterar_status == "concluida":
                missoes[nome_missao]["status"] = alterar_status
                print("Você alterou status da missão.",missoes[nome_missao])
            else:
                print("Digite um dos 3 status.")
        else:
            print("Missão não encontrada.")

    elif opcao_menu == 3:
        consultar_missao = input("Digite o nome da missão para consultar:")

        if consultar_missao in missoes:
            print("Missão encontrada.", missoes[consultar_missao])
        else:
            print("Missão não encontrada.")

    elif opcao_menu == 4:
        pendente = 0
        concluida = 0
        em_andamento = 0
        soma = 0

        for chave, valor in missoes.items():
            if valor["status"] == "pendente":
                pendente += 1
            elif valor["status"] == "em andamento":
                em_andamento += 1
            elif valor["status"] == "concluida":
                concluida += 1
                soma = soma + valor["recompensa"]


        print(f"""
Pendente: {pendente}
Em andamento: {em_andamento}
Concluida: {concluida}
Soma recompensas concluidas: {soma}
""")

    elif opcao_menu == 5:
        maior = 0
        chave_maior = 0
        loop = 0

        for chave_ma, valor_maior in missoes.items():
            if loop == 0:
                maior = valor_maior["recompensa"]
                chave_maior =  chave_ma
            else:
                if valor_maior["recompensa"] > maior:
                    maior = valor_maior["recompensa"]
                    chave_maior = chave_ma  
            loop += 1

        print("Maior:",chave_maior, maior)

    elif opcao_menu == 6:
        print("Saindo...")
        break

    else:
        print("Opção invalida.")


    
