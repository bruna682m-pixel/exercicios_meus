# %%
faturamento = 0
count = 0

while True:
    valor_compra = input("Digite o valor da compra")
    pagamento = input("Digite a forma de pagamento 1- pix, 2- cartão e 3- dinheiro")

    if valor_compra == "0":
        break

    valor_compra = float(valor_compra)
        
    faturamento = faturamento + valor_compra
    count += 1

print("""
Faturamento:
""", faturamento,
"""
Total de clientes:""", count)


            
