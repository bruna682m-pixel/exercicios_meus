# %%

espacos = 0

palavra = input("Digite uma palavra:")

for i in palavra:
    if i == " ":
        espacos += 1

print("Sua palavra tem",espacos,"espaços.")