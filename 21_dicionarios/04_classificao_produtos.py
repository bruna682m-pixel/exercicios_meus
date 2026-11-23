# %%
produtos = {
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 900,
    "Fone": 120,
    "Webcam": 200
}

por_nome = dict(sorted(produtos.items()))
menor_maior = dict(sorted(produtos.items(), key=lambda item: item[1]))
maior_menor = dict(sorted(produtos.items(), key=lambda item: item[1], reverse=True))

print(f"""
Ordenado por nome: {por_nome}
Do menor para maior {menor_maior}
Do maior para menor: {maior_menor}
""")