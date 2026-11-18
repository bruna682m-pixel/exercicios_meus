# %%
# minha
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

conjunto_d1 = set(d1)
conjunto_d2 = set(d2)

semelhante = conjunto_d1 & conjunto_d2

print(semelhante)

# %%
# site
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

common_keys = d1.keys() & d2.keys()

print("Common keys:", common_keys)