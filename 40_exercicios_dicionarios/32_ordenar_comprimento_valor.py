# %%
# site
words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}

ordenado = dict(sorted(words.items(), key=lambda item: len(item[1])))

print(ordenado)