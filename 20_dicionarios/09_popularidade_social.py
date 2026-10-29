# %%

perfis = {    
    "Lia": 120,    
    "Caio": 85,    
    "Bia": 120,    
    "Davi": 40,    
    "Noah": 200
}
chave_maior = 0 
chave = 0
loop = 0
maior = 0
mais_100_curtidas = []
soma = 0
media = 0
empate = []

nome = input("Digite o nome:")

if nome in perfis:
    print("Você esta cadastrado.")
else:
    print("Não está cadastrado.")

for chave, valor in perfis.items():
    if loop == 0:
        chave_maior = chave
        maior = valor
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave

    if valor > 100:
        mais_100_curtidas.append(chave)

    soma = soma + valor

media = soma / len(perfis)

for chave_empate, valor_empate in perfis.items():
    if maior == valor_empate:
        empate.append(chave)

if len(empate) == 1:
    print("Não houve empate.")
else:
    print("Houve empate.",empate)

print(f"""
Mais curtido: {maior}
Mais de 100 curtidas: {mais_100_curtidas}
Média: {media}
""")


    
