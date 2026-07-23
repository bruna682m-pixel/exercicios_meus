# %%
conta = 0

hora_entrada = input("Digite a sua hora de entrada")
hora_saida = input("Digite a sua hora de saida")
hora_entrada = int(hora_entrada)
hora_saida = int(hora_saida)

total = hora_saida - hora_entrada

if total < 0:
    total = (24 - hora_entrada) + hora_saida


if total <= 2:
    conta = 15
    print(conta)
elif total <= 5:
    conta = 25
else:
    conta = 40

print("Sua conta deu:", conta, "voce ficou", total, "horas")

# %%
