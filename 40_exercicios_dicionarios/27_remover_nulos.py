# %%
data = {"name": "Alice", "age": None, "city": "Paris", "score": None}

dict_sem_none = {
    chave: valor 
    for chave, valor in data.items()
    if valor is not None
}

print(dict_sem_none)

# %%
# site
data = {"name": "Alice", "age": None, "city": "Paris", "score": None}

cleaned = {k: v for k, v in data.items() if v is not None}

print(cleaned)