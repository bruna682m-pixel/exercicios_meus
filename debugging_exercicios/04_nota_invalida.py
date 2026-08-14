# %%

nota = float(input("Digite sua nota: ")) # pedindo uma nota

if nota < 0 or nota > 10: # é para aceitar números de 0 a 10 mas está aceitando maior que 10
    print("Nota inválida.") # se for maior que 10 e menor que 0 imprime
elif nota >= 5: # se nota for maior = a 5 aprovado
    print("Aprovado")
else:
    print("Reprovado") # se não reprovado

# não cheaga a ser um problema grave mas mostra se foi aprovado ou reprovado mesmo quando a entrada é inválida
# coloquei dentro do elif verificar todas as opções primeiro
# não aceita negativo, 
# 5 está aprovado certo
# aceita 12 está errado

