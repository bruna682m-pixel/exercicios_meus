# %%
scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}

alto = max(scores, key=scores.get)

print("Alto: ", alto)

best_score = max(scores.values())
all_top = [k for k, v in scores.items() if v == best_score]
print("All top scorers:", all_top)

# %%
scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}

loop = 0
maior = 0
chave_maior = 0

for chave, valor in scores.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave
    loop += 1

print("Maior scores: ", chave_maior)