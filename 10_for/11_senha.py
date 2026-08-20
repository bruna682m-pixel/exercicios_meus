# %%

senha_correta = "python123"
numero_max = 3

for i in range(1, numero_max+1):
    senha = input("Digite sua senha:")

    if senha_correta == senha:
        print("Senha correta!")
        break

else:
    print("Conta bloqueada.")
    