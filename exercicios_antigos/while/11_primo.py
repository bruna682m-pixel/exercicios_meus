# Solicitar um número inteiro positivo ( consistir ) e mostrar se é ou não primo
# %%

numero = 3

numero = 2 %1 
print(numero)

numero = 2 % 2
print(numero)
count = 2

while numero % 1 == 0 and numero % 2 == 0 and numero % count == 0:
        print("è primo")
        count += 1

# %%
numero = int(input("Digite um número para ver se é primo."))
count = 2

while numero < 0:
    numero = int(input("Digite um número para ver se é primo."))

while numero % 1 == 0 and numero % 2 == 0 and numero % count == 0:
    print("è primo")
    count += 1
    
    

print("sai")
# %%
# %%
numero = int(input("Digite um número para ver se é primo."))
count = 2


while numero < 0:
    numero = int(input("Digite um número para ver se é primo."))

while count < numero:
    total = numero % count
    print(numero, "/" ,count ,total)
    count += 1
    if numero % count:
        print("Seu número é primo")
    else:
        print("Seu número não é primo")
    
    

print("sai",total)

# %%
numero = int(input("Digite um número para ver se é primo."))
count = 2
primo = True

while numero < 2:
    numero = int(input("Digite um número para ver se é primo."))

while count < numero:
    if numero % count == 0:
       primo = False
       break
    count += 1
    
if primo:
      print("Seu número é primo")
else:
      print("Seu número não é primo")



print("sai")
  
  

  


  


  
  

  


  


