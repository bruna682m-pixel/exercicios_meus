# %%
inventario = {
    "pocao": 3,
    "espada": 1,
    "moeda": 25,
    "chave": 2
}
qtd_total = 0

total_tipos = len(inventario)
escolha = input("Escolha um item para usar:")

for chave, valor in inventario.items():
    if escolha in inventario:
        if valor >= 1:
            inventario[chave] -= 1
        else:
            print("Seus itens acabaram use outro.")

    qtd_total = qtd_total + valor
else:
    print("Este item não está no inventário.")
    
print(f"""
Inventário: {inventario}
Total itens: {total_tipos}
Qtd total: {qtd_total}
""")