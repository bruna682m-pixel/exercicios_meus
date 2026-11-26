# %%
import json
import copy
livros = [    ("Dom Casmurro", "Machado de Assis", "Romance"),    ("O Alienista", "Machado de Assis", "Conto"),    ("O Cortiço", "Aluísio Azevedo", "Romance"),    ("A Hora da Estrela", "Clarice Lispector", "Romance"),    ("Vidas Secas", "Graciliano Ramos", "Romance"),    ("O Ateneu", "Raul Pompeia", "Romance")]

biblioteca = {}
agrupados = {}


for titulo, autor, genero in livros:
    biblioteca[titulo] = {
        "autor": autor,
        "genero": genero
    }

for chave, valor in biblioteca.items():
   agrupados.setdefault(valor["genero"], []).append(chave)

for genero, lista_livros in agrupados.items():
    qtd = len(lista_livros)
    print(f"Gênero: {genero} | Qtd de livros: {qtd}")

ordenado = dict(sorted(agrupados.items(), key=lambda item: len(item[1])))

dados_json = json.dumps(ordenado, indent=4)

profunda = copy.deepcopy(ordenado)

profunda["Conto"].append(100)

print(f"""
Lista convertida para dict: {biblioteca}
Agrupado por gênero: {agrupados}
Ordenado gênero por qtd: {ordenado}
Resultado de gênero por qtd em json: {dados_json}
Original: {ordenado}
Copia_profunda: {profunda}

""")

