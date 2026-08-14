# %%
# permite saque 0, -1, -100,

saldo = 500 # saldo de 500

saque = float(input("Digite o valor do saque: ")) # pedindo quanto quer sacar

if saque <= 0: # permite saque 0 então troquei para <= 0
    print("Valor inválido.")

elif saque > saldo: # se saque for maior que saldo não deixa sacar
    print("Saldo insuficiente.")

else: # se qualquer um dos ifs forem falso vem para ca e deixar fazer o saque
    saldo = saldo - saque # 
    print("Saque realizado.")
    print("Saldo:", saldo)

# mudei o 0 para <= 0 para não permitir saque = 0 e negativo
# criei condições mais expecificas para não permitir 0 ou negativo
# mesmo quando digitava 0 ou negativo ele fazia o calculo so saque e mostrava o resultado e saque realizado
# por isso coloquei no if, elif e else