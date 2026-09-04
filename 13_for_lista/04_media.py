# %%
notas = [7, 8, 5, 9, 6]
media = 0
soma = 0
aprovados = 0
reprovados = 0

for i in notas:
    
    if i >= 6:
        aprovados += 1
    else:
        reprovados += 1

soma = soma + i
media = soma / len(notas)

print(f"""
Aprovados: {aprovados}
Reprovados; {reprovados}
Média: {media}
""")