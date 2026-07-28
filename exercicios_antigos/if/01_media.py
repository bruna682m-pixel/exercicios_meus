# %%
# 1)Solicitar duas notas para o cálculo da média , mostrar a média e se a média for Maior ou igual a 6,
#mostrar “Aprovado”, caso contrário mostrar “Reprovado”.

nota1 = input("Digite a nota 1")
nota2 = input("Digite a nota 2")

nota1 = float(nota1)
nota2 = float(nota2)

soma_media = nota1 + nota2 

media = soma_media / 2

if media >= 6:
    print("Aprovado", media)
else:
    print("Reprovado", media)




# %%
