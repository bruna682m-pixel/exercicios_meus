# %%
a = 0
e = 0
i = 0
o = 0
u = 0

palavra = input("Digite uma palavra:")

for letra in palavra:

    if letra == "a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra == "u":
        u += 1

print(f"""
A:{a}
E:{e}
I:{i}
O:{o}
U:{u}
""")