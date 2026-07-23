# %%

total = 0
count = 0

while True:
    moeda = input("Digite quantas moedas voce quer colocar no cofrinho:")

    if moeda == "":
        break

    moeda = float(moeda)
    total = total + moeda
    count = count + 1
    print(count)

print("""
O cofrinho tem: """, total, """moedas
O total de moedas foi""", count)


# %%
