# %%
# meu apos consulta
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 99, "c": 3}

conjunto_d1 = set(d1)
conjunto_d2 = set(d2)

interseccao = {k: d1[k] for k in conjunto_d1 & conjunto_d2 if d1[k] == d2[k]}

print(interseccao)

# %%
# site 
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 99, "c": 3}

intersection = {k: d1[k] for k in d1.keys() & d2.keys() if d1[k] == d2[k]}

print("Intersection:", intersection)