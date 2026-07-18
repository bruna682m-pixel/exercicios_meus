# %%
saldo = input("Informe seu saldo?")
saque = input("informe quanto quer sacar?")
resto = 0


saldo = float(saldo)
saque = float(saque)
resto = float(resto)

if saque <= 0:
  print("Digite um valor maior que 0")
elif saldo > 0:
    if saldo >= saque:
        resto = saldo - saque
        print("voce sacou",saque, "seu saldo atual é" ,resto)
    else:
        print("Saldo insuficiente")
else:
    print("saldo insuficiente")



