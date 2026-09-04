# %%

numeros = [12, 45, 7, 89, 23, 56]
maior = 0

for i, num in enumerate(numeros):

    if i == 0:
        maior = num
    elif num > maior:
            maior = num

print(maior)
# %%
