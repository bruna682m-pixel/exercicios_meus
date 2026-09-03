# %%
import random
soma = 0
maior = 0
dado1 = 0
dado2 = 0
dado3 = 0
dado4 = 0
dado5 = 0
dado6 = 0

for i in range(1, 7):
    numero_dado = random.randint(1,6)

    if numero_dado == 1:
        dado1 += 1
    elif numero_dado == 2:
        dado2 += 1
    elif numero_dado == 3:
        dado3 += 1
    elif numero_dado == 4:
        dado4 += 1
    elif numero_dado == 5:
        dado5 += 1
    else:
        dado6 += 1

    soma = soma + numero_dado

    if i == 1:
        maior = numero_dado
    else:
        if numero_dado > maior:
            maior = numero_dado

print(f"""
1: {dado1}
2: {dado2}
3: {dado3}
4: {dado4}
5: {dado5}
6: {dado6}
Soma: {soma}
Maior: {maior}
""")    
        


# %%
