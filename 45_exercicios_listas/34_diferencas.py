# %%

lista_a = [1, 2, 3, 4, 5]
lista_b = [2, 4, 6]
diferenca = []

for i in lista_a:
    if i not in lista_b:    
        diferenca.append(i)

print(f"A diferença entre as listas são: {diferenca}")


