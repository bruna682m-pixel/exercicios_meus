# %%
lista = [10, 20, 10, 30, 40, 40, 20, 50]

lista_unica = list(dict.fromkeys(lista))

print(f"Lista limpa: {lista_unica}")