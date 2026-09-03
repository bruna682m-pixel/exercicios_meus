# %%

import random
soma_pc = 0
soma_jogador = 0
numero_jogador = 0

for i in range(1, 7):
    numero_pc = random.randint(1,6)
    numero_jogador = random.randint(1,6)

    soma_pc = soma_pc + numero_pc
    soma_jogador = soma_jogador + numero_jogador

if soma_pc > soma_jogador:
    print("A maquina ganhou.")
elif soma_pc == soma_jogador:
    print("Empate.")
else:
    print("Você ganhou.")

print(f"""
Soma PC: {soma_pc}
Sua soma: {soma_jogador}
""")    
        


# %%
