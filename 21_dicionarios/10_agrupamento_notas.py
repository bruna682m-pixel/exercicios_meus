# %%
alunos = {    "Ana": 8.5,    "Carlos": 6.0,    "Pedro": 9.5,    "Mariana": 7.0,    "Lucas": 5.5,    "Fernanda": 9.0}

agrupando_notas = {}
notas_ordenadas = {}

for chave, valor in alunos.items():
    if valor >= 7:
        agrupando_notas.setdefault("aprovados", []).append((chave, valor))
    else:
        agrupando_notas.setdefault("reprovados", []).append((chave, valor))


notas_ordenadas["aprovados"] = sorted(agrupando_notas["aprovados"], key=lambda item: item[1], reverse=True)
notas_ordenadas["reprovados"] = sorted(agrupando_notas["reprovados"], key=lambda item: item[1], reverse=True)

print("Ordenado notas por classificação:", notas_ordenadas)

print(agrupando_notas)

