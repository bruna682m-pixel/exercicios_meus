# %%

numero_max = 5
maior = 0
nome_maior = ""

for i in range(1, numero_max+1):
    nome = input("Digite seu nome:")
    nota = float(input("Digite sua nota:"))

    if i == 1:
        maior = nota
        nome_maior = nome
    else:
        if nota > maior:
            maior = nota
            nome_maior = nome

print("Maior nota:",maior)
print("Nome:",nome_maior)
        

    
