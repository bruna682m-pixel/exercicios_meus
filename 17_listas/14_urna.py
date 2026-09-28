# %%

candidato = ["candidato A", "candidato B", "candidato C"]

escolha = int(input("Digite o índice do candidato para votar"))

candidato_a = 0
candidato_b = 0
candidato_c = 0


if escolha >= 0 and escolha <= len(candidato) -1:
    if escolha == 0:
        candidato_a += 1
    elif escolha == 1:
        candidato_b += 1
    elif escolha == 2:
        candidato_c += 1
    else:
        print("Escolha invalida.")






