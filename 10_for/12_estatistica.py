# %%

numero_max = 5
aprovados = 0
reprovados = 0
maior = 0
menor = 0
media = 0
soma = 0
nome_maior = ""

for i in range(1, numero_max+1):
    nota = float(input("Digite sua nota:"))
    nome = input("Digite seu nome:")

    if nota >= 5:
        aprovados += 1
    else:
        reprovados +=1

    soma = soma + nota
    media = soma / numero_max

    if i == 1:
        maior = nota
        menor = nota
        nome_maior = nome
    else:
        if nota > maior:
            maior = nota
            nome_maior = nome

        if nota < menor:
            menor = nota

print(f"""
Aprovados:{aprovados}
Reprovados:{reprovados}
Maior nota:{maior}
Menor nota: {menor}
Média da turma:{media}

""")
    