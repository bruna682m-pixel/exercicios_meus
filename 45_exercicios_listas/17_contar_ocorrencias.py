# %%
# minha solução
lista = [10, 20, 30, 10, 40, 10, 50]
alvo = 0

for i in lista:
    if i == 10:
        alvo += 1

print(f"O número 10 apareceu {alvo} vezes")

# %%
# solução proposta
lista = [10, 20, 30, 10, 40, 10, 50]
alvo = 10

ocorrencia = lista.count(alvo)

print(f"O número {alvo} apareceu {ocorrencia} vezes")