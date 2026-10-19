# %%
estoque = {
    "Caderno": 10,
    "Caneta": 25,
    "Borracha": 8
}

estoque_atualizar = input("Qual produto você quer atualizar:")

if estoque_atualizar in estoque:
    quantidade =  int(input("Digite a nova quantidade do produto:"))

    if quantidade > 0:
        estoque[estoque_atualizar] = quantidade
    else:
        print("Quantidade negativa.")
else:
    print("Produto não existe.")

print(estoque)