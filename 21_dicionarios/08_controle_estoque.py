# %%
estoque_atual = {    "Mouse": 10,    "Teclado": 5,    "Monitor": 3}
novas_entregas = {    "Mouse": 5,    "Teclado": 8,    "Fone": 12,    "Monitor": 2}
loop = 0
maior = 0
chave_maior = 0

copia_estoque = estoque_atual.copy()

print("Copia de estoque:",copia_estoque)

for chave, valor in novas_entregas.items():
    print("Percorrendo novas entregas: ", chave, valor)

    copia_estoque[chave] = copia_estoque.get(chave, 0) + valor

print("soma das qtd de produto que já existem: ", copia_estoque)

for chave_cadastro, valor_cadastro in copia_estoque.items():
    if chave_cadastro not in estoque_atual:
        estoque_atual[chave_cadastro] = valor_cadastro

    if loop == 0:
        maior = valor_cadastro
        chave_maior = chave_cadastro
    else:
        if valor_cadastro > maior:
            maior = valor_cadastro
            chave_maior = chave_cadastro
    loop += 1

maior_lambda = max(estoque_atual, key=lambda chave: estoque_atual[chave])    

print("Maior estoque:", chave_maior, maior)
print("Estoque atualizado:", estoque_atual)
print("Maior com lambda:", maior_lambda, estoque_atual[maior_lambda])











