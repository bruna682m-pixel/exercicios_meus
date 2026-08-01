#%%
# Solicitar um número inteiro positivo ( consistir ), calcular o fatorial e mostrar

numero = input("Digite um número para calcular o fatorial")
numero = int(numero)

total = 0
count = 1
copia_total = 0
total = copia_total


while count <= numero:
    if numero >= 1:
        total = numero * count
        print("o fatorial do numero",numero,"x",count,"=",total)
        count += 1
        print(total)

print("sai", copia_total)


# %%
total = 0
count = 0
resultado = 0

while count <= 3:
    total = 3 * 3
    print("o fatorial do numero",3,"x",2,"=",total)
    count += 1

print("sai",resultado)
# %%
#%%
# Solicitar um número inteiro positivo ( consistir ), calcular o fatorial e mostrar

#%%
# Solicitar um número inteiro positivo ( consistir ), calcular o fatorial e mostrar

numero = input("Digite um número para calcular o fatorial")
numero = int(numero)

total = 0
count = 1
copia_total = 0


while count <= numero:
    if numero >= 1:
        total = numero * count
        print("o fatorial do numero",numero,"x",count,"=",total)
        count += 1
        total = copia_total
        print(copia_total)

print("sai", copia_total)

numero = input("Digite um número para calcular o fatorial")
numero = int(numero)

total = 0
copia_total = 0


while numero <= 1:
    if numero >= 1:
        total = numero * total
        print("o fatorial do numero",numero,"x","=",total)
        total = copia_total
        print(copia_total)

print("sai", copia_total)

# %%
# resultado final

total = 1

numero = input("Digite um número para calcular o fatorial:")
numero = int(numero)

copia_numero = numero

if numero > 0:
   while numero >= 1:
      total = total * numero
      numero -= 1  

   print("O fatorial de",copia_numero,"é igual a:",total)
elif numero == 0:
  print("O fatorial de",copia_numero,"é igual a: 1",)
else:
    print("Digite um número positivo") 
 


  


  