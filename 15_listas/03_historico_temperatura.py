# %%

temperaturas = []
maior = 0
menor = 0
menor = 0
acima_30 = 0
abaixo_20 = 0
soma = 0
posicao_maior = 0
volta = 0

while True:
    temperatura = input("Digite as temperaturas ou enter para parar:")

    if temperatura == "":
        print("saindo...")
        break
    else:
        temperatura = int(temperatura)
        temperaturas.append(temperatura)

    print("temperaturas:",temperaturas)

    if volta == 0:
        maior = temperatura
        menor = temperatura
    else:
        if temperatura >= maior:
            maior = temperatura
        if temperatura <= menor:
            menor = temperatura

    soma = soma + temperatura
    media = soma / len(temperaturas)

    if temperatura > 30:
        acima_30 += 1

    if temperatura < 20:
        abaixo_20 += 1

    volta += 1

    for i, enu in enumerate(temperaturas):
        if enu >= enu:
            posicao_maior = i

print("Posição do maior:",posicao_maior)
print("última temperatura:", temperaturas[-1])
print("Primeira temperatura:",temperaturas[0])
print("Acima de 30:",acima_30)
print("Abaixo de 20:",abaixo_20)
print("Média:",media)
print("Maior:",maior)
print("Menor:",menor)