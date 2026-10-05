# %%
print("Solução minha.")

lista = [23, 65, 19, 90]
aux = 0

print(f"Lista original: {lista}")

for i, enu in enumerate(lista):
    if i == 0:
        aux = enu

    if i == 2:
        lista[0] = enu
        lista[2] = aux


print(f"Lista trocada: {lista}")

# %%
# Solução sugerida
lista = [23, 65, 19, 90]
idx1, idx2 = 0, 2

print(f"Lista original", lista)

lista[idx1] , lista[idx2] = lista[idx2], lista[idx1]

print(f"Trocada: {lista}")