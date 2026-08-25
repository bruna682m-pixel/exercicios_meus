
# %%
candidato_a = 0
candidato_b = 0
candidato_c = 0
invalidos = 0
total_votos = 0

while True:
    opcao = int(input("""
    Digite uma opção:
    
    1- Candidato A
    2- Candidato B
    3- Candidato C
    0- Encerrar votação
    """))

    if opcao == 1:
        candidato_a += 1
        total_votos += 1
        print("Você votou no candidato A.")

    elif opcao == 2:
        candidato_b += 1
        total_votos += 1
        print("Você votou no candidato B.")

    elif opcao == 3:
        candidato_c += 1
        total_votos += 1
        print("Você votou no candidato C.")

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
        total_votos += 1
        invalidos += 1

if candidato_a == 0 and candidato_b == 0 and candidato_c == 0:
    print("Nenhum voto.")

elif candidato_a == candidato_b and candidato_a == candidato_c:
    print("Empate entre os 3 candidatos.")

elif candidato_a == candidato_b and candidato_a > candidato_c:
    print("Empate entre candidato A e candidato B.")
    
elif candidato_a == candidato_c and candidato_a > candidato_b:
    print("Emmpate entre candidato A e candidato C.")
elif candidato_b == candidato_c and candidato_b > candidato_a:
    print("Empate entre candidato B e candidato C")
           
elif candidato_a > candidato_b and candidato_a > candidato_c:
    print("candidato A venceu.")

elif candidato_b > candidato_a and candidato_b > candidato_c:
    print("candidato B venceu.")

else:
    print("Candidato C venceu.")
    
print(f"""
    Resultado

Total de votos: {total_votos}

Candidato A: {candidato_a}
Candidato B: {candidato_b}
Candidato C: {candidato_c}
Votos inválidos: {invalidos}

""")


