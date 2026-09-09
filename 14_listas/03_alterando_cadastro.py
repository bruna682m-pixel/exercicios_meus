# %%

nomes = ["ana", "bianca", "carlos", "daniel", "eduardo"]

remover = int(input("Qual posição você deseja alterar?"))

novo_nome = input("Qual será o novo nome?")

nomes.pop(remover)
nomes[remover].append(novo_nome)
print(nomes)

# %%
nomes = ["ana", "bianca", "carlos", "daniel", "eduardo"]

remover = int(input("Qual posição você deseja alterar?"))

novo_nome = input("Qual será o novo nome?")

nomes.pop(remover)
nomes.insert(remover, novo_nome)
print(nomes)