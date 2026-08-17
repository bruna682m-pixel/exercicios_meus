# %%
numero_max = 10

numero = int(input("Digite um número para fazer a tabuada.")) # fora pede a entrada 1 vez

for i in range(1, numero_max+1): # dentro pede entrada toda iteração

    print(numero, "x", i, "=", numero * i)