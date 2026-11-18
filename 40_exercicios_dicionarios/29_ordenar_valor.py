# %%
# minha
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}

ordenado = sorted(scores.values())

print(ordenado)

# %%
# minha apos resultado
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}

ordenado = sorted(scores.items(), key=lambda item: item[1])

print(ordenado)

# %%
# site
scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}

sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))

print(sorted_scores)