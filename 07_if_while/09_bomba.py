# %%
import random

tentativas = 5
codigo_secreto = random.randint(1000,9999)

while True:
    opcao = int(input("Digite o código secreto:"))

    if opcao == codigo_secreto:
        print("Bomba desarmada.")
        break

    tentativas -= 1

    if tentativas == 0:
        print("Suas tentativas acabaram.")
        break
    else:
        print("Restam",tentativas,"tentativas")
   

   