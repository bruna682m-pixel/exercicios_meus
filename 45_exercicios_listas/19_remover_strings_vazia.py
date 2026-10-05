# %%

lista = ["Mike", "", "Emma", "Kelly", "", "Brad"]

print("Lista original:",lista)

for i, enu in enumerate(lista):
    if enu == "":
        lista.pop(i)

print("Lista sem espaços vazios", lista)

# %%
lista = ["Mike", "", "Emma", "Kelly", "", "Brad"]
alvo = ""

lista_alterada = [x for x in lista if x != alvo]

print("Lista sem espaços:",lista_alterada)

# %%
lista = ["Mike", "", "Emma", "Kelly", "", "Brad"]

lista_limpa = list(filter(None, lista))

print(f"Lista limpa: {lista_limpa}")

