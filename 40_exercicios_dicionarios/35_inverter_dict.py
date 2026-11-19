# %%
original = {"a": 1, "b": 2, "c": 3}

inverso = {
    valor: chave
    for chave, valor in original.items()
}

print(inverso)

# %%
original = {"a": 1, "b": 2, "c": 3}

invertido = {v: k for k, v in original.items()}

print(invertido)