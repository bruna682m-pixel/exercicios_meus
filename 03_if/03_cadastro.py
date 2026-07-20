# %%

nome = input("Digite seu nome:")
idade = input("Dgite sua idade:")
cidade = input("Digite sua cidade:")
profissao = input("Digite sua profissão:")
salario = input("Digite seu salário:")

filhos = input("""

               Tem filhos?
               1 - sim
               2- não
               
               """)

casado = input("""
Voce é casado(a)?
               1- sim
               2- não
""")

if filhos == "1":
    filhos = "Tenho filhos"
elif filhos == "2":
    filhos = "Sem filhos"
else:
    filhos = "opção invalida"
    print("Digite a opção certa")

if casado == "1":
    casado = "Sou casado(a)"
elif casado == "2":
    casado = "Não sou casado"
else:
    casado = "opção invalida"
    print("Digite a opção certa")

print("""
Nome: """, nome, """
Idade: """, idade, """
Cidade: """, cidade, """
Profissão:  """, profissao, """
Salário:  """, salario, """
Filhos: """, filhos, """
Casado:  """, casado)