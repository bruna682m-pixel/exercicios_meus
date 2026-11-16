# %%

expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
soma = 0

for chave, valor in expenses.items():
    soma = soma + valor

print("Total expenses: ", soma)
