
# Mostrar apenas o valor do termo da posição informada da série de Fibonacci

# %%
soma = 0
numero = int(input("Digite um número:"))
res = 0
pri = 0
seg = 0
a = 0
b = 1

for i in range(0, numero+1):
   soma = a + b
   #print(soma)
   a = soma
   b = i
   print(b)


   

        
  

# %%
