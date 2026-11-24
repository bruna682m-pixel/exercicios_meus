# %%
import json
livros = {    "101": {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},    "102": {"titulo": "O Cortiço", "autor": "Aluísio Azevedo"},    "103": {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector"}}

dados_json = json.dumps(livros, indent=4)

json_dicionario = json.loads(dados_json)

print(dados_json)
print(json_dicionario)
print("Titulo do segundo livro:", json_dicionario["102"]["titulo"])