# %%
# Mostrar se um número é ou não primo ( consistir )

numero = 7

for i in range(1, numero+1):
    total = numero % i
    if total == 0:
        print("primo")
    else:
        print("nao")
    
    print("i",i)
    print(total)
# %%
numero = 7

for i in range(1, numero+1):
    if numero % i == 0:
        print("primo")
    else:
        print("nao")
    
    print("i",i)
    print(total)
