# %%
total = 0
count = 0

while True:
    valores = input("Entre com os valores de depósito:")

    if valores == "":
        break

    valores = float(valores)    
    total = total + valores
    count += 1

print("Seu depósito deu:", total, "o loop rodou:", count)

