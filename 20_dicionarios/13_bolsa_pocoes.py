# %%
pocoes = {
    "vida": 4,
    "mana": 2,
    "veneno": 3,
    "energia": 1
}
acabaram = []
total = 0

print(pocoes)

while True:
    escolha = input("Qual poção você quer usar ou digite sair para parar:")

    if escolha == "sair":
        print("Saindo.....")
        break

    if escolha in pocoes:
        if pocoes[escolha] > 0:
            pocoes[escolha] -= 1
            print("Você escolheu a poção.",escolha)
        else:
            print("As poções deste tipo acabaram.")
    else:
        print("Essa poção não existe.")

for chave, valor in pocoes.items():
    if valor == 0:
        acabaram.append(chave)
    else:
        total += valor

print(f"""
Poções: {pocoes}
Poções acabadas: {acabaram}
Total restante: {total}
""")
# %%
