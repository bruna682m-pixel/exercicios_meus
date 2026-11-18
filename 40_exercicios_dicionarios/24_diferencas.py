# %%
# minha

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 40}

conjunto_d1 = set(d1)
conjunto_d2 = set(d2)

diferencas = conjunto_d1 - conjunto_d2

print(diferencas)

# %%
# site
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 40}

only_in_d1 = d1.keys() - d2.keys()

print("Keys only in d1:", only_in_d1)