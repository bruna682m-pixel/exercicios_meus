# %%

numero_max = 10
classificacao1 = 0
classificacao2 = 0
classificacao3 = 0
classificacao4 = 0

for i in range(1, numero_max+1):
    nota = float(input("Digite a sua nota:"))

    if nota >= 0 and nota <= 4.9:
        classificacao1 += 1
    elif nota <= 6.9:
        classificacao2 += 1
    elif nota <= 8.9:
        classificacao3 += 1
    elif nota <= 10:
        classificacao4 += 1
    elif nota < 0 or nota > 10:
        print("Fora da classificão.")

print(f"""
Notas de 0 a 4.9: {classificacao1}
Notas de 5 a 6.9: {classificacao2}
Notas de 7 a 8.9: {classificacao3}
Notas de 9 a 10: {classificacao4}
""")
# %%
