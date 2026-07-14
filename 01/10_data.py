dias = input("me diga os dia ")
horas = input("me diga as horas ")
minutos = input("me diga os minutos ")

dias = int(dias)
horas = int(horas)
minutos = int(minutos)

total_dias = dias * 1440
total_horas = horas * 60

total_tudo_minuto = total_dias + total_horas + minutos

print("voce digitou ", minutos, "minutos ")
print(dias, "em minutos fica ", total_dias)
print(horas, "em minutos fica ", total_horas)
print("o total de tudo em minutos fica ", total_tudo_minuto)
