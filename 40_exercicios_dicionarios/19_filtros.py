# %%
scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}

filtro = {
    chave: valor 
    for chave, valor in scores.items()
    if valor > 60
}

print(filtro)

# %%
scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}

passing = {k: v for k, v in scores.items() if v > 60}
print(passing)