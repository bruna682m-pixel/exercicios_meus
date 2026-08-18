import random

numero_pc = random.randint(1,5)
numero_max = 5

for i in range(1,numero_max+1):
  tentativa = int(input("Digite um número:"))
  
  if numero_pc > tentativa:
    print("é maior")
  elif numero_pc < tentativa:
    print("é menor")
  else:
    print("Você acertou.")
    break
    
else:
    print("Suas tentativas acabaram")
    
 
 
 