
print("""
Preço do ingresso: R$ 40.00
""")

idade = input("Digite sua idade?")

estudante = input("""
Você é estudante ?
1 - Sim
2 - Não
""")

professor = input("""
Você é professor?
1 - Sim
2 - Não
""")

aposentado = input("""
Você é aposentado?
1 - Sim
2 - Não
""")

idade = int(idade)
conta = 40
brinde = "Nenhum"

if idade <= 12 or idade >= 60:
  conta = 40/2
elif estudante == "1" or    professor == "1":
  desconto = 40*0.20
  conta = 40 - desconto


if idade >= 60 and estudante == "1":
  brinde = "Combo"
elif idade <= 12 and estudante == "1":
  brinde = "pipoca"
elif idade >= 18 and idade <= 25 and estudante == "1":
  brinde = "refri"
elif aposentado == "1":
  brinde = "batata pequena"

if estudante == "1":
  estudante = "Sim"
elif estudante == "2":
  estudante = "Não"
 
if aposentado == "1":
  aposentado = "Sim"
elif aposentado == "2":
  aposentado = "Não"
 
if professor == "1":
  professor = "Sim"
elif professor == "2":
  professor = "Não"
 
print("""
Idade:""", idade,
""" 
Estudante:""", estudante,
"""
Aposentado:""", aposentado, 
"""
Professor:""", professor, 
"""Sua conta deu: """, conta, """Voce ganhou brinde: """, brinde
     )
 
 
 
 
