# %%
original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

original_vazia = {}

for chave, valor in original.items():
    original_vazia.setdefault(valor, []).append(chave)
    

print(original_vazia)