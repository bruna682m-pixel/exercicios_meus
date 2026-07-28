# %%
total_pessoas = 0
pergunta = 0

while total_pessoas <= 8:
    pergunta = input("Entraram quantas pessoas no elevador?")

    pergunta = int(pergunta)

    total_pessoas = total_pessoas + pergunta

    if total_pessoas >= 8:
      print("Elevador cheio. Limite de 8 pessoas")
      break


