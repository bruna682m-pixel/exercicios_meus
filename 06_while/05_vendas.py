# %%
faturamento = 0
mais_caro = 0
mais_caro_nome = 0
qtd = 0
total = 0
count = 1

while True:
    nome = input("Digite o nome do produto:")

    if nome == "fim":
        break    

    preco = input("Digite o preco do produto?")
    qtd = input("Digite qual a quantidade do produto que voce quer:")

    preco = float(preco)
    qtd = float(qtd)
    
    total = preco * qtd
    faturamento = faturamento + total

    if count == 1:
        mais_caro = preco
        mais_caro_nome = nome

    if preco > mais_caro:
        mais_caro = preco
        mais_caro_nome = nome

    count = count + 1

print("""
Faturamento:""",faturamento,"""
Produto mais caro:
""", mais_caro_nome, """R$""", mais_caro, """
Quantidade vendas:""", qtd)






# %%
