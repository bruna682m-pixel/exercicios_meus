# %%
arsenal = {
    "espada": 35,
    "arco": 25,
    "machado": 45,
    "adaga": 15,
    "cajado": 30,
    "picarreta": 45
}

maior = 0
chave_maior = 0
acima_30 = []
loop = 0
media = 0
soma = 0
abaixo_media = []
dano_igual = []

escolha = input("Digite qual arma equipar?")

if escolha in arsenal:
    print("Você equipou.")
else:
    print("Está arma não existe.")

for chave, valor in arsenal.items():
    if loop == 0:
        maior = valor
        chave_maior = chave
    else:
        if valor > maior:
            maior = valor
            chave_maior = chave
    loop += 1

    print(chave, valor)

    if valor > 30:
        acima_30.append(chave)

    soma = soma + valor

media = soma / len(arsenal)

for chave_media, valor_media in arsenal.items():
    if valor_media < media:
        abaixo_media.append(chave_media)

    if valor_media == maior:
        dano_igual.append(chave_media) 

if len(dano_igual) == 1:
    print("Sem armas com dano igual.")
    print(f"Maior dano: {chave_maior} {maior}")
else:
    print("Armas com dano iguais são:",dano_igual)

print(f"""
Arsenal: {arsenal}
Dano maior que 30: {acima_30}
Média de dano: {media}
Abaixo média: {abaixo_media}
""")