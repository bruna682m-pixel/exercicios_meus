# %%
# minha
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}

novo_dict1 = dict1.copy()

for chave, valor in dict2.items():
    novo_dict1[chave] = novo_dict1.get(chave, 0) + valor

print(novo_dict1)

# %%
# site
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}

novo_dict1 = dict1.copy()

for chave, valor in dict2.items():
    novo_dict1[chave] = novo_dict1.get(chave, 0) + valor

print(novo_dict1)