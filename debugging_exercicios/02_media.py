# %%
# erro estava na proridade dos operadores estava dividindo primeiro 
# o certo somar as notas que ficam dentro () e depois dividir

nota1 = float(input("Digite a primeira nota: ")) # pedindo nota 1
nota2 = float(input("Digite a segunda nota: ")) # pedindo nota 2
nota3 = float(input("Digite a terceira nota: ")) # pedindo nota 3

media = (nota1 + nota2 + nota3) / 3 # calculando media antes soma tudo e direto dividia por 3
# agora coloquei os () para dar prioridade para soma e fazer ela primeiro depois dividir

print("Média:", media) #imprime a media 

if media >= 5: # aprovado se nota for >= a 5
    print("Aprovado")
else:
    print("Reprovado") # reprova se for menor que 5 de 4 para baixo