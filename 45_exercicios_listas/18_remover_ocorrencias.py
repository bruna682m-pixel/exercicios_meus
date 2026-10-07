# %%
# Minha solução
lista = [5, 20, 15, 20, 25, 50, 20]
alvo = 20
lista_sem_20 = []

print("Lista original", lista)

for i, enu in enumerate(lista):
    if enu != alvo:
        lista_sem_20.append(enu)

print(f"Lista alterada: {lista_sem_20}")

# %%
# solução proposta
lista = [5, 20, 15, 20, 25, 50, 20]
alvo = 20

lista_limpa = [x for x in lista if x != alvo]

print(f"Lista limpa: {lista_limpa}")



