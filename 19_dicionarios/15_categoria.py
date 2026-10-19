# %%

categoria = {}
loop = 1
ocorrencia = 0

while True:
    if loop <= 5:
        palavras = input("Digite 5 palavras:")

        if palavras not in categoria:
            categoria[palavras] = 1
        else:
            categoria[palavras] += 1
            print(categoria)

        loop += 1
    else:
        print("Apenas 5 palavras")
        break


        