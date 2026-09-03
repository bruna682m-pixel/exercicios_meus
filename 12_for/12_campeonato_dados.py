# %%
import random

vencedor = ""

while True:
    vitorias_pc = 0
    vitorias_jogador = 0
    empate = 0
    
    for i in range(1, 6): 
        numero_dado_pc = random.randint(1,6)
        numero_dado_jogador = random.randint(1,6)

        print(f"""
Jogador: {numero_dado_jogador}
Computador: {numero_dado_pc}
""")

        if numero_dado_jogador > numero_dado_pc:
            print("Você ganhou a rodada.")
            vitorias_jogador +=1
        elif numero_dado_pc == numero_dado_jogador:
            print("Empate na rodada.")
            empate += 1
        else:
            print("O computador ganhou a rodada.")
            vitorias_pc += 1

    if vitorias_pc > vitorias_jogador:
        vencedor = "Computador"
    elif vitorias_pc == vitorias_jogador:
        vencedor = "Empate"
    else:
        vencedor = "Jogador"

    print(f"""
    ===== RESULTADO =====

Vitórias do jogador: {vitorias_jogador}
Vitórias do computador: {vitorias_pc}
Empates: {empate}
Campeão: {vencedor}
""")

    opcao = int(input("Jogar de novo: 1- sim - 2- não"))

    if opcao == 1:
        print("voltando...")
    elif opcao == 2:
        print("Saindo...")
        break
    else:
        print("Opção invalida.")






# %%
