# %%

total_peso = 0
maximo = 0
count = 0


while True:
    peso = input("Digite o peso levantados a cada serie")
    if peso == "0":
        break

    peso = float(peso)

    if count == 0:
        maximo = peso

    if peso > maximo:
       maximo = peso
    
    count += 1
   
    total_peso = total_peso + peso
    

print("O total de peso foi:", total_peso, "O maior peso foi:", maximo)

# %%
