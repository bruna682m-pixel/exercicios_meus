# %%

lista = ["Mike", "", "Emma", "Kelly", "", "Brad"]
lista_sem_espacos = []

print("Lista original:",lista)

for i, enu in enumerate(lista):
    if enu != "":
        lista_sem_espacos.append(enu)
        
print("Lista sem espaços vazios", lista_sem_espacos)

# %%
lista = ["Mike", "", "Emma", "Kelly", "", "Brad"]
alvo = ""

lista_alterada = [x for x in lista if x != alvo]

print("Lista sem espaços:",lista_alterada)

# %%
lista = ["Mike", "", "Emma", "Kelly", "", "Brad"]

lista_limpa = list(filter(None, lista))

print(f"Lista limpa: {lista_limpa}")

