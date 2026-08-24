# %%

palavra = input("Digite uma palavra:")
letra = input("Digite uma letra:")

for i in palavra:
    if i == letra:
        break
    else:
        print(i)