# %%

lista = [120, "Python", 120.01, "asw", False, [10,20]]
elemento1 = 0

lista[-1] # elemento -1

# %%
lista[-1:] # elemento [-1:]

# %%
lista[0] # primeiro elemento

# %%
lista = [120, "Python", 120.01, "asw", False, [10,20]]
elemento1 = ""
palavra = []

for i, enu in enumerate(lista):
    if i == 1:
        elemento1 = enu

for letra in elemento1:
    palavra.append(letra)

print(palavra[-1])

# %%
lista[1][-1]
        
    



