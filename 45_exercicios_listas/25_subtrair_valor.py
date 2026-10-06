# %%
lista = [5, 10, 15, 20, 25]

for i, enu in enumerate(lista):
    if enu == 20: 
        lista[i] = 200

print(lista)

# %%
lista = [5, 10, 15, 20, 25]
alvo = 20
novo_valor = 200

if alvo in lista:
    index = lista.index(alvo)
    lista[index] = novo_valor

print(f"Lista modificada: {lista}")
