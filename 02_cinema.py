# %%
texto = input (""" Selecione seu tipo de ingresso:
(1) meia entrada
(2) Interira

""")

idade = input("Digite a sua idade? ")
idade = int(idade)
conta = 0
conta = float(conta)

if idade <= 12:
    if texto == "1":
        conta = 15/2
        texto = "Meia"
    elif texto == "2":
        conta = 15
        texto = "inteira"
    else:
        print("Digite uma opçaõ de entrada certa")
elif idade >= 13 and idade <= 59:
    if texto == "1":
        conta = 30/2
        texto = "Meia"
    elif texto == "2":
        conta = 30
        texto = "Inteira"
    else:
        print("Digite uma opçaõ de entrada certa")
elif idade > 59:
    if texto == "1":
        conta = 20/2
        texto = "meia"
    elif texto == "2":
        conta = 20
        texto = "inteira"
    else:
        print("Digite uma opçaõ de entrada certa")
else:
    print("digite uma idade certa.")

print("Sua idade é", idade, "voce escolheu", texto, "sua conta deu:", conta)
# %%
