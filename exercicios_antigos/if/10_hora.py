# %%
# Dado um número inteiro de segundos, mostrar a quantas horas, minutos e segundos ele corresponde.

# %%
total = 0
resto = 0

total = 3660 // 3600
print("total hora",total)

resto = 3660 % 3600
print(resto)

total = resto // 60
print ("total min",total)

resto = resto % 60
print (resto)

# %%
total = 0
resto = 0

segundos_entrada = input("Digite o valor em segundos:")

segundos_entrada = int(segundos_entrada)

total = segundos_entrada // 3600
print("O total em horas é:",total)

resto = segundos_entrada % 3600
print(resto)

total = resto // 60
print("O total em minutos é:", total)

resto = resto % 60
print("O total em segundos é:",resto)

