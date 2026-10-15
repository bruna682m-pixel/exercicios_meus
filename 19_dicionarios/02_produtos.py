# %%

produtos = {
    "Teclado": "R$200",
    "Meias": "R$ 100",
    "Mouse": "R$ 60",
    "Uva": "R$ 7.99",
    "Mala": "R$ 500"  
    }

produto = input("Entre com o nome do produto:")

if produto in produtos:
    print(produtos[produto])
else:
    print("Não temos este produto.")


