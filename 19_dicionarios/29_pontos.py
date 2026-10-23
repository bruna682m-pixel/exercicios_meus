# %%
# dicionário vazio
pontos = {}

# %%
# criando dicionário
pontos = {
    "Ana": 100,
    "Bia": 50,
    "Caio": 300
}

pontos["Duda"] = 101 #adicionar novo par de chave/valor se não existir é adicionado se já existir é substituído

print(pontos)

# %%
pontos = {
    "Ana": 100,
    "Bia": 50,
    "Caio": 300
}

nome = input("Digite seu nome:")

# impedir cadastro de chave repertida
if nome not in pontos:
    ponto = int(input("Digite os pontos:"))
    pontos[nome] = ponto
else:
    print("Já cadastrado.")

print(pontos)

# %%
# retornando apenas o valor de uma chave
pontos_duda = pontos["Duda"]
print(pontos_duda)

# %%
# usando get para caso a chave não existir retornar none em vez de keyerror
print(pontos.get("Duda"))

# %%
# se chave está no dicionário
if "Caio" in pontos:
    print("Está.")
else:
    print("Não está")

# %%
# se chave não existe no dicionário
if "Caio" not in pontos:
    print("Não está.")
else:
    print("Está")

# %%
# retornar as chaves
print("Chaves:", pontos.keys())

# %%
# percorrer chaves com keys
for chave in pontos.keys():
    print(chave)

# %%
# percorrer chaves
for chave in pontos:
    print(chave)

# %%
# retornar apenas as chaves
print(pontos.values())

# %%
# atualizar chave se existir se não cria uma nova
pontos["Bia"] = 70

# %%
# retornar chave_valor items retorna o par
print("Items:", pontos.items())

# %%
# deletar chave/valor
del pontos["Bia"]

# %%
print(pontos)

# %%
# remover chave e colocar valor em uma variavel
valor_removido = pontos.pop("Bia")

# %%
print(pontos)
print(valor_removido)

# %%
# remover todas as chaves/valor do dicionário
pontos.clear()

# %%
# atualizar ou adicionar chaves/valores de 2 ou mais de uma vez
pontos.update({
    "Bia": 80,
    "Edu": 10
})

# %%
# qtd de pares chave/valor
qtd = len(pontos)
print(qtd)

# %%
# percorrer chaves
for chave in pontos:
    print(chave)

# %%
# percorrer valor
for valor in pontos.values():
    print(valor)

# %%
# percorrer chave/valor
for chave, valor in pontos.items():
    print(chave, valor)

# %% 
# dicioário aninhado
produtos = {
    "P001": {
        "nome": "Caderno",
        "preco": 15.50,
        "estoque": 10
    },
    "P002": {
        "nome": "Caneta",
        "preco": 2.50,
        "estoque": 30
    }
}

# %%
# acessar preço
print(produtos["P001"]["preco"]) 

# %%
# percorrer dicionário aninhado
for codigo, dados in produtos.items():
    print(codigo, dados["nome"], dados["preco"])

# %%
produtos["P001"]["estoque"] = 8

# %%
print(produtos)

# %%
# pesquisar produto pelo nome dentro de um dicionário 
for codigo, dados in produtos.items():
    if dados["nome"] == "Caderno":
        print(codigo, dados)