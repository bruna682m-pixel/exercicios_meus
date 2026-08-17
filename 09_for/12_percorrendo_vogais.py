# %%
palavra = input("Digite uma palavra:")
vogais = 0

for i in palavra:
    if i == "a":
        vogais += 1
    elif i == "e":
        vogais += 1
    elif i == "i":
        vogais += 1
    elif i == "o":
        vogais += 1
    elif i == "u":
        vogais += 1


print("Sua palavra tem",vogais,"vogais")

# %%
# usando in

palavra = input("Digite uma palavra:")
vogais = 0

for i in palavra:
    if i in "aeiou":
        vogais += 1
    
print("Sua palavra tem",vogais,"vogais")


