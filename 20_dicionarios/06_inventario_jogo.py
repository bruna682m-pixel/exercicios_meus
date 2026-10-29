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

if escolha in inventario:
    valor = inventario[escolha]
    if valor > 0:
        inventario[escolha] -= 1
    else:
        print("Seus itens acabaram use outro.")
else:
    print("Este item não está no inventário.")

for valor in inventario.values():
    qtd_total = qtd_total  + valor  


print(f"""
Inventário: {inventario}
Total itens: {total_tipos}
Qtd total: {qtd_total}
""")