# %%
count = 0
maximo = 0
minimo = 0
soma = 0

while True:
    consumo = input("Digite o consumo dos meses:")

    if consumo == "-1":
        break

    consumo = float(consumo)    

    if count == 0:
        maximo = consumo
        minimo = consumo

    if maximo < consumo:
        maximo = consumo

    if minimo > consumo:
        minimo = consumo

    soma = soma + consumo
    count += 1

media = soma / count

print("""
Média =""", media, """
Maior valor =""", maximo, """
Menor valor =""", minimo)

