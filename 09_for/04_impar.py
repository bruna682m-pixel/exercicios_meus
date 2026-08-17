# %%

numero = 2
numero_max = 20

for i in range(1, numero_max+1):
    if i % numero == 1:
        print("números impares",i)

# %%
numero = 2
numero_max = 20

for i in range(1, numero_max+1):
    if i % 2 != 0: # forma conceitual
        print("números impares",i)