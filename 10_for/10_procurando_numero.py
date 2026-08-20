# %%
numero_lista = [4, 8, 25, 26, 23, 42]
numero = int(input("Digite um número:"))

for i in numero_lista:
    if i == numero:
        print("Número encontrado.")
        break
else:
    print("Número não encontrado")
        

