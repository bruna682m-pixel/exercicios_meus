# %%
saldo = input("Informe seu saldo?")
saque = input("informe quanto quer sacar?")
resto = 0


saldo = float(saldo)
saque = float(saque)
resto = float(resto)

if saldo > 0:
    if saldo > saque:
        resto = saldo - saque
        print("voce sacou",saque, "seu saldo atual é" ,resto)
    else:
        print("voce não tem dinheiro")
else:
    print("sem dinheiro")



