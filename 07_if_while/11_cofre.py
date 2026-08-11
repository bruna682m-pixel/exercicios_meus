# %%
senha = 0
tentativas = 3
count = 1

while True:
    if count == 1:
        senha = int(input("Configure uma senha."))

    opcao = int(input("Digite a senha:"))

    if opcao == senha:
        print("Senha correta.")
        break
    else:
        if tentativas <= 0:
            print("Suas tentativas acabaram.")
            break
        else:
            tentativas -= 1
            print("Senha incorreta. Faltam",tentativas,"tentativas.")

    count += 1
