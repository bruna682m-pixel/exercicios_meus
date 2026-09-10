# %%

notas = []
aprovados = 0
reprovados = 0

while True:
    notas_usuario = input("Digite as notas:")

    if notas_usuario == "":
        break
    else:
        notas_usuario = int(notas_usuario)
        notas.append(notas_usuario)

    for i in notas:
        if i >= 6:
            aprovados+=1
            print("Aprovados:",aprovados)
        else:
            reprovados+=1
            print("reprovados:",reprovados)

print(len(notas))
print(max(notas))
print(min(notas))
print(sum(notas)/ len(notas))
print(sum(notas))

 # %%
notas = []
aprovados = 0
reprovados = 0
maior = 0
menor = 0

while True:
    notas_usuario = input("Digite as notas:")

    if notas_usuario == "":
            break
    else:
        notas_usuario = int(notas_usuario)
        notas.append(notas_usuario)

for i, enu in enumerate(notas):
    if enu >= 6:
        aprovados+=1
        print("Aprovados:",aprovados)
    else:
        reprovados+=1
        print("reprovados:",reprovados)

    if i == 0:
        maior = enu
        menor = enu
    else:
        if enu > maior:
            maior = enu
        if enu < menor:
            menor = enu

    print("maior",maior)
    print("menor",menor)


print(len(notas))
print(max(notas))
print(min(notas))
print(sum(notas)/ len(notas))
print(sum(notas))
