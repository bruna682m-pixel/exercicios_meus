# %%

numero_max = 6
positivos = 0
zeros = 0 
negativos = 0

for i in range(1, numero_max+1):
    numero = float(input("Digite 6 números:"))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

print(f"""
Positivos:{positivos}
Negativos:{negativos}
Zeros:{zeros}
""")
# %%
