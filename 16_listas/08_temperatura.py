# %%

# %%

temperaturas = []
maior = 0
menor = 0
acima_30 = 0
abaixo_20 = 0
soma = 0
posicao_maior = 0
volta = 0
dia_maior_temp = 0
semana = 0

while volta <= 6:
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
            dia_maior_temp = volta
            maior = temperatura
        if temperatura <= menor:
            menor = temperatura

    soma = soma + temperatura
    media = soma / len(temperaturas)

    if temperatura > 30:
        acima_30 += 1

    if temperatura < 20:
        abaixo_20 += 1

    for i, enu in enumerate(temperaturas):
        if maior == enu:
            dia_maior_temp = i

    if dia_maior_temp == 0:
        semana = "Domingo"
    elif dia_maior_temp == 1:
        semana = "Segunda=feira"
    elif dia_maior_temp == 2:
        semana = "Terça-feira"
    elif dia_maior_temp == 3:
        semana = "Quarta-feira"
    elif semana == 4:
        semana = "Quinta-feira"
    elif dia_maior_temp == 5:
        semana = "Sexta-feira"
    elif dia_maior_temp == 6:
        semana = "Sabado"

    volta += 1


print("Dia da maior temperatura:",semana,dia_maior_temp)
print("Acima de 30:",acima_30)
print("Abaixo de 20:",abaixo_20)
print("Média:",media)
print("Maior:",maior)
print("Menor:",menor)