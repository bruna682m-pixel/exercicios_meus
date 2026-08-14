# %%

import random # importando random

numero_pc = random.randint(1, 10) # variavel com número sorteado pelo pc sorteia 1 vez por loop
tentativas = 0 # contando as tentativas

while True: # loop 
    numero = int(input("Digite um número: ")) # pedindo um número

    tentativas += 1 # contando as tentativas 

    if numero > numero_pc: # se número for maior que o número que o pc sorteou e imprime uma dica
        print("O número secreto é menor.")

    elif numero < numero_pc: # se número for menor que o do pc imprime dica
        print("O número secreto é maior.")

    else:
        print("Acertou!") # se o as condições acima forem falsas vem p/ cá e a pessoa acertou
        break

    if tentativas >= 5: # se passar de 5 tentativas encerra o programa
        print("Você perdeu.")
        break

print("Tentativas:", tentativas) # mostra tentativas
print("Número secreto:", numero_pc) # aqui está o erro está imprimindo o número que a pessoa digita não o número segreto

# em vez de print("Número secreto:", numero) fica print("Número secreto:", numero_pc)