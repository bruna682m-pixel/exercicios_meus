
# %%
python = {"Ana", "Carlos", "Pedro", "Mariana"}
java = {"Carlos", "Pedro", "Lucas", "Fernanda"}

intersecao = python & java
diferenca_python = python - java
diferenca_java = java - python
uniao = python | java

print(f"""
matriculados em ambos os cursos: {intersecao}
Apenas em python: {diferenca_python}
Apenas em java: {diferenca_java}
Todos alunos matriculados: {uniao}
""")
