# %%

import random
numero_pc = random.randint(1,10)
palpites_lista = []
primeira_tentativa = 0
ultima_tentativa = 0
inversa = 0

for i in range(1, 6):
    palpite = int(input("Digite seu palpite:"))

    palpites_lista.append(palpite)

    print("Tentativas realizadas",palpites_lista)

    if palpite == numero_pc:
        print("Acertou. Foram", len(palpites_lista), "tentativas")
        break
    elif palpite > numero_pc:
        print("Chute alto.")
    elif palpite < numero_pc:
        print("Chute baixo.")
else:
    print("Acabou suas tentativas.")

primeira_tentativa = palpites_lista[0]
ultima_tentativa = palpites_lista[-1]
inversa = palpites_lista[::-1]

print(f"""
Primeira tentativa: {primeira_tentativa}
última tentativa: {ultima_tentativa}
Tentativas em ordem inversa: {inversa}
""")
