# %%
funcionarios = [
    ("Ana", 2500),
    ("Carlos", 3200),
    ("Mariana", 2800),
    ("Pedro", 3000)
]

dicionario_funcionarios = dict(funcionarios)

print("Lista convertida para dict: ", dicionario_funcionarios)

nome_pesquisa = input("Digite um nome para pesquisar:")

if nome_pesquisa in dicionario_funcionarios:
    print("Funcionário encontrado: ", nome_pesquisa, dicionario_funcionarios[nome_pesquisa])
else:
    print("Funcionário não encontrado.")


