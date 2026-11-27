# %%
import copy
import json

por_categoria = {}
total_por_produto = {}

produtos = {
    "Mouse": {"categoria": "Periféricos", "estoque": 15, "preco": 50},
    "Teclado": {"categoria": "Periféricos", "estoque": 8, "preco": 120},
    "Monitor": {"categoria": "Monitores", "estoque": 5, "preco": 800},
    "Webcam": {"categoria": "Periféricos", "estoque": 12, "preco": 180},
    "Notebook": {"categoria": "Computadores", "estoque": 3, "preco": 3500},
    "Tablet": {"categoria": "Computadores", "estoque": 7, "preco": 1500}
}

vendas = {
    "Mouse": 4,
    "Teclado": 3,
    "Monitor": 2,
    "Webcam": 5,
    "Notebook": 1,
    "Tablet": 2
}

copia_profunda = copy.deepcopy(produtos)


for chave, valor in vendas.items():
    if chave in copia_profunda:
        copia_profunda[chave]["estoque"] -= valor


for produto, categoria in copia_profunda.items():
    por_categoria.setdefault(categoria["categoria"], []).append(produto)

    total_por_produto[produto] = vendas[produto] * categoria["preco"]


maior = max(total_por_produto, key=lambda chave: total_por_produto[chave])

ordenar_vendas = dict(sorted(total_por_produto.items(), key=lambda item: item[1], reverse=True))


dados_json = json.dumps(ordenar_vendas, indent=4)

print(f"""
Original: {produtos}
Copia profunda: {copia_profunda}
Produto por categoria: {por_categoria}
Total por produto: {total_por_produto}
Maior venda: {maior}
Ordenado produtos por vendas: {ordenar_vendas}
Dados em json: {dados_json}

""")



