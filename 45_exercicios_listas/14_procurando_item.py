# %%
print("Solução minha") 
inventario =  ["Laptop", "Mouse", "Monitor", "Keyboard", "Tablet"]
encontrado = False

if "Tablet" in inventario:
        encontrado = True

print("Tablet está no inventário:", encontrado)

# %%
# Solução recomendada
inventario =  ["Laptop", "Mouse", "Monitor", "Keyboard"]
alvo = "Tablet"

if alvo in inventario:
    print(f"{alvo} está no inventario? True")
else: print(f"{alvo} está no inventario? False")
