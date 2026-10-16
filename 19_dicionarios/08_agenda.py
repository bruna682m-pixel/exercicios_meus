# %%
contatos = {
    "Ana": "11955555555",
    "Bianca": "11911111111",
    "Carlos": "11922222222",
             
    }

while True:
    opcao_menu = int(input("""Escolha uma opção do menu:
    1- Adicionar um contato
    2- Consultar contato
    3- Fechar
    """))

    if opcao_menu == 1:
        chave_nome = input("Digite o nome do novo contato:")
        contatos[chave_nome] = input("Digite número do contato:")
        print("Contato adicionada:",contatos)
    elif opcao_menu == 2:
        nome = input("Digite o nome do contato para pesquisar:")

        if nome in contatos:
            print(contatos[nome])
        else:
             print("Este contato não existe")
    elif opcao_menu == 3:
        print("Fechando...")
        break
    else:
        print("Opção invalida.")

