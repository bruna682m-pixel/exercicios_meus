# %%
produtos = {    
    "P01": 
        {"nome": "Teclado", "preco": 120, "quantidade": 4},    
    "P02": 
        {"nome": "Mouse", "preco": 60, "quantidade": 10},    
    "P03": 
        {"nome": "Monitor", "preco": 800, "quantidade": 2},    
    "P04": 
        {"nome": "Webcam", "preco": 150, "quantidade": 0}}

valor_cada_produto = 0
total_estoque = 0
loop = 0
chave_maior = 0
maior = 0

for chave, dados in produtos.items():
    print(dados["nome"])
    print(dados["quantidade"])

    if dados["quantidade"] == 0:
        print("Sem estoque.")

    valor_cada_produto = dados["preco"] * dados["quantidade"]  
    print(f"Valor cada produto:{valor_cada_produto}")  

    total_estoque = total_estoque + valor_cada_produto 
    
    if loop == 0:
        maior = valor_cada_produto
        chave_maior = dados["nome"]
    else:
        if valor_cada_produto > maior:
            maior = valor_cada_produto
            chave_maior = dados["nome"]

    loop += 1

print(f"""
Total estoque: {total_estoque}
Maior valor no estoque: {chave_maior} {maior}
""")
