
# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
#compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
#escreva o custo total da compra.
# %%

qtd = input("Qual a quantidade de maças?")

qtd = int(qtd)
total = 0

if qtd < 12:
    total = qtd * 1.30
    print("Voce pegou",qtd,"maças. O custo total deu:",total)
else:
    total = qtd * 1
    print("Voce pegou",qtd,"maças. O custo total deu:",total)

# 7,11,14  
