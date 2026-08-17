# %%

numero_max = 100

numero = int(input("Digite um número para descobrir seus multiplos:"))

for i in range(1, numero_max+1):
    if i % numero == 0:
        print(i, "é múltiplo de", numero)
    

