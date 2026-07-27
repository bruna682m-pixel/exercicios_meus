# %%

litros = 100
pergunta = 0

while litros >= 20:
    pergunta = input("Quantos litros de água usados?")

    print(pergunta)

    pergunta = float(pergunta)

    litros = litros - pergunta

    print(litros)

print("Atenção: nível baixo.")
