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

for chave, valor in produtos.items():
    for chave_externo, valor_externo in valor.items():
       
