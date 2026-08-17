# %%

palavra = input("Digite uma palavra:")
qtd = 0

for i in palavra:
    if i == "a":
        qtd +=1

print("A letra a aparece",qtd,"vezes.")
