# %%
# minha com dica
main = {"a": 1, "b": 2, "c": 3, "d": 4}
subset = {"a": 1, "c": 3}

par_main = main.items()
par_subset = subset.items()

conjunto_main = set(par_main)
conjunto_subset = set(par_subset)

subconjunto = conjunto_subset <= conjunto_main

print(subconjunto)

# %%
# site
main = {"a": 1, "b": 2, "c": 3, "d": 4}
subset = {"a": 1, "c": 3}

is_subset = subset.items() <= main.items()
print(is_subset)