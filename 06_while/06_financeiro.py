# %%
valores = 0
opcao = 0
total_gasto = 0
total_recebido = 0
total = 0

while True:
    valores = input("Digite valores")
    opcao = input("""
    1- Despesa
    2- Receita
    3- Sair
    """)

    opcao = int(opcao)
    valores = float(valores)

    if opcao == 3:
        break

    if opcao == 1:
        total_gasto = total_gasto - valores
    elif opcao == 2:
        total_recebido = total_recebido + valores

total = total_recebido - total_gasto

print("""
Recebido:""",total_recebido,"""
Gasto:""",total_gasto,"""
Saldo:""",total)



# %%
