
# Mostrar apenas o valor do termo da posição informada da série de Fibonacci

# %%
# mostrando apenas no número que corresponde a sequência
soma = 0
a = 0
b = 1

numero = int(input("Digite um número para calcular a serie de Fibonacci:"))

for i in range(0, numero+1):
   soma = a + b
   
   a = b
   b = soma

   if numero == i:
         print("O resultado deu:",a)

# %%
# mostrando a sequência até o número digitado
soma = 0
a = 0
b = 1

numero = int(input("Digite um número para calcular a serie de Fibonacci: :"))

for i in range(0, numero):
   soma = a + b
   print("O resultado deu:",soma)

   a = b
   b = soma


   
   

   

  


   

        
  

# %%
