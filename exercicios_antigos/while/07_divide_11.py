# %%
# 7-Escreva um algoritmo que gere o números de 1000 a 1999 e escreva aqueles que dividido por 11
#dão resto igual a 5.

numero = 1000

while numero <= 1999:
    if numero % 11 == 5:
        print("este tem resto 5",numero)
    numero += 1

print("sai")


