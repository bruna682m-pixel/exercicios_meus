# %%

gols = 0
media = 0
count = 0

while True:
    valor_gol = input("Digite quantos gols por partida")
    if valor_gol == "-1":
        break

    valor_gol = int(valor_gol)    
    gols = gols + valor_gol
    count += 1
    media = gols / count

print("O total de gols foi:", gols, "A média de gol foi:", media)
# %%
