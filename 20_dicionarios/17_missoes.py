
# %%

missoes = {    
    "encontrar a chave": "pendente",    
    "derrotar o goblin": "concluida",    
    "resgatar o aldeao": "pendente",    
    "explorar a caverna": "em andamento",    
    "entregar o artefato": "concluida"
}


while True:
    print("1- Listar missões, 2- atualizar, 3- Listar por estado 4- sair")
    opcao = int(input("Digite uma opção."))

    if opcao == 1:
        print("Lista de missões.",missoes)

    elif opcao == 2:
        editar_missao = input("Digite a missão para alterar:")

        if editar_missao in missoes:
            estado = input("Digite o novo estado da missão:")
            if estado == "pendente" or estado == "em andamento" or estado == "concluida":
                missoes[editar_missao] = estado
                print("Estado da missão atualizado.",missoes)
            else:
                print("Estado invalido.")
        else:
            print("Missão não existe.")

    elif opcao == 3:
        total_pendente = 0
        total_concluido = 0
        total_em_andamento = 0

        pendente = {}
        concluido = {}
        em_andamento = {}

        print("Listando por estados.")
        
        for chave, valor in missoes.items():
            if valor == "pendente":
                pendente[chave] = valor
                total_pendente += 1
            elif valor == "concluida":
                concluido[chave] = valor
                total_concluido += 1
            else:
                em_andamento[chave] = valor
                total_em_andamento += 1

        if len(missoes) == len(concluido):
            print("Você concluiu todas as missões.")

        print(f"""
Pendente: {pendente} {total_pendente}
Em andamento: {em_andamento} {total_em_andamento}
Concluida: {concluido} {total_concluido}
""")

    elif opcao == 4:
        print("Saindo......")
        break

    else:
        print("Opção invalida.")

    

