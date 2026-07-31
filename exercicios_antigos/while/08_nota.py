# %%
#Escrever um algoritmo que lê um valor em #Reais (R$) e calcule qual o menor número #possível de notas de 100, 50, 10, 5 e 1 em #que o valor lido pode ser decomposto. #Escrever o valor lido e a relação de notas #necessárias.

total = 0
resto = 0

valor_reais = input("Digite um valor em reais:")

valor_reais = float(valor_reais)

total = valor_reais // 100
resto = valor_reais % 100
print("total em notas de 100 = ",total)

total = resto // 50
resto = resto % 50
print("total em notas de 50 = ",total)

total = resto // 10
resto = resto % 10
print("total em notas de 10= ",total)

total = resto // 5
resto = resto % 5
print("total em notas de 5 = ",total)

total = resto // 1
resto = resto % 1
print("total em notas de 1 = ",total)

