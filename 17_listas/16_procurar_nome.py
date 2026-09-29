# %%

nomes = ["Ana", "Bianca", "Carlos", "Fernanda"]

opcao_nome = input("Digite um nome:")

for i, enu in enumerate(nomes):
    if enu == opcao_nome:
        print("Nome encontrado. No índice:",i)
        break
else:
    print("Nome não encontrado.")



# %%
