# %%
estoque = {
    "Teclado": 8,
    "Mouse": 3,
    "Monitor": 0,
    "Headset": 5,
    "Webcam": 0
}

sem_estoque = []
menos_5 = []
qtd_total = 0
qtd_produtos = 0
pelo_menos_1 = True

for chave, valor in estoque.items():
    if valor == 0:
        sem_estoque.append(chave)

    if valor < 5:
        menos_5.append(chave)

    if valor == 0:
        pelo_menos_1 = False

    qtd_total = qtd_total + valor
qtd_produtos = len(estoque)

print(f"""
Sem estoque: {sem_estoque}
Menos de 5: {menos_5}
Qtd total no estoque: {qtd_total}
Qtd de produtos: {qtd_produtos}
Pelo menos 1: {pelo_menos_1}
""")