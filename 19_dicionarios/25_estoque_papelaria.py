# %%
estoque = {
    "Lapis": 12,
    "Caneta": 5,
    "Caderno": 0,
    "Borracha": 8,
    "Regua": 3
}

sem_estoque = []
reposicao = []
loop = 0
maior = 0
chave_maior = 0
soma = 0

for chave, valor in estoque.items():
    if valor == 0:
        sem_estoque.append(chave)

    if valor < 6:
        reposicao.append(chave)

    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave

    loop += 1

    soma = soma + valor

produto = input("Digite o produto para pesquisar: ")

if produto in estoque:
    print("Seu produto está no estoque.")
else:
    print("Não está no estoque.")

print(f"""
Estoque: {estoque}
Sem estoque: {sem_estoque}
Reposição: {reposicao}
Maior: {chave_maior, maior}
Soma: {soma}
""")

