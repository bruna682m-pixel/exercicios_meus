# %%

numeros = [10, 25, 7, 42, 18, 30]
encontrou = False

remover = int(input("Digite um número:"))

for i, enu in enumerate(numeros):
    if enu == remover:
        encontrou = True
        print("posição:",i)
        

