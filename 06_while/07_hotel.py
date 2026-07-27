# %%
count = 20
opcao = 0

while count >= 20:
    opcao = input("""
1- Fazer reserva
2- Cancelar reserva
3- Consultar quartos livres
4- Encerrar sistema
""")
    opcao = int(opcao)

    if opcao == 1:
        if count > 20:
            print("Todos os quartos reservados.")
            break
        else:
            count = count - 1
    if opcao == 2:
        if count == 20:
            print("Voce não pode reservar. Quartos todos livres")
        else:
            count = count + 1
    if opcao == 3:
        print("Temos",count,"quartos livres")
    if opcao == 4:
        break

    
# %%
count = 20
opcao = 0

while count >= 0:
    opcao = input("""
1- Fazer reserva
2- Cancelar reserva
3- Consultar quartos livres
4- Encerrar sistema
""")
    opcao = int(opcao)
    print(opcao)
    print(count)
    if opcao == 1:
        if count >= 20:
            print("Todos os quartos reservados.")
        else:
            count = count - 1
    if opcao == 2:
        if count >= 20:
            print("Voce não pode cancelar"". Quartos todos livres")
        else:
            count = count + 1
    if opcao == 3:
        print("Temos",count,"quartos livres")
    if opcao == 4:
        print("Saindo")
        break

print("fora")
# %%
