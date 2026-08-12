# %%
count = 1
reprovado = 0
aprovado = 0
media_geral = 0
media = 0
media_soma_geral = 0
menor = 0
maior = 0

while count <= 5:
    nome = input("Digite seu nome:")
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    nota3 = float(input("Digite a terceira nota:"))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 5:
        print("Você foi aprovado. Sua méida foi de:",media)
        aprovado +=1
    else:
        print("Você foi reprovado. Sua média foi de:",media)
        reprovado += 1
    
    media_soma_geral = media_soma_geral + media

    if count == 1:
        maior = media
        menor = media
    else:
        if media > maior:
            maior = media
            
        if media < menor:
            menor = media

    media_geral = media_soma_geral / count
    count +=1

print("Quantidade de alunos",count - 1,)
print("A maior média foi:",maior,"e a menor média foi:",menor)
print("Foram aprovados",aprovado,"alunos. E foram reprovados",reprovado,"alunos")
print("A média geral foi:",round(media_geral, 2))


