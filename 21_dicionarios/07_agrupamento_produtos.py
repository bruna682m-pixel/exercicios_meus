# %%
produtos = [    ("Camisa", "Roupa"),    ("Calça", "Roupa"),    ("Notebook", "Eletrônico"),    ("Celular", "Eletrônico"),    ("Tênis", "Calçado"),    ("Meia", "Roupa"),    ("Tablet", "Eletrônico")]

agrupando_categoria = {}

for i in produtos:
   categoria = i[1]
   produto = i[0]
   agrupando_categoria.setdefault(categoria, []).append(produto)
   

print(agrupando_categoria)