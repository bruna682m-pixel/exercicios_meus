# %%

loop = 1
lista_notas = []
maior = 0 
menor = 0
total_sumsum = 0
maior_max = 0
menor_min = 0
media_sum = 0

while loop <= 4:
    notas = int(input("Digite 4 notas:"))

    lista_notas.append(notas)

    for i in lista_notas:
        if loop == 1:
            maior = i
            menor = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
    
    loop += 1

maior_max = max(lista_notas)
menor_min = min(lista_notas)
total_sum = sum(lista_notas)
media_sum = total_sum / len(lista_notas)

print(f"""
Maior: {maior}
Menor: {menor}
Maior max: {maior_max}
Menor min: {menor_min}
Media sum: {media_sum}
""")
