# %%
# Solicitar um número inteiro positivo ( consistir ) e mostrar se é ou não primo

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



