# %%
# minha
import copy
original = {"name": "Alice", "scores": [90, 85, 92]}

copia_rasa = original.copy()

print("Copia rasa:", copia_rasa)

copia_profunda = copy.deepcopy(original)

print("Copia profunda:", copia_profunda)

# %%
# site
import copy
original = {"name": "Alice", "scores": [90, 85, 92]}

raso = original.copy()
raso["scores"].append(100)
print("Copia rasa:",raso["scores"])
print("Dict original depois da adição: ", original["scores"])

print()

original = {"name": "Alice", "scores": [90, 85, 92]}

profunda = copy.deepcopy(original)
profunda["scores"].append(99)
print("Copia profunda:",profunda["scores"])
print("Dict original depois da adição: ", original["scores"])


