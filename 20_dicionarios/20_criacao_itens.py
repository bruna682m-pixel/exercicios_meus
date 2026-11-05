# %%
materiais = {    
    "madeira": 6,    
    "ferro": 4,    
    "cristal": 2,    
    "ervas": 5
}
receitas = {    
    "espada": {"madeira": 1, "ferro": 2},    
    "pocao": {"ervas": 3, "cristal": 1},    
    "cajado": {"madeira": 2, "cristal": 2}
}

objeto_criar = input("Escolha um objeto para criar:")

for chave, valor in receitas.items():
    if objeto_criar in receitas:
        if valor[objeto_criar] == "espada":
            print(valor)

print(f"""
Materiais e quantidades: {materiais}
Receitas e quantidades: {receitas}

""")