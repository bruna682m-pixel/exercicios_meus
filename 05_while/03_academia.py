# %%

total_peso = 0
maximo = 0

while True:
    peso = input("Digite o peso levantados a cada serie")
    if peso == "0":
        break
    
    maximo = max(peso)
    peso = float(peso)
    total_peso = total_peso + peso
    

print("O total de peso foi:", total_peso, "O maior peso foi:", maximo)

# %%
