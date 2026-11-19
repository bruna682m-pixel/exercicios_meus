# %%
# minha
data = {"a": 1, "b": 2, "c": 3, "d": 2}
unicos = False

valores = data.values()

valores_set = set(valores)

if len(valores_set) == len(data):
    unicos = True

print("Apenas valores unicos:", unicos)

# %%
# site
data = {"a": 1, "b": 2, "c": 3, "d": 2}

values = list(data.values())
is_unique = len(values) == len(set(values))

print(is_unique)