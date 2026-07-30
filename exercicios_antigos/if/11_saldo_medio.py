
- ler o saldo medio do cliente,

- calcular o valor do credito em função da tabela a seguir:
SALDO MÉDIO % CREDITO
0 a 200 0%
201 a 400 20%
401 a 600 30%
Acima de 601 40%

- mostrar como saída uma mensagem informando o saldo médio e o valor do crédito

# %%
credito = 0
saldo_medio = input("Digite o seu saldo medio:")

saldo_medio = float(saldo_medio)


if saldo_medio <= 200:
    credito = saldo_medio * 0
elif saldo_medio >= 201 and saldo_medio <= 400:
    credito = saldo_medio * 0.20
elif saldo_medio >= 401 and saldo_medio <= 600:
    credito = saldo_medio * 0.30
else:
    credito = saldo_medio * 0.40
    

print("Seu saldo é de R$",saldo_medio, "E voce recebeu R$",credito, "de credito")

