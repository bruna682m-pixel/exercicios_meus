# %%
inventario = {
    "pocao": 3,
    "espada": 1,
    "moeda": 25,
    "chave": 2
}
total_tipos = len(inventario)
escolha = input("Escolha um item para usar:")

for chave, valor in inventario.items():
    if chave == escolha:
        if 
        inventario[chave] -= 1

qtd_total = qtd_total + valor

print(f"""
Inventário: {inventario}
Total itens: {total_tipos}

""")