# %%

numeros = [5, -3, 0, 8, -10, 0, 7, -2]
negativos = 0
zeros = 0
positivos = 0

for i in numeros:
    if i < 0:
        negativos += 1
    elif i > 0:
        positivos += 1
    else:
        zeros += 1

print(f"""
Posítivos: {positivos}
Negatívos: {negativos}
Zeros: {zeros}
""")