# %%
# minha
data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}

maior = max(data, key=lambda comida: len(data[comida]))

print(maior)

# %%
# site
data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}

longest_key = max(data.items(), key=lambda item: len(item[1]))[0]

print(longest_key)