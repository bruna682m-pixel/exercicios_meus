#Ler três notas de 10 alunos de uma turma. Para cada aluno, calcule a média ponderada, como
#segue:

#MP = ( n1*2 + n2*4 + n3*3 ) / 10

#Além disso, calcule a média geral da turma. Mostre a média de cada aluno e uma mensagem
#"Aprovado", caso a média seja maior ou igual a sete, e uma mensagem "Reprovado", caso
#contrário. Ao final, mostre a média geral.

# %%
count = 1
media_ponderada = 0
media_geral = 0
soma_media_geral = 0

while count <= 10:
    nota1 = input("Digite a nota 1")
    nota2 = input("Digite a nota 2")
    nota3 = input("Digite a nota 3")

    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)

    media_ponderada = (nota1*2 + nota2*4 + nota3*3) / 10

    soma_media_geral = soma_media_geral + media_ponderada

    media_geral = soma_media_geral / count

    if media_ponderada >=7:
        print("Aprovado",media_ponderada)
    else:
        print("Reprovado",media_ponderada)

    count +=1

print("A média da turma é:", media_geral)


