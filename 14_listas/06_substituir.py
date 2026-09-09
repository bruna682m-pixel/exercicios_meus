# %%

numeros = [10, 20, 30, 40, 20, 50]

substituir = int(input("Digite um número para substituir:"))
novo_numero = int(input("Digite o novo número:"))

for i, num in enumerate(numeros):
    if num == substituir:
        numeros[i] = novo_numero
       

print(numeros)

# %%
