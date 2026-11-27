# %%


alunos = {
    "Ana": {"notas": [8, 9, 7], "turma": "A"},
    "Carlos": {"notas": [5, 6, 4], "turma": "B"},
    "Mariana": {"notas": [9, 10, 8], "turma": "A"},
    "Pedro": {"notas": [6, 7, 5], "turma": "B"},
    "Lucas": {"notas": [10, 9, 10], "turma": "A"},
    "Fernanda": {"notas": [4, 5, 6], "turma": "B"}
}

por_turma = {}
media_notas = {}
soma = {}


for chave, valor in alunos.items():
    por_turma.setdefault(valor["turma"], []).append(chave)
    for notas in valor["notas"]:
        
        media_notas[chave] = soma / 3
        

print("teste")
print(media_notas)

print()

print(f"""
Agrupado por turmas: {por_turma}
""")

